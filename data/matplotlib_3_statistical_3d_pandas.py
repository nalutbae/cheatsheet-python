# matplotlib: statistical plots, 3D plots, and pandas integration

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import os

SAVE_DIR = os.path.join(os.path.dirname(__file__), "matplotlib_examples")
os.makedirs(SAVE_DIR, exist_ok=True)

print("=" * 5, "Box plot (whisker plot)", "=" * 5)

rng = np.random.default_rng(42)
data_a = rng.normal(0, 1, 100)
data_b = rng.normal(1, 1.5, 100)
data_c = rng.normal(-0.5, 0.8, 100)

fig, ax = plt.subplots()
bp = ax.boxplot([data_a, data_b, data_c], tick_labels=["A", "B", "C"],
                patch_artist=True,
                boxprops=dict(facecolor="lightblue"),
                medianprops=dict(color="red", linewidth=2))
ax.set_title("Box Plot Comparison")
ax.set_ylabel("Value")
ax.grid(True, alpha=0.3, axis="y")
path = os.path.join(SAVE_DIR, "boxplot.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# Notched box plot
fig, ax = plt.subplots()
ax.boxplot([data_a, data_b, data_c], tick_labels=["A", "B", "C"],
           notch=True, patch_artist=True,
           boxprops=dict(facecolor="lightgreen"))
ax.set_title("Notched Box Plot")
path = os.path.join(SAVE_DIR, "boxplot_notched.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Violin plot", "=" * 5)

fig, ax = plt.subplots()
parts = ax.violinplot([data_a, data_b, data_c], showmeans=True, showmedians=True)
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(["A", "B", "C"])
ax.set_title("Violin Plot")
path = os.path.join(SAVE_DIR, "violin.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Heatmap", "=" * 5)

# Correlation matrix heatmap
data = rng.standard_normal((100, 5))
corr = np.corrcoef(data.T)

fig, ax = plt.subplots()
im = ax.imshow(corr, cmap="RdBu_r", vmin=-1, vmax=1, aspect="auto")
ax.set_xticks(range(5))
ax.set_yticks(range(5))
ax.set_xticklabels([f"Var{i+1}" for i in range(5)])
ax.set_yticklabels([f"Var{i+1}" for i in range(5)])
ax.set_title("Correlation Matrix Heatmap")

# Add text annotations
for i in range(5):
    for j in range(5):
        ax.text(j, i, f"{corr[i, j]:.2f}", ha="center", va="center", fontsize=9)

fig.colorbar(im, ax=ax, label="Correlation")
path = os.path.join(SAVE_DIR, "heatmap.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Contour plot", "=" * 5)

x_grid = np.linspace(-3, 3, 100)
y_grid = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x_grid, y_grid)
Z = np.sin(X) * np.cos(Y)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Contour lines
cs = axes[0].contour(X, Y, Z, levels=15, cmap="viridis")
axes[0].clabel(cs, inline=True, fontsize=8)
axes[0].set_title("Contour Lines")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")

# Filled contour
cf = axes[1].contourf(X, Y, Z, levels=15, cmap="viridis")
fig.colorbar(cf, ax=axes[1])
axes[1].set_title("Filled Contour")
axes[1].set_xlabel("x")
axes[1].set_ylabel("y")

fig.suptitle("Contour Plots")
fig.tight_layout()
path = os.path.join(SAVE_DIR, "contour.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "3D surface and scatter", "=" * 5)

# 3D surface plot
fig = plt.figure(figsize=(10, 5))

ax1 = fig.add_subplot(121, projection="3d")
X_3d = np.linspace(-5, 5, 50)
Y_3d = np.linspace(-5, 5, 50)
X3, Y3 = np.meshgrid(X_3d, Y_3d)
Z3 = np.sin(np.sqrt(X3**2 + Y3**2))
ax1.plot_surface(X3, Y3, Z3, cmap="viridis", alpha=0.8)
ax1.set_title("3D Surface")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")

# 3D scatter plot
ax2 = fig.add_subplot(122, projection="3d")
n = 100
x3 = rng.standard_normal(n)
y3 = rng.standard_normal(n)
z3 = rng.standard_normal(n)
colors3 = rng.standard_normal(n)
ax2.scatter(x3, y3, z3, c=colors3, cmap="plasma", alpha=0.6, s=30)
ax2.set_title("3D Scatter")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")

fig.suptitle("3D Plots")
fig.tight_layout()
path = os.path.join(SAVE_DIR, "plot3d.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Area plot (stacked)", "=" * 5)

x = np.arange(1, 11)
y1 = np.array([1, 3, 4, 3, 5, 6, 7, 8, 7, 9])
y2 = np.array([2, 2, 3, 4, 3, 4, 5, 4, 5, 6])
y3 = np.array([1, 1, 2, 2, 3, 2, 3, 3, 4, 3])

fig, ax = plt.subplots()
ax.stackplot(x, y1, y2, y3, labels=["A", "B", "C"],
             colors=["steelblue", "coral", "green"], alpha=0.7)
ax.set_title("Stacked Area Chart")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend(loc="upper left")
ax.grid(True, alpha=0.3)
path = os.path.join(SAVE_DIR, "area_stacked.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Pandas integration", "=" * 5)

import pandas as pd

df = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "sales": [120, 150, 170, 200, 230, 250, 280, 260, 240, 210, 180, 160],
    "expenses": [80, 90, 100, 110, 120, 130, 140, 135, 125, 110, 95, 85],
    "profit": [40, 60, 70, 90, 110, 120, 140, 125, 115, 100, 85, 75],
})

# Line plot from DataFrame
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["month"], df["sales"], marker="o", label="Sales", linewidth=2)
ax.plot(df["month"], df["expenses"], marker="s", label="Expenses", linewidth=2)
ax.plot(df["month"], df["profit"], marker="^", label="Profit", linewidth=2)
ax.set_title("Monthly Financial Report")
ax.set_xlabel("Month")
ax.set_ylabel("Amount ($)")
ax.legend()
ax.grid(True, alpha=0.3)
path = os.path.join(SAVE_DIR, "pandas_line.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# Bar chart from DataFrame
fig, ax = plt.subplots(figsize=(10, 5))
x_pos = np.arange(len(df))
width = 0.25
ax.bar(x_pos - width, df["sales"], width, label="Sales", color="steelblue")
ax.bar(x_pos, df["expenses"], width, label="Expenses", color="coral")
ax.bar(x_pos + width, df["profit"], width, label="Profit", color="green")
ax.set_xticks(x_pos)
ax.set_xticklabels(df["month"])
ax.set_title("Monthly Financial Comparison")
ax.set_ylabel("Amount ($)")
ax.legend()
path = os.path.join(SAVE_DIR, "pandas_bar.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# DataFrame.plot() shortcut
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

df.plot(x="month", y=["sales", "expenses", "profit"], kind="line", ax=axes[0, 0], title="Line")
df.plot(x="month", y="sales", kind="bar", ax=axes[0, 1], title="Bar", color="steelblue")
df[["sales", "expenses", "profit"]].plot(kind="hist", ax=axes[1, 0], title="Histogram", bins=6, alpha=0.7)
df.plot(x="month", y="sales", kind="area", ax=axes[1, 1], title="Area", alpha=0.5)

fig.suptitle("DataFrame.plot() Methods", fontsize=14)
fig.tight_layout()
path = os.path.join(SAVE_DIR, "pandas_plot_shortcuts.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# Clean up
import shutil
shutil.rmtree(SAVE_DIR, ignore_errors=True)
print(f"\nCleaned up: {SAVE_DIR}")