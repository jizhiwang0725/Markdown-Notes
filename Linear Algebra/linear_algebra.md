<link rel="stylesheet" href="../style.css">

# Table of contents 
- [Table of contents](#table-of-contents)
- [Vectors](#vectors)
  - [Linear combination](#linear-combination)
  - [Span](#span)
  - [Linear independence](#linear-independence)
  - [Basis](#basis)
  - [Dimension](#dimension)
  - [Unit vector](#unit-vector)
  - [Cross-product](#cross-product)
- [Angle \& Inner Product](#angle--inner-product)
  - [Inner product](#inner-product)
  - [Sin rule](#sin-rule)
  - [Cauchy - Schwarz inequality](#cauchy---schwarz-inequality)
  - [Triangle inequality](#triangle-inequality)
  - [Area of parallelogram](#area-of-parallelogram)
- [Matrix](#matrix)
  - [Rows and columns](#rows-and-columns)
  - [Matrix multiplication (outer product)](#matrix-multiplication-outer-product)
  - [Rank](#rank)
  - [Transpose operations](#transpose-operations)
  - [Symmetric matrix](#symmetric-matrix)
  - [Matrix mapping](#matrix-mapping)
- [Square Matrices](#square-matrices)
  - [Upper/Lower triangular](#upperlower-triangular)
  - [Determinant](#determinant)
  - [Determinant properties](#determinant-properties)
  - [Determinant operations](#determinant-operations)
  - [Inverse](#inverse)
- [Norms](#norms)
  - [General equations](#general-equations)
  - [The 1-norm (Manhattan norm)](#the-1-norm-manhattan-norm)
  - [The 2-norm (Euclidean norm)](#the-2-norm-euclidean-norm)
  - [The infinity norm (Maximum/Chebyshev norm)](#the-infinity-norm-maximumchebyshev-norm)
  - [Frobenius norm (matrix only)](#frobenius-norm-matrix-only)
- [Linear Systems](#linear-systems)
  - [Linear equation](#linear-equation)
  - [System of linear equations](#system-of-linear-equations)
  - [Solving linear systems (Gaussian elimination)](#solving-linear-systems-gaussian-elimination)
- [Least Squares](#least-squares)
  - [Normal equation](#normal-equation)
  - [Moore-Penrose inverse (pseudo-inverse)](#moore-penrose-inverse-pseudo-inverse)
  - [QR decomposition (Gram-Schmidt process)](#qr-decomposition-gram-schmidt-process)
- [Four fundamental subspaces](#four-fundamental-subspaces)
  - [Subspace](#subspace)
  - [Finding four fundamental subspaces](#finding-four-fundamental-subspaces)
  - [Four subspaces as a "instruction manual" for a matrix](#four-subspaces-as-a-instruction-manual-for-a-matrix)
  - [Rank-nullity theorem](#rank-nullity-theorem)
  - [Orthogonal components](#orthogonal-components)
- [Linear transformation](#linear-transformation)
  - [Definition](#definition)
  - [Terminology](#terminology)
  - [Projection](#projection)
  - [Projection operator](#projection-operator)
  - [Projection along all-1s vector (mean)](#projection-along-all-1s-vector-mean)
  - [Reflection operator](#reflection-operator)
- [Orthogonal Systems (Gram-Schmidt Process)](#orthogonal-systems-gram-schmidt-process)
  - [Orthogonal matrix](#orthogonal-matrix)
  - [Semi-orthogonal matrix](#semi-orthogonal-matrix)
  - [Properties of orthogonal matrix](#properties-of-orthogonal-matrix)
  - [Spectral theorem](#spectral-theorem)
  - [Gram-Schmidt process](#gram-schmidt-process)
- [Eigenthings](#eigenthings)
  - [Eigenvalue](#eigenvalue)
  - [Eigenvector](#eigenvector)
  - [Eigenspace](#eigenspace)
  - [Special matrices](#special-matrices)
  - [Geometric/Algebraic multiplicity](#geometricalgebraic-multiplicity)
- [Similar Matrices](#similar-matrices)
  - [Change of basis](#change-of-basis)
  - [Sharing properties](#sharing-properties)
- [Diagonalization](#diagonalization)
  - [Diagonalizability](#diagonalizability)
  - [Goal](#goal)
  - [Calculation](#calculation)
- [Singular Value Decomposition (SVD)](#singular-value-decomposition-svd)
  - [Different components](#different-components)
  - [Geometric concept](#geometric-concept)
  - [Full SVD](#full-svd)
  - [Thin SVD](#thin-svd)
  - [Rank-1 decomposition](#rank-1-decomposition)
  - [Find four fundamental subspaces](#find-four-fundamental-subspaces)
  - [Application - image compression](#application---image-compression)
  - [Application - recommender system](#application---recommender-system)
- [Principal Component Analysis (PCA)](#principal-component-analysis-pca)
  - [Calculation](#calculation-1)
  - [Truncated SVD (Rank-k approximation)](#truncated-svd-rank-k-approximation)
- [Population Model](#population-model)
  - [Stable state (long-term behavior)](#stable-state-long-term-behavior)
  - [Dominant eigenvalue](#dominant-eigenvalue)
  - [Dominant eigenvector](#dominant-eigenvector)
  - [Damping ratio](#damping-ratio)
  - [Extrapolation of model at t=0](#extrapolation-of-model-at-t0)
- [Markov Process](#markov-process)
  - [Transition matrix (column stochastic matrix)](#transition-matrix-column-stochastic-matrix)
  - [Perron-Frobenius theorem](#perron-frobenius-theorem)
  - [Stationary distribution](#stationary-distribution)
  - [Markov's property](#markovs-property)
  - [Two-state Markov process](#two-state-markov-process)
- [PageRank (Application of Markov Process)](#pagerank-application-of-markov-process)
  - [Goal](#goal-1)
  - [Links are endorsements (Quantity and quality)](#links-are-endorsements-quantity-and-quality)
  - ["Random surfer" behaviour](#random-surfer-behaviour)
  - [Teleportation parameter (damping factor)](#teleportation-parameter-damping-factor)
- [Undirected Graphs](#undirected-graphs)
  - [Adjacency matrix](#adjacency-matrix)
  - [Degree matrix](#degree-matrix)
  - [Laplacian matrix](#laplacian-matrix)
  - [Fiedler vector](#fiedler-vector)
- [Directed graphs](#directed-graphs)
  - [Adjacency matrix](#adjacency-matrix-1)
  - [Degree matrix](#degree-matrix-1)
  - [Laplacian matrix](#laplacian-matrix-1)


# Vectors
## Linear combination

A collection of vectors in space $\mathbb{R}^N$
 
Let $a_1$ and $a_2$ be vectors in $\mathbb{R}^3$, defined as:

$$
a_1 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}, \quad
a_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}
$$

These vectors span a 2D plane ($\mathbb{R}^2$) within $\mathbb{R}^3$.  

## Span
All possible linear combinations of the vectors.  

$$
span(\{a_1, a_2\}) = c_1a_1 + c_2a_2
$$

## Linear independence

A collection $S$ of vectors in same space $\mathbb{R}^N$ is linearly independent if none of the vectors in $S$ can be expressed as a linear combination of the other vectors in $S$.  

To find if a set of vectors are linearly independent:  

Suppose you have three vectors $v_1, v_2, v_3$ in $\mathbb{R}^3$, your matrix $A$ is:

$$
A = \begin{bmatrix} 
    | & | & | \\ 
    \vec{v}_1 & \vec{v}_2 & \vec{v}_3 \\ 
    | & | & | 
    \end{bmatrix}
$$

Set up a homogeneous equation:
$$
Ax=0
$$

Apply Gaussian elimination, transform the matrix to REF or RREF form:
1. If every column has a pivot - linear independent  
2. Otherwise - linear dependent  

:bulb: If there are more vectors than the dimension in a set of vectors, then it is not a linearly independent set!  

E.g. Suppose you have vectors $v_1, v_2, v_3, v_4$ in $\mathbb{R}^3$

## Basis

A set of linearly independent vectors that **span the entire space** can be the basis of a subspace. 

Let $a_1$ and $a_2$ be vectors in $\mathbb{R}^2$, defined as:

$$
a_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad
a_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

These vectors are linearly independent & can be a set of basis in $\mathbb{R}^2$ that spans $\mathbb{R}^2$.

## Dimension
Number of individual vectors in a basis are needed to build a specific space.   

## Unit vector
A vector that points at the same direction and has a Euclidean norm of 1. 

Suppose we have a vector $v_1$ in $\mathbb{R}^2$
The unit vector of it is 
$$
\hat{v}_1 = \frac{1}{||v_1||_2} .  v_1 . 
$$

## Cross-product
:exclamation: Only in $\mathbb{R}^3$  
The cross product of two vectors $a$ and $b$ produces a new vector that is perfectly orthogonal (perpendicular) to both $a$ and $b$. It is useful for finding the normal vector to a plane.
$$
\|a \times b\| = \|a\| \|b\| \sin(\theta)
$$

[Back to Table of Contents](#table-of-contents)

# Angle & Inner Product 

## Inner product 
From cosine rule:

$$
\|a - b \|^2 = \|a\|^2 + \|b\|^2 - 2 \|a\|\|b\|cos(\theta)  
$$

From expansion:

$$
\begin{aligned}
\|a - b\|^2 &= (a_1 - b_1)^2 + (a_2 - b_2)^2 ... (a_N - b_N)^2 \\
\|a - b\|^2 &= (a_1^2 + a_2^2 + ... + a_N^2) + (b_1^2 + b_2^2 + ... + b_N^2) - 2(a_1b_1 + a_2b_2 + ... + a_Nb_N)\\
\|a - b\|^2 &= \|a\|^2 + \|b\|^2 - 2(a_1b_1 + a_2b_2 + ... + a_Nb_N) \\
\end{aligned}
$$

Equate them:

$$
\begin{aligned}
\|a\|^2 + \|b\|^2 - 2(a_1b_1 + a_2b_2 + ... + a_Nb_N) &= \|a\|^2 + \|b\|^2 - 2 \|a\|\|b\|cos(\theta) \\
a_1b_1 + a_2b_2 + ... + a_Nb_N &= \|a\|\|b\|cos(\theta) \\
a^Tb &= \|a\|\|b\|cos(\theta)
\end{aligned}
$$

:bulb: $a^Ta = \|a\|^2$ because $cos(\theta) = 1$

**Geometric meaning**  
Length of the projection multiplied by the length of the vector it is resting on.  
1. Positive inner product - pointing in the same direction.  
2. Zero inner product - orthogonal.  
3. Negative inner product - pointing opposite directions.   

## Sin rule 

$$
\begin{aligned}
sin^2(\theta) &= 1 - cos^2(\theta) \\ 
sin^2(\theta) &= 1 - (\frac{a^Tb}{\|a\|\|b\|})^2 \\ 
sin^2(\theta) &= \frac{\|a\|^2\|b\|^2-(a^Tb)^2}{\|a\|\|b\|}
\end{aligned}
$$

## Cauchy - Schwarz inequality 

$$
\begin{aligned}
|cos(\theta)| &= \frac{a^Tb}{\|a\|\|b\|} \\
a^Tb &= \|a\|\|b\| cos (\theta) \quad (0 \le |cos(\theta)| \le 1) \\
|a^Tb| &\le \|a\|\|b\|
\end{aligned} 
$$

You need this inequality to prove triangle inequality.  

## Triangle inequality
Sum of two sides is greater or equals to the third side. Shortest distance between two points is a straight line.  

Suppose we have two vectors $a, b$ in $\mathbb{R}^2$:

$$
\begin{aligned}
\|a + b\|^2 &= (a + b) \cdot (a + b) \\
\|a + b\|^2 &= a \cdot a + a \cdot b + b \cdot a + b \cdot b && \text{(Distributive)} \\
\|a + b\|^2 &= \|a\|^2 + 2(a \cdot b) +\|b\|^2  \\ 
\|a + b\|^2 &\le \|a\|^2 + 2\|a\|\|b\| +\|b\|^2 && \text{(Cauchy-Schwarz \ Inequality)} \\ 
\|a + b\|^2 &\le (\|a\|+ \|b\|)^2 && \text{(Factorization)} \\ 
|| a + b || &\le ||a|| + ||b|| && \text{(Triangle \ Inequality)}
\end{aligned}
$$

Reverse inequality, sets a **lower bound** on the distance between the tips of two vectors:

$$  
\begin{aligned}
\|a\|_2 &\le \|a - b\|_2 + \|b\|_2 \\
\|a\|_2 - \|b\|_2 &\le \| a - b \|_2 
\end{aligned}
$$
$$
\begin{aligned}
\|b\|_2 &\le \|a - b\|_2 + \|a\|_2 \\
\|b\|_2 - \|a\|_2 &\le ||a - b||_2
\end{aligned}
$$
$$
|\|a\| - \|b\|| \le ||a - b||
$$

## Area of parallelogram 
$$
\begin{aligned}
A &= \|a\| \times h \\
A &= \|a\|\times (\|b\| sin (\theta))
\end {aligned}
$$

[Back to Table of Contents](#table-of-contents)

# Matrix

## Rows and columns 
Suppose we have a matrix $A \in \mathbb{R}^{m\times n}$  
$m$ - number of rows.  
$n$ - number of columns.  

1. **For a transformation:**
   - $m$ indicates the OUTPUT is in a **m dimensional SPACE**.  
   - $n$ This indicates the INPUT is in a **n dimensional SPACE**.  
      :exclamation: the rank of the matrix indicates OUTPUT DIMENSION.  

2. **For a set of vectors:**  
   - $m$ indicates the dimensional space the vectors are in.  
   - $n$ indicates the number of vectors.  

## Matrix multiplication (outer product)
Suppose we have matrices $A$ and $B$.  

$$
A = \begin{bmatrix}
   1 & 2 & 3 \\
   -2 & 5 & 3  
\end{bmatrix}
\quad
B = \begin{bmatrix}
   7 & 4 \\
   -2 & 3 \\
   1 & 5 
\end{bmatrix}
$$

Every column of $AB$ is a linear combination of the columns of $A$ with the scalars coming from the corresponding column of $B$.  

$$
AB = 
\begin{bmatrix}
  6 & 25 \\
  -21 & 22  
\end{bmatrix} \\
$$

E.g. for the second row in $A$ and second column in $B$: 

$$
AB = 
4\begin{bmatrix}
   1 \\
   -2
\end{bmatrix} +
3\begin{bmatrix}
  2 \\
  5  
\end{bmatrix} +
5\begin{bmatrix}
  3 \\
  3  
\end{bmatrix} = 
\begin{bmatrix}
  25 \\
  22  
\end{bmatrix}
$$

## Rank 
Dimension of the output space spanned by its columns.  
= Number of pivots after doing row reduction.  
= Number of independent rows/columns.  

$$
rank(A) = dim(Col(A))
$$

## Transpose operations

$$
\begin{aligned}
   (A^T)_{ij} &= A_{ij} \\
   (A^T)^T &= A \\
   (A + B)^T &= A^T + B^T \\
   (cA)^T &= c(A^T) \\
   (AB)^T &= B^TA^T
\end{aligned}
$$

## Symmetric matrix 
$$
A = A^T
$$

If $A$ is a symmetric matrix, then any two eigenvector with different eigenvalue are orthogonal. 


## Matrix mapping
**Injective (One-to-one)** 
If every unique input vector $x$ produces a unique output vector $Ax$. 
- The equation $Ax=0$ has **only** the trivial solution (no information loss).   

- The column of the matrix must be linearly independent. This usually requires the matrix to be "tall".  

- Not surjective because you can't reach any 3D point that has a non-zero z-coordinate.  

**Surjective (Onto)**  
There are no "unreachable" vectors in the codomain.
- The columns of $A$ (column space) must span the entire output space.  

- The matrix must have **a pivot in every row**. This usually requires the matrix to be wide. 

- Not injective because all points with different values lands on the same spot (there is a information lost).   

**Bijective (One-to-one and onto)**  
Both injective and surjective

- Matrix must be square and **invertible** ($det \neq 0$), and the matrix has a full set of pivots (linearly independent) 

[Back to Table of Contents](#table-of-contents)

# Square Matrices 

## Upper/Lower triangular
Where all the non-zero entries are:
- Upper triangle - all the non-zero entries are ABOVE the diagonal entries.   
- Lower triangle - all the non-zero entries are BELOW the diagonal entries.   

$$
\text{Square matrices} = 
\begin{cases}
   \text{Upper triangular} && \text{if } a_{ij} = 0 \quad \forall i > j \\
   \text{Lower triangular} && \text{if } a_{ij} = 0 \quad \forall i < j    
\end{cases}
$$ 

## Determinant 
:warning: Only square matrices have determinant.  

**Cofactor expansion**  
Pick a row or a column that has most 0s in and do the cofactor expansion. Repeat this until the determinant is found.  
:warning: The sign alternates from + to - !  

**Triangular or diagonal matrices**  
The determinant is the product of the main diagonal entries.  

**Zero determinant**  
1. Has less than n pivots.   
   = Rank is less than n. 
2. Columns/Rows are linearly dependent.  

## Determinant properties
1. If you add a multiple of one row to another row, the determinant does not change.  
2. Row/column swap - the determinant is multiplied by -1.  
3. Scalar multiplication of a row - if you multiply a single row by a scalar k, the determinant is multiplied by k.  

## Determinant operations 
$$
\begin{aligned}
det(AB) &= det(A) \times det(B) && \text{(Product rule)}\\
det(kA) &= k^ndet(A) && \text{(Scaling)}\\
det(A^T) &= det(A) && \text{(Transposition)}\\
det(A^{-1}) &= \frac{1}{det(A)} && \text{(Inverse)} \\ 
det(A^P) &= (det(A))^P && \text{(Exponents)}
\end{aligned}
$$

## Inverse
:warning: Only square matrices can have an inverse.    

**Gaussian elimination**

$$
[A | I] \to [I | A^{-1}]
$$

**Cofactor expansion**
1. Find the determinant.
2. Find the minor $M$. 
3. Find the matrix of cofactors $C$.

   $$
   \begin{bmatrix}
   + & - & + \\
   - & + & - \\
   + & - & +
   \end{bmatrix}
   $$

4. Find the adjugate matrix  
   
   $$
   adj(A) = C^T
   $$

5. Find the inverse.  

   $$
   A^{-1} = \frac{1}{det(A)}adj(A)
   $$

**NO inverse**
1. $det(A) = 0$.  

2. Columns (Rows) are linearly dependent.  
= Rank is less than $n$ - it fails to span the full n-dimensional space. 

3. There is a NON-trivial null space - some points will be crushed into lower dimensions after applying this linear transformation.

4. Zero is an eigenvalue. 

[Back to Table of Contents](#table-of-contents)

# Norms
## General equations
**The p-norm**

$$
\|v\|_p = \left( \sum_{i=1}^n |v_i|^p \right)^{\frac{1}{p}}
$$

**Induced p-norm**  
to find the maximum stretch a matrix can apply to any vector if measure in p-norm. 

$$
\|A\|_p = \max_{x \neq 0} \frac{\|Av\|_p}{\|v\|_p}
$$

## The 1-norm (Manhattan norm)

**Vector**  
Measures the distance if you were forced to travel exclusively along the grid axes.    

$$
\|v\|_1 = \sum_{i=1}^n |v_i|
$$  

**Induced**
$$
\|A\|_1 = \max_{1 \le j \le n}\sum^n_{i=1}|a_{ij}|
$$

If you measure vectors using the "Manhattan" grid distance, this matrix cannot stretch any vector's length by more than a multiplier of $\|A\|_1$.    

Maximum column modulus sum.  

**Use case**  
Lasso regression, and situations where making small errors in many directions is penalized heavily.  

## The 2-norm (Euclidean norm)  
**Vector**  
"Length" of the vector.   

$$
\|v\|_2 = \sqrt{\sum_{i=1}^n v_i^2}
$$

**Induced**  

$$
\|A\|_2 = \max_{x \neq 0} \frac{\|Ax\|_2}{\|x\|_2}
$$

This matrix cannot stretch any vector's length by more than a multiplier of $\|A\|_2$. 

1. To make the math easier, mathematicians square the output length to get rid of the square root.  
$$
\begin{aligned}
\|Ax\|^2_2 &= (Ax)^T(Ax) \\
         &= x^T(A^TA)x && \text{(Scalar)}
\end{aligned}
$$
2. To maximize this equation, we are looking for the maximum scaling factor of the matrix $A^TA$-maximum eigenvalue  $\lambda_{max}$.  
3. Square root the maximum eigenvalue to get $\|A\|_2$.  

**Use case**  
Standard distance calculation, least squares regression in machine learning.  

## The infinity norm (Maximum/Chebyshev norm)  
**Vector**  
Takes the largest absolute value. 

$$
||v||_\infin = max(|v_1|, |v_2| \cdots |v_n|)
$$  

**Induced**

$$
\begin{aligned}
\|A\|_\infin &= \max_{1 \le i \le n}\sum^n_{i=1}|a_{ij}|
\end{aligned}
$$

This matrix guarantees that the new largest coordinate will never be more than $\|A\|_\infin$ times larger than the origin.

Maximum row modulus sum.  

**Use case**  
Worst-case scenario analysis, determining the maximum error in numerical computing. 

## Frobenius norm (matrix only)  
Square root of sum of the square of all entries in $A$.  
Total overall energy of the matrix.  

$$
\|A\|_F=\sqrt{\sum^N_{j=1}\sum^M_{i=1} (a_{ij})^2}
$$   

[Back to Table of Contents](#table-of-contents)

# Linear Systems

## Linear equation 

$$
a^Tx = b \\
\begin{aligned}
   a &- \text{Coefficient vector (normal vector to the hyperplane)} \\
   b &- \text{Scalar}
\end{aligned}
$$

## System of linear equations
Any collection of two or more linear equations with the same number of unknowns.

$$
Ax=b
$$

**Inconsistent system**  
System with no solutions.  

## Solving linear systems (Gaussian elimination)

**Gaussian elimination**
1. Form an augmented matrix  
   
   $$
   [A \ | \ b]
   $$

2. Elementary row operation on the matrix until you get RREF.  
   - Swap two rows. 
   - Multiply a row by a non-zero constant. 
   - Add a constant multiple of a row to another row.

**Possible outcomes**
1. NO solution - there is a row of RREF that looks like:
   
   $$
   \begin{bmatrix}
   0 & \cdots & 0 \ | \ 1
   \end{bmatrix}
   $$

2. One solution (Full rank)

3. Infinite solution - there is a row of RREF that looks like:  

   $$
   \begin{bmatrix}
   0 & \cdots & 0 \ | \ 0
   \end{bmatrix}
   $$

   Identify the free column(s) (the columns that have NO pivot). Use the free variable(s) as the scalars. 

**General solution**

$$
\text{Particular } + \text{General}
$$

[Back to Table of Contents](#table-of-contents)

# Least Squares

## Normal equation

$$
\begin{aligned}
   A &\in \mathbb{R}^{M\times N} && \text{(Inputs)} \\
   b &\in \mathbb{R}^M && \text{(Labels)}
\end{aligned}
$$

$\because$ $b$ is a vector that is NOT in $Col(A)$.

$\therefore$ $Ax=b$ does NOT have a solution.  

**Goal: To approximate the solution**  
Look for a vector $\hat{x}$ such that $A\hat{x}$ is CLOSEST to $b$ among all vectors in $Col(A)$ by **projecting** $b$ onto $Col(A)$.  

$$
\begin{aligned}
& A\hat{x} = proj_{Col(A)}(b) = \hat{b} \\
&\because (b-\hat{b}) \perp Col(A) \\
&\therefore A^T \cdot (b-\hat{b}) = 0 \\
\end{aligned}
$$
$$
\begin{aligned}
A^Tb - A^TA\hat{x} &= 0 && (\text{Substitute } \hat{b} = A\hat{x})\\
A^TA\hat{x} &= A^Tb && \text{(Normal equation)}
\end{aligned}
$$

Solve it using augmented matrix. Coefficents in the $\hat{x}$ is the coefficient for the approximation.

## Moore-Penrose inverse (pseudo-inverse)
Rearranging the normal equation to solve $\hat{x}$:  

$$
\begin{aligned}
\hat{x} &= (A^TA)^{-1}A^Tb \\
\end{aligned}
$$

Becasue $A$ could be a tall matrix, it doesn't have a inverse. However, if you multiply the pseudoinverse on the left side, you get the identity matrix:  

$$
\begin{aligned}
A^+ &= (A^TA)^{-1}A^T \\
A^+A &= (A^TA)^{-1}(A^TA) = I
\end{aligned}
$$

**When $A^{T}A$ is a singular matrix**  
1. $A$ is linearly dependent, the data has redundent.  

2. If there are more feature than the number of data (tall data).  

**Build the pseudo-inverse using SVD**  

$$
\begin{aligned}
   A &= U\Sigma V^T \\
   A^{+} &= (V^{T})^{-1} \Sigma^+ U^{-1} \\
\end{aligned}
$$

Because $U$ and $V$ are orthogonal matrices, their inverse is just their transpose.  

$$
   A^{+} = V\Sigma^+U^{T}
$$

For $\Sigma^+$:
$$
   \Sigma_{ij}^{-1} = \frac{1}{\Sigma_{ij}}
$$
If the singular value is zero, leave it zero.   

:bulb: The entries of an inverse of a diagonal matrix are the reciprocals.  

**Least square**

$$
\hat{x} = A^+b
$$


## QR decomposition (Gram-Schmidt process)
Suppose we have the matrix $A$.  
Factor $A$ into two special matrices.  

$$
\begin{aligned}
A &= QR \\
Q &- \text{The orthogonal matrix} \\
R &- \text{The upper triangular matrix}   
\end{aligned}
$$

Substitute this into the normal equation:  

$$
\begin{aligned}
(QR)^T(QR)x &= (QR)^Tb \\
R^TQ^TQRx   &= R^TQ^Tb   && (\text{Distribute the transpose}) \\
R^TIRx      &= R^TQ^Tb   && (Q^{-1} = Q^T) \\
Rx          &= Q^Tb
\end{aligned}
$$




[Back to Table of Contents](#table-of-contents)

# Four fundamental subspaces  

## Subspace
Subspace must satisfy three strict tests:  
1. It must contain the **ZERO** vector.

2. Closure under addition  
   If you take any two vectors in the space and add tem together, the resulting vector must also be in the space.

3. Closure under scalar multiplication  
   If you take any vector in the space and multiply it by any real number, the resulting vector must still be in the space. 

## Finding four fundamental subspaces
Suppose we have a matrix $A$ in $\mathbb{R}^{M\times N}$.  
Find RREF matrix $R$ of $A$.

**Column space** ($Col(A)$)  
Look at the pivot columns in $R$  
❗Go back to the original matrix $A$ to find the corresponding columns.

**Row space** ($Col(A^T)/Row(A)$)  
Choose the non-zero rows of $R$.  

**Null space** ($Nul(A)$)  
Solve $Rx=0$.  

**Left null space** ($Nul(A^T)$)   
Transpose $A$ and then perform the exact same null space algorithm on $A^T$.

## Four subspaces as a "instruction manual" for a matrix

**Inputs**
   - **$Nul(A)$: "The blind spot"**  
   The null space contains all the inputs that the matrix completely crushes down to zero.  
   If the null space contains anything other than the zero vector, it means you have infinite solution.  

   - **$Col(A^T)/Row(A)$: "The essential inputs"**  
   Because the Row Space and the Null Space are orthogonal complements, the Row Space represents the "good" data. It is the exact part of the input that makes it safely through the matrix without being crushed to zero. 
   

**Outputs**
   - **$Col(A)$: "The reachable world"**  
   Set of all possible outputs the matrix can produce. 

   - **$Nul(A^T)$: "The impossible restrictions"**  
   This space is the orthogonal complement to the Column Space. It represents the strict constraints or physical laws that govern the output space. It tells you exactly what conditions the output must satisfy. Because the Left Null Space and Column Space are orthogonal complements, to make $Ax = b$ solvable, $b$ must be perpendicular to the left null space.

## Rank-nullity theorem
Suppose we have a matrix $A \in \mathbb{R}^{m\times n}$:  

$$
\begin{aligned}
   \text{rank(A) + nullity(A)} &= \text{number of columns of A} \\
   \text{dim(Col(A)) + dim(Nul(A))} &= n \text{ (Dimension of the input space)} \\
   \text{Preserved info} + \text{Destroyed info} &= \text{Total dimension}
\end{aligned}
$$

## Orthogonal components

$$
S^{\perp} \text{(Orthogonal component)} = \{v \in \mathbb{R}^k : u^Tv=0 \quad \forall u \in S\}
$$
$$
\begin{aligned}
   Nul(A) \text{ and } Col(A^T) \text{ are orthogonal component} \\
   Nul(A^T) \text{ and } Col(A) \text{ are orthogonal component} \\
\end{aligned}
$$

$S$ and $S^{\perp}$ are perfectly perpendicular and cover the entire space:

$$
\mathbb{R}^k = S \oplus S^\perp
$$

**Unique Decomposition**  
Every single vector $w$ in the entire space can be uniquely written as the sum of two vectors: $w = s+ v$.  

**No overlap**  
The only vector that exists in both $S$ and $S^\perp$ is $\vec{0}$.  

[Back to Table of Contents](#table-of-contents)

# Linear transformation

## Definition

$$ 
\begin{aligned}
T:\mathbb{R}^n \to \mathbb{R}^m \text{ is a linear transformation if } \begin{cases}
                     \forall u, v \in \mathbb{R}^n && T(u+v) = T(u) + T(v) \\
                     \forall u \in \mathbb{R}^n, c \in \mathbb{R} && T(cu) = cT(u)
                     \end{cases}
\end{aligned}
$$

## Terminology
**Kernel**  
The exact same thing as the Null Space ($Nul(A)$). It is all inputs that map to zero.

**Image**  
The exact same thing as the Column Space ($Col(A)$). It is the set of all reachable outputs.

## Projection 

$$
proj_a(b) = comp_a(b) \hat{a}
$$
$$
\begin{aligned}
comp_a(b) &= \|b\| cos(\theta) \\
comp_a(b) &= \frac{\|b\|a^Tb}{\|a\|\|b\|} && \text{(Cosine Rule)} \\
comp_a(b) &= \frac{a^Tb}{\|a\|} && \text{(Scalar)}
\end{aligned}
$$
$$
\begin{aligned}
\hat{a} = \frac{a}{\|a\|} && \text{(Vector)}
\end{aligned}
$$
$$
proj_a(b) = \frac{a^Tb}{\|a\|^2} a
$$

## Projection operator 

$$
\begin{aligned}
proj_a(b) &= a (\frac{a^Tb}{a^Ta}) && \text{(Swap two parts because one is scalar one is vector)} \\
proj_a(b) &= (\frac{aa^T}{a^Ta})b && \text{(Associative (Outer Product))} \\
\end{aligned}
$$
$$
P_a = \frac{aa^T}{\|a\|^2}
$$

1. It is symmetric   
   
   $$
   P^T = P
   $$

2. It is idempotent  
   
   $$
   P^2 = P
   $$

## Projection along all-1s vector (mean)

$$
proj_{\vec{1}} (x) = P_1 x = \bar{x}\vec{1} \\
P_1 = \frac{1}{N} \begin{bmatrix}
                  1 & \cdots & 1 \\
                  \vdots & \ddots & \vdots \\
                  1 & \cdots & 1
                  \end{bmatrix}
$$

For any vector $x$ in $\mathbb{R}^n$, the mean centered vector $(x-\bar{x}\vec{1})$ can be expressed as:

$$
\begin{aligned}
(x - \bar{x}\vec{1})    &= (x - P_{\vec{1}}x) \\
                        &= (I - P_{\vec{1}})x \\
\end{aligned}
$$

Centred matrix:

$$
(I - P_{\vec{1}})_{ij} = 
\begin{cases} 
\frac{N-1}{N} & \text{if } i = j \\ 
-\frac{1}{N} & \text{if } i \neq j 
\end{cases}
$$

## Reflection operator 
From projection operator:
Suppose we want to reflect a vector $b$ about a vector $a$.    

1. **Find the midpoint and the distance from the midpoint**  

   $$
   d =(P_a(b) - b)
   $$ 

2. **Flip (mid point + distance)**
   
   $$
   \begin{aligned}
   \hat{b} &= P_a(b) + (P_a(b) - b) \\
           &= 2P_a(b) - b \\
           &= 2\frac{aa^T}{\|a\|^2}b - b \\
           &= (2\frac{aa^T}{\|a\|^2} - I)b 
 
   \end{aligned}
   $$

Reflection operator: 

$$
   R_a = (2\frac{aa^T}{\|a\|^2} - I) = 2P - I
$$

[Back to Table of Contents](#table-of-contents)

# Orthogonal Systems (Gram-Schmidt Process)

## Orthogonal matrix 
A square matrix whose columns and rows are made up of mutually perpendicular vectors of length exactly 1.  

## Semi-orthogonal matrix
1. **Semi-orthogonal tall matrix**  
   If a matrix has more rows than columns ($m > n$), it can be column semi-orthogonal - columns are mutually perpendicular vectors of length 1.  
   
   $$
   A = \begin{bmatrix}
      1 & 0 \\
      0 & 1 \\
      0 & 0
   \end{bmatrix}
   $$

   If you multiply it from the LEFT, you get the identity matrix:  
   
   $$
   A^TA = I_n \text{ (Identity matrix of the smaller value)}
   $$

   **Geometric meaning**  
   Embedding - multiplying a vector by a column semi orthogonal matrix acts as an isometry. It takes a vector from a lower-dimensional space and maps it into a higher dimensional space **WITHOUT changing its length and angles between vectors**.  

2. **Semi-orthogonal wide matrix**  
   If a matrix has more columns than rows ($m < n$), it can be row semi-orthogonal - rows are mutually perpendicular vectors of length 1.  

   $$
   A = \begin{bmatrix}
      1 & 0 & 0 \\
      0 & 1 & 0 
   \end{bmatrix}
   $$

   If you multiply it from the RIGHT, you get the identity matrix 
   
   $$
   AA^T = I_m \text{ (Identity matrix of the smaller value)}
   $$

   **Geometric meaning**  
   Projection - This matrix maps vectors from a higher-dimensional space down to a lower-dimensional space. Information is lost, but the projection perfectly captures the remaining dimensions.  

## Properties of orthogonal matrix  
Suppose we have a orthogonal matrix $Q$":

$$
Q^{-1} = Q^T \\
Q^TQ = I \\ 
QQ^T = I
$$


## Spectral theorem 
A matrix can be **orthogonally diagnalized if and only if it is a symmetric matrix**  
1. Real eigenvalue  
   Every single eigenvalue will be a real number
2. Orthogonal eigenvectors  
3. Orthogonal diagnalization 
   
**Geometric meaning**
Symmetric matrix only stretches things along perpendicular axes

## Gram-Schmidt process
**Goal**  
To make all vectors in this matrix orthogonal to each other while **preserving the column space**, which makes certain calculations easier.

Suppose we have a matrix $A$:
$$
A = \begin{bmatrix} 
    | & | & | \\ 
    v_1 & v_2 & v_3 \\ 
    | & | & | 
    \end{bmatrix}
$$

**To make $v_2$ orthogonal to $v_1$, we replace $v_2$ with $q_2$:**

$$
\begin{aligned}
q_2 &= v_2 - proj_{v_1} (v_2) \\
    &= v_2 - \frac{v_1^Tv_2}{\|v_1\|^2} v_1 \\
\end{aligned}
$$

**To make $v_3$ orthogonal to $v_1$ and $v_2$, we replace $v_3$ with $q_3$:**
$$
\begin{aligned}
q_3 &= v_3 - proj_{q_1} (v_3) - proj_{q_2} (v_3)\\
            &= v_3 - \frac{q_1^Tv_3}{\|q_1\|^2} q_1 - \frac{q_2^Tv_3}{\|q_2\|^2} q_2\\
\end{aligned}
$$
:exclamation: Watch out which vector it is projected onto, is the orthogonal vectors!

**Normalize all the vectors to get a orthogonal set:**

:exclamation: Remember to normalize all the vectors to get a orthogonal set!  
$$
\begin{aligned}
\tilde{v}_1 &= \frac{v_1}{\|v_1\|} \\ 
\tilde{v}_2 &= \frac{q_2}{\|q_2\|} \\ 
\tilde{v}_3 &= \frac{q_3}{\|q_3\|} \\   
\end{aligned}
$$
**Finally, form the new matrix with $\tilde{v}_1$, $\tilde{v}_2$ and $\tilde{v}_3$:**
$$
= \begin{bmatrix} 
   | & | & | \\ 
   \tilde{v}_1 & \tilde{v}_2 & \tilde{v}_3 \\ 
   | & | & | 
   \end{bmatrix}
$$



[Back to Table of Contents](#table-of-contents)

# Eigenthings
Suppose we have a matrix $A$ in $\mathbb{R}^{N\times N}$. 
$$
\begin{aligned}
Av &= \lambda v \\
(A - \lambda I)v &= 0 \\
det(A - \lambda I) &= 0
\end{aligned}
$$

A number $\lambda$ in an eigenvalue of $A$ if there exists $v \neq \vec{0}$.  
After applying the matrix $A$, the eigenvectors in this eigenspace are scaled by the corresponding eigenvalue. 
## Eigenvalue   
**Trace rule**  
The sum of the eigenvalues is always exactly equal to the trace of the matrix. 
$$
\sum_{i=1}^n\lambda_i = Tr(A)
$$

**Determinant rule**  
The product of the eigenvalues is always exactly equal to the determinant of the matrix.  
$$
\prod^n_{i=1}\lambda_i = det(A)
$$

**Matrix power**
$$
A^kx = \lambda^k x
$$

**The transpose**  
$A$ and $A^T$ have same eigenvalues.

## Eigenvector
Zero vector doesn't count.  
Different eigenvectors drawn from different eigenspaces are mathematically guaranteed to be linearly independent.  

## Eigenspace
The set of all possible eigenvectors for this eigenvalue, plus the vector $\vec{0}$ (subspace).
$$
E_{\lambda} = Nul(A-\lambda I)
$$

## Special matrices
**Singular matrix** ($det(A)=0$)
- Eigenvalues  
At least one $\lambda = 0$  
- Eigenvectors  
The eigenvector associated with $\lambda = 0$ from the null space of the matrix.  
  
**Diagonal/Triangular matrix**
- Eigenvalues    
The diagonal entries are the eigenvalues.  

**Invertible matrix** ($A^{-1}$)  
- Eigenvalues  
If $A$ has an eigenvalue $\lambda$, then its inverse has eigenvalues $\lambda^{-1}$.
- Eigenvectors  
They have the same eigenvectors

**Orthogonal matrix**  
- Eigenvalues  
All eigenvalues have an absolute magnitude of 1, no scaling effect. Can be rotation (imaginary), reflection (-1).   

**Symmetric matrix**
- Eigenvectors  
All eigenvector corresponding to **different eigenvalues** in a symmetric matrix are always orthogonal to each others. If eigenvalues are repeated, choose the orthogonal ones ourselves.    

**Markov/Stochastic matrix**
- Eigenvalues  
The largest eigenvalue is always 1. Every other eigenvalue is less than 1. 
- Eigenvectors  
The eigenvector associated with $\lambda = 1$ is called the steady-state vector. If you multiply the matrix over and over again into infinity, the system will settle exactly onto this eigenvector

## Geometric/Algebraic multiplicity
**Algebraic (AM)**  
The number of times it appears as a repeated root in the characteristic polynomial of the matrix.  

**Geometric (GM)**  
The dimension of the eigenspace associated with that eigenvalue.  
 = Number of linearly independent eigenvectors you can find for that eigenvalue. 

**Relationship**
$$
\begin{aligned}
   1 \le GM \le AM
\end{aligned}
$$

[Back to Table of Contents](#table-of-contents)

# Similar Matrices
## Change of basis

Two $n \times n$ matrices are similar if there exists an 
invertible matrix P such that: 

$$
A = P^{-1}BP
$$

Suppose there are two set of basis:  

$$
\begin{aligned}
   S &- \text{Standard basis} \\
   \mathcal{E} &- \text{A new basis}
\end{aligned}
$$

Now you have a vector coordinates $x_\mathcal{E}$ are **written** in the **NEW basis**. You want to apply your linear transformation $M$ to it, but $M$ only "speaks" the standard language.  

1. **Translate to standard language**  
   Matrix $P$ takes a vector **OUT of a new basis** and puts it into the standard basis, because $P$ is the set of new basis written in standard basis.  

   $$
   \text{Standard vector } = Px_\mathcal{E}
   $$

2. **Apply the transformation**  

   $$
   \text{Transformed standard vector} = M(Px_\mathcal{E})
   $$

3. **Translate back**  
   Matrix $P^{-1}$ puts a vector **BACK to the new basis**.  

   $$
   \text{Final transformed vector in } \mathcal{E} = P^{-1}(MPx_\mathcal{E})
   $$

Now the new transformation matrix form has the same geometric transformation as $M$ but in the new coordinate system.  

$$
M_\mathcal{E} = P^{-1}MP
$$

## Sharing properties
If $A$ and $B$ are similar, they are guaranteed to have the exact same:
   - Determinant 
   - Trace
   - Eigenvalues
   - Rank

[Back to Table of Contents](#table-of-contents)

# Diagonalization
## Diagonalizability
If $GM = AM$ for every single eigenvalue, the matrix has a full set of linearly independent eigenvectors (spans the whole space), this matrix is diagonalizable. 

## Goal
Suppose we have a linear transformation $A$ that is diagonalizable. By changing our basis to its eigenvectors, we made all our vectors made out of eigenvectors. Therefore, we made this transformation just a matter of scaling, and scaling has the following property: 

$$
D = 
\begin{bmatrix}
   a & 0 \\
   0 & b
\end{bmatrix} \quad
D^k = 
\begin{bmatrix}
   a^k & 0 \\
   0 & b^k
\end{bmatrix} \quad
$$

If we decompose a noisy matrix in form $PDP^{-1}$, the calculation of $A^k$ will become:

$$
\begin{aligned}
   A^k &= (PDP^{-1})^k \\
       &= PDP^{-1}PDP^{-1}P \cdots P^{-1}PDP^{-1} \\
       &= PD(P^{-1}P)D(P^{-1}P) \cdots (P^{-1}P)DP^{-1} && \text{(Association)} \\
       &= PD^kP^{-1}
\end{aligned}
$$
  
## Calculation
Suppose we have a diagonalizable matrix $A$:

We want to change the basis of the standard system to its eigenvectors. By definition, a transformation only stretches its eigenvectors, hence the new transformation in our new basis is a diagonal matrix with entries correspond to its eigenvalues.    

$$
\begin{aligned}
D &= P^{-1}AP \\
A &= PDP^{-1}   
\end{aligned}
$$

1. Find the eigenvalues, construct the "Dictionary" matrix ($P$).   
   The eigenvectors are the coordinate system we are trying to translate into. 
 
2. Construct the diagonal matrix with eigenvalues  
   :exclamation: Columns have to match with the eigenvectors

3. Find $P^{-1}$.

**Orthogonally diagonalizable**  
Symmetric and orthogonal matrix $Q$ with $Q^{-1} = Q^T$ and the diagonal matrix $D$ such that $A = QDQ^T$.  

[Back to Table of Contents](#table-of-contents)

# Singular Value Decomposition (SVD)
To "do" SVD means to take a messy, complex matrix $A$ and break it down into three much simpler matrices multiplied together.  

$$
A = U\Sigma V^T
$$ 

:exclamation: Beacause we need to put our standard vector **into the NEW basis**, we need to multiply by $V^{-1}$ first, and because $V$ is an orthogonal matrix, $V^T = V^{-1}$. 

## Different components 
**The right singular vectors** ($V$)  
The columns of $V$ are exactly the Principal Components in PCA.   

**Singular values** ($\Sigma$)  
If a singular value is exactly 0, it means the matrix completely squashes that dimension into nothingness. The number of non-zero signular values is exactly the Rank of the matrix.  

**The left singular vectors** ($U$)  
After the data has been aligned and stretched, $U$ picks the data up and rotates it into its final resting position in the output space. 

## Geometric concept 
**Latent space mapping**  
Each matrices changes the bases of the dimensional space.  
- Rows in $U$ as the axis and the concept as the data. 

- Rows in $V$ as the axis and the concept as the data.  

**Linear transformation**
- $V^T$: A pure rotation or reflection of the space.   
  Change of basis for the input  

- $\Sigma$: A pure stretching or squishing along the coordinate axes.  

- $U$: Another pure rotation or reflection.  
  Changes the basis for the output. 

## Full SVD 
Suppose you have a $m\times n$ matrix $A$

**Find the right singular vector** ($V \in \mathbb{R}^{n\times n}$)
1. Because we are dealing with rectangular matrices, we first calculate $A^TA$ to make it a square matrix (This always give you a symmetric matrix).  

   $$
   A^TA = VDV^{-1}
   $$

2. Because it is $A^TA$ is symmetric, by spectral theorem, the eigenvectors forms a orthogonal set, meaning:

   $$
   V^{-1} = V^T
   $$
   $$
   A^TA = VDV^T
   $$

3. Find the eigenvalues and eigenvectors of that symmetric matrix to get $V$.  
:exclamation: Remember to normalize those eigenvectors so they have a length of 1!  
       
1. Get $V^T$.   

**Find the Singular Values** ($\Sigma \in \mathbb{R}^{m\times n}$)  
1. Take the eigenvalues of $A^TA$ in Step 1. 
   
2. Take the square root of each eigenvalue to get the eigenvalues of $A$.  
   
   $$
   \begin{aligned}
   A^TA &= V\Sigma^T(U^TU)\Sigma V^T \\
   A^TA &= V\Sigma^T\Sigma V^T \\
   A^TA &= V\Sigma^2V^T  && (\Sigma\text{ is a diagonal matrix})    
   \end{aligned}
   $$ 
   $$
   \sigma_i = \sqrt{\lambda_i}
   $$

3. Place them, from largest to smallest, down the main diagonal of the matrix $\Sigma$. Fill the rest of the matrix with zeros. 

**Find the left singular vectors**  ($U \in \mathbb{R^{m\times m}}$)  

1. For every non-zero singular value you found, you can calculate the corresponding column of U using this formula:  

   $$
   \begin{aligned}
   AV &= (U\Sigma V^T)V \\
   AV &= U\Sigma I \\
   U &= AV\Sigma^{-1} \\
   \end{aligned}
   $$

   $$   
   u_i = \frac{Av_i}{\sigma_i}
   $$

2. If the original matrix had more rows than columns, find remaining vectors that are orthogonal to all the vectors you already have, use Gram-Schmidt process.

## Thin SVD
Chops off the bottom zero rows of $\Sigma$ and the corresponding "useless" rightmost columns of $U$.  
- $U \in \mathbb{R}^{m\times n}$
- $\Sigma \in \mathbb{R}^{n\times n}$

**Advantages** 
1. Memory saving.
2. Faster computation.  
3. No information loss.  

## Rank-1 decomposition 
Rewrite the matrix as a sum of individual "layers":  

$$
A = (\sigma_1 u_1 v_1^T) + (\sigma_2 u_2 v_2^T) + \cdots + (\sigma_r u_r v_r^T)
$$

Each layer tells you **ONE** single concept (e.g. Action genre). We can now throw away most of the layers that have a tiny singular value. 

By decomposing the data, the algorithm can figure out what "hidden concept" a user likes. 

## Find four fundamental subspaces
Suppose we have a matrix $A \in \mathbb{R^{m\times n}}$.  

**Find the rank**  
Count the number of strictly positive, non-zero singular values. That number is the rank $(r)$ of the matrix.  

**Output space (U)**  
- $Col(A) \in \mathbb{R}^{m\times r}$  
  Take the first $r$ columns of $U$. These vectors form a perfect orthonormal basis for the column space.

  For the first $r$ columns, the equation $Av_i = \sigma_i u_i$. 

- $Nul(A^T) \in \mathbb{R}^{m \times (m-r)}$  
  Take the **remaining** $(m-r)$ columns of $U$. These vectors form an orthonormal basis for the left null space.    

**Input space (V)**   
:exclamation: In $V$ NOT in $V^T$ 
- $Col(A^T)/Row(A) \in \mathbb{R}^{n \times r}$  
  Take the first $r$ columns of $V$. These vectors form a perfect orthonormal basis for the row space.

- $Nul(A) \in \mathbb{R}^{n \times (n-r)}$  
  Take the **remaining** $(n-r)$ columns of $V$. These vectors form an orthonormal basis for the null space. ($dim(Nul(A)) = n-r$)  

  For any column after the r-th column, the singular value is 0, which gives you $Av_i = 0$.  

## Application - image compression
Take a high-resolution photo and run SVD on it, you will get thousands of singular value ($\Sigma$). The first few $\sigma$ values hold almost all the visual information. The last thousand $\sigma$ values just hold tiny, imperceptible details and can be discarded.  

## Application - recommender system  

Suppose there is a massive matrix where rows are millions of Netflix users and columns are thousands of movies. Most of the matrix is blank because you haven't watched every movie.  

1. $U$ **matrix**  
   The rows are users, columns are concepts.

   Holds numbers that represents **how much a user like a specific concept**.  

   Example: If concept 1 represents "Sci-Fi", user A might have a high positive value (they love Sci-Fi), while user B might have a negative value (they hate it).  

2. $\Sigma$ **matrix**  
   Values represent the weight of each latent factor (concept) across the entire dataset 
   
   Example: Sci-fi has the most popularity hence has the highest eigenvalue.  

3. $V$ **matrix**  
   The rows are items, columns are concepts, 

   Holds numbers that represents **how strongly an item aligns with a specific concept**

   Example: The movie Dune would have a high value in Sci-Fi row, while the movie The Notebook would have a near-zero or negative value.  


[Back to Table of Contents](#table-of-contents)

# Principal Component Analysis (PCA)
Dimensionality reduction technique - take massive, messy, high-dimensional datasets and compress them down to just a few dimensions while throwing away as little "information" as possible.  

It looks for the angles where the data is most spread out - high variance.  

## Calculation 
1. Find the average mean of all the data, and shift the entire cloud of data so that the center sits exactly at the origin.  
$$
\begin{aligned}
   X_c &= (X - \vec{1}\bar{x})
\end{aligned}
$$

2. Calculate covariance matrix to find out how all variables relate to each other. The covariance matrix is proportional to $A^TA$. 
$$
C = \frac{1}{(n-1)}X^T_cX_c
$$

1. Because the covariance matrix is symmetric, by spectral theorem, we are mathematically guaranteed to find perfectly orthogonal eigenvectors (SVD). 

   $$
   C = U\Sigma V^T
   $$

   - Eigenvectors are the Principal Components 
   - Eigenvalues tell the exact variance along each component 

2. Create feature matrix $W$ by selecting the top-K eigenvectors that have the highest eigenvalues (variance).

3. Compress the data by projecting the centred dataset using the matrix $W$.  
$$
Y = X_cW
$$ 

## Truncated SVD (Rank-k approximation)
Choose a target rank and keep only the top k largest singular value 

- Keep the first k columns of $U$.  
- Keep the top-left $k\times k$ block of $\Sigma$.  
- Keep the first $k$ rows of $V^T$.  

[Back to Table of Contents](#table-of-contents)

# Population Model
Suppose we have a population matrix $A$  
$$
A = \begin{bmatrix}
   \text{Prey natural growth}  & \text{Predation impact} \\
   \text{Predator growth} & \text{Predator starvation}
\end{bmatrix}
$$

Main diagonals are the reproduction terms, others are the predation terms.  

Suppose we have population of Rabbits $R$ and Foxes $F$.  
Population growth:
$$
\begin{bmatrix}
   R_{t+1} \\
   F_{t+1}
\end{bmatrix} = 
A
\begin{bmatrix}
   R_{t} \\
   F_{t}
\end{bmatrix}
$$

## Stable state (long-term behavior)
Suppose we have a population of insects lives in two habitats: Forest (F) and Dryland (D). Each year some insects move between the habitats. The population update is modeled by:

$$
\begin{bmatrix}
   F_{k+1} \\ 
   D_{k+1}
\end{bmatrix} = 
\begin{bmatrix}
  0.8 & 0.3 \\
  0.2 & 0.7 
\end{bmatrix} 
\begin{bmatrix}
   F_k \\
   D_k
\end{bmatrix}
$$

Suppose we have a starting population $x_0:$ of:  

$$
x_0 = \begin{bmatrix}
   F_0 \\
   D_0 \\
\end{bmatrix}
$$

To find the long-term behaviour we have to solve:

$$
\text{Stable state} = \lim_{t \to \infin} 
\begin{bmatrix}
  0.8 & 0.3 \\
  0.2 & 0.7 
\end{bmatrix} 
x_0 
$$

To make the calculation easier, we diagonalize the population matrix.  

$$
\begin{aligned}
   A &= PDP^{-1}
\end{aligned}
$$
The eigenvalues and the corresponding eigenvectors are:  
$$
\begin{aligned}
\lambda_1 = 1&, \quad
v_1 = \begin{bmatrix}
   3 \\
   2
\end{bmatrix} \\
\lambda_2 = 0.5&, \quad
v_2 = \begin{bmatrix}
   -1 \\
   1
\end{bmatrix} \\
\end{aligned} 

$$

## Dominant eigenvalue 
$$
\begin{aligned}
\text{Stable state} &=  
\begin{bmatrix}
  3 & -1 \\
  2 & 1 
\end{bmatrix}
\lim_{t \to \infin}  
\left(
\begin{bmatrix}
  1^t & 0 \\
  0 & 0.5^t 
\end{bmatrix}
\right) 
\begin{bmatrix}
  0.2 & 0.2 \\
  -0.4 & 0.6 
\end{bmatrix} 
x_0 \\

&=  
\begin{bmatrix}
  3 & -1 \\
  2 & 1 
\end{bmatrix}  
\begin{bmatrix}
  1 & 0 \\
  0 & 0 
\end{bmatrix}
\begin{bmatrix}
  0.2 & 0.2 \\
  -0.4 & 0.6 
\end{bmatrix} 
x_0 \\

&= 
\begin{bmatrix} 
0.6 & 0.6 \\ 
0.4 & 0.4 
\end{bmatrix}
x_0

\end{aligned}
$$

The dominant eigenvalue falls in three possible categories:
1. $\lambda$ > 1  
   Gradual increase in population - thrive.  
2. $\lambda$ = 1  
   Stable population.
3. $\lambda$ < 1  
   Gradual decrease in population - extinct.  

## Dominant eigenvector

If the population converges to stable. The dominant eigenvector shows the ratio of the final population.  
$$
\begin{aligned}
\text{Forest Population} &: \text{Dryland Population} \\
3&:2
\end{aligned}
$$

## Damping ratio

$$
\frac{\lambda_1}{|\lambda_2|}
$$

**High damping ratio**
The dominant eigenvalue vastly overpowers the others. The population will "snap" back to its stable distribution very quickly, almost without bouncing.  

**Low damping ratio**
Eigenvalues are close in size. The population will experience wild, dramatic demographic swings for many generations before finally settling down.  

## Extrapolation of model at t=0
Because we've now changed the basis to eigenvectors: 
$$
x_0 = c_1\mathbf{v}_1 + c_2\mathbf{v}_2
$$
$$
x_t = c_1(\lambda_1)^t\mathbf{v}_1 + c_2(\lambda_2)^t\mathbf{v}_2
$$
$$
\begin{aligned}
x_{\text{stable}}(t) &= c_1(\lambda_1)^tv_1 \\
x_{\text{extrapolated}}(0) &= c_1v_1
\end{aligned}
$$



[Back to Table of Contents](#table-of-contents)

# Markov Process 

## Transition matrix (column stochastic matrix)
Each column should add up to 1.

$$
\begin{aligned}
P_{ij} &= \text{Probability moving from state } j \to i \\
&= \frac{A_{ij}}{\sum_i A_{ij}}
\end{aligned}
$$

**Dominant eigenvalue = 1**  
The dominant eigenvalue is always 1. This is proven by calculating the $\|P\|_1 = 1$   

Proposition: If $T$ is a column stochastic matrix and $v$ is an eigenvector of $T$ with all non-negative entries, then corresponding eigenvalue is 1.  

Because a transition matrix only moves things around and never creates or destroys them, the total "mass" of the system must be perfectly conserved. The only scaling factor that leaves the total mass unchanged is exactly 1.  

## Perron-Frobenius theorem
Suppose $A$ is a $M\times M$ matrix with non-negative entries.  
Suppose also that there is some positive integer $r$ such that all entries of the matrix $A^r$ are strictly positive numbers (irreducible).  
Then:
1. $A$ has a positive eigenvalue $\lambda_1$ with a corresponding eigenvector whose entries are all positive. 
2. If $\lambda$ is any other eigenvalue of $A$, then $|\lambda| < \lambda_1$.  
3. $\lambda_1$ has multiplicity 1. 

Conclusion 1 in the theorem guarantees that there is a probability vector that is an eigenvector of $T$.  

From the proposition we know that 1 is the corresponding eigenvalue. Thus, there really is a stationary distribution.  

Conclusion 2 says that all other eigenvalues of $T$ are smaller than 1 in absolute value - limit to 0.  

Conclusion 3 means that all eigenvectors corresponding to the eigenvalue 1 must be constant multiples of the stationary distribution vector.

## Stationary distribution 
Because the dominant eigenvalue is 1, other eigenvalues are less than 1. The eigenvector when the $\lambda = 1$ will give you the stationary distribution.  
:exclamation: Remember to normalize the eigenvector, as probability always adds up to 1!  

$$
\text{Stationary distribution} = \lim_{t \to \infin} 
P^tx_0 
$$

## Markov's property  
The future state depends **ONLY** on the **current state**, completely independent of the past sequence of events.


## Two-state Markov process
A small town has two types of weather: Sunny (S) and Rainy (R). The weather tomorrow depends on today's weather according to the following rules: 
- If today is sunny, tomorrow is sunny with probability 0.7 and rainy with probability 0.3.  
- If to day is rainy, tomorrow is sunny with probability 0.4 and rainy with probability 0.6.  

$$
\begin{array}{ccc}
\qquad \text{ Today is sunny} & \text{Today is rainy} & \\
\qquad \downarrow & \downarrow & \\

% First column with left bracket
P = \left[ \begin{array}{c} 0.7 \\ 0.3 \end{array} \right. & 

% Second column with right bracket
\left. \begin{array}{c} 0.4 \\ 0.6 \end{array} \right] & 

% Third column with the row labels
\begin{array}{l} \to \text{Tomorrow is sunny} \\ \to \text{Tomorrow is rainy} \end{array} \\
\end{array}
$$

[Back to Table of Contents](#table-of-contents)

# PageRank (Application of Markov Process)
## Goal 
To find out which node is more important - to find the PageRank vector $x$.  

$$
x = \lim_{t \to \infin} P^t x_0
$$

## Links are endorsements (Quantity and quality)
PageRank assumes that if Page A links to Page B, Page A is effectively casting a "vote" or endorsing Page B as a credible source of information. However, not all votes are equal. The algorithm assumes that a vote from a highly important page is worth more than a vote from an obscure page. 

**The math translation**  
A page's rank is determined by the sum of the ranks of all the pages linking to it, divided by the number of outbound links those referring pages have.

## "Random surfer" behaviour
- The surfer does not read the page or care what the content is about
- Equal probability.   

## Teleportation parameter (damping factor)
There are pages with no outgoing links. If the surfer lands here, the math stops.  

To fix this (make the matrix irreducible), the algorithm assumes that the surfer eventually gets bored. At any given moment, there is a certain probability that the surfer stops clicking links, types a completely random URL into their browser, and teleports somewhere else on the web.  

$$
\gamma - \text{Damping factor} \\
0 \le \gamma \le 1 \\
\text{Typically, } \gamma = 0.85
$$

Then the transformation matrix becomes:  
$$
T = \gamma P + (1-\gamma) \frac{1}{N}\hat{1}
$$
$$
x_{t+1} = Tx_t 
$$

**Edge cases**
- If $\gamma = 1$:   
  The surfer **NEVER** teleports. The system relies entirely on the links ($P$). If there are pages with no outgoing links ("dead ends"), the surfer gets stuck, and the math fails to find a unique stationary distribution.

- If $\gamma = 0$:  
   The surfer **ONLY** teleports. They completely ignore the actual links on the web. The PageRank becomes perfectly equal for every single page ($\frac{1}{N}$), making the algorithm useless.

[Back to Table of Contents](#table-of-contents)

# Undirected Graphs 
## Adjacency matrix 

$$
A_{ij} = 
\begin{cases}
   \text{if node j is connected to node i} && 1 \\
   \text{if node j is NOT connected to node i} && 0 
\end{cases}
$$
$$
\text{ From} \\
A = 
\begin{bmatrix} 
0 & 1 & 0 & 0 \\ 
1 & 0 & 1 & 0 \\ 
0 & 1 & 0 & 1 \\ 
0 & 0 & 1 & 0 
\end{bmatrix} \text{ To} \\
$$

:exclamation:$A$ has to be symmetric for an undirected graph!  

## Degree matrix 

$$
D_{ij} = 
\begin{cases}
   \text{if } j = i && \text{Total number of edges connected to the node} \\
   \text{if } j \neq i && 0 
\end{cases}
$$
$$
D = 
\begin{bmatrix} 
1 & 0 & 0 & 0 \\ 
0 & 2 & 0 & 0 \\ 
0 & 0 & 2 & 0 \\ 
0 & 0 & 0 & 1 
\end{bmatrix}
$$

## Laplacian matrix 
From physics of diffusion - heat flow from cold to hot.  

1. **Setup**  
   Looking at a specific node $i$.      
   Let $x_i$ be the temperature at node $i$.
   Let $x_j$ be the temperature at a neighboring node $j$.  

2. **Total net flow from node i**
   $$
   \text{Net flow from node i }  = \sum_{j\in neighbours} (x_i - x_j)
   $$

3. **Using adjacency matrix**  
   When this node $j$ is NOT connected to $i$, zero value in the adjacency matrix removes the heat. 
   $$
   \text{Net flow from node i }  = \sum_{j = 1}^N A_{i,j} (x_i - x_j)
   $$

4. **Algebraic expansion**
   $$
   \text{Net flow from node i }  = \sum_{j = 1}^N A_{i,j} x_i - \sum_{j = 1}^N A_{i,j} x_j
   $$
   Because $x_i$ is a constant, we can put it out of the summation. 
   $$
   \text{Net flow from node i }  = x_i \sum_{j = 1}^N A_{i,j}  - \sum_{j = 1}^N A_{i,j} x_j
   $$
   We then identify that $\sum_{j = 1}^N A_{i,j}$ is simply the degree of the node. 
   $$
   \text{Net flow from node i }  = x_i D_{i,i}  - \sum_{j = 1}^N A_{i,j} x_j
   $$

5. **Moving to matrix form (all nodes)** 
   $$
   \begin{aligned}
   \text{Total flow } &= Dx - Ax \\
   \text{Total flow } &= (D - A)x
   \end{aligned}
   $$
   Where $D-A$ is the Laplacian Matrix.  

$$
L_{ij} = 
\begin{cases}
   \text{if } j = i && \text{Degree of the node} \\
   \text{if two nodes are connected} && -1 \\
   \text{if two nodes are NOT connected} && 0
\end{cases}
$$

$$
\begin{aligned}
   L &= D - A \\
   &=  
   \begin{bmatrix} 
   1 & 0 & 0 & 0 \\ 
   0 & 2 & 0 & 0 \\ 
   0 & 0 & 2 & 0 \\ 
   0 & 0 & 0 & 1 
   \end{bmatrix} - 
   \begin{bmatrix} 
   0 & 1 & 0 & 0 \\ 
   1 & 0 & 1 & 0 \\ 
   0 & 1 & 0 & 1 \\ 
   0 & 0 & 1 & 0 
   \end{bmatrix} \\
   &= 
   \begin{bmatrix} 
   1 & -1 & 0 & 0 \\ 
   -1 & 2 & -1 & 0 \\ 
   0 & -1 & 2 & -1 \\ 
   0 & 0 & -1 & 1 
   \end{bmatrix}
\end{aligned}
$$

## Fiedler vector
1. **Find the laplacian matrix**
2. **Solve the eigenvalue problem**  
   
   $$
   Lv=\lambda v
   $$

3. **Identify the Fiedler vector**  
   Sort the eigenvalues in **increasing** order.  
   
   $\lambda_2$ is called the **algebraic connectivity** of the graph. It tells you how well connected the graph is (if it's zero, the graph is disconnected).  

   $v_2$ is the Fiedler vector.  

4. **Use the vector for partitioning**  
   Since the vector is orthogonal to the all-ones vector, its component must sum to zero, meaning some values will be positive and some will be negative
   - Positive values: Belong to one "cluster".  
   - Negative values: Belong to the other.  
   

[Back to Table of Contents](#table-of-contents)

# Directed graphs
## Adjacency matrix  
   Loss of symmetry - column from, row go. 

## Degree matrix  
   Two different degree matrices:   
   - In-degree matrix ($D_{in}$),  number of edges pointing TOWARD the node (calculated by adding the ROWS of adjacency matrix)
  
   - Out-degree matrix ($D_{out}$), number of edges pointing AWAY the node (calculated by adding the COLUMNS of adjacency matrix)
   
## Laplacian matrix
   $$
   L= D_{out} - A^T
   $$

[Back to Table of Contents](#table-of-contents)

