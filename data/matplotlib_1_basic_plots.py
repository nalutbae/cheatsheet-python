# matplotlib: line plots, scatter plots, bar charts, and basic customization

import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for script execution

import matplotlib.pyplot as plt
import numpy as np
import os

SAVE_DIR = os.path.join(os.path.dirname(__file__), "matplotlib_examples")
os.makedirs(SAVE_DIR, exist_ok=True)

print("=" * 5, "Line plot", "=" * 5)

# Simple line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Sine Wave")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
path = os.path.join(SAVE_DIR, "line_simple.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# Multiple lines with legend
x = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots()
ax.plot(x, np.sin(x), label="sin(x)", color="blue", linewidth=2)
ax.plot(x, np.cos(x), label="cos(x)", color="red", linewidth=2, linestyle="--")
ax.plot(x, np.sin(x) + np.cos(x), label="sin+cos", color="green", linestyle=":")
ax.set_title("Trigonometric Functions")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True, alpha=0.3)
path = os.path.join(SAVE_DIR, "line_multi.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# Line style and marker customization
x = [1, 2, 3, 4, 5]
y = [1, 4, 2, 8, 5]
fig, ax = plt.subplots()
ax.plot(x, y, marker="o", markersize=10, markerfacecolor="red",
        markeredgecolor="black", linewidth=2, linestyle="-.", color="navy")
ax.set_title("Custom Line Style and Markers")
path = os.path.join(SAVE_DIR, "line_style.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Scatter plot", "=" * 5)

rng = np.random.default_rng(42)
x = rng.standard_normal(100)
y = 2 * x + rng.standard_normal(100) * 0.5
colors = rng.standard_normal(100)
sizes = rng.uniform(20, 200, 100)

fig, ax = plt.subplots()
scatter = ax.scatter(x, y, c=colors, s=sizes, cmap="viridis", alpha=0.6, edgecolors="black")
ax.set_title("Scatter Plot with Color and Size")
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.colorbar(scatter, label="z value")
path = os.path.join(SAVE_DIR, "scatter.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# Scatter with regression line
x_data = rng.standard_normal(50)
y_data = 1.5 * x_data + 0.5 + rng.standard_normal(50) * 0.3
coeffs = np.polyfit(x_data, y_data, 1)
x_fit = np.linspace(x_data.min() - 0.5, x_data.max() + 0.5, 100)
y_fit = np.polyval(coeffs, x_fit)

fig, ax = plt.subplots()
ax.scatter(x_data, y_data, color="steelblue", alpha=0.7, label="Data")
ax.plot(x_fit, y_fit, color="red", linewidth=2, label=f"y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}")
ax.set_title("Scatter with Regression Line")
ax.legend()
path = os.path.join(SAVE_DIR, "scatter_regression.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Bar chart", "=" * 5)

# Vertical bar chart
categories = ["A", "B", "C", "D", "E"]
values = [23, 45, 56, 78, 32]
colors_bar = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

fig, ax = plt.subplots()
ax.bar(categories, values, color=colors_bar, edgecolor="black", linewidth=0.5)
ax.set_title("Vertical Bar Chart")
ax.set_ylabel("Value")
ax.set_xlabel("Category")
for i, v in enumerate(values):
    ax.text(i, v + 1, str(v), ha="center", va="bottom")
path = os.path.join(SAVE_DIR, "bar_vertical.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# Horizontal bar chart
fig, ax = plt.subplots()
ax.barh(categories, values, color=colors_bar, edgecolor="black")
ax.set_title("Horizontal Bar Chart")
ax.set_xlabel("Value")
for i, v in enumerate(values):
    ax.text(v + 1, i, str(v), va="center")
path = os.path.join(SAVE_DIR, "bar_horizontal.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# Grouped bar chart
x_pos = np.arange(len(categories))
width = 0.35
values_a = [23, 45, 56, 78, 32]
values_b = [18, 52, 43, 65, 40]

fig, ax = plt.subplots()
ax.bar(x_pos - width / 2, values_a, width, label="Group A", color="steelblue")
ax.bar(x_pos + width / 2, values_b, width, label="Group B", color="coral")
ax.set_xticks(x_pos)
ax.set_xticklabels(categories)
ax.set_title("Grouped Bar Chart")
ax.legend()
path = os.path.join(SAVE_DIR, "bar_grouped.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# Stacked bar chart
fig, ax = plt.subplots()
ax.bar(categories, values_a, label="Group A", color="steelblue")
ax.bar(categories, values_b, bottom=values_a, label="Group B", color="coral")
ax.set_title("Stacked Bar Chart")
ax.legend()
path = os.path.join(SAVE_DIR, "bar_stacked.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Histogram", "=" * 5)

rng = np.random.default_rng(42)
data_normal = rng.standard_normal(1000)
data_skewed = rng.exponential(2, 1000)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].hist(data_normal, bins=30, color="steelblue", edgecolor="black", alpha=0.7)
axes[0].set_title("Normal Distribution")
axes[0].set_xlabel("Value")
axes[0].set_ylabel("Frequency")

axes[1].hist(data_skewed, bins=30, color="coral", edgecolor="black", alpha=0.7)
axes[1].set_title("Exponential Distribution")
axes[1].set_xlabel("Value")
axes[1].set_ylabel("Frequency")

fig.suptitle("Histograms", fontsize=14)
fig.tight_layout()
path = os.path.join(SAVE_DIR, "histogram.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# Overlapping histograms
fig, ax = plt.subplots()
ax.hist(data_normal, bins=30, alpha=0.5, label="Normal", color="blue")
ax.hist(data_skewed, bins=30, alpha=0.5, label="Exponential", color="red")
ax.set_title("Overlapping Histograms")
ax.legend()
path = os.path.join(SAVE_DIR, "histogram_overlap.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Pie chart", "=" * 5)

labels = ["Python", "JavaScript", "Java", "C++", "Other"]
sizes = [35, 25, 20, 12, 8]
explode = (0.1, 0, 0, 0, 0)

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%",
       colors=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"],
       shadow=True, startangle=140)
ax.set_title("Programming Language Popularity")
path = os.path.join(SAVE_DIR, "pie.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Error bars and fill_between", "=" * 5)

x = np.linspace(0, 10, 50)
y = np.sin(x)
y_err = 0.2 + 0.1 * np.random.default_rng(42).standard_normal(50)

fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=y_err, fmt="o-", color="steelblue",
            ecolor="gray", elinewidth=1, capsize=3, markersize=4)
ax.set_title("Line with Error Bars")
path = os.path.join(SAVE_DIR, "errorbar.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# fill_between (confidence interval)
x = np.linspace(0, 10, 100)
y = np.sin(x)
y_upper = y + 0.3
y_lower = y - 0.3

fig, ax = plt.subplots()
ax.plot(x, y, color="blue", linewidth=2)
ax.fill_between(x, y_lower, y_upper, color="blue", alpha=0.2)
ax.set_title("Line with Confidence Band")
path = os.path.join(SAVE_DIR, "fill_between.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# Clean up example files
import shutil
shutil.rmtree(SAVE_DIR, ignore_errors=True)
print(f"\nCleaned up: {SAVE_DIR}")