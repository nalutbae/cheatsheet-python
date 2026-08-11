# numpy: array creation and basic operations

import numpy as np

print("=" * 5, "Array creation from Python data", "=" * 5)

# From Python list
arr1 = np.array([1, 2, 3, 4, 5])
print(f"1D array: {arr1}")  # [1 2 3 4 5]
print(f"Type: {type(arr1)}")  # <class 'numpy.ndarray'>
print(f"Dtype: {arr1.dtype}")  # int64
print(f"Shape: {arr1.shape}")  # (5,)
print(f"Size: {arr1.size}")  # 5
print(f"Ndim: {arr1.ndim}")  # 1

# 2D array from nested list
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D array:\n{arr2}")
print(f"Shape: {arr2.shape}")  # (2, 3)
print(f"Ndim: {arr2.ndim}")  # 2
print(f"Size: {arr2.size}")  # 6

# 3D array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"\n3D shape: {arr3.shape}")  # (2, 2, 2)

# Specify dtype explicitly
arr_float = np.array([1, 2, 3], dtype=np.float32)
arr_int = np.array([1.5, 2.7, 3.9], dtype=np.int32)
arr_bool = np.array([0, 1, 0, 1], dtype=np.bool_)
print(f"\nFloat32: {arr_float} (dtype={arr_float.dtype})")
print(f"Int32: {arr_int} (dtype={arr_int.dtype})")
print(f"Bool: {arr_bool} (dtype={arr_bool.dtype})")

# Common dtypes
print(f"\nCommon dtypes:")
print(f"  np.int8: {np.int8(1).nbytes} byte, range [{np.iinfo(np.int8).min}, {np.iinfo(np.int8).max}]")
print(f"  np.int32: {np.int32(1).nbytes} bytes, range [{np.iinfo(np.int32).min}, {np.iinfo(np.int32).max}]")
print(f"  np.float32: {np.float32(1).nbytes} bytes")
print(f"  np.float64: {np.float64(1).nbytes} bytes")

print("=" * 5, "Array creation functions", "=" * 5)

# zeros, ones, empty
z = np.zeros((3, 4))
print(f"zeros(3,4):\n{z}")

o = np.ones((2, 3))
print(f"ones(2,3):\n{o}")

e = np.empty((2, 2))  # uninitialized values
print(f"empty(2,2):\n{e}")

# full: fill with a specific value
f = np.full((3, 3), 7)
print(f"full(3,3,7):\n{f}")

# zeros_like, ones_like, full_like
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\nzeros_like:\n{np.zeros_like(arr)}")
print(f"ones_like:\n{np.ones_like(arr)}")
print(f"full_like(99):\n{np.full_like(arr, 99)}")

# Identity and eye
I = np.eye(4)
print(f"\neye(4):\n{I}")

diag = np.diag([1, 2, 3])
print(f"\ndiag([1,2,3]):\n{diag}")

print("=" * 5, "Range and linspace", "=" * 5)

# arange: like Python's range but returns array
a1 = np.arange(10)
print(f"arange(10): {a1}")  # [0 1 2 3 4 5 6 7 8 9]

a2 = np.arange(2, 10, 2)
print(f"arange(2,10,2): {a2}")  # [2 4 6 8]

a3 = np.arange(0, 1, 0.2)
print(f"arange(0,1,0.2): {a3}")  # [0.  0.2 0.4 0.6 0.8]

# linspace: evenly spaced numbers over interval
l1 = np.linspace(0, 1, 5)
print(f"linspace(0,1,5): {l1}")  # [0.   0.25 0.5  0.75 1.  ]

l2 = np.linspace(0, 2 * np.pi, 5)
print(f"linspace(0,2π,5): {l2}")

# logspace: logarithmically spaced
log1 = np.logspace(0, 3, 4)  # 10^0 to 10^3
print(f"logspace(0,3,4): {log1}")  # [   1.   10.  100. 1000.]

# geomspace: geometrically spaced
geo1 = np.geomspace(1, 1000, 4)
print(f"geomspace(1,1000,4): {geo1}")  # [   1.   10.  100. 1000.]

print("=" * 5, "Random number generation", "=" * 5)

# Set seed for reproducibility
rng = np.random.default_rng(42)

# Random floats in [0, 1)
r1 = rng.random((2, 3))
print(f"random(2,3):\n{r1}")

# Random integers
r2 = rng.integers(0, 10, size=5)
print(f"integers(0,10,5): {r2}")

r3 = rng.integers(1, 7, size=10)  # dice rolls
print(f"Dice rolls: {r3}")

# Normal distribution
r4 = rng.standard_normal((3, 3))
print(f"standard_normal(3,3):\n{r4}")

# Custom mean and std
r5 = rng.normal(loc=100, scale=15, size=5)
print(f"Normal(100,15,5): {r5}")

# Uniform distribution
r6 = rng.uniform(low=0, high=10, size=5)
print(f"Uniform(0,10,5): {r6}")

# Choice and shuffle
r7 = rng.choice([1, 2, 3, 4, 5], size=3, replace=False)
print(f"Choice (no replace): {r7}")

arr_shuffle = np.arange(10)
rng.shuffle(arr_shuffle)
print(f"Shuffled: {arr_shuffle}")

print("=" * 5, "Array attributes and methods", "=" * 5)

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.float64)
print(f"Array:\n{a}")
print(f"Shape: {a.shape}")  # (3, 3)
print(f"Ndim: {a.ndim}")  # 2
print(f"Size: {a.size}")  # 9
print(f"Dtype: {a.dtype}")  # float64
print(f"Itemsize: {a.itemsize}")  # 8 bytes
print(f"Nbytes: {a.nbytes}")  # 72 bytes (9 * 8)

# T attribute (transpose)
print(f"\nTranspose:\n{a.T}")

# Flat iterator
print(f"Flat: {list(a.flat)}")  # [1.0, 2.0, ..., 9.0]

# Convert to Python list
print(f"To list: {a.tolist()[:3]}")  # [[1.0, 2.0, 3.0], ...]

# Type conversion
print(f"As int32: {a.astype(np.int32).dtype}")  # int32
print(f"As bool: {np.array([0, 1, 0, 1]).astype(bool)}")  # [False True False True]

# Summary statistics
print(f"\nSum: {a.sum()}")  # 45.0
print(f"Mean: {a.mean()}")  # 5.0
print(f"Std: {a.std():.4f}")  # 2.5820
print(f"Var: {a.var():.4f}")  # 6.6667
print(f"Min: {a.min()}")  # 1.0
print(f"Max: {a.max()}")  # 9.0
print(f"Argmin: {a.argmin()}")  # 0
print(f"Argmax: {a.argmax()}")  # 8
print(f"Cumsum: {a.cumsum()}")  # [ 1.  3.  6. 10. 15. 21. 28. 36. 45.]
print(f"Cumprod: {a.cumprod()}")  # [1.0 2.0 6.0 24.0 120.0 720.0 ...]

# Axis-specific operations
print(f"\nSum axis=0 (columns): {a.sum(axis=0)}")  # [12. 15. 18.]
print(f"Sum axis=1 (rows): {a.sum(axis=1)}")  # [ 6. 15. 24.]
print(f"Mean axis=0: {a.mean(axis=0)}")  # [4. 5. 6.]
print(f"Min axis=1: {a.min(axis=1)}")  # [1. 4. 7.]
print(f"Max axis=0: {a.max(axis=0)}")  # [7. 8. 9.]