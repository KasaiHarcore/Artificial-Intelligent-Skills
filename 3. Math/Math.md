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

- Right | Left Distributive: $c (\vec{a} + \vec{b}) = c \vec{a} + c \vec{b}$ || $(c + d) \vec{a} = c \vec{a} + d \vec{a}$
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

For short, we can say:

- Given $N$ n-vectors $\vec{x}_1, \vec{x}_2, ..., \vec{x}_N$.
- Goal: Partition (divide, cluster) into $k$ groups
- Want vectors in the same group to be close to one another.

Let's $G_j \subset ({1, \cdots, N})$ is group $j$ for $j = 1, 2, ..., k$; $c_i$ is group that $x_i$ is in: $i \in G_{c_i}$.

Example: I have 4 number $1,2,3,4$ and I want to divide them into 2 groups. Then $G_1 = \{1, 2\}$ and $G_2 = \{3, 4\}$. With $c_1 = 1$ and $c_2 = 1$.

With each group represent *n-vector*. And we want each representative to be close to the vectors in the group. Thus $ \| \vec{x}_i - \vec{z}_j \|$ to be small. Where $\vec{z}_j$ is the representative of group $j$.

So the clustering objective is to minimize the sum of the squared distances of each vector to its representative:

$$
J^{\text{clust}} = \frac{1}{N} \sum_{i=1}^{N} \| \vec{x}_i - \vec{z}_{c_i} \|^2
$$

Because $c_i$ only appears in term $\| \vec{x}_i - \vec{z}_{c_i} \|^2$, so we have to minimize over $c_i$:

$$
\| \vec{x}_i - \vec{z}_{c_i} \|^2 = \min_{j} \| \vec{x}_i - \vec{z}_j \|^2
$$

Ok so after we have partitioned the vectors into groups, we can find the representative of each group by minimizing the sum of the squared distances of the vectors in the group to the representative:

$$
J^{\text{clust}} = J_1 + \cdots + J_k
$$

Where:

$$
J_j = \frac{1}{N} \sum_{i \in G_j} \| \vec{x}_i - \vec{z}_j \|^2
$$

So that we choose $z_j$ to minimize mean squared distance of vectors in group $j$ to $z_j$. This mean:

$$
z_j = \frac{1}{|G_j|} \sum_{i \in G_j} \vec{x}_i
$$

K-mean algorithms can be using in many application such as: Classification, Guessing missing entries, Recommendation Engine, Document clustering, etc.

# Chapter 5: Linear Independence

### 5.1 Linear dependence

Set of *n-vectors* ${a_1, \cdots, a_k}$ (with $k \geq1$) are *linearly independent* if:

$$
\beta_1 a_1 + \cdots + \beta_k a_k = 0
$$

For some $\beta_1, \cdots, \beta_k$ not all zero.

From here we can proof a set of vectors are linearly dependent by proof a random $a_i$ can be written as a linear combination of the other vectors.

$$
a_i = \sum_{j \neq i} -\frac{\beta_j}{\beta_i} a_j
$$

**NOTE THAT**: Linear independence is a property of a set of vectors, not of a single vector.

Some properties:

- {$a_1$} is linearly dependent only if $a_1 = 0$.
- {$a_1, a_2$} is linearly dependent if only one $a_i$ is a multiple of the other

**Linear Independence**

A collection of *n_vectors* $a_1, \cdots, a_k$ (with $k \geq1$) is *linearly independent* if it's not linearly dependent:

$$
\beta_1 a_1 + \cdots + \beta_k a_k = 0
$$

Only holds for $\beta_1 = \cdots = \beta_k = 0$. Which mean only independent if all coefficients is zero.

Example:

- A list consisting of a single vector is linearly dependent only if the vector is zero. Else, it's linearly independent (vector is not zero).
- Any list of vectors containing the zero vector is linearly dependent.
- A list of vectors is linearly dependent if and only if one of the vectors is a multiple of the other one
- The vectors:

$$
a_1 = \begin{bmatrix} 0.2 \\ -7.0 \\ 8.6\end{bmatrix}, a_2 = \begin{bmatrix} -0.1 \\ 2.0 \\ -1.0\end{bmatrix}, a_3 = \begin{bmatrix} 0.0 \\ -1.0 \\ 2.2\end{bmatrix}
$$

are linearly dependent, since $a_1 + 2a_2 - 3a_3 = 0$. We can express any of these vectors as a linear combination of the other two.

- The vectors:

$$
a_1 = \begin{bmatrix} 1 \\ 0 \\ 0\end{bmatrix}, a_2 = \begin{bmatrix} 0 \\ -1 \\ 1\end{bmatrix}, a_3 = \begin{bmatrix} -1 \\ 1 \\ 1\end{bmatrix}
$$

are linearly independent. We can't express any of these vectors as a linear combination of the other two. Which can only be true if all coefficients are zero.

**Linear combinations of linearly independent vectors**

Suppose $x$ is linear combination of lnearly independent vectors $a_1, \cdots, a_k$:

$$
x = \beta_1a_1 + \cdots + \beta_ka_k
$$

Then coefficients $\beta_1, \cdots, \beta_k$ are unique, if:

$$
x = \gamma_1a_1 + \cdots + \gamma_ka_k
$$

Then $\beta_i = \gamma_i$ for all $i = 1, \cdots, k$.

To see this, we can subtract the two equations to get:

$$
0 = (\beta_1 - \gamma_1)a_1 + \cdots + (\beta_k - \gamma_k)a_k
$$

Which only be true if $\beta_i - \gamma_i = 0, \forall i$ This gives us a good interpretation: A list of vectors is linearly independent if and only if for any linear combination of them, we can infer or deduce the associated coefficients.

**Superset**: If we add vectors to a linearly dependent collection of vectors, the new collection is also linearly dependent.

**Subset**: Removing vectors from a collection of vectors preserves linear independence.

### 5.2 Basis

**Independence-dimension inequality** If the *n-vector* $a_1, \cdots, a_k$ are linearly independent, then $k \leq n$, In words:

***A linearly independent collection of n-vector can have at most n elements***

In other way:

***Any collection of n + 1 or more n-vectors is linearly dependent***

This can be show by using Basis:

**Basis**: A collection of *n* linearly independent n-vector is called a *basis*. If the n-vectors $a_1, \cdots, a_n$ are a basis, then any n-vector $b$ can be expressed as a linear combination of the basis vectors:

$$
\beta_1a_1 + \cdots + \beta_na_n + \beta_{n + 1}b = 0
$$

If $\beta_{n + 1} = 0$, then we have:

$$
\beta_1a_1 + \cdots + \beta_na_n = 0
$$

Which since $a_1, \cdots, a_n$ are linearly independent, we have $\beta_1 = \cdots = \beta_n = 0$. But if the linear combination is 0, which mean all $\beta_i$ are zero. So we conclude that $\beta_{n + 1} \neq0$. If it's not zero then:

$$
b = (\frac{-\beta_1}{\beta_{n + 1}})a_1 + \cdots + (\frac{-\beta_n}{\beta_{n + 1}})a_n
$$

**Expansion in a basis**:

Any n-vector b can be expressed as linear combination of them:

$$
b = \beta_1a_1 + \cdots + \beta_na_n
$$

for some $\beta_1, \cdots, \beta_n$. The coefficients are unique.

### 5.3 Orthonormal vectors

- Set of n-vectors $a_1, \cdots, a_k$ are (mutually) *orthogonal* if $a_i \perp a_j$ for all $i \neq j$.
- They are normalized if $\| a_i \| = 1$ for all $i$.

=> The are orthonormal if both hold, and can be expressed using inner products as:

$$
a_i^T a_j = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}
$$

**Linear independence of orthonormal vectors**: To see this, suppose $a_1, \cdots, a_k$ are orthonormal:

$$
\beta_1a_1 + \cdots | \beta_ka_k = 0
$$

Taking inner product with $a_i$:

$$
0 = a_i^T(\beta_1a_1 + \cdots + \beta_ka_k) \\

= \beta_1(a_i^Ta_1) + \cdots + \beta_k(a_i^Ta_k) \\

= \beta_i
$$

since $a_i^Ta_j = 0$ for $i \neq j$ and $a_i^Ta_i = 1$. Thus, $\beta_i = 0$ for all $i$. The linear combination of $a_1, \cdots, a_k$ that is zero is the one with all coefficients zero.

**Linear combinations of orthonormal vectors**: Suppose a vector x is a linear combination of $a_1, \cdots, a_k$ where $a_1, \cdots, a_k$ are orthonormal:

$$
x = \beta_1a_1 + \cdots + \beta_ka_k
$$

Taking the inner product of the left-hand and right-hand sides of this equation with $a_i$ yields:

$$
a_i^Tx = a_i^T(\beta_1a_1 + \cdots + \beta_ka_k) = \beta_i
$$

using the same argument as above. So if a vector is a linear combination of orthonormal vector, we can easily find the coefficients of the linear combination by taking the inner product of the vectors.

**Orthonormal basis**: Is a set of vectors that are mutually orthogonal and have unit length.

### 5.4 Gram-Schmidt (orthogonalization) algorithm

This is an algorithm to check if $a_1, \cdots, a_k$ are linearly independent

Given n-vectors $a_1, \cdots, a_k$. For $i = 1, \cdots, k$:

1. Orthogonalization:$\hat{q_i} = a_i - (q_1^Ta_i)q_1 - \cdots - (q_{i-1}^Ta_i)q_{i-1}$
2. Test for linear dependence: if$\hat{q_i} = 0$, then $a_1, \cdots, a_k$ are linearly dependent => quit
3. Normalization:$q_i = \hat{q_i} / ||\hat{q_i}||$

- if G-S does not stop early, then $a_1, \cdots, a_k$ are linearly independent
- if G-S stops early in iteration $i = j$, then $a_j$ is a linear combination of $a_1, \cdots, a_{j-1}$ (so $a_1, \cdots, a_k$ are linearly dependent)

**Analysis of Gram-Schmidt algorithm**: Let show that the following hold, for $i = 1, \cdots, k$, assuming that $a_1, \cdots, a_k$ are linearly independent:

1. $\hat{q_i} \neq0$, so the linear dependence test in step 2 is not satisfied, and we do not have a divide-by-zero error in step 3.
2. $q_1, \cdots, q_i$ are orthonormal.
3. $a_i$ is a linear combination of $q_1, \cdots, q_i$.
4. $q_i$ is a linear combination of $a_1, \cdots, a_i$.

We can show this by induction: For $q_1, \cdots, q_i$ are orthonormal, assume it's true for $i - 1$. We will:

- Make orthogonalization step ensures that: $\hat{q_i} \perp q_1, \cdots, \hat{q_i} \perp q_{i-1}$. To see this:

$$
q_j^T\hat{q_i} = q_j^T a_i - (q_1^Ta_i)(q_j^Tq_1) - \cdots - (q_{j-1}^Ta_i)(q_j^Tq_{j-1}) = q_j^Ta_i - q_j^Ta_i = 0, \forall j < i
$$

- So $q_1, \cdots, q_i$ are orthonormal.
- Normalization step ensures that $\|q_i\| = 1$.

Assuming G-S has not terminate before iteration $i$

- $a_i$ is a linear combination of $q_1, \cdots, q_i$:

$$
a_i = \hat{q_i} + (q_1^Ta_i)q_1 + \cdots + (q_{i-1}^Ta_i)q_{i-1} = q_i + (q_1^Ta_i)q_1 + \cdots + (q_{i-1}^Ta_i)q_{i-1}
$$

- $q_i$ is a linear combination of $a_1, \cdots, a_i$, by induction on $i$:

$$
q_i = \frac{1}{\hat{\|q_i\|}} (a_i - (q_1^Ta_i)q_1 - \cdots - (q_{i-1}^Ta_i)q_{i-1})
$$

and (by induction assumpption) each $q_1, \cdots, q_{i-1}$ is a linear combination of $a_1, \cdots, a_{i-1}$.

**Complexity**:

- Step 1 of iteration $i$ requires $i - 1$ inner products which cost $(i - 1)(2n - 1)$ flops
- Need $2n(i - 1)$ flops to compute $\hat{q_i}$
- $3n$ flops to compute $\|\hat{q_i}\|$ and $q_i$
- Total cost: $\sum_{i = 1}^{k} ((4n - 1)(i - 1) + 3n) = (4n - 1) \frac{k(k - 1)}{2} + 3kn = O(kn^2)$

Where using $\sum_{i = 1}^{k} i = \frac{k(k + 1)}{2}$

# Chapter 6: Matrices

### 6.1 Matrices

A matrix is a rectangular array of numbers, e.g:

$$
\begin{bmatrix} 0 & 1 & -2.3 & 0.1 \\ 1.3 & 4 & -0.1 & 0 \\ 4.1 & -1 & 0 & 1.7\end{bmatrix}
$$

- It's size given by (row dimension) x (column dimension). The matrix above is a 3x4 matrix.
- Elements also called entries or coefficients.
- $B_{ij}$ is the element in the $i$-th row and $j$-th column.
- $i$ is the row index, $j$ is the column index; indexes start at 1.
- Two matrices are equal (denoted with $=$) if they have the same size and their corresponding elements are equal.

**Matrix indexing**: Standard notation indexs the rows and columns of a matrix starting from 1. In computer language, it's often stored as 2-dimensional arrays, which are indexed starting from 0. Some advance programming level allow to index starting from 1.

**Square, tall, and wide matrices**:

- Square: number of rows = number of columns.
- Tall: number of rows > number of columns.
- Wide: number of rows < number of columns.

**Column and row vector**: An n-vector can be interpreted as an $n \times1$ matrix; we do not distinguish between vectors and matrices with one column. A row vector can be interpreted as a $1\times n$ matrix which is 1 row and n columns. Matrix with size $1\times1$ is a scalar.

**Block matrices and Submatrices**: A block matrix is a matrix whose elements are matrices. A submatrix is a matrix formed by selecting certain rows and columns of a matrix.

Example:

$$
A = \begin{bmatrix} B & C \\ D & E \end{bmatrix}
$$

Consider with real number:

$$
B = \begin{bmatrix} 0 & 2 & 3\end{bmatrix}
$$

$$
C = \begin{bmatrix} -1\end{bmatrix}
$$

$$
D = \begin{bmatrix} 2 & 2 & 1 \\ 1 & 3 & 5\end{bmatrix}
$$

$$
E = \begin{bmatrix} 4 & 4\end{bmatrix}
$$

Then:

$$
A = \begin{bmatrix} 0 & 2 & 3 & -1 \\ 2 & 2 & 1 & 4 \\ 1 & 3 & 5 & 4\end{bmatrix}
$$

With submatrix, it have a general form as:

$$
A_{p:q, r:s} = \begin{bmatrix} A_{p,r} & A_{p,r+1} & \cdots & A_{p,s} \\ A_{p+1,r} & A_{p+1,r+1} & \cdots & A_{p+1,s} \\ \vdots & \vdots & \ddots & \vdots \\ A_{q,r} & A_{q,r+1} & \cdots & A_{q,s} \end{bmatrix}
$$

Example:

$$
A_{2:3, 3:4} = \begin{bmatrix} 1 & 4 \\ 5 & 4\end{bmatrix}
$$

**Relation matrice**

A relation is a set of pairs of object, labeled $1, \cdots, n$ such as:

$$
\mathcal{R} = \{ (i, j) \mid i, j \in \{1, \cdots, n\} \}
$$

Example with a directed graph:

$$
\mathcal{R} = \{ (1, 2), (1, 3), (2, 3), (3, 1) \}
$$

Can be represented as a matrix:

$$
A = \begin{bmatrix} 0 & 1 & 1 \\ 0 & 0 & 1 \\ 1 & 0 & 0\end{bmatrix}
$$

Where $A_{ij} = 1$ if $(i, j) \in\mathcal{R}$ and $0$ otherwise.

### 6.2 Zero and identity matrices

**Zero matrix**: A matrix with all elements equal to zero. Denoted by $0$ or $0_{m \times n}$.

**Identity matrix**: A square matrix with ones on the diagonal and zeros elsewhere. Denoted by $I$ or $I_n$. can be express:

$$
I_{ij} = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}
$$

The column vectors of the $n \times n$ identity matrix are the unit vectors of size n. Using block matrix notation with vector $e_i$:

$$
I = \begin{bmatrix} e_1 & e_2 & \cdots & e_n \end{bmatrix}
$$

Where $e_k$ is the k-th column of the identity matrix. Some time a subscript is used to denote the size of the identity matrix, e.g $I_{m \times n}$. Example:

$$
A = \begin{bmatrix} 1 & 2 & 3\\ 4 & 5 & 6\end{bmatrix}
$$

then:

$$
\begin{bmatrix} I & A \\ 0 & I \end{bmatrix} = \begin{bmatrix} 1 & 0 & 1 & 2 & 3 \\ 0 & 1 & 4 & 5 & 6 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1\end{bmatrix}
$$

**Spare matrices**: Same like vector, if most of the elements in a matrix are zero, it's called a sparse matrix. It's often stored in a special format to save memory.

**Diagonal matrix**: A square matrix with non-zero elements only on the diagonal. Denoted by $D$, $D_n$ or $\text{diag}$. Example:

**Traingular matrix**: A square matrix with all elements above or below the diagonal equal to zero. A lower triangular matrix has all elements above the diagonal equal to zero. A upper triangular matrix has all elements below the diagonal equal to zero.

### 6.3 Transpose, addition, and norm

##### 6.3.1 Transpose

The transpose of an $m \times n$ matrix $A$ is denoted $A^T$, and defined by:

$$
A^T_{ij} = A_{ji, i = 1, \cdots, m, j = 1, \cdots, n}
$$

Example:

$$
\begin{bmatrix} 0 & 4 \\ 7 & 0 \\ 3 & 1\end{bmatrix}^T = \begin{bmatrix} 0 & 7 & 3 \\ 4 & 0 & 1\end{bmatrix}
$$

Transpose converts columns to row vectorrs and vice versa. It has the following properties:

- $(A^T)^T = A$
- $(A + B)^T = A^T + B^T$
- $(\alpha A)^T = \alpha A^T$

**Tranpose of block matrices**: The transpose of a block matrix is the block of each matrix transposed inside the block. Example:

$$
\begin{bmatrix} A & B \\ C & D \end{bmatrix}^T = \begin{bmatrix} A^T & C^T \\ B^T & D^T \end{bmatrix}
$$

**Document-term matrix**: Consider a corpus (collection) of N documents, with word count vectors for a dictionary with n words. The *document-term* matrix associated with the corpus is an $N \times n$ matrix $A$ where $A_{ij}$ is the number of times word $j$ appears in document $i$. The transpose of the document-term matrix is the *term-document* matrix.

**Data matrix**: Consider a dataset with n samples and p features. The data matrix is an $n \times p$ matrix $X$ where $X_{ij}$ is the value of the j-th feature for the i-th sample. The transpose of the data matrix is the *feature matrix*.

**Symmetric matrix**: A square matrix is symmetric if $A = A^T$. It has the following properties:

- $(A + B)^T = A^T + B^T$
- $(\alpha A)^T = \alpha A^T$

##### 6.3.2 Addition, Subtraction and Scalar Multiplication

Same like vector, we can add or subtract matrices of the same size:

$$
(A + B)_{ij} = A_{ij} + B_{ij}
$$

Scalar multiplication:

$$
(\alpha A)_{ij} = \alpha A_{ij}
$$

Properties:

- $A + B = B + A$
- $\alpha (A + B) = \alpha A + \alpha B$
- $(A + B)^T = A^T + B^T$

##### 6.3.3 Norm

The norm of a matrix is a generalization of the notion of length for vectors. The most common norm is the Frobenius norm:

$$
\|A\|_F = \sqrt{\sum_{i=1}^m \sum_{j=1}^n |A_{ij}|^2}
$$

Agrees with vector norm when $n = 1$. It has the following properties:

- $\|A\|_F \geq0$
- $\|A\|_F = 0$ if and only if $A = 0$
- $\|\alpha A\|_F = |\alpha| \|A\|_F$
- $\|A + B\|_F \leq \|A\|_F + \|B\|_F$

Distance between matrices: $d(A, B) = \|A - B\|_F$

### 6.4 Matrix-vector multiplication

If $A$ is an $m \times n$ matrix and $x$ is an $n$-vector, then the matrix-vector product $y = Ax$ is them $m$-vector $y$ with elements:

$$
y_i = \sum_{k = 1}^{n}A_{ik}x_k = A_{i1}x_1 + \cdots + A_{in}x_n
$$

Example:

$$
\begin{bmatrix} 0 & 2 & -1 \\ -2 & 1 & 1\end{bmatrix} \begin{bmatrix} 2 \\ 1 \\ -1\end{bmatrix} = \begin{bmatrix} 0\cdot2 + 2\cdot1 + (-1) \cdot (-1) \\ -2\cdot2 + 1\cdot1 + 1\cdot (-1) \end{bmatrix} = \begin{bmatrix} 3 \\ -4\end{bmatrix}
$$

**General examples:**

- Zero matrix: $0\cdot x = 0$
- Identity matrix: $I \cdot x = x$
- Picking out columns and rows: $A \cdot e_i = i$ and $e_j^T \cdot A = A_j$
- Summing or averaging columns or rows: The $m$-vector $A1$ is the sum of the columns of $A$; its $i$-th entry is the sum of the entries in the $i$-th row of A. Average can be made by dividing by $n$.
- Difference Maitrx: The $(n - 1) \times n$ matrix:

$$
D = \begin{bmatrix} -1 & 1 & 0 & \cdots & 0 \\ 0 & -1 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & 1\end{bmatrix}
$$

The vector $Dx$ is the vector of differences of consecutive entries of $x$:

$$
Dx = \begin{bmatrix} x_2 - x_1 \\ x_3 - x_2 \\ \vdots \\ x_n - x_{n - 1} \end{bmatrix}
$$

- Running sum matrix: The $n \times n$ matrix:

$$
S = \begin{bmatrix} 1 & 0 & 0 & \cdots & 0 \\ 1 & 1 & 0 & \cdots & 0 \\ 1 & 1 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & 1 & 1 & \cdots & 1\end{bmatrix}
$$

is called the running sum matrix. The $i$-th entry of the *n*-vector $Sx$ is the sum of the first $i$ entries of $x$:

$$
Sx = \begin{bmatrix} x_1 \\ x_1 + x_2 \\ x_1 + x_2 + x_3 \\ \vdots \\ x_1 + x_2 + \cdots + x_n \end{bmatrix}
$$

**Inner product:** When $a$ and $b$ are vectors of the same length, their inner product is the sum of the products of their corresponding entries. The inner product of $a$ and $b$ is denoted by $a \cdot b$ or $a^Tb$:

**Linear dependence of columns:** We can express the conceopts of linear dependence and independence of vectors in terms of matrix-vector multiplication. The columns of a matrix $A$ are linearly dependent if $Ax = 0$ for some $x \neq0$. The columns of a matrix $A$ are linearly independent if $Ax = 0$ implies $x = 0$.

**Expansion in a basis:** If the columns of $A$ are a basis, which means $A$ is square with linearly independent columns $a_1, \cdots, a_n$, then for any n-vector $b$ there is a unique n-vector $x$ that satisfies $Ax = b$. In this case, vector $x$ gives the coefficient in the expansion of $b$ in the basis $a_1, \cdots, a_n$.

- Properties of matrix-vector multiplication:

  - $(A + B)x = Ax + Bx$
  - $(\alpha A)x = \alpha(Ax)$

### 6.5 Complexity

In computer represent, An $m \times n$ matrix usually represent as an array of floating point number, which need $8mn$ bytes. Some factor to stores more efficiently by using spare or traigular matrix.

For matrix addition, subtraction, scalar multiplication, for a normal operation, need $mn$ flops. When it's spare, scalar multiplication can be done in $\text{nnz}(A)$ flops. If one of two matrix is spare, it need $\min \{ \text{nnz}(A), \text{nnz}(B) \}$ flops. While add or sub need only $\text{nnz}(A) + \text{nnz}(B)$ flops.

Transposition only need 0 flops

Matrix-vector multiplication need $m(2n - 1)$ flops for a matrix $m \times n$ and a vector $n$. Which can be simplify to $2mn$ flops

# Chapter 7: Matrix Example

### 7.1 Geomatric transformations

**Scaling** is the mapping $y = ax$, where $a$ is a scalar. This can be expressed as $y = Ax$, with $A = aI$. This mapping stretches a vector by factor $|a|$ (or shrinks if $|a| < 1$), and flips the vector if $a < 0$.

**Dilation** is the mapping $y = Dx$, where $D$ is a diagonal matrix, $D = \text{diag}(d_1, d_2)$. This mapping stretches or shrinks the vector by different factors along the two different axes (Or shinks if $d_i < 1$ and flips if $d_i < 0$).

**Rotation** Suppose that $y$ is the vector obtained by rotating $x$ by $\theta$ radians counterclockwise. Then we have:

$$
y = \begin{bmatrix} \cos (\theta) & -\sin (\theta) \\ \sin (\theta) & \cos (\theta) \end{bmatrix}x
$$

**Reflection** Suppose that $y$ is the vector obtained by reflecting $x$ through the line that passes through the origin, inclined $\theta$ radians with respect to horizontal:

$$
y = \begin{bmatrix} \cos (2\theta) & \sin (2\theta) \\ \sin (2\theta) & -\cos (2\theta) \end{bmatrix}x
$$

**Projection onto a line** The projection of the point $x$ onto a set is the point in the set that closet to $x$

$$
y = \begin{bmatrix} (1/2)(1 + \cos(2\theta)) & (1/2)(\sin(2\theta)) \\ (1/2)(\sin(2\theta)) & (1/2)(1 - \cos(2\theta)) \end{bmatrix}x
$$

**Finding the matrix**: When a geometric transformation is represented by matrix-vector multiplication, a simple method to find the matrix is to find its columns. The $i$-th columns is the vector obtained by applying the transformation to $e_i$

**Change of coordinates** Suppose we are on a plane with three axes point, the 3-vector $x^{\text{body}}$ describes a location using the body coordinates, and $x^{\text{earth}}$ describes the same location in earth-fixed coordinates. Then we have:

$$
x^{\text{earth}} = p + Qx^{\text{body}}
$$

where $p$ is the location of the airplane center and $Q$ is a $3\times3$ matrix. The $i$-th column of $Q$ gives the earth-fixed coordinates for the $i$-th axis of the airplane. For an airplane in level flight, heading due South, we have:

$$
Q = \begin{bmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 1\end{bmatrix}
$$

### 7.2 Selectors matrix

An $m \times n$ selector matrix: each row is a unit vector:

$$
A = \begin{bmatrix} e_{i_1}^T \\ e_{i_2}^T \\ \vdots \\ e_{i_m}^T \end{bmatrix}
$$

When it multiplies a vector, it simply copies the $k_{i}th$ entry of $x$ into the $i_{th}$ entry of $y = Ax$:

$$
y = (x_{k_1}, x_{k_2}, \cdots, x_{k_m})
$$

In words, each entry of $Ax$ is a selection of an entry of $x$. The identity matrix, and the *reverser matrix* are special cases of the selector matrix.

For slicing matrix:

$$
A = \begin{bmatrix} 0_{m \times (r - 1)} & I_(m \times m) & 0_{m \times (n - s)} \end{bmatrix}
$$

Where $m = s - r + 1$. We have $Ax = x_{r:s}$ multiplying by $A$ gives the r:s slice of a vector.

**Down-sampling**. Another example is the $(n / 2) \times n$ matrix (with n odd):

$$
A = \begin{bmatrix} 1 & 0 & 0 & 0 & \cdots & 0 & 0 \\ 0 & 0 & 1 & 0 & \cdots & 0 & 0 \\ 0 & 0 & 0 & 0 & \cdots & 0 & 1\end{bmatrix}
$$

If $y = Ax$, we have $y = (x_1, x_3, x_5, \cdots, x_{n - 1})$. When $x$ is a time series, $y$ is called the $2\times$ down-sampled version of $x$.

**Image cropping** Suppose $x$ is an image with $M \times N$ pixels (both even). Let $y$ be the $(M / 2) \times (N / 2)$ image that is the upper left corner of the image $x$ is a cropped version. Then we have $y = Ax$, where $A$ is an $(MN / 4) \times (MN)$ selector matrix.

**Permutation matrices** An $n \times n$ *permutation matrices* is ine in which each colomns is a unit vector, and each row is transpose of a unit vector. This mean $y = Ax$ can be expressed as $y_i = x_{\pi_i}$, where $\pi$ is a permutation. Example: Consider the permutation $\pi = (3, 1, 2)$, the associated matrix is:

$$
A = \begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}
$$

Multiplying a 3-vector by A re-orders its entries

### 7.3 Incidence matrix

**Directed Graph**

A graph with *n* vertices or nodes, m (directed) edges or links. Each edge connected from on of the nodes and into another one. DG are often drawn with vertices as circles or dot, and the edges as arrows.

Incidence matrix is $n \times m$ matrix:

$$
A_{ij} = \begin{cases} 1 \text{ edge j points to node i} \\
-1 \text{ edge j points from node i} \\
0 \text{ otherwise}\end{cases}
$$

Example with $n = 4$ and $m = 5$ (or in words is 4 vertices 5 edges):

- From node 1: (1, 2), (1, 4)
- From node 2: (2, 3)
- From node 3: (3, 4), (3, 1)
- From node 4: None

Then we will have a matrix:

$$
A = \begin{bmatrix} -1 & -1 & 0 & 0 & 0 \\ 1 & 0 & -1 & 0 & 0 \\ 0 & 0 & 1 & -1 & -1 \\ 0 & 1 & 0 & 0 & 1\end{bmatrix}
$$

##### 7.3.1 Networks

**Flow conservation**

- m-vector $x$ gives flows (of something) along the edges
- examples: heat, money, power, mass, people,...
- $x_j > 0$ means flow follows edge direction
- $Ax$ is *n*-vector that gives the total or net flows
- $(Ax)_i$ is the net flow into node $i$
- $Ax = 0$ is flow conservation; $x$ called a circulation (From a point follow any edge that go back to that same point)
