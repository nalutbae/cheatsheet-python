# pandas: file I/O, plotting, and practical patterns

import pandas as pd
import numpy as np
import os
import tempfile

EXAMPLE_DIR = os.path.join(os.path.dirname(__file__), "pandas_examples")
os.makedirs(EXAMPLE_DIR, exist_ok=True)

print("=" * 5, "Reading and writing CSV", "=" * 5)

# Create sample DataFrame
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age": [25, 30, 35, 28, 22],
    "city": ["Seoul", "Tokyo", "London", "Paris", "Berlin"],
    "score": [85.5, 92.0, 78.5, 95.0, 88.0],
})

csv_path = os.path.join(EXAMPLE_DIR, "data.csv")

# Write CSV
df.to_csv(csv_path, index=False)
print(f"Written to {csv_path}")

# Read CSV
df_read = pd.read_csv(csv_path)
print(f"Read from CSV:\n{df_read}")

# Read CSV with options
df_custom = pd.read_csv(csv_path, usecols=["name", "score"], nrows=3)
print(f"\nSelected columns, 3 rows:\n{df_custom}")

# Read CSV with dtype specification
df_typed = pd.read_csv(csv_path, dtype={"age": "int32", "score": "float32"})
print(f"\nWith dtypes:\n{df_typed.dtypes}")

print("=" * 5, "Reading and writing JSON", "=" * 5)

json_path = os.path.join(EXAMPLE_DIR, "data.json")

# Write JSON
df.to_json(json_path, orient="records", indent=2)
print(f"Written JSON to {json_path}")

# Read JSON
df_json = pd.read_json(json_path)
print(f"\nRead from JSON:\n{df_json}")

# JSON with different orientations
print(f"\norient='index':\n{df.to_json(orient='index', indent=2)[:200]}...")
print(f"\norient='split':\n{df.to_json(orient='split', indent=2)[:200]}...")

print("=" * 5, "Reading and writing Excel", "=" * 5)

# Note: requires openpyxl for .xlsx files
# pip install openpyxl
try:
    excel_path = os.path.join(EXAMPLE_DIR, "data.xlsx")

    # Write Excel with multiple sheets
    with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Sheet1", index=False)
        df[["name", "score"]].to_excel(writer, sheet_name="Scores", index=False)

    # Read Excel
    df_excel = pd.read_excel(excel_path, sheet_name="Sheet1")
    print(f"Read from Excel:\n{df_excel}")

    # List all sheets
    xl = pd.ExcelFile(excel_path)
    print(f"\nSheet names: {xl.sheet_names}")

    # Read specific sheet
    df_scores = pd.read_excel(excel_path, sheet_name="Scores")
    print(f"\nScores sheet:\n{df_scores}")

except ImportError:
    print("openpyxl not installed. Install with: pip install openpyxl")

print("=" * 5, "Reading HTML tables", "=" * 5)

html_path = os.path.join(EXAMPLE_DIR, "table.html")
html_content = """<!DOCTYPE html>
<html><body>
<table>
  <tr><th>Name</th><th>Age</th><th>City</th></tr>
  <tr><td>Alice</td><td>25</td><td>Seoul</td></tr>
  <tr><td>Bob</td><td>30</td><td>Tokyo</td></tr>
  <tr><td>Charlie</td><td>35</td><td>London</td></tr>
</table>
</body></html>"""
with open(html_path, "w") as f:
    f.write(html_content)

# Read HTML table (requires lxml or html5lib)
try:
    tables = pd.read_html(html_path)
    print(f"Number of tables: {len(tables)}")
    print(f"First table:\n{tables[0]}")
except Exception as e:
    print(f"read_html requires lxml/html5lib: {e}")

print("=" * 5, "Reading other formats", "=" * 5)

# Clipboard (read from system clipboard)
# df_clipboard = pd.read_clipboard()  # interactive only

# Parquet (requires pyarrow or fastparquet)
# df.to_parquet("data.parquet")
# df_parquet = pd.read_parquet("data.parquet")

# Feather (fast binary format)
# df.to_feather("data.feather")
# df_feather = pd.read_feather("data.feather")

# Pickle
pkl_path = os.path.join(EXAMPLE_DIR, "data.pkl")
df.to_pickle(pkl_path)
df_pkl = pd.read_pickle(pkl_path)
print(f"Read from pickle:\n{df_pkl.head()}")

print("=" * 5, "Apply, map, and vectorized operations", "=" * 5)

df = pd.DataFrame({
    "name": ["alice", "bob", "charlie", "diana", "eve"],
    "score": [85, 92, 78, 95, 88],
    "attendance": [90, 85, 70, 95, 80],
})

# apply on Series
print(f"Name capitalized: {df['name'].apply(str.title).tolist()}")

# apply on DataFrame (row-wise)
df["grade"] = df["score"].apply(lambda x: "A" if x >= 90 else "B" if x >= 80 else "C")
print(f"\nWith grade:\n{df}")

# apply on DataFrame (column-wise)
print(f"\nColumn means:\n{df[['score', 'attendance']].apply(np.mean)}")

# applymap / map (element-wise)
df_upper = df[["name"]].apply(lambda x: x.str.upper())
print(f"\nUppercase names:\n{df_upper}")

# map: Series value substitution
grade_map = {"A": "Excellent", "B": "Good", "C": "Average"}
df["grade_label"] = df["grade"].map(grade_map)
print(f"\nMapped grades:\n{df}")

# replace
df_replaced = df.replace({"grade_label": {"Good": "Great"}})
print(f"\nReplaced:\n{df_replaced}")

# Vectorized operations (much faster than apply)
df["weighted"] = df["score"] * 0.7 + df["attendance"] * 0.3
print(f"\nWeighted score (vectorized):\n{df}")

# pd.cut: binning continuous values
df["score_bin"] = pd.cut(df["score"], bins=[0, 80, 90, 100], labels=["C", "B", "A"])
print(f"\nBinned scores:\n{df}")

# pd.qcut: quantile-based binning
df["score_quartile"] = pd.qcut(df["score"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])
print(f"\nQuartile scores:\n{df}")

print("=" * 5, "Duplicates and value counts", "=" * 5)

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"],
    "city": ["Seoul", "Tokyo", "Seoul", "London", "Tokyo", "Busan"],
    "score": [85, 92, 85, 78, 92, 88],
})

# Detect duplicates
print(f"Duplicated rows:\n{df.duplicated()}")
print(f"\nDuplicated (subset):\n{df.duplicated(subset=['name'])}")
print(f"Number of duplicate rows: {df.duplicated().sum()}")

# Drop duplicates
print(f"\nDrop duplicates (all columns):\n{df.drop_duplicates()}")
print(f"\nDrop duplicates (subset):\n{df.drop_duplicates(subset=['name'])}")
print(f"\nDrop duplicates (keep last):\n{df.drop_duplicates(subset=['name'], keep='last')}")

# Value counts
print(f"\nValue counts (name):\n{df['name'].value_counts()}")
print(f"\nValue counts (city, normalize):\n{df['city'].value_counts(normalize=True)}")

# Crosstab
ct = pd.crosstab(df["name"], df["city"])
print(f"\nCrosstab:\n{ct}")

print("=" * 5, "Practical data cleaning patterns", "=" * 5)

# Real-world messy data
messy = pd.DataFrame({
    "Name": ["  Alice  ", "BOB", "  charlie", "Diana  ", None],
    "Age": ["25", "thirty", "35", "28", "unknown"],
    "Email": ["alice@example.com", "BOB@TEST.ORG", "charlie@mail.com", "diana@work.net", ""],
    "Score": ["85.5", "92", "78.5", "N/A", "88"],
})

print(f"Messy data:\n{messy}")
print(f"Dtypes:\n{messy.dtypes}")

# Convert columns with errors='coerce'
messy["Score_clean"] = pd.to_numeric(messy["Score"], errors="coerce")
print(f"\nScore after to_numeric(coerce):\n{messy['Score_clean']}")

messy["Age_clean"] = pd.to_numeric(messy["Age"], errors="coerce")
print(f"Age after to_numeric(coerce):\n{messy['Age_clean']}")

# Clean strings
messy["Name_clean"] = messy["Name"].str.strip().str.title()
print(f"\nName after strip+title:\n{messy['Name_clean']}")

# Clean email (lowercase)
messy["Email_clean"] = messy["Email"].str.strip().str.lower()
print(f"Email after strip+lower:\n{messy['Email_clean']}")

# Fill missing numeric values
messy["Score_clean"] = messy["Score_clean"].fillna(messy["Score_clean"].mean())
messy["Age_clean"] = messy["Age_clean"].fillna(messy["Age_clean"].median())
print(f"\nAfter filling NaN:\n{messy[['Name_clean', 'Age_clean', 'Score_clean']]}")

# Final cleaned DataFrame
clean = messy[["Name_clean", "Age_clean", "Email_clean", "Score_clean"]].copy()
clean.columns = ["name", "age", "email", "score"]
print(f"\nFinal cleaned data:\n{clean}")
print(f"\nClean dtypes:\n{clean.dtypes}")

print("=" * 5, "Performance tips", "=" * 5)

# Large DataFrame example
rng = np.random.default_rng(42)
large_df = pd.DataFrame({
    "category": rng.choice(["A", "B", "C", "D"], size=100000),
    "value": rng.standard_normal(100000),
    "group": rng.choice(["X", "Y"], size=100000),
})

# Use categorical dtype for string columns with few unique values
large_df["category_cat"] = large_df["category"].astype("category")
print(f"Object dtype memory: {large_df['category'].memory_usage(deep=True)} bytes")
print(f"Category dtype memory: {large_df['category_cat'].memory_usage(deep=True)} bytes")

# Use .values or .to_numpy() for faster iteration
values = large_df["value"].to_numpy()
print(f"\nNumPy array type: {type(values)}, shape: {values.shape}")

# Use query() for filtering large DataFrames (can be faster than boolean indexing)
result = large_df.query("value > 2 and category == 'A'")
print(f"Query result shape: {result.shape}")

# Prefer vectorized operations over apply
large_df["double_value"] = large_df["value"] * 2  # vectorized (fast)
print(f"Vectorized operation done, new column mean: {large_df['double_value'].mean():.4f}")

# Clean up example files
import shutil
shutil.rmtree(EXAMPLE_DIR, ignore_errors=True)
print(f"\nCleaned up example directory: {EXAMPLE_DIR}")