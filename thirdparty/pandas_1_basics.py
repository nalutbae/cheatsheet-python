# pandas: Series and DataFrame creation, data types, and basic inspection

import pandas as pd
import numpy as np

print("=" * 5, "Series: one-dimensional labeled array", "=" * 5)

# Create Series from list
s1 = pd.Series([10, 20, 30, 40, 50])
print(f"Series from list:\n{s1}")
print(f"Index: {s1.index.tolist()}")  # [0, 1, 2, 3, 4]
print(f"Values: {s1.values}")  # [10 20 30 40 50]
print(f"Dtype: {s1.dtype}")  # int64

# Create Series with custom index
s2 = pd.Series([85, 92, 78, 95], index=["Alice", "Bob", "Charlie", "Diana"])
print(f"\nSeries with custom index:\n{s2}")
print(f"Access by label: s2['Alice'] = {s2['Alice']}")  # 85
print(f"Access by position: s2[0] = {s2.iloc[0]}")  # 85

# Create Series from dict
scores = {"math": 90, "english": 85, "science": 92, "history": 78}
s3 = pd.Series(scores)
print(f"\nSeries from dict:\n{s3}")
print(f"Access by label: s3['math'] = {s3['math']}")  # 90

# Series with name
s4 = pd.Series([25, 30, 35], name="age")
print(f"\nSeries with name: {s4.name}")  # age

# Series dtypes
s_int = pd.Series([1, 2, 3])
s_float = pd.Series([1.5, 2.5, 3.5])
s_str = pd.Series(["a", "b", "c"])
s_bool = pd.Series([True, False, True])
s_datetime = pd.Series(pd.to_datetime(["2025-01-01", "2025-07-31"]))
print(f"\nInt dtype: {s_int.dtype}")  # int64
print(f"Float dtype: {s_float.dtype}")  # float64
print(f"String dtype: {s_str.dtype}")  # object or string
print(f"Bool dtype: {s_bool.dtype}")  # bool
print(f"Datetime dtype: {s_datetime.dtype}")  # datetime64[ns]

# Convert dtype
s = pd.Series(["1", "2", "3"])
print(f"\nString series: {s.dtype}")  # object
s_converted = s.astype(int)
print(f"Converted to int: {s_converted.dtype}")  # int64
print(f"Values: {s_converted.tolist()}")  # [1, 2, 3]

# Series with NaN
s_nan = pd.Series([1, 2, None, 4, np.nan])
print(f"\nSeries with NaN:\n{s_nan}")
print(f"isna():\n{s_nan.isna()}")
print(f"notna():\n{s_nan.notna()}")
print(f"Count non-null: {s_nan.count()}")  # 3

print("=" * 5, "DataFrame: two-dimensional labeled data", "=" * 5)

# Create DataFrame from dict of lists
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [25, 30, 35, 28],
    "city": ["Seoul", "Tokyo", "London", "Paris"],
    "score": [85.5, 92.0, 78.5, 95.0],
}
df = pd.DataFrame(data)
print(f"DataFrame from dict:\n{df}")
print(f"\nShape: {df.shape}")  # (4, 4)
print(f"Columns: {df.columns.tolist()}")  # ['name', 'age', 'city', 'score']
print(f"Index: {df.index.tolist()}")  # [0, 1, 2, 3]
print(f"Dtypes:\n{df.dtypes}")

# Create DataFrame from list of dicts
rows = [
    {"name": "Alice", "age": 25, "city": "Seoul"},
    {"name": "Bob", "age": 30, "city": "Tokyo"},
    {"name": "Charlie", "age": 35, "city": "London"},
]
df2 = pd.DataFrame(rows)
print(f"\nDataFrame from list of dicts:\n{df2}")

# Create DataFrame from list of lists
data_list = [
    ["Alice", 25, "Seoul"],
    ["Bob", 30, "Tokyo"],
    ["Charlie", 35, "London"],
]
df3 = pd.DataFrame(data_list, columns=["name", "age", "city"])
print(f"\nDataFrame from list of lists:\n{df3}")

# Create DataFrame from numpy array
arr = np.random.default_rng(42).standard_normal((3, 4))
df4 = pd.DataFrame(arr, columns=["A", "B", "C", "D"], index=["x", "y", "z"])
print(f"\nDataFrame from numpy array:\n{df4}")
print(f"Values type: {type(df4.values)}")  # <class 'numpy.ndarray'>

# Create DataFrame with custom index
df_custom = pd.DataFrame(
    {"score": [85, 92, 78, 95]},
    index=["Alice", "Bob", "Charlie", "Diana"],
)
print(f"\nDataFrame with custom index:\n{df_custom}")

print("=" * 5, "DataFrame inspection methods", "=" * 5)

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age": [25, 30, 35, 28, None],
    "city": ["Seoul", "Tokyo", "London", "Paris", "Berlin"],
    "score": [85.5, 92.0, 78.5, 95.0, 88.0],
    "passed": [True, True, False, True, True],
})

# head / tail
print(f"head(3):\n{df.head(3)}")
print(f"\ntail(2):\n{df.tail(2)}")

# info: concise summary
print(f"\n--- df.info() ---")
df.info()

# describe: statistical summary
print(f"\n--- df.describe() ---\n{df.describe()}")

# Shape and size
print(f"\nShape: {df.shape}")  # (5, 5)
print(f"Size: {df.size}")  # 25
print(f"ndim: {df.ndim}")  # 2

# Column dtypes
print(f"\nDtypes:\n{df.dtypes}")

# Non-null counts
print(f"\nCount:\n{df.count()}")

# Unique values
print(f"\nnunique (name): {df['name'].nunique()}")  # 5
print(f"nunique (city): {df['city'].nunique()}")  # 5
print(f"unique (passed): {df['passed'].unique()}")  # [True, False]

# Memory usage
print(f"\nMemory usage:\n{df.memory_usage()}")

print("=" * 5, "Selecting columns and rows", "=" * 5)

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [25, 30, 35, 28],
    "score": [85, 92, 78, 95],
})

# Select single column (Series)
print(f"Single column (Series):\n{df['name']}")
print(f"Type: {type(df['name'])}")  # <class 'pandas.Series'>

# Select multiple columns (DataFrame)
print(f"\nMultiple columns:\n{df[['name', 'score']]}")
print(f"Type: {type(df[['name', 'score']])}")  # <class 'pandas.DataFrame'>

# Select by label: .loc[row_label, col_label]
print(f"\nloc[0]:\n{df.loc[0]}")  # first row as Series
print(f"\nloc[0:2]:\n{df.loc[0:2]}")  # rows 0-2 (inclusive)
print(f"\nloc[:, 'name']:\n{df.loc[:, 'name']}")  # all rows, 'name' column
print(f"\nloc[0:2, ['name', 'age']]:\n{df.loc[0:2, ['name', 'age']]}")

# Select by position: .iloc[row_pos, col_pos]
print(f"\niloc[0]:\n{df.iloc[0]}")  # first row
print(f"\niloc[0:2]:\n{df.iloc[0:2]}")  # rows 0-1 (exclusive end)
print(f"\niloc[:, 0]:\n{df.iloc[:, 0]}")  # all rows, first column
print(f"\niloc[1:3, 0:2]:\n{df.iloc[1:3, 0:2]}")  # rows 1-2, cols 0-1

# Boolean indexing
print(f"\nAge > 28:\n{df[df['age'] > 28]}")
print(f"\nScore >= 90:\n{df[df['score'] >= 90]}")
print(f"\nMultiple conditions:\n{df[(df['age'] > 25) & (df['score'] >= 85)]}")

# Query method
print(f"\nQuery age > 28:\n{df.query('age > 28')}")
print(f"\nQuery score >= 90:\n{df.query('score >= 90')}")

print("=" * 5, "Adding and modifying data", "=" * 5)

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
})

# Add a new column
df["city"] = ["Seoul", "Tokyo", "London"]
print(f"Add column:\n{df}")

# Add column from calculation
df["age_months"] = df["age"] * 12
print(f"\nCalculated column:\n{df}")

# Add column with condition
df["age_group"] = df["age"].apply(lambda x: "young" if x < 30 else "senior")
print(f"\nConditional column:\n{df}")

# Modify existing column
df["age"] = df["age"] + 1
print(f"\nAge + 1:\n{df}")

# Add a new row
new_row = pd.DataFrame({"name": ["Diana"], "age": [29], "city": ["Paris"], "age_months": [348], "age_group": ["young"]})
df = pd.concat([df, new_row], ignore_index=True)
print(f"\nAfter adding row:\n{df}")

# Drop column
df_no_months = df.drop(columns=["age_months"])
print(f"\nDrop column:\n{df_no_months}")

# Drop row
df_no_row = df.drop(index=0)
print(f"\nDrop row 0:\n{df_no_row}")

# Rename columns
df_renamed = df.rename(columns={"name": "full_name", "age": "years"})
print(f"\nRenamed columns:\n{df_renamed.columns.tolist()}")

# Replace values
df_copy = df.copy()
df_copy["city"] = df_copy["city"].replace({"Seoul": "서울", "Tokyo": "도쿄"})
print(f"\nReplaced values:\n{df_copy}")

print("=" * 5, "Handling missing data", "=" * 5)

df_missing = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age": [25, 30, None, 28, None],
    "score": [85, None, 78, 95, 88],
    "city": ["Seoul", None, "London", "Paris", None],
})
print(f"DataFrame with missing data:\n{df_missing}")

# Detect missing values
print(f"\nisna():\n{df_missing.isna()}")
print(f"\nisna().sum():\n{df_missing.isna().sum()}")
print(f"\nTotal missing: {df_missing.isna().sum().sum()}")  # 4

# Drop missing values
print(f"\ndropna() (any row with NaN):\n{df_missing.dropna()}")
print(f"\ndropna(subset=['age']):\n{df_missing.dropna(subset=['age'])}")
print(f"\ndropna(axis=1) (columns with NaN):\n{df_missing.dropna(axis=1)}")

# Fill missing values
print(f"\nfillna(0):\n{df_missing.fillna(0)}")
print(f"\nfillna with dict:\n{df_missing.fillna({'age': df_missing['age'].mean(), 'score': 0, 'city': 'Unknown'})}")

# Forward and backward fill
df_time = pd.DataFrame({
    "date": pd.date_range("2025-01-01", periods=5),
    "value": [10, None, None, 40, 50],
})
print(f"\nTime series with gaps:\n{df_time}")
print(f"\nffill():\n{df_time.ffill()}")
print(f"\nbfill():\n{df_time.bfill()}")

# Interpolate
print(f"\ninterpolate():\n{df_time.interpolate()}")

print("=" * 5, "String operations", "=" * 5)

df_str = pd.DataFrame({
    "name": ["  alice  ", "BOB", "Charlie", "diana  "],
    "email": ["alice@example.com", "bob@test.org", "CHARLIE@Mail.COM", "diana@work.net"],
})

# String methods via .str accessor
print(f"lower: {df_str['name'].str.lower().tolist()}")
print(f"upper: {df_str['name'].str.upper().tolist()}")
print(f"title: {df_str['name'].str.title().tolist()}")
print(f"strip: {df_str['name'].str.strip().tolist()}")
print(f"lstrip: {df_str['name'].str.lstrip().tolist()}")
print(f"rstrip: {df_str['name'].str.rstrip().tolist()}")

# String contains and match
print(f"\ncontains('a'): {df_str['name'].str.contains('a', case=False).tolist()}")
print(f"startswith(' '): {df_str['name'].str.startswith(' ').tolist()}")
print(f"endswith(' '): {df_str['name'].str.endswith(' ').tolist()}")

# String replacement
print(f"replace spaces: {df_str['name'].str.strip().str.replace('a', '@').tolist()}")

# String split
print(f"split('@'): {df_str['email'].str.split('@').tolist()}")
print(f"split expand:\n{df_str['email'].str.split('@', expand=True)}")

# String length
print(f"\nlen: {df_str['name'].str.len().tolist()}")

# Extract with regex
df_emails = df_str["email"].str.extract(r"(\w+)@(\w+)\.(\w+)")
df_emails.columns = ["user", "domain", "tld"]
print(f"\nRegex extract:\n{df_emails}")