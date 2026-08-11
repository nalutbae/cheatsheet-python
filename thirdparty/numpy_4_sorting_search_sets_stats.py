# numpy: sorting, searching, set operations, and statistics

import numpy as np

print("=" * 5, "Sorting", "=" * 5)

# 1D sorting
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Original: {arr}")
print(f"sort (ascending): {np.sort(arr)}")  # [1 1 2 3 4 5 6 9]
print(f"sort (descending): {np.sort(arr)[::-1]}")  # [9 6 5 4 3 2 1 1]

# argsort: indices that would sort the array
idx = np.argsort(arr)
print(f"argsort: {idx}")  # [1 3 6 0 2 4 7 5]
print(f"Sorted via argsort: {arr[idx]}")  # [1 1 2 3 4 5 6 9]

# 2D sorting
mat = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
print(f"\n2D array:\n{mat}")
print(f"Sort axis=0 (columns):\n{np.sort(mat, axis=0)}")
print(f"Sort axis=1 (rows):\n{np.sort(mat, axis=1)}")

# Sorting structured array
names = np.array(["Alice", "Bob", "Charlie", "Diana"])
scores = np.array([85, 92, 78, 95])
order = np.argsort(scores)
print(f"\nSorted by score:")
for i in order:
    print(f"  {names[i]}: {scores[i]}")

# Partial sorting (partition)
arr2 = np.array([7, 2, 3, 1, 6, 5, 4])
partitioned = np.partition(arr2, 3)
print(f"\nPartition at index 3: {partitioned}")  # first 3 are smallest
print(f"3 smallest: {np.partition(arr2, 3)[:3]}")  # not necessarily sorted

# argpartition
top3_idx = np.argpartition(arr2, 3)[:3]
print(f"Indices of 3 smallest: {top3_idx}")

print("=" * 5, "Searching", "=" * 5)

arr = np.array([1, 2, 3, 4, 5, 4, 3, 2, 1])

# argmax / argmin
print(f"argmax: {np.argmax(arr)}")  # 4 (index of max value 5)
print(f"argmin: {np.argmin(arr)}")  # 0 (index of min value 1)

# 2D argmax/argmin
mat = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\nargmax axis=0: {np.argmax(mat, axis=0)}")  # [1 1 1]
print(f"argmax axis=1: {np.argmax(mat, axis=1)}")  # [2 2]

# where: return indices where condition is True
indices = np.where(arr > 3)
print(f"\nwhere(arr > 3): {indices[0]}")  # [3 4 5]

# nonzero: indices of non-zero elements
sparse = np.array([0, 1, 0, 2, 0, 3, 0])
print(f"nonzero: {np.nonzero(sparse)[0]}")  # [1 3 5]

# searchsorted: find insertion points in sorted array
sorted_arr = np.array([1, 3, 5, 7, 9])
print(f"\nsearchsorted(4): {np.searchsorted(sorted_arr, 4)}")  # 2
print(f"searchsorted(6): {np.searchsorted(sorted_arr, 6)}")  # 3
print(f"searchsorted(5, right): {np.searchsorted(sorted_arr, 5, side='right')}")  # 3

# Extract values satisfying condition
data = np.array([10, 25, 30, 15, 40, 5, 35])
result = np.extract(data > 20, data)
print(f"extract(>20): {result}")  # [25 30 40 35]

print("=" * 5, "Set operations", "=" * 5)

a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5, 6, 7])

# Unique
arr = np.array([1, 2, 2, 3, 3, 3, 4])
unique, counts = np.unique(arr, return_counts=True)
print(f"unique: {unique}")  # [1 2 3 4]
print(f"counts: {counts}")  # [1 2 3 1]

# Intersection
print(f"\nintersect1d: {np.intersect1d(a, b)}")  # [3 4 5]

# Union
print(f"union1d: {np.union1d(a, b)}")  # [1 2 3 4 5 6 7]

# Set difference (in a but not in b)
print(f"setdiff1d: {np.setdiff1d(a, b)}")  # [1 2]

# Symmetric difference (in either but not both)
print(f"setxor1d: {np.setxor1d(a, b)}")  # [1 2 6 7]

# Membership test
test = np.array([2, 4, 6, 8])
mask = np.isin(test, a)
print(f"\nisin([2,4,6,8], a): {mask}")  # [ True  True False False]
print(f"Members: {test[mask]}")  # [2 4]

# In1d: test each element of arr1 in arr2
print(f"in1d: {np.in1d([1, 3, 5, 7], a)}")  # [ True  True  True False]

print("=" * 5, "Statistics", "=" * 5)

data = np.array([12, 15, 18, 22, 25, 28, 30, 35, 40, 45])

# Basic statistics
print(f"Sum: {np.sum(data)}")  # 270
print(f"Mean: {np.mean(data):.2f}")  # 27.00
print(f"Median: {np.median(data):.1f}")  # 26.5
print(f"Std: {np.std(data):.2f}")  # 9.72
print(f"Var: {np.var(data):.2f}")  # 94.50
print(f"Min: {np.min(data)}")  # 12
print(f"Max: {np.max(data)}")  # 45
print(f"Range: {np.ptp(data)}")  # 33 (peak-to-peak)

# Percentiles
print(f"\n25th percentile: {np.percentile(data, 25):.1f}")  # 19.5
print(f"50th percentile: {np.percentile(data, 50):.1f}")  # 26.5
print(f"75th percentile: {np.percentile(data, 75):.1f}")  # 33.75
print(f"90th percentile: {np.percentile(data, 90):.1f}")  # 41.5

# Quantiles (same as percentiles but 0-1 range)
print(f"\nQ1: {np.quantile(data, 0.25):.1f}")
print(f"Q2: {np.quantile(data, 0.50):.1f}")
print(f"Q3: {np.quantile(data, 0.75):.1f}")

# Correlation
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
corr = np.corrcoef(x, y)
print(f"\nCorrelation matrix:\n{corr}")
print(f"Correlation coefficient: {corr[0, 1]:.4f}")

# Covariance
cov = np.cov(x, y)
print(f"Covariance matrix:\n{cov}")

# Weighted statistics
values = np.array([1, 2, 3, 4, 5])
weights = np.array([1, 2, 3, 2, 1])
weighted_mean = np.average(values, weights=weights)
print(f"\nWeighted mean: {weighted_mean:.2f}")  # 3.00

# Axis-specific statistics on 2D arrays
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nMatrix:\n{mat}")
print(f"Mean (all): {mat.mean():.2f}")  # 5.0
print(f"Mean axis=0: {mat.mean(axis=0)}")  # [4. 5. 6.]
print(f"Mean axis=1: {mat.mean(axis=1)}")  # [2. 5. 8.]
print(f"Std axis=0: {np.round(mat.std(axis=0), 2)}")
print(f"Sum axis=0: {mat.sum(axis=0)}")  # [12 15 18]
print(f"Cumsum axis=1:\n{mat.cumsum(axis=1)}")

# Histogram
data_hist = np.random.default_rng(42).standard_normal(1000)
counts, bin_edges = np.histogram(data_hist, bins=10)
print(f"\nHistogram bins: {len(counts)}")
print(f"Counts: {counts[:5]}...")
print(f"Bin edges: {np.round(bin_edges[:5], 2)}...")

# Bincount: count occurrences of each value
int_arr = np.array([0, 1, 1, 2, 2, 2, 3, 3, 3, 3])
print(f"\nbincount: {np.bincount(int_arr)}")  # [1 2 3 4]

# Digitize: bin assignment
bins = np.array([0, 10, 20, 30, 40, 50])
values = np.array([5, 15, 25, 35, 45])
indices = np.digitize(values, bins)
print(f"Digitize: {indices}")  # [1 2 3 4 5]