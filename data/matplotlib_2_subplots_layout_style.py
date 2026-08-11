# matplotlib: subplots, axes customization, and advanced layouts

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import os

SAVE_DIR = os.path.join(os.path.dirname(__file__), "matplotlib_examples")
os.makedirs(SAVE_DIR, exist_ok=True)

print("=" * 5, "Subplots: grid layout", "=" * 5)

# Create a 2x2 grid of subplots
x = np.linspace(0, 2 * np.pi, 100)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(x, np.sin(x), color="steelblue")
axes[0, 0].set_title("sin(x)")
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].plot(x, np.cos(x), color="coral")
axes[0, 1].set_title("cos(x)")
axes[0, 1].grid(True, alpha=0.3)

axes[1, 0].plot(x, np.tan(x), color="green")
axes[1, 0].set_title("tan(x)")
axes[1, 0].set_ylim(-5, 5)
axes[1, 0].grid(True, alpha=0.3)

axes[1, 1].plot(x, np.exp(-x), color="purple")
axes[1, 1].set_title("exp(-x)")
axes[1, 1].grid(True, alpha=0.3)

fig.suptitle("2x2 Subplot Grid", fontsize=16)
fig.tight_layout()
path = os.path.join(SAVE_DIR, "subplots_grid.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# Unshare axes for clarity
fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharey=False)

for i, (func, name, color) in enumerate([
    (np.sin, "sin", "blue"),
    (np.cos, "cos", "red"),
    (np.tan, "tan", "green"),
]):
    axes[i].plot(x, func(x), color=color)
    axes[i].set_title(name)
    axes[i].grid(True, alpha=0.3)

fig.suptitle("1x3 Subplots (unshared y-axis)")
fig.tight_layout()
path = os.path.join(SAVE_DIR, "subplots_row.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Subplot2grid and GridSpec", "=" * 5)

# subplot2grid: flexible layouts
fig = plt.figure(figsize=(12, 8))

ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
ax1.plot(x, np.sin(x), color="steelblue")
ax1.set_title("Wide (2 cols)")

ax2 = plt.subplot2grid((3, 3), (0, 2), rowspan=2)
ax2.plot(x, np.cos(x), color="coral")
ax2.set_title("Tall (2 rows)")

ax3 = plt.subplot2grid((3, 3), (1, 0))
ax3.plot(x, np.exp(-x), color="green")
ax3.set_title("Small")

ax4 = plt.subplot2grid((3, 3), (1, 1))
ax4.plot(x, np.log1p(x), color="purple")
ax4.set_title("Small")

ax5 = plt.subplot2grid((3, 3), (2, 0), colspan=3)
ax5.plot(x, x ** 2, color="orange")
ax5.set_title("Full width bottom")

fig.suptitle("subplot2grid Layout", fontsize=14)
fig.tight_layout()
path = os.path.join(SAVE_DIR, "subplot2grid.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# GridSpec
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(12, 8))
gs = GridSpec(3, 3, figure=fig, hspace=0.4, wspace=0.3)

ax1 = fig.add_subplot(gs[0, :2])
ax1.plot(x, np.sin(x))
ax1.set_title("Top: spans 2 cols")

ax2 = fig.add_subplot(gs[0, 2])
ax2.plot(x, np.cos(x))
ax2.set_title("Top right")

ax3 = fig.add_subplot(gs[1:, :])
ax3.plot(x, np.sin(x) * np.exp(-x / 5))
ax3.set_title("Bottom: full width")

fig.suptitle("GridSpec Layout", fontsize=14)
path = os.path.join(SAVE_DIR, "gridspec.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Twin axes (dual y-axis)", "=" * 5)

t = np.linspace(0, 10, 100)
temp = 20 + 5 * np.sin(t)
humidity = 60 + 20 * np.cos(t * 0.5)

fig, ax1 = plt.subplots(figsize=(10, 5))

color1 = "tab:red"
ax1.set_xlabel("Time (hours)")
ax1.set_ylabel("Temperature (°C)", color=color1)
ax1.plot(t, temp, color=color1, linewidth=2)
ax1.tick_params(axis="y", labelcolor=color1)

ax2 = ax1.twinx()
color2 = "tab:blue"
ax2.set_ylabel("Humidity (%)", color=color2)
ax2.plot(t, humidity, color=color2, linewidth=2, linestyle="--")
ax2.tick_params(axis="y", labelcolor=color2)

ax1.set_title("Temperature and Humidity Over Time")
fig.tight_layout()
path = os.path.join(SAVE_DIR, "twin_axes.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Axes customization", "=" * 5)

# Custom tick labels and formatting
from matplotlib.ticker import FuncFormatter

x = np.linspace(0, 10, 100)
y = x ** 2

fig, ax = plt.subplots()
ax.plot(x, y, color="steelblue", linewidth=2)

# Custom axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 110)

# Custom ticks
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.set_xticklabels(["zero", "two", "four", "six", "eight", "ten"], rotation=45)

# Y-axis formatter (add "m²" suffix)
ax.yaxis.set_major_formatter(FuncFormatter(lambda val, pos: f"{val:.0f} m²"))

ax.set_title("Custom Ticks and Formatting")
ax.grid(True, alpha=0.3, linestyle="--")
path = os.path.join(SAVE_DIR, "custom_ticks.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# Log scale
x_log = np.logspace(0, 5, 100)
y_log = x_log ** 0.5

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(x_log, y_log)
axes[0].set_title("Linear Scale")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")

axes[1].plot(x_log, y_log)
axes[1].set_xscale("log")
axes[1].set_yscale("log")
axes[1].set_title("Log-Log Scale")
axes[1].set_xlabel("x (log)")
axes[1].set_ylabel("y (log)")

fig.suptitle("Linear vs Log Scale")
fig.tight_layout()
path = os.path.join(SAVE_DIR, "log_scale.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# Annotate with arrows
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, color="steelblue", linewidth=2)

# Add annotation with arrow
ax.annotate("Maximum", xy=(np.pi / 2, 1), xytext=(3, 1.3),
            arrowprops=dict(arrowstyle="->", color="red", lw=2),
            fontsize=12, color="red", fontweight="bold")

ax.annotate("Zero crossing", xy=(np.pi, 0), xytext=(4.5, -0.5),
            arrowprops=dict(arrowstyle="->", color="green", lw=1.5),
            fontsize=10, color="green")

ax.set_title("Annotations with Arrows")
ax.grid(True, alpha=0.3)
path = os.path.join(SAVE_DIR, "annotations.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Styling and appearance", "=" * 5)

# Built-in styles
x = np.linspace(0, 10, 100)

styles = ["default", "ggplot", "seaborn-v0_8-whitegrid"]
fig, axes = plt.subplots(1, len(styles), figsize=(15, 4))

for ax, style in zip(axes, styles):
    with plt.style.context(style):
        ax.plot(x, np.sin(x), linewidth=2)
        ax.plot(x, np.cos(x), linewidth=2)
        ax.set_title(f"Style: {style}")
        ax.grid(True, alpha=0.3)

fig.tight_layout()
path = os.path.join(SAVE_DIR, "styles.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# rcParams for global customization
with plt.rc_context({"font.size": 14, "figure.facecolor": "lightgray"}):
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), linewidth=3, color="navy")
    ax.set_title("Custom rcParams")
    path = os.path.join(SAVE_DIR, "rcparams.png")
    fig.savefig(path, dpi=100)
    plt.close(fig)
    print(f"Saved: {path}")

# Color maps
rng = np.random.default_rng(42)
data = rng.standard_normal((10, 10))

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
cmaps = ["viridis", "RdBu", "plasma"]
for ax, cmap in zip(axes, cmaps):
    im = ax.imshow(data, cmap=cmap, aspect="auto")
    ax.set_title(cmap)
    fig.colorbar(im, ax=ax)

fig.suptitle("Color Maps")
fig.tight_layout()
path = os.path.join(SAVE_DIR, "colormaps.png")
fig.savefig(path, dpi=100)
plt.close(fig)
print(f"Saved: {path}")

# Clean up
import shutil
shutil.rmtree(SAVE_DIR, ignore_errors=True)
print(f"\nCleaned up: {SAVE_DIR}")