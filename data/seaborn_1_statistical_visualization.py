# seaborn: statistical data visualization built on matplotlib

import matplotlib
matplotlib.use("Agg")

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

SAVE_DIR = os.path.join(os.path.dirname(__file__), "seaborn_examples")
os.makedirs(SAVE_DIR, exist_ok=True)

# Set seaborn style
sns.set_theme(style="whitegrid")

print("=" * 5, "Built-in datasets", "=" * 5)

# Load built-in datasets
tips = sns.load_dataset("tips")
print(f"Tips dataset shape: {tips.shape}")
print(f"Tips columns: {tips.columns.tolist()}")
print(tips.head())

iris = sns.load_dataset("iris")
print(f"\nIris dataset shape: {iris.shape}")
print(f"Iris columns: {iris.columns.tolist()}")
print(iris.head())

print("=" * 5, "Relational plots: scatter and line", "=" * 5)

# Scatter plot with semantic mapping
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time",
                size="size", sizes=(20, 200), alpha=0.7, ax=ax)
ax.set_title("Tips: Bill vs Tip (colored by time, sized by party)")
path = os.path.join(SAVE_DIR, "scatter_hue_size.png")
fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {path}")

# relplot: Faceted scatter
g = sns.relplot(data=tips, x="total_bill", y="tip",
                col="time", hue="smoker", style="smoker",
                height=4, aspect=1.2)
g.fig.suptitle("Tips by Time and Smoker", y=1.02)
path = os.path.join(SAVE_DIR, "relplot_facet.png")
g.fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(g.fig)
print(f"Saved: {path}")

# Line plot with confidence interval
fig, ax = plt.subplots(figsize=(8, 5))
sns.lineplot(data=tips, x="size", y="total_bill", marker="o", ax=ax)
ax.set_title("Average Bill by Party Size (with 95% CI)")
path = os.path.join(SAVE_DIR, "line_ci.png")
fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Distribution plots", "=" * 5)

# Histogram with KDE
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(data=tips, x="total_bill", kde=True, ax=axes[0])
axes[0].set_title("Histogram + KDE")
sns.histplot(data=tips, x="total_bill", hue="time", kde=True, ax=axes[1])
axes[1].set_title("Split by Time")
fig.suptitle("Distribution of Total Bill")
fig.tight_layout()
path = os.path.join(SAVE_DIR, "histplot.png")
fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {path}")

# KDE plot
fig, ax = plt.subplots(figsize=(8, 5))
sns.kdeplot(data=tips, x="total_bill", hue="time", fill=True, alpha=0.5, ax=ax)
ax.set_title("KDE: Total Bill by Time")
path = os.path.join(SAVE_DIR, "kdeplot.png")
fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {path}")

# Ecdf plot (empirical cumulative distribution)
fig, ax = plt.subplots(figsize=(8, 5))
sns.ecdfplot(data=tips, x="total_bill", hue="time", ax=ax)
ax.set_title("ECDF: Total Bill by Time")
path = os.path.join(SAVE_DIR, "ecdfplot.png")
fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {path}")

# Rugplot (marginal ticks)
fig, ax = plt.subplots(figsize=(8, 5))
sns.kdeplot(data=tips, x="total_bill", ax=ax)
sns.rugplot(data=tips, x="total_bill", height=0.05, color="red", ax=ax)
ax.set_title("KDE + Rug Plot")
path = os.path.join(SAVE_DIR, "rugplot.png")
fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Categorical plots", "=" * 5)

# Box plot
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.boxplot(data=tips, x="day", y="total_bill", ax=axes[0])
axes[0].set_title("Box Plot: Bill by Day")
sns.boxplot(data=tips, x="day", y="total_bill", hue="time", ax=axes[1])
axes[1].set_title("Box Plot: Bill by Day and Time")
fig.tight_layout()
path = os.path.join(SAVE_DIR, "boxplot.png")
fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {path}")

# Violin plot
fig, ax = plt.subplots(figsize=(8, 5))
sns.violinplot(data=tips, x="day", y="total_bill", hue="time",
               split=True, inner="quartile", ax=ax)
ax.set_title("Violin Plot: Bill by Day (split by time)")
path = os.path.join(SAVE_DIR, "violin.png")
fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {path}")

# Bar plot (with confidence intervals)
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=tips, x="day", y="total_bill", hue="time", ax=ax)
ax.set_title("Bar Plot: Mean Bill by Day and Time")
path = os.path.join(SAVE_DIR, "barplot.png")
fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {path}")

# Count plot
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(data=tips, x="day", hue="time", ax=ax)
ax.set_title("Count Plot: Observations by Day and Time")
path = os.path.join(SAVE_DIR, "countplot.png")
fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {path}")

# Point plot
fig, ax = plt.subplots(figsize=(8, 5))
sns.pointplot(data=tips, x="day", y="total_bill", hue="time",
              markers=["o", "s"], linestyles=["-", "--"], ax=ax)
ax.set_title("Point Plot: Mean Bill by Day and Time")
path = os.path.join(SAVE_DIR, "pointplot.png")
fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {path}")

# Swarm plot
fig, ax = plt.subplots(figsize=(8, 5))
sns.swarmplot(data=tips, x="day", y="total_bill", hue="time", size=4, ax=ax)
ax.set_title("Swarm Plot: All Data Points by Day")
path = os.path.join(SAVE_DIR, "swarmplot.png")
fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {path}")

print("=" * 5, "Regression and correlation", "=" * 5)

# Regression plot
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.regplot(data=tips, x="total_bill", y="tip", scatter_kws={"alpha": 0.5}, ax=axes[0])
axes[0].set_title("regplot: Bill vs Tip")
sns.residplot(data=tips, x="total_bill", y="tip", ax=axes[1])
axes[1].set_title("residplot: Residuals")
fig.tight_layout()
path = os.path.join(SAVE_DIR, "regplot.png")
fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {path}")

# lmplot with facets
g = sns.lmplot(data=tips, x="total_bill", y="tip", col="time",
               hue="smoker", height=4, aspect=1.2)
g.fig.suptitle("lmplot: Bill vs Tip by Time and Smoker", y=1.02)
path = os.path.join(SAVE_DIR, "lmplot.png")
g.fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(g.fig)
print(f"Saved: {path}")

# Heatmap: correlation matrix
numeric_cols = iris.select_dtypes(include=[np.number])
corr = numeric_cols.corr()

fig, ax = plt.subplots(figsize=(7, 6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdBu_r", center=0,
            square=True, linewidths=0.5, ax=ax)
ax.set_title("Iris Correlation Matrix")
path = os.path.join(SAVE_DIR, "heatmap_corr.png")
fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {path}")

# Clustermap
g = sns.clustermap(corr, annot=True, fmt=".2f", cmap="RdBu_r",
                   center=0, figsize=(7, 7))
g.fig.suptitle("Iris Clustermap", y=1.02)
path = os.path.join(SAVE_DIR, "clustermap.png")
g.fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(g.fig)
print(f"Saved: {path}")

print("=" * 5, "Multi-plot grids", "=" * 5)

# Pairplot
g = sns.pairplot(iris, hue="species", height=2.5)
g.fig.suptitle("Iris Pairplot", y=1.02)
path = os.path.join(SAVE_DIR, "pairplot.png")
g.fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(g.fig)
print(f"Saved: {path}")

# Jointplot
g = sns.jointplot(data=tips, x="total_bill", y="tip", kind="reg",
                   height=6, ratio=4, marginal_ticks=True)
g.fig.suptitle("Jointplot: Bill vs Tip", y=1.02)
path = os.path.join(SAVE_DIR, "jointplot.png")
g.fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(g.fig)
print(f"Saved: {path}")

# Jointplot with KDE
g = sns.jointplot(data=tips, x="total_bill", y="tip", kind="kde",
                   height=6, fill=True, cmap="Blues")
g.fig.suptitle("Jointplot (KDE): Bill vs Tip", y=1.02)
path = os.path.join(SAVE_DIR, "jointplot_kde.png")
g.fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(g.fig)
print(f"Saved: {path}")

print("=" * 5, "Themes and color palettes", "=" * 5)

# Seaborn themes
themes = ["darkgrid", "whitegrid", "dark", "white", "ticks"]
fig, axes = plt.subplots(1, len(themes), figsize=(20, 4))

for ax, theme in zip(axes, themes):
    with sns.axes_style(theme):
        sns.barplot(data=tips, x="day", y="total_bill", ax=ax)
        ax.set_title(f'Style: "{theme}"')

fig.suptitle("Seaborn Themes", fontsize=14)
fig.tight_layout()
path = os.path.join(SAVE_DIR, "themes.png")
fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {path}")

# Color palettes
palettes = ["deep", "muted", "bright", "pastel", "colorblind", "Spectral", "coolwarm"]
fig, axes = plt.subplots(len(palettes), 1, figsize=(10, 2 * len(palettes)))

for ax, pal in zip(axes, palettes):
    colors = sns.color_palette(pal, 8)
    sns.barplot(x=range(8), y=[1] * 8, palette=colors, ax=ax)
    ax.set_ylabel("")
    ax.set_yticks([])
    ax.set_title(f'Palette: "{pal}"', fontsize=10)

fig.suptitle("Seaborn Color Palettes", fontsize=14)
fig.tight_layout()
path = os.path.join(SAVE_DIR, "palettes.png")
fig.savefig(path, dpi=100, bbox_inches="tight")
plt.close(fig)
print(f"Saved: {path}")

# Diverging palette
pal_div = sns.diverging_palette(220, 20, as_cmap=True)
print(f"Diverging palette (for heatmap): {type(pal_div).__name__}")

# Custom palette from list
custom_colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]
custom_pal = sns.color_palette(custom_colors)
print(f"Custom palette: {custom_pal}")

# Clean up
import shutil
shutil.rmtree(SAVE_DIR, ignore_errors=True)
print(f"\nCleaned up: {SAVE_DIR}")