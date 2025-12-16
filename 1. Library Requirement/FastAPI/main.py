"""Single-file FastAPI blog tutorial.

Run with:
- `uvicorn main:app --reload`
- or `fastapi dev main.py`

This file intentionally includes multiple FastAPI concepts:
- Routers (`APIRouter`)
- Dependency injection (`Depends`) for auth + data access
- Validation (`Path`, `Query`, Pydantic models)
- Middleware (request id + timing)
- Custom exceptions + exception handlers
- Auth (OAuth2 password flow demo)
- Testing snippet (`TestClient`) (optional, not executed)

Beginner notes:
- FastAPI automatically creates interactive docs at:
    - Swagger UI:  http://127.0.0.1:8000/docs
    - ReDoc:      http://127.0.0.1:8000/redoc
- Type hints (like `int`, `bool`, `Optional[str]`) are not just for IDE help:
    FastAPI reads them to validate inputs and generate docs.

For most of this tutorial please interact with the API using the docs UI
"""

from __future__ import annotations

# `from __future__ import annotations` makes type hints "lazy" (stored as strings).
# It's helpful for modern typing like `list[BlogOut]` without import cycles.

import asyncio
from datetime import datetime, timezone
import time
import uuid
from contextlib import asynccontextmanager
from dataclasses import dataclass

# Available support typing format
from typing import Any, Optional

import httpx
from fastapi import (
    APIRouter,
    Depends,
    FastAPI,
    HTTPException,
    Path,
    Query,
    Request,
    Response,
    status,
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field


# -------------------- App lifecycle --------------------


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Lifespan is the recommended replacement for old @app.on_event("startup").
    # Put one-time setup here:
    # - connect DB
    # - create HTTP clients
    # - warm caches
    # - load ML models
    yield
    # Put cleanup here:
    # - close DB
    # - close HTTP clients
    # - flush telemetry


app = FastAPI(
    # These fields show up in the generated docs.
    title="FastAPI Blog Tutorial",
    version="1.1.0",
    description="A single-file blog API demonstrating core FastAPI patterns.",
    lifespan=lifespan,
)


# -------------------- Middleware --------------------

# Middleware runs for *every* HTTP request.
# Typical uses: CORS, logging, request IDs, auth, rate limiting.


app.add_middleware(
    CORSMiddleware,
    # NOTE: allow_origins=["*"] is convenient for learning, but too open for production.
    # In real apps, list exact origins (e.g. ["https://your-frontend.com"]).
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_request_id_and_timing(request: Request, call_next):
    # A request ID helps you trace logs across services.
    # If the client provides an X-Request-ID header, we keep it; otherwise we generate one.
    request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
    start = time.perf_counter()

    # `call_next` forwards the request to the route handler.
    response: Response = await call_next(request)

    # Add debugging/tracing headers to the response.
    elapsed_ms = (time.perf_counter() - start) * 1000
    response.headers["X-Request-ID"] = request_id
    response.headers["X-Process-Time-ms"] = f"{elapsed_ms:.2f}"
    return response


# -------------------- Models --------------------

# Pydantic models define:
# - request bodies (what the client sends)
# - response shapes (what your API returns)
# They also provide validation + clear API docs.


class MessageOut(BaseModel):
    # A tiny response schema for the home route.
    message: str


class TokenOut(BaseModel):
    # What our demo auth endpoint returns.
    access_token: str
    token_type: str = "bearer"


class BlogCreate(BaseModel):
    # Request model for creating a blog post.
    # `Field(..., ...)` means it's required and has extra validation.
    blog_title: str = Field(..., min_length=1, max_length=200)
    blog_content: str = Field(..., min_length=1)
    published: bool = False


class BlogUpdate(BaseModel):
    # Request model for partial updates (PATCH): all fields optional.
    blog_title: Optional[str] = Field(None, min_length=1, max_length=200)
    blog_content: Optional[str] = Field(None, min_length=1)
    published: Optional[bool] = None


class BlogReplace(BaseModel):
    # Request model for full replace (PUT): all fields required.
    blog_title: str = Field(..., min_length=1, max_length=200)
    blog_content: str = Field(..., min_length=1)
    published: bool = False


class BlogOut(BaseModel):
    # Response model for blog data.
    blog_id: int
    blog_title: str
    blog_content: str
    published: bool
    created_at: datetime
    updated_at: datetime


# -------------------- Custom exceptions --------------------

# In FastAPI you can raise:
# - `HTTPException` directly (common)
# - your own Python exceptions + a custom exception handler (clean separation)


class BlogNotFoundError(Exception):
    def __init__(self, blog_id: int):
        self.blog_id = blog_id


@app.exception_handler(BlogNotFoundError)
async def blog_not_found_handler(_: Request, exc: BlogNotFoundError):
    # This converts our plain Python exception into a proper HTTP response.
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Blog not found", "blog_id": exc.blog_id},
    )


# -------------------- “DB” layer (in-memory) --------------------

# This tutorial uses an in-memory store to keep the file simple.
# Important limitations:
# - Data resets when the server restarts
# - Not safe for multi-process deployments
# - Real apps use a database (Postgres/MySQL/etc.)


@dataclass
class BlogRecord:
    blog_id: int
    blog_title: str
    blog_content: str
    published: bool
    created_at: datetime
    updated_at: datetime


class BlogStore:
    def __init__(self) -> None:
        # Our "database": a dict keyed by blog_id.
        self._data: dict[int, BlogRecord] = {}
        self._next_id: int = 1

    def list(self, offset: int, limit: int, published: Optional[bool]) -> list[BlogRecord]:
        # Pagination pattern: `offset` + `limit`.
        values = list(self._data.values())
        values.sort(key=lambda r: r.blog_id)
        if published is not None:
            values = [r for r in values if r.published is published]
        return values[offset : offset + limit]

    def get(self, blog_id: int) -> BlogRecord:
        # Raise our custom exception if not found.
        if blog_id not in self._data:
            raise BlogNotFoundError(blog_id)
        return self._data[blog_id]

    def create(self, blog_id: int, payload: BlogCreate) -> BlogRecord:
        now = datetime.now(timezone.utc)
        self._data[blog_id] = BlogRecord(
            blog_id=blog_id,
            blog_title=payload.blog_title,
            blog_content=payload.blog_content,
            published=payload.published,
            created_at=now,
            updated_at=now,
        )
        return self._data[blog_id]

    def create_auto_id(self, payload: BlogCreate) -> BlogRecord:
        blog_id = self._next_id
        self._next_id += 1
        return self.create(blog_id, payload)

    def update(self, blog_id: int, payload: BlogUpdate) -> BlogRecord:
        record = self.get(blog_id)
        if payload.blog_title is not None:
            record.blog_title = payload.blog_title
        if payload.blog_content is not None:
            record.blog_content = payload.blog_content
        if payload.published is not None:
            record.published = payload.published
        record.updated_at = datetime.now(timezone.utc)
        return record

    def replace(self, blog_id: int, payload: BlogReplace) -> BlogRecord:
        record = self.get(blog_id)
        record.blog_title = payload.blog_title
        record.blog_content = payload.blog_content
        record.published = payload.published
        record.updated_at = datetime.now(timezone.utc)
        return record

    def delete(self, blog_id: int) -> None:
        _ = self.get(blog_id)
        del self._data[blog_id]


_store = BlogStore()


def get_store() -> BlogStore:
    # Dependency injection (DI) provider.
    # In a real app, you'd likely return a DB session here, e.g. `Session`.
    return _store


# -------------------- Auth (OAuth2 demo) --------------------

# This is a *demo* auth setup. It's intentionally simple for beginners.
# Concepts shown:
# - OAuth2 Password flow shape (login endpoint + Bearer token)
# - Dependency-based protection of endpoints


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# `OAuth2PasswordBearer` reads the `Authorization: Bearer <token>` header.
# It does NOT validate by itself; it only extracts the token string.


class User(BaseModel):
    username: str


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    # Dependency that protects routes.
    # Demo-only: treat token "demo-token" as authenticated.
    # Real apps: decode JWT, verify signature + expiry, fetch user from DB, etc.
    if token != "demo-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return User(username="demo")


auth_router = APIRouter(prefix="/auth", tags=["auth"])

# Routers help you split a large API into modules.
# In a bigger project you'd move each router into its own file.


@auth_router.post("/token", response_model=TokenOut)
def issue_token(form: OAuth2PasswordRequestForm = Depends()) -> TokenOut:
    # OAuth2 Password flow expects form-encoded fields:
    # - username
    # - password
    # Demo-only: any username/password gets the same token.
    # In real code: verify password hash, issue JWT with expiry, etc.
    _ = form.username
    _ = form.password
    return TokenOut(access_token="demo-token")


app.include_router(auth_router)


# -------------------- Routers (blog endpoints) --------------------


# REST naming: use plural nouns for collections.
# - Collection: /blogs
# - Single resource: /blogs/{blog_id}
blog_router = APIRouter(prefix="/blogs", tags=["blog"])


@app.get("/", response_model=MessageOut, tags=["meta"])
def root() -> MessageOut:
    # `response_model=...` makes docs clearer and filters the output.
    return MessageOut(message="Hello World")


@blog_router.get(
    "",
    response_model=list[BlogOut],
    response_model_exclude_none=True,
)
def list_blogs(
    # Dependencies can be function parameters.
    # FastAPI will call `get_store()` and inject the result into `store`.
    store: BlogStore = Depends(get_store),
    # Query params: /blog?offset=0&limit=20
    offset: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    published: Optional[bool] = Query(None, description="Filter by published=true/false"),
) -> list[BlogOut]:
    records = store.list(offset=offset, limit=limit, published=published)
    return [
        BlogOut(
            blog_id=r.blog_id,
            blog_title=r.blog_title,
            blog_content=r.blog_content,
            published=r.published,
            created_at=r.created_at,
            updated_at=r.updated_at,
        )
        for r in records
    ]


@blog_router.get("/{blog_id}", response_model=BlogOut)
def get_blog(
    # Path params are declared inside the path string.
    # This means requests like: GET /blog/123
    blog_id: int = Path(..., ge=1, description="Blog id must be >= 1"),
    store: BlogStore = Depends(get_store),
) -> BlogOut:
    record = store.get(blog_id)
    return BlogOut(
        blog_id=record.blog_id,
        blog_title=record.blog_title,
        blog_content=record.blog_content,
        published=record.published,
        created_at=record.created_at,
        updated_at=record.updated_at,
    )


@blog_router.post(
    "",
    response_model=BlogOut,
    status_code=status.HTTP_201_CREATED,
)
def create_blog(
    requested: BlogCreate,
    response: Response,
    store: BlogStore = Depends(get_store),
) -> BlogOut:
    # REST: POST to the collection creates a new resource.
    record = store.create_auto_id(requested)
    response.headers["Location"] = f"/blogs/{record.blog_id}"
    return BlogOut(
        blog_id=record.blog_id,
        blog_title=record.blog_title,
        blog_content=record.blog_content,
        published=record.published,
        created_at=record.created_at,
        updated_at=record.updated_at,
    )


@blog_router.put(
    "/{blog_id}",
    response_model=BlogOut,
)
def replace_blog(
    blog_id: int = Path(..., ge=1),
    requested: BlogReplace = ...,
    store: BlogStore = Depends(get_store),
) -> BlogOut:
    # REST: PUT replaces the whole resource.
    record = store.replace(blog_id, requested)
    return BlogOut(
        blog_id=record.blog_id,
        blog_title=record.blog_title,
        blog_content=record.blog_content,
        published=record.published,
        created_at=record.created_at,
        updated_at=record.updated_at,
    )


@blog_router.patch(
    "/{blog_id}",
    response_model=BlogOut,
)
def update_blog(
    blog_id: int = Path(..., ge=1),
    requested: BlogUpdate = ...,
    store: BlogStore = Depends(get_store),
) -> BlogOut:
    # REST: PATCH updates only fields provided by the client.
    record = store.update(blog_id, requested)
    return BlogOut(
        blog_id=record.blog_id,
        blog_title=record.blog_title,
        blog_content=record.blog_content,
        published=record.published,
        created_at=record.created_at,
        updated_at=record.updated_at,
    )


@blog_router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(
    blog_id: int = Path(..., ge=1),
    store: BlogStore = Depends(get_store),
) -> Response:
    # 204 means “No Content”. It's a common status code for deletes.
    store.delete(blog_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


app.include_router(blog_router)