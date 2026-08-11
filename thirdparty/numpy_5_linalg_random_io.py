# numpy: linear algebra, random, and file I/O

import numpy as np

print("=" * 5, "Linear algebra (numpy.linalg)", "=" * 5)

# Matrix creation
A = np.array([[2, 1], [1, 3]])
B = np.array([[1, 2], [3, 4]])

# Matrix multiplication
print(f"A @ B:\n{A @ B}")
print(f"np.matmul(A, B):\n{np.matmul(A, B)}")

# Element-wise vs matrix multiplication
C = np.array([[1, 2], [3, 4]])
D = np.array([[5, 6], [7, 8]])
print(f"\nElement-wise C * D:\n{C * D}")
print(f"Matrix C @ D:\n{C @ D}")

# Dot product of vectors
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(f"\nDot product: {np.dot(v1, v2)}")  # 32

# Cross product
v3 = np.array([1, 0, 0])
v4 = np.array([0, 1, 0])
print(f"Cross product: {np.cross(v3, v4)}")  # [0 0 1]

# Matrix determinant
print(f"\nDeterminant of A: {np.linalg.det(A):.1f}")  # 5.0

# Matrix inverse
A_inv = np.linalg.inv(A)
print(f"Inverse of A:\n{A_inv}")
print(f"Verify A @ A_inv:\n{np.round(A @ A_inv, 10)}")  # ≈ identity

# Pseudo-inverse (for non-square or singular matrices)
M = np.array([[1, 2], [3, 4], [5, 6]])  # 3x2 matrix
M_pinv = np.linalg.pinv(M)
print(f"\nPseudo-inverse shape: {M_pinv.shape}")  # (2, 3)

# Solve linear system Ax = b
A_sys = np.array([[3, 1], [1, 2]])
b_sys = np.array([9, 8])
x = np.linalg.solve(A_sys, b_sys)
print(f"\nSolve Ax=b: x = {x}")  # [2. 3.]
print(f"Verify: A@x = {A_sys @ x}")  # [9. 8.]

# Eigenvalues and eigenvectors
M_eig = np.array([[4, -1], [2, 1]])
eigenvalues, eigenvectors = np.linalg.eig(M_eig)
print(f"\nEigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}")

# Singular Value Decomposition (SVD)
M_svd = np.array([[1, 2], [3, 4], [5, 6]])
U, S, Vt = np.linalg.svd(M_svd)
print(f"\nSVD: U shape {U.shape}, S {S}, Vt shape {Vt.shape}")
# Reconstruct
reconstructed = U @ np.diag(S) @ Vt
print(f"Reconstructed (close to original): {np.allclose(M_svd, reconstructed)}")

# Norm
v = np.array([3, 4])
print(f"\nL2 norm of [3,4]: {np.linalg.norm(v):.1f}")  # 5.0
print(f"L1 norm of [3,4]: {np.linalg.norm(v, ord=1):.1f}")  # 7.0

# Matrix condition number
print(f"Condition number of A: {np.linalg.cond(A):.4f}")

# Trace
print(f"Trace of A: {np.trace(A)}")  # 5

# Matrix rank
print(f"Rank of A: {np.linalg.matrix_rank(A)}")  # 2

print("=" * 5, "Advanced random (numpy.random)", "=" * 5)

rng = np.random.default_rng(42)

# Distributions
print("Common distributions:")
normal = rng.normal(loc=0, scale=1, size=5)
print(f"  Normal(0,1): {np.round(normal, 3)}")

uniform = rng.uniform(low=0, high=10, size=5)
print(f"  Uniform(0,10): {np.round(uniform, 3)}")

poisson = rng.poisson(lam=5, size=5)
print(f"  Poisson(5): {poisson}")

binomial = rng.binomial(n=10, p=0.5, size=5)
print(f"  Binomial(10,0.5): {binomial}")

exponential = rng.exponential(scale=2, size=5)
print(f"  Exponential(2): {np.round(exponential, 3)}")

chi2 = rng.chisquare(df=2, size=5)
print(f"  Chi-squared(2): {np.round(chi2, 3)}")

beta = rng.beta(a=2, b=5, size=5)
print(f"  Beta(2,5): {np.round(beta, 3)}")

# Random integers
dice = rng.integers(1, 7, size=10)
print(f"\nDice rolls: {dice}")

# Random choice with probabilities
items = ["A", "B", "C", "D"]
probs = [0.4, 0.3, 0.2, 0.1]
choices = rng.choice(items, size=10, p=probs)
print(f"Weighted choice: {choices}")

# Shuffle
arr = np.arange(10)
rng.shuffle(arr)
print(f"Shuffled: {arr}")

# Permutation (returns copy)
perm = rng.permutation(10)
print(f"Permutation: {perm}")

# Seed for reproducibility
rng1 = np.random.default_rng(123)
rng2 = np.random.default_rng(123)
print(f"\nSame seed rng1: {rng1.random(3)}")
print(f"Same seed rng2: {rng2.random(3)}")  # identical

# Sampling without replacement
sample = rng.choice(52, size=5, replace=False)
print(f"Poker hand: {sorted(sample)}")

print("=" * 5, "File I/O", "=" * 5)

import os

EXAMPLE_DIR = os.path.join(os.path.dirname(__file__), "thirdparty_examples")
os.makedirs(EXAMPLE_DIR, exist_ok=True)

# Save and load .npy (binary, single array)
arr = np.arange(12).reshape(3, 4)
npy_path = os.path.join(EXAMPLE_DIR, "array.npy")
np.save(npy_path, arr)
loaded = np.load(npy_path)
print(f"Saved and loaded .npy:")
print(f"  Original shape: {arr.shape}")
print(f"  Loaded shape: {loaded.shape}")
print(f"  Equal: {np.array_equal(arr, loaded)}")  # True

# Save and load .npz (multiple arrays)
arr1 = np.arange(6)
arr2 = np.arange(10, 16)
arr3 = np.ones((2, 3))
npz_path = os.path.join(EXAMPLE_DIR, "arrays.npz")
np.savez(npz_path, first=arr1, second=arr2, third=arr3)
loaded_npz = np.load(npz_path)
print(f"\nLoaded .npz:")
print(f"  Keys: {list(loaded_npz.keys())}")
print(f"  first: {loaded_npz['first']}")
print(f"  second: {loaded_npz['second']}")
loaded_npz.close()  # always close npz files

# Savez compressed (smaller file size)
npz_comp_path = os.path.join(EXAMPLE_DIR, "arrays_compressed.npz")
np.savez_compressed(npz_comp_path, first=arr1, second=arr2, third=arr3)
npy_size = os.path.getsize(npy_path)
npz_size = os.path.getsize(npz_path)
comp_size = os.path.getsize(npz_comp_path)
print(f"\nFile sizes: .npy={npy_size}B, .npz={npz_size}B, compressed={comp_size}B")

# Save and load CSV text
csv_path = os.path.join(EXAMPLE_DIR, "data.csv")
data = np.arange(20).reshape(5, 4)
np.savetxt(csv_path, data, delimiter=",", header="col0,col1,col2,col3",
           comments="", fmt="%d")
print(f"\nSaved CSV:")
with open(csv_path) as f:
    print(f.read())

# Load CSV text
loaded_csv = np.loadtxt(csv_path, delimiter=",", skiprows=1, dtype=int)
print(f"Loaded CSV:")
print(loaded_csv)
print(f"Equal: {np.array_equal(data, loaded_csv)}")

# Load CSV with specific columns
col1_col3 = np.loadtxt(csv_path, delimiter=",", skiprows=1, usecols=(1, 3), dtype=int)
print(f"Columns 1,3: {col1_col3}")

# Save/load with header for readability
data_path = os.path.join(EXAMPLE_DIR, "measurements.csv")
measurements = np.array([
    [1.0, 23.5, 0.95],
    [2.0, 24.1, 0.93],
    [3.0, 22.8, 0.97],
    [4.0, 23.9, 0.94],
])
np.savetxt(data_path, measurements, delimiter=",",
           header="time,temperature,efficiency", comments="", fmt="%.2f")
loaded_meas = np.loadtxt(data_path, delimiter=",", skiprows=1)
print(f"\nLoaded measurements:\n{loaded_meas}")

# Clean up
import shutil
shutil.rmtree(EXAMPLE_DIR)
print("\nCleaned up examples directory")

print("=" * 5, "Practical: data analysis example", "=" * 5)

# Simulate experimental data
rng2 = np.random.default_rng(42)
n = 1000
temps = rng2.normal(25, 3, n)  # temperature readings
pressures = 101.3 + 0.5 * (temps - 25) + rng2.normal(0, 0.5, n)
efficiency = 0.95 - 0.002 * (temps - 25) ** 2 + rng2.normal(0, 0.01, n)

# Statistical summary
print(f"Temperature: mean={temps.mean():.2f}, std={temps.std():.2f}")
print(f"Pressure: mean={pressures.mean():.2f}, std={pressures.std():.2f}")
print(f"Efficiency: mean={efficiency.mean():.4f}, std={efficiency.std():.4f}")

# Correlation
corr_temp_eff = np.corrcoef(temps, efficiency)[0, 1]
print(f"Correlation(temp, efficiency): {corr_temp_eff:.4f}")

# Filtering
high_eff = efficiency[efficiency > 0.93]
print(f"High efficiency (>0.93): {len(high_eff)} samples out of {n}")

# Best efficiency range
best_temp_idx = np.argmax(efficiency)
print(f"Best efficiency: {efficiency[best_temp_idx]:.4f} at temp={temps[best_temp_idx]:.2f}")

# Binning analysis
temp_bins = np.digitize(temps, bins=[20, 22, 24, 26, 28, 30])
for bin_num in range(1, 7):
    mask = temp_bins == bin_num
    if mask.any():
        avg_eff = efficiency[mask].mean()
        print(f"  Temp bin {bin_num}: avg efficiency={avg_eff:.4f}, count={mask.sum()}")