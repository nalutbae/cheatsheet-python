# numpy: indexing, slicing, and boolean masks

import numpy as np

print("=" * 5, "Basic indexing", "=" * 5)

a = np.arange(10)
print(f"Array: {a}")  # [0 1 2 3 4 5 6 7 8 9]

# Single element
print(f"a[0]: {a[0]}")  # 0
print(f"a[-1]: {a[-1]}")  # 9
print(f"a[5]: {a[5]}")  # 5

# Slicing: start:stop:step
print(f"a[2:7]: {a[2:7]}")  # [2 3 4 5 6]
print(f"a[:5]: {a[:5]}")  # [0 1 2 3 4]
print(f"a[5:]: {a[5:]}")  # [5 6 7 8 9]
print(f"a[::2]: {a[::2]}")  # [0 2 4 6 8]
print(f"a[::-1]: {a[::-1]}")  # [9 8 7 6 5 4 3 2 1 0]
print(f"a[1:8:3]: {a[1:8:3]}")  # [1 4 7]

# Modify via indexing
a_copy = a.copy()
a_copy[0] = 100
a_copy[3:6] = [30, 40, 50]
print(f"Modified: {a_copy}")  # [100 1 2 30 40 50 6 7 8 9]

print("=" * 5, "2D array indexing", "=" * 5)

b = np.arange(20).reshape(4, 5)
print(f"2D array:\n{b}")

# Row and column access
print(f"b[0]: {b[0]}")  # [0 1 2 3 4] (first row)
print(f"b[-1]: {b[-1]}")  # [15 16 17 18 19] (last row)
print(f"b[1, 2]: {b[1, 2]}")  # 7 (row 1, col 2)
print(f"b[2, -1]: {b[2, -1]}")  # 14 (row 2, last col)

# Row slicing
print(f"b[0:2]: \n{b[0:2]}")  # first two rows

# Column access
print(f"b[:, 0]: {b[:, 0]}")  # [0 5 10 15] (first column)
print(f"b[:, -1]: {b[:, -1]}")  # [4 9 14 19] (last column)

# Sub-matrix
print(f"b[1:3, 2:4]:\n{b[1:3, 2:4]}")  # rows 1-2, cols 2-3

# Strided access
print(f"b[::2, ::2]:\n{b[::2, ::2]}")  # every other row and col

print("=" * 5, "Fancy indexing (integer arrays)", "=" * 5)

c = np.arange(10, 20)
print(f"Array: {c}")  # [10 11 12 13 14 15 16 17 18 19]

# Select specific indices
indices = [0, 2, 5, 9]
print(f"c[[0,2,5,9]]: {c[indices]}")  # [10 12 15 19]

# Select with negative indices
print(f"c[[-1, -3, -5]]: {c[[-1, -3, -5]]}")  # [19 17 15]

# Fancy indexing on 2D arrays
d = np.arange(12).reshape(3, 4)
print(f"\n2D array:\n{d}")

# Select specific rows
print(f"d[[0, 2]]:\n{d[[0, 2]]}")  # rows 0 and 2

# Select specific elements with paired indices
rows = [0, 1, 2]
cols = [1, 3, 0]
print(f"d[rows, cols]: {d[rows, cols]}")  # [1, 7, 8]

# Modify with fancy indexing
d_copy = d.copy()
d_copy[[0, 2], [1, 3]] = [100, 200]
print(f"After modification:\n{d_copy}")

# Fancy indexing with np.ix_
print(f"np.ix_ selection:\n{d[np.ix_([0, 2], [1, 3])]}")

print("=" * 5, "Boolean masks and conditional indexing", "=" * 5)

data = np.array([5, 12, 3, 18, 7, 25, 9, 30, 2])
print(f"Data: {data}")

# Create boolean mask
mask = data > 10
print(f"mask (>10): {mask}")  # [False True False True False True False True False]

# Apply mask
print(f"data[mask]: {data[mask]}")  # [12 18 25 30]
print(f"data[data > 10]: {data[data > 10]}")  # same

# Compound conditions
mask_and = (data > 5) & (data < 20)
mask_or = (data < 5) | (data > 25)
mask_not = ~(data > 15)
print(f"5 < data < 20: {data[mask_and]}")  # [12 18 7 9]
print(f"data<5 | data>25: {data[mask_or]}")  # [5 3 30 2]
print(f"NOT data>15: {data[mask_not]}")  # [5 12 3 7 9 2]

# np.where: conditional selection
result = np.where(data > 10, data, 0)
print(f"where(data>10, data, 0): {result}")  # [0 12 0 18 0 25 0 30 0]

result2 = np.where(data > 10, "high", "low")
print(f"where(data>10, 'high', 'low'): {result2}")

# Boolean operations on 2D arrays
matrix = np.arange(12).reshape(3, 4)
print(f"\nMatrix:\n{matrix}")

even_mask = matrix % 2 == 0
print(f"Even mask:\n{even_mask}")
print(f"Even values: {matrix[even_mask]}")  # [0 2 4 6 8 10]

# Count True values
print(f"Count even: {np.sum(even_mask)}")  # 6
print(f"Any > 10: {np.any(matrix > 10)}")  # True
print(f"All < 20: {np.all(matrix < 20)}")  # True

# np.argwhere: find indices where condition is True
indices = np.argwhere(matrix > 5)
print(f"Indices where > 5:\n{indices}")

# np.extract: extract elements satisfying condition
extracted = np.extract(matrix > 5, matrix)
print(f"Extract > 5: {extracted}")

print("=" * 5, "Modifying arrays with masks", "=" * 5)

arr = np.arange(10, dtype=float)
print(f"Original: {arr}")

# Set values based on condition
arr[arr < 5] = 0
print(f"After arr[arr<5]=0: {arr}")  # [0. 0. 0. 0. 0. 5. 6. 7. 8. 9.]

arr2 = np.arange(10, dtype=float)
arr2[arr2 > 5] *= 10
print(f"After arr[arr>5]*=10: {arr2}")  # [0. 1. 2. 3. 4. 5. 60. 70. 80. 90.]

# Clip values
arr3 = np.array([1, 5, 10, 15, 20, 25])
clipped = np.clip(arr3, 5, 20)
print(f"clip(5, 20): {clipped}")  # [5 5 10 15 20 20]

# Replace values with put
arr4 = np.arange(5)
np.put(arr4, [0, 4], [100, 400])
print(f"After put: {arr4}")  # [100 1 2 3 400]

# place: replace based on condition
arr5 = np.arange(10)
np.place(arr5, arr5 % 3 == 0, [-1])
print(f"After place: {arr5}")  # [-1 1 2 -1 4 5 -1 7 8 -1]

print("=" * 5, "View vs copy", "=" * 5)

original = np.arange(6)
view = original[2:5]  # view shares data
view[0] = 100
print(f"Original after view modification: {original}")  # [0 1 100 3 4 5]

original2 = np.arange(6)
copy = original2[2:5].copy()  # independent copy
copy[0] = 100
print(f"Original after copy modification: {original2}")  # [0 1 2 3 4 5] (unchanged)

# Check if array owns its data
print(f"View base: {view.base is not None}")  # True
print(f"Copy base: {copy.base is None}")  # True
print(f"View shares memory: {np.shares_memory(original, view)}")  # True
print(f"Copy shares memory: {np.shares_memory(original2, copy)}")  # False