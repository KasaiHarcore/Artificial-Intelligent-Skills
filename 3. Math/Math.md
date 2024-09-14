All information about this notebook will be covered in the Introduction to Applied Linear Algebra - Vectors, Matrices, and Least Squares (Stanford ENGR108) - 2020

# Chapter 1: Vectors

### 1.1 Vectors

A vector is an ordered finite list of numbers. Vectors commonly written as vertical arrays in square brackets:

$$
\begin{bmatrix} x_{1} \\ ... \\ x_{n} \end{bmatrix}
$$

or in round brackets:

$$
(x_{1}, x_{2}, ..., x_{n})
$$

- The entries of a vector are the *elements* (entries, coefficients, components) of the vector.
- The *size* (or dimension / length) of the vector is the number of elements in the vector. Example with vector $(1.1, 3, -2.4, 5)$:

  - The size of the vector is 4.
  - The third variable is -2.4.
- A vector of size n is called an *n-vector*.
- In vector, a number stand alone is a 1-vector or scalar.
- A vector can be represent by point with arrow on top of it: $\vec{a}$.
- For a subscripted vector, the subscript is the index of the element. Example: with same example above, third element is $a_{3} = -2.4$.
- $a_{i}$ is the ith element of the vector $\vec{a}$.
- In an *n-vector*, indexes run ${i} \in \{1, 2, ..., n\}$.

Notices that: Some time a subscript will not represent a scalar but a vector.

**Block or Stacks vector**

Suppose we have $\vec{b}, \vec{c}, \vec{d}$ define as:

$$
\vec{a} = \begin{bmatrix} \vec{b} \\ \vec{c} \\ \vec{d} \end{bmatrix}
$$

where $\vec{b}, \vec{c}, \vec{d}$ are vectors. Then $\vec{a}$ is a block vector. If $\vec{b}$ have size $m$, $\vec{c}$ have size $n$, $\vec{d}$ have size $p$, then $\vec{a}$ have size $m + n + p$.

$$
\vec{a} = (b_{1}, b_{2}, ..., b_{m}, c_{1}, c_{2}, ..., c_{n}, d_{1}, d_{2}, ..., d_{p})
$$

This vector can include a scalars. For example if $\vec{a}$ is a 3-vector, then $(1, a)$ is the 4-vector $(1, a_{1}, a_{2}, a_{3})$.

**Subvectors**

In the equation above, we say that $\vec{b}$, $\vec{c}$, $\vec{d}$ are subvectors or slices of $\vec{a}$, with sizes $m$, $n$, $p$ respectively. Colon notation used to denote subvectors. For example:

$$
\vec{a}_{r:s} = (a_{r}, a_{r+1}, ..., a_{s})
$$

The subscript $r:s$ denotes the subvector of $\vec{a}$ from the rth element to the sth element. If $r = 1$ and $s = n$, then $\vec{a}_{1:n}$ is the entire vector $\vec{a}$.

**Zero vector**

A *zero vector* is a vector whose elements are all zero. It is denoted by $\vec{0}$.

**Unit vector**

A *unit vector* is a vector whose length is 1. It is denoted by $\vec{e}_{i}$, where $i$ is the index of the 1 in the vector. For example, $\vec{e}_{3}$ is the 3-vector $(0, 0, 1)$.

**One vector**

A *one vector* is a vector whose elements are all 1. It is denoted by $\vec{1}$.

**Sparse vector**

A vetor is said to be *spare* if most of its elements are zero. (> 50% of elements are zero).

### 1.2 Vector addition

Two vector of the *same size* can be added together by adding the corresponding elements. Can be denote like normal addition number by number:

$$
\vec{a} + \vec{b} = (a_{1} + b_{1}, a_{2} + b_{2}, ..., a_{n} + b_{n})
$$

Similar to vector subtraction:

$$
\vec{a} - \vec{b} = (a_{1} - b_{1}, a_{2} - b_{2}, ..., a_{n} - b_{n})
$$

**Properties of vector addition**

- Commutative: $\vec{a} + \vec{b} = \vec{b} + \vec{a}$
- Associative: $(\vec{a} + \vec{b}) + \vec{c} = \vec{a} + (\vec{b} + \vec{c})$
- Identity: $\vec{a} + \vec{0} = \vec{0} + \vec{a} = \vec{a}$
- Inverse: $\vec{a} + (-\vec{a}) = \vec{0}$

Another way to think about vector addition is to consider the vectors as displacements in space. The sum of two vectors is the vector that represents the total displacement.

### 1.3 Scalar-vector multiplication

Another operation is *scalar multiplication* or *scalar-vector multiplication*. A vector can be multiplied by a scalar (a number) by multiplying each element of the vector by the scalar. For example:

$$
(-2) \vec{a} = (-2) (a_{1}, a_{2}, ..., a_{n}) = \begin{bmatrix} -2a_{1} \\ -2a_{2} \\ ... \\ -2a_{n} \end{bmatrix}
$$

Scalar-vector multiplication can also be written with the scalar on the right:

$$
\vec{a} (-2) = (-2) \vec{a}
$$

The meaning is the same

**Properties of scalar-vector multiplication**

- Right Distributive: $c (\vec{a} + \vec{b}) = c \vec{a} + c \vec{b}$ || $(c + d) \vec{a} = c \vec{a} + d \vec{a}$
- Associative: $c (d \vec{a}) = (cd) \vec{a}$

**Linear combination**

If $\vec{a}_{1}, \vec{a}_{2}, ..., \vec{a}_{k}$ are vectors and $c_{1}, c_{2}, ..., c_{k}$ are scalars, then the linear combination of the vectors is:

$$
c_{1} \vec{a}_{1} + c_{2} \vec{a}_{2} + ... + c_{k} \vec{a}_{k}
$$

### 1.4 Inner product (Dot product)

The *inner product* or *dot product* of two vectors is a scalar. The dot product of two vectors $\vec{a}$ and $\vec{b}$ of the same size is:

$$
a^T b = a_{1} b_{1} + a_{2} b_{2} + ... + a_{n} b_{n}
$$

where $a^T$ is the transpose of the vector $\vec{a}$. Some other notations for the dot product are $\langle\vec{a}, \vec{b} \rangle$ or $\vec{a} \cdot\vec{b}$.

As a specific example of the inner product, we have:

$$
\begin{bmatrix} 1 \\ 2 \\ 3\end{bmatrix}^T \begin{bmatrix} 4 \\ 5 \\ 6\end{bmatrix} = 1\cdot4 + 2\cdot5 + 3\cdot6 = 32
$$

When $n = 1$, the inner product reduces to the usual product of two numbers.

**Properties of the inner product**

- Commutative: $\vec{a}^T \vec{b} = \vec{b}^T \vec{a}$
- Associative with scalar multiplication: $(c \vec{a})^T \vec{b} = c (\vec{a}^T \vec{b}) = \vec{a}^T (c \vec{b})$
- Distributivity with vector addition: $\vec{a}^T (\vec{b} + \vec{c}) = \vec{a}^T \vec{b} + \vec{a}^T \vec{c}$

### 1.5 Complexity of vector computations

**Computer representation of numbers and vectors**

- In a computer, real numbers are stored in computer using *floating point format*, which represents a real number using a block of 64bits (0s and 1s), or *8 bytes*
- The floating point format has a fixed number of significant digits, and the exponent is used to represent numbers that are too large or too small to be represented exactly

I'll stop here because this not focus too much on anything else except math. For more information, please seek google or the book.

# Chapter 2: Linear functions

### 2.1 Linear functions

Given a $f: \mathbb{R}^{n} \rightarrow\mathbb{R}$, a *function* that maps real n-vector to real number, it satisfies the *superposition property* if:

$$
f(\alpha\vec{a} + \beta\vec{b}) = \alpha f(\vec{a}) + \beta f(\vec{b})
$$

hold for all $\vec{a}, \vec{b} \in\mathbb{R}^{n}$ and all scalars $\alpha, \beta\in\mathbb{R}$.

A function that satisfies the superposition property is called a *linear function*.

**Linear function of inner product**

Suppose $\vec{a}$ is an *n-vector*. We can define a function as:

$$
f(\vec{x}) = \vec{a}^T \vec{x}
$$

Here, $f(\vec{x})$ is a weighted sum of entries of x

**Superposition and linearity**

The inner product function define above satisfies the property:

$$
f(\alpha\vec{x} + \beta\vec{y}) = \vec{a}^T (\alpha\vec{x} + \beta\vec{y}) = \alpha (\vec{a}^T \vec{x}) + \beta (\vec{a}^T \vec{y}) = \alpha f(\vec{x}) + \beta f(\vec{y})
$$

We can easily deduce that inner product function is a linear function

If a function $f$ is linear, superposition extends to linear combinations of any number of vectors, and not just linear combination of two vector:

$$
f(\alpha_1\vec{x}_1 + \alpha_2\vec{x}_2 + ... + \alpha_k\vec{x}_k) = \alpha_1 f(\vec{x}_1) + \alpha_2 f(\vec{x}_2) + ... + \alpha_k f(\vec{x}_k)
$$

for any n vector $\vec{x}_1, ..., \vec{x}_k$ and any scalars $\alpha_1, ..., \alpha_k$. To prove this, we simply use the superposition property k times.

Note that: The superposition property sometime broken down into two properties:

- Homogeneity: $f(\alpha\vec{x}) = \alpha f(\vec{x})$
- Additivity: $f(\vec{x} + \vec{y}) = f(\vec{x}) + f(\vec{y})$

**Affine function**

A linear function plus a constant is called an *affine function*. An affine function is a function of the form:

$$
f(\vec{x}) = \vec{a}^T \vec{x} + b
$$

where $\vec{a}$ is an n-vector and $b$ is a scalar.

### 2.2 Taylor approximation

In many applications, scalar-valued functions of n variables, or relations between n variables and a scalar one, can be *approximated* as linear or affine functions. In these cases, the function is approximated by its *Taylor series*.

Let $z$ be an *n-vector*. The (first-order) *Taylor approximation* of a function $f: \mathbb{R}^{n} \rightarrow\mathbb{R}$ at a point $\vec{z}$ is the affine function:

$$
\hat{f}(\vec{x}) = f(\vec{z}) + \nabla f(\vec{z})^T (\vec{x} - \vec{z})
$$

where $\nabla f(\vec{z})$ is the gradient of $f$ at $\vec{z}$, which is an n-vector. The gradient is the vector of partial derivatives of $f$ with respect to each of the n variables.

- $\hat{f}$ is very close to $f$ when $\vec{x}$ is close to $\vec{z}$.

Example: Consider the function $f: \mathbb{R}^{2} \rightarrow\mathbb{R}$ given by $f(x) = \vec{x}_1 + \exp(\vec{x}_2 - \vec{x}_1)$ which is not linear or affine. To find the Taylor approximation $\hat{f}$ near the point $\vec{z} = (1, 2)$, we take partial derivatives to obtain

$$
\nabla f(\vec{z}) = \begin{bmatrix} 1 - \exp(\vec{z}_2 - \vec{z}_1) \\ \exp(\vec{z}_2 - \vec{z}_1) \end{bmatrix}
$$

which evaluates to (-1.7183, 2.7183) at $\vec{z}$. The Taylor approximation is:

$$
\hat{f}(\vec{x}) = f(\vec{z}) + \nabla f(\vec{z})^T (\vec{x} - \vec{z}) = 3 + (-1.7183, 2.7183)^T (\vec{x} - (1, 2))
$$

### 2.3 Regression model

Very commonly used affine function given by:

$$
\hat{y} = \vec{x}^T \beta + b
$$

where $\vec{x}$ is an n-vector of features, $\beta$ is an n-vector of coefficients, and $b$ is a scalar. The model is used to predict a scalar output $y$ from the features $\vec{x}$.

# Chapter 3

### 3.1 Norms and Distance

Given a vector $\vec{x}$, the *norm* of $\vec{x}$ is a nonnegative scalar that measures the length (or size) of the vector. The norm of $\vec{x}$ is denoted by $\| \vec{x} \|$, is the squareroot of the sum of the squares of the elements of $\vec{x}$:

$$
\| \vec{x} \| = \sqrt{x_{1}^2 + x_{2}^2 + ... + x_{n}^2}
$$

It's also can be represent as:

$$
\| \vec{x} \| = \sqrt{\vec{x}^T \vec{x}}
$$

Example:

$$
\| \begin{bmatrix} 1 \\ 2 \\ 3\end{bmatrix} \| = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{14}
$$

**Properties of norms**

- Nonnegativity homogeneity: $\| \beta\vec{x} \| = |\beta| \| \vec{x} \|$
- Triangle 'inequality': $\| \vec{x} + \vec{y} \| \leq \| \vec{x} \| + \| \vec{y} \|$ - You can dive deeper after learning about Cauchy-Schwarz inequality and distance calculation
- Nonnegativity : $\| \vec{x} \| \geq0$
- Definiteness: $\| \vec{x} \| = 0$ if and only if $\vec{x} = \vec{0}$

**Mean squared**

The *mean squared* of a vector $\vec{x}$ is the average of the squares of the elements of $\vec{x}$:

$$
\text{mean squared}(\vec{x}) = \frac{1}{n} \vec{x}^T \vec{x} = \frac{1}{n} \| \vec{x} \|^2
$$

**Root mean squared**

So RMS is the squareroot of the mean squared:

$$
\text{RMS}(\vec{x}) = \sqrt{\text{mean squared}(\vec{x})} = \sqrt{\frac{1}{n} \vec{x}^T \vec{x}} = \frac{1}{\sqrt{n}} \| \vec{x} \|
$$

- The RMS value of a vector *x* is useful when comparing norms of vectors with different dimensions
- Return a 'typical' value of the elements of the vector

**Norm of sums**

The norm of the sum of two vectors is bounded by the sum of the norms of the vectors:

$$
\| \vec{x} + \vec{y} \| = \sqrt{(x + y)^T (x + y)}\\ 

                          = x^Tx + x^Ty + y^Tx +y^Ty\\

                          = \sqrt{\| \vec{x}\|^2 + 2\vec{x}^T\vec{y} + \| \vec{y}\|^2}
$$

**Norm of block vectors**

The norm of a stacked vector is the square root of the sum of the squares of the elements of the vectors

**Chebyshev inequality**

Suppose that *k* of the numbers $|x_1|, |x_2|, ..., |x_n|$ are $\geq a$. Then the sum of the squares of the numbers is $\geq a^2k$:

$$
x_1^2 + x_2^2 + ... + x_n^2\geq a^2k
$$

So:

$$
\| \vec{x} \|^2\geq\sqrt{k} a
$$

This call *Chebyshev inequality*, this used in statistics to provide an upper bound on the probability that a random variable deviates from its mean.

Also RMS can be used to bound the maximum value of a vector:

$$
\frac{k}{n} \leq (\frac{\text{RMS}(\vec{x})}{a})^2
$$

### 3.2 Distance

For the distance, we will separte into categories:

**Euclidean distance (L2)**

The *Euclidean distance* between two vectors $\vec{x}$ and $\vec{y}$ is the norm of the difference of the vectors:

$$
\text{dist} = \| \vec{x} - \vec{y} \|
$$

- Good in many applications but sensitive to outliers

**Mahattan distance (L1 or Taxicab Distance)**

The *Manhattan distance* between two vectors $\vec{x}$ and $\vec{y}$ is the sum of the absolute differences of the elements of the vectors:

$$
\text{dist} = \sum_{i=1}^{n} |x_i - y_i|
$$

- Works well when differences between dimensions are equally important. Used in certain applications of sparse data and linear programming.

**Minkowski distance**

Generalized form of both Euclidean and Manhattan distance:

$$
\text{dist} = (\sum_{i=1}^{n} |x_i - y_i|^p)^{1/p}
$$

- Flexible type in distance calculation, depending on the value of *p*:

  -*p = 1*: Manhattan distance

  -*p = 2*: Euclidean distance

  -*p = $\infty$*: Chebyshev distance

**Chebyshev distance (L-infinity)**

The *Chebyshev distance* between two vectors $\vec{x}$ and $\vec{y}$ is the maximum absolute difference of the elements of the vectors:

$$
\text{dist} = \max_{i} |x_i - y_i|
$$

### 3.3 Standard deviation

For *n-vector* $\vec{x}$, we have:

$$
\text{avg}(\vec{x}) = \frac{1^Tx}{n}
$$

Then de-meaned vector is:

$$
\hat{\vec{x}} = \mu = \vec{x} - \text{avg}(\vec{x}) \vec{1}
$$

Then standard deviation of $\vec{x}$ is:

$$
\text{std}(\vec{x}) = \sqrt{\sigma^2} = \text{rms}(\hat{\vec{x}}) = \sqrt{\frac{\|\vec{x} - (\frac{1^T\vec{x}}{n})\vec{1}\|^2}{n}}
$$

- The standard deviation give 'typical' amount $\vec{x}_i$ vary from the mean
- $\text{std}(\vec{x}) = 0$ if and only if all elements of $\vec{x}$ are equal

We can turn RMS into standard deviation by:

$$
\text{std}(\vec{x}) = \sqrt{\text{mean squared}(\vec{x}) - \text{avg}(\vec{x})^2}
$$

**Properties of standard deviation**

- Adding a constant: For any vector $\vec{x}$ and scalar $c$, $\text{std}(\vec{x} + c) = \text{std}(\vec{x})$. This is because the mean of $\vec{x} + c$ is the mean of $\vec{x}$ plus $c$ so it doesn't change the standard deviation.
- Multiplying by a scalar: For any vector $\vec{x}$ and scalar $c$, $\text{std}(c\vec{x}) = |c| \text{std}(\vec{x})$. This is because the mean of $c\vec{x}$ is $c$ times the mean of $\vec{x}$, and the standard deviation is the RMS of the de-meaned vector.

**Standardization**

In term of AI, there is a bunch of technique to standardize the data. One of the most common is *standardization* or *z-score normalization*. This is done by subtracting the mean and dividing by the standard deviation:

$$
\text{z} = \frac{1}{\text{std}(\vec{x})} (\vec{x} - \text{avg}(\vec{x}) \vec{1})
$$

Standardization is useful when the features have different scales, and we want to give them equal importance range (e.g. [0, 1]).

### 3.4 Angle

**Cauchy-Schwarz inequality**

With two n-vector $\vec{a}$ and $\vec{b}$, the dot product of the vectors is bounded by the product of the norms of the vectors:

$$
|\vec{a}^T \vec{b}| \leq \| \vec{a} \| \| \vec{b} \|
$$

written out:

$$
|a_1 b_1 + a_2 b_2 + ... + a_n b_n| \leq (a_1^2 + a_2^2 + ... + a_n^2)^{\frac{1}{2}} (b_1^2 + b_2^2 + ... + b_n^2)^{\frac{1}{2}}
$$

The inequality cleary hold if $\vec{a}$ and $\vec{b}$ equal to zero. So we suppose now that $\vec{a}$ and $\vec{b}$ are not zero. Then we can define $\alpha = \| \vec{a} \|$ and $\beta = \| \vec{b} \|$. We observe:

$$
0\leq \| \beta\vec{a} - \alpha\vec{b} \|^2 \\ = \beta^2 \| \vec{a} \|^2 - 2\alpha\beta\vec{a}^T \vec{b} + \alpha^2 \| \vec{b} \|^2 \\ = 2\| \vec{a} \|^2 \| \vec{b} \|^2 - 2 \| \vec{a} \| \| \vec{b} \| (a^Tb)
$$

And now we can show triangle inequality based on Cauchy-Schwarz inequality:

$$
\| \vec{a} + \vec{b} \|^2 = \| \vec{a} \|^2 + \| \vec{b} \|^2 + 2\vec{a}^T \vec{b} \leq (\| \vec{a} + \vec{b} \|)^2
$$

**Angle between vectors**

The *angle* between two vectors $\vec{a}$ and $\vec{b}$ is the angle $\theta$ such that:

$$
\theta = \cos^{-1} \frac{\vec{a}^T \vec{b}}{\| \vec{a} \| \| \vec{b} \|}
$$

where $\cos^{-1}$ is the inverse cosine function. The angle is between 0 and $\pi$.

The angle between $\vec{a}$ and $\vec{b}$ is written as $\angle(\vec{a}, \vec{b})$ (can expressed in degrees). The angle is not affected by scaling each of the vector by a positive scalar.

$$
\angle(\vec{a}, \vec{b}) = \angle(\alpha\vec{a}, \beta\vec{b})
$$

Relationship between angle and dot product:

- Orthogonal vectors: $\vec{a}^T \vec{b} = 0$ if and only if $\angle(\vec{a}, \vec{b}) = \frac{\pi}{2}$
- Aligned vectors: $\vec{a}^T \vec{b} = \| \vec{a} \| \| \vec{b} \|$ if and only if $\angle(\vec{a}, \vec{b}) = 0$
- Anti-aligned vectors: $\vec{a}^T \vec{b} = -\| \vec{a} \| \| \vec{b} \|$ if and only if $\angle(\vec{a}, \vec{b}) = \pi$
- Acute angle: $\vec{a}^T \vec{b} > 0$ if and only if $\angle(\vec{a}, \vec{b}) < \frac{\pi}{2}$
- Obtuse angle: $\vec{a}^T \vec{b} < 0$ if and only if $\angle(\vec{a}, \vec{b}) > \frac{\pi}{2}$

**Norm of sum via angles**

For vectors *x* and *y*, we have:

$$
\| \vec{x} + \vec{y} \|^2 = \| \vec{x} \|^2 + \| \vec{y} \|^2 + 2 \| \vec{x} \| \| \vec{y} \| \cos(\angle(\vec{x}, \vec{y}))
$$

Where $\theta = \angle(\vec{x}, \vec{y})$. From this we can make obersevation:

- If *x* and *y* are aligned (angle = 0), then $\| \vec{x} + \vec{y} \| = \| \vec{x} \| + \| \vec{y} \|$. Thus, norm addition.
- If *x* and *y* are orthogonal (angle = $\frac{\pi}{2}$), then $\| \vec{x} + \vec{y} \| = \sqrt{\| \vec{x} \|^2 + \| \vec{y} \|^2}$. Thus, *Pythagorean theorem*.

**Correlation coefficient**

Suppose $\vec{a}$ and $\vec{b}$ are two n-vectors, with associated de-meaned vectors

$$
\hat{\vec{a}} = \vec{a} - \text{avg}(\vec{a}) \vec{1}
$$

$$
\hat{\vec{b}} = \vec{b} - \text{avg}(\vec{b}) \vec{1}
$$

Assume that $\| \hat{\vec{a}} \| \neq0$ and $\| \hat{\vec{b}} \| \neq0$. The *correlation coefficient* between $\vec{a}$ and $\vec{b}$ is:

$$
\text{corr}(\vec{a}, \vec{b}) = p = \frac{\hat{\vec{a}}^T \hat{\vec{b}}}{\| \hat{\vec{a}} \| \| \hat{\vec{b}} \|}
$$

Thus, $p = \cos(\theta)$, where $\theta = \angle(\hat{\vec{a}}, \hat{\vec{b}})$. With $\text{corr}(\vec{a}, \vec{b}) \in [-1, 1]$. The correlation coefficient is a measure of the linear relationship between two vectors.

We also can express correlation coefficient in terms of the vectors $\vec{u}$ and $\vec{v}$ obtained by standardizing the vectors. With $u = \frac{\hat{\vec{a}}}{\text{std}(\vec{a})}$ and $v = \frac{\hat{\vec{b}}}{\text{std}(\vec{b})}$, we have:

$$
\text{corr}(\vec{a}, \vec{b}) = p = \frac{u^Tv}{n}
$$

**Standard deviation of sum**

We can derive a formula for the standard deviation of a sum from:

$$
\text{std}(\vec{a} + \vec{b}) = \sqrt{\text{std}(\vec{a})^2 + 2p\text{std}(\vec{a})\text{std}(\vec{b}) + \text{std}(\vec{b})^2}
$$

### 3.5 Complexity

- Norm calculation and RMS value take $2n$ flops.
- Distance take $3n$ flops.
- Angle calculation take $6n$ flops.
- De-mean vector take $2n$ flops.
- Standard deviation take $4n$ flops.
- Standardizing costs $5n$ flops.
- Correlation coefficient take $10n$ flops.

# Chapter 4: Clustering

### 4.1 Clustering
