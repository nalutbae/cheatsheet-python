# numpy: reshaping, broadcasting, and arithmetic operations

import numpy as np

print("=" * 5, "Reshaping arrays", "=" * 5)

a = np.arange(12)
print(f"Original: {a}")  # [0 1 2 3 4 5 6 7 8 9 10 11]

# Reshape to 2D
b = a.reshape(3, 4)
print(f"reshape(3,4):\n{b}")

# Reshape to 3D
c = a.reshape(2, 2, 3)
print(f"reshape(2,2,3):\n{c}")

# -1 means "infer this dimension"
d = a.reshape(3, -1)
print(f"reshape(3,-1):\n{d}")  # shape (3, 4)

e = a.reshape(-1, 6)
print(f"reshape(-1,6):\n{e}")  # shape (2, 6)

# Flatten arrays
f = b.flatten()  # returns a copy
g = b.ravel()    # returns a view when possible
print(f"flatten: {f}")  # [0 1 2 3 4 5 6 7 8 9 10 11]
print(f"ravel: {g}")  # [0 1 2 3 4 5 6 7 8 9 10 11]

# flatten vs ravel: flatten always copies, ravel may return view
print(f"flatten base: {f.base is None}")  # True (copy)
print(f"ravel base: {g.base is not None}")  # True (view)

# Transpose
print(f"\nOriginal:\n{b}")
print(f"Transpose:\n{b.T}")
print(f"Transpose shape: {b.T.shape}")  # (4, 3)

# Swap axes
c3d = np.arange(24).reshape(2, 3, 4)
print(f"\n3D shape: {c3d.shape}")  # (2, 3, 4)
swapped = np.swapaxes(c3d, 0, 2)
print(f"swapaxes(0,2) shape: {swapped.shape}")  # (4, 3, 2)

# Expand and squeeze dimensions
arr = np.arange(5)
print(f"\n1D shape: {arr.shape}")  # (5,)

expanded = np.expand_dims(arr, axis=0)
print(f"expand_dims(axis=0) shape: {expanded.shape}")  # (1, 5)

expanded2 = np.expand_dims(arr, axis=1)
print(f"expand_dims(axis=1) shape: {expanded2.shape}")  # (5, 1)

# np.newaxis is an alias for None
new_axis = arr[np.newaxis, :]
print(f"newaxis row shape: {new_axis.shape}")  # (1, 5)
new_axis2 = arr[:, np.newaxis]
print(f"newaxis col shape: {new_axis2.shape}")  # (5, 1)

# Squeeze: remove dimensions of size 1
squeezed = expanded.squeeze()
print(f"squeeze shape: {squeezed.shape}")  # (5,)

# Flip
print(f"\nflip (1D): {np.flip(arr)}")  # [4 3 2 1 0]
print(f"flipud (2D):\n{np.flipud(b)}")  # reverse rows
print(f"fliplr (2D):\n{np.fliplr(b)}")  # reverse columns

# Roll
print(f"roll(3): {np.roll(arr, 3)}")  # [2 3 4 0 1]

print("=" * 5, "Broadcasting", "=" * 5)

# Broadcasting rules:
# 1. If arrays have different ndim, prepend 1s to smaller shape
# 2. Dimensions of size 1 are stretched to match the other array
# 3. If sizes don't match and neither is 1, error

# Scalar + array (broadcasts scalar to all elements)
a1 = np.array([1, 2, 3])
print(f"Array + 10: {a1 + 10}")  # [11 12 13]

# 1D + 1D with broadcasting
row = np.array([[1, 2, 3]])  # shape (1, 3)
col = np.array([[10], [20], [30]])  # shape (3, 1)
result = row + col  # shape (3, 3)
print(f"\nBroadcasting (1,3) + (3,1):\n{result}")

# Broadcasting with 2D + 1D
matrix = np.ones((3, 4))
vector = np.array([1, 2, 3, 4])
result = matrix + vector  # broadcast (3,4) + (4,)
print(f"Matrix + vector:\n{result}")

# Broadcasting with 3D arrays
a_3d = np.ones((2, 3, 4))
b_1d = np.array([1, 2, 3, 4])
result_3d = a_3d * b_1d  # (2,3,4) * (4,)
print(f"3D broadcast shape: {result_3d.shape}")  # (2, 3, 4)

# Outer product via broadcasting
x = np.array([1, 2, 3])
y = np.array([10, 20, 30, 40])
outer = x[:, np.newaxis] * y[np.newaxis, :]
print(f"\nOuter product:\n{outer}")

# Distance matrix via broadcasting
points = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
dists = np.sqrt(np.sum(diff ** 2, axis=-1))
print(f"\nDistance matrix:\n{np.round(dists, 2)}")

print("=" * 5, "Element-wise arithmetic", "=" * 5)

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print(f"a + b: {a + b}")  # [11 22 33 44]
print(f"a - b: {a - b}")  # [ 9 18 27 36]
print(f"a * b: {a * b}")  # [ 10  40  90 160]
print(f"a / b: {a / b}")  # [10. 10. 10. 10.]
print(f"a // b: {a // b}")  # [10 10 10 10]
print(f"a % b: {a % b}")  # [0 0 0 0]
print(f"a ** b: {a ** b}")  # [    10    400  27000 2560000]

# Numpy functions (equivalent operators)
print(f"np.add(a, b): {np.add(a, b)}")
print(f"np.subtract(a, b): {np.subtract(a, b)}")
print(f"np.multiply(a, b): {np.multiply(a, b)}")
print(f"np.divide(a, b): {np.divide(a, b)}")
print(f"np.power(a, b): {np.power(a, b)}")
print(f"np.mod(a, b): {np.mod(a, b)}")
print(f"np.floor_divide(a, b): {np.floor_divide(a, b)}")

# In-place operations
c = np.array([1.0, 2.0, 3.0])
c += 10  # in-place addition
print(f"In-place +=: {c}")  # [11. 12. 13.]
c *= 2  # in-place multiplication
print(f"In-place *=: {c}")  # [22. 24. 26.]

# Comparison operations
x = np.array([1, 5, 3, 8, 2])
y = np.array([2, 4, 3, 7, 5])
print(f"\nx == y: {x == y}")  # [False False True False False]
print(f"x != y: {x != y}")  # [True True False True True]
print(f"x > y: {x > y}")  # [False True False True False]
print(f"x < y: {x < y}")  # [True False False False True]
print(f"x >= y: {x >= y}")  # [False True True True False]

# Logical operations
a_bool = np.array([True, True, False, False])
b_bool = np.array([True, False, True, False])
print(f"\nlogical_and: {np.logical_and(a_bool, b_bool)}")  # [True False False False]
print(f"logical_or: {np.logical_or(a_bool, b_bool)}")  # [True True True False]
print(f"logical_not: {np.logical_not(a_bool)}")  # [False False True True]
print(f"logical_xor: {np.logical_xor(a_bool, b_bool)}")  # [False True True False]

print("=" * 5, "Mathematical functions", "=" * 5)

angles = np.array([0, np.pi / 6, np.pi / 4, np.pi / 3, np.pi / 2])
print(f"sin: {np.round(np.sin(angles), 3)}")
print(f"cos: {np.round(np.cos(angles), 3)}")
print(f"tan: {np.round(np.tan(angles), 3)}")

# Exponential and logarithmic
vals = np.array([1, 2, 4, 8, 16])
print(f"\nexp(0): {np.exp(0)}")  # 1.0
print(f"log(e): {np.log(np.e)}")  # 1.0
print(f"log2: {np.log2(vals)}")  # [0. 1. 2. 3. 4.]
print(f"log10: {np.log10(vals)}")  # [0. 0.301 0.602 0.903 1.204]

# Rounding
x = np.array([1.23, 2.67, 3.14, -1.5, -2.5])
print(f"\nround(1): {np.round(x, 1)}")  # [ 1.2  2.7  3.1 -1.5 -2.5]
print(f"around: {np.around(x)}")  # [ 1.  3.  3. -2. -2.]
print(f"floor: {np.floor(x)}")  # [ 1.  2.  3. -2. -3.]
print(f"ceil: {np.ceil(x)}")  # [ 2.  3.  4. -1. -2.]
print(f"trunc: {np.trunc(x)}")  # [ 1.  2.  3. -1. -2.]

# Absolute values
neg = np.array([-3, -1, 0, 2, 4])
print(f"\nabs: {np.abs(neg)}")  # [3 1 0 2 4]

# Square root and power
nums = np.array([1, 4, 9, 16, 25])
print(f"sqrt: {np.sqrt(nums)}")  # [1. 2. 3. 4. 5.]
print(f"square: {np.square(nums)}")  # [1 16 81 256 625]

# Sign function
signed = np.array([-5, -1, 0, 1, 5])
print(f"sign: {np.sign(signed)}")  # [-1 -1 0 1 1]

print("=" * 5, "Matrix operations", "=" * 5)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication (@ operator or np.matmul)
print(f"A @ B:\n{A @ B}")
print(f"np.matmul(A, B):\n{np.matmul(A, B)}")

# Dot product
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(f"\nDot product: {np.dot(v1, v2)}")  # 32

# Inner and outer products
print(f"Inner product: {np.inner(v1, v2)}")  # 32
outer = np.outer(v1, v2)
print(f"Outer product:\n{outer}")

# Matrix determinant and inverse
det = np.linalg.det(A)
print(f"\nDeterminant: {det:.1f}")  # -2.0

inv = np.linalg.inv(A)
print(f"Inverse:\n{inv}")

# Verify: A @ inv ≈ I
identity = np.round(A @ inv, 10)
print(f"A @ inv:\n{identity}")  # approximately identity

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"\nEigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}")

# Matrix rank
rank = np.linalg.matrix_rank(A)
print(f"Rank: {rank}")  # 2

# Norm
print(f"Frobenius norm: {np.linalg.norm(A):.4f}")  # 5.4772
print(f"L2 norm of vector: {np.linalg.norm(v1):.4f}")  # 3.7417

# Solve linear system: Ax = b
A_sys = np.array([[3, 1], [1, 2]])
b_sys = np.array([9, 8])
x_sol = np.linalg.solve(A_sys, b_sys)
print(f"\nSolve Ax=b: x = {x_sol}")  # [2. 3.]
print(f"Verify: A @ x = {A_sys @ x_sol}")  # [9. 8.]