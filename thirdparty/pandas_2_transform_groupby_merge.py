# pandas: data transformation, grouping, merging, and time series

import pandas as pd
import numpy as np

print("=" * 5, "Sorting", "=" * 5)

df = pd.DataFrame({
    "name": ["Charlie", "Alice", "Bob", "Diana", "Eve"],
    "age": [35, 25, 30, 28, 25],
    "score": [78, 85, 92, 95, 88],
})

# Sort by column
print(f"Sort by age:\n{df.sort_values('age')}")
print(f"\nSort by age (descending):\n{df.sort_values('age', ascending=False)}")

# Sort by multiple columns
print(f"\nSort by age then score:\n{df.sort_values(['age', 'score'])}")

# Sort by index
df_indexed = df.set_index("name")
print(f"\nSort by index:\n{df_indexed.sort_index()}")

# nlargest / nsmallest
print(f"\nTop 3 scores:\n{df.nlargest(3, 'score')}")
print(f"\nBottom 2 ages:\n{df.nsmallest(2, 'age')}")

print("=" * 5, "GroupBy: split-apply-combine", "=" * 5)

df = pd.DataFrame({
    "department": ["Engineering", "Engineering", "Marketing", "Marketing", "Engineering", "Marketing"],
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
    "salary": [90000, 85000, 75000, 80000, 95000, 70000],
    "experience": [5, 3, 4, 2, 7, 1],
})

# Group by single column
grouped = df.groupby("department")
print(f"Grouped object: {type(grouped)}")
print(f"Groups: {grouped.groups}")

# Aggregation
print(f"\nMean salary by department:\n{df.groupby('department')['salary'].mean()}")
print(f"\nMultiple aggregations:\n{df.groupby('department')['salary'].agg(['mean', 'median', 'min', 'max', 'count'])}")

# Named aggregations
result = df.groupby("department").agg(
    avg_salary=("salary", "mean"),
    total_salary=("salary", "sum"),
    avg_exp=("experience", "mean"),
    count=("name", "count"),
)
print(f"\nNamed aggregations:\n{result}")

# Group by multiple columns
df_multi = pd.DataFrame({
    "dept": ["Eng", "Eng", "Eng", "Mkt", "Mkt", "Mkt"],
    "level": ["Senior", "Junior", "Senior", "Senior", "Junior", "Junior"],
    "salary": [120, 80, 110, 100, 70, 75],
})
print(f"\nGroup by multiple columns:\n{df_multi.groupby(['dept', 'level'])['salary'].mean()}")

# Transform: broadcast group result back to original shape
df["dept_avg"] = df.groupby("department")["salary"].transform("mean")
print(f"\nTransform (dept_avg):\n{df}")

# Filter: keep groups that meet condition
large_depts = df.groupby("department").filter(lambda x: len(x) >= 3)
print(f"\nDepartments with 3+ members:\n{large_depts}")

# Apply custom function
def salary_range(group):
    return group["salary"].max() - group["salary"].min()

print(f"\nSalary range by dept:\n{df.groupby('department').apply(salary_range)}")

print("=" * 5, "Merging, joining, and concatenating", "=" * 5)

employees = pd.DataFrame({
    "emp_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "dept_id": [101, 102, 101, 103],
})

departments = pd.DataFrame({
    "dept_id": [101, 102, 104],
    "dept_name": ["Engineering", "Marketing", "HR"],
})

# Inner join (default)
inner = pd.merge(employees, departments, on="dept_id", how="inner")
print(f"Inner join:\n{inner}")

# Left join
left = pd.merge(employees, departments, on="dept_id", how="left")
print(f"\nLeft join:\n{left}")

# Right join
right = pd.merge(employees, departments, on="dept_id", how="right")
print(f"\nRight join:\n{right}")

# Outer join
outer = pd.merge(employees, departments, on="dept_id", how="outer")
print(f"\nOuter join:\n{outer}")

# Join on different column names
salaries = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "salary": [90000, 85000, 78000, 95000],
})
different_cols = pd.merge(employees, salaries, left_on="emp_id", right_on="id", how="inner")
print(f"\nJoin on different columns:\n{different_cols}")

# Concatenate vertically
df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df2 = pd.DataFrame({"A": [5, 6], "B": [7, 8]})
vertical = pd.concat([df1, df2], ignore_index=True)
print(f"\nVertical concat:\n{vertical}")

# Concatenate horizontally
df3 = pd.DataFrame({"C": [10, 20], "D": [30, 40]})
horizontal = pd.concat([df1, df3], axis=1)
print(f"\nHorizontal concat:\n{horizontal}")

# Concatenate with keys
with_keys = pd.concat([df1, df2], keys=["first", "second"])
print(f"\nConcat with keys:\n{with_keys}")

print("=" * 5, "Pivot tables and reshaping", "=" * 5)

sales = pd.DataFrame({
    "region": ["East", "East", "West", "West", "East", "West"],
    "product": ["A", "B", "A", "B", "A", "B"],
    "quarter": ["Q1", "Q1", "Q1", "Q1", "Q2", "Q2"],
    "sales": [100, 150, 120, 180, 110, 190],
})

# Pivot table
pivot = sales.pivot_table(values="sales", index="region", columns="product", aggfunc="sum")
print(f"Pivot table:\n{pivot}")

# Multiple aggregations
pivot_multi = sales.pivot_table(
    values="sales", index="region", columns="quarter", aggfunc=["sum", "mean"]
)
print(f"\nMultiple agg:\n{pivot_multi}")

# Melt: wide to long
wide = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "math": [90, 85],
    "english": [88, 92],
    "science": [95, 80],
})
long = wide.melt(id_vars=["name"], var_name="subject", value_name="score")
print(f"\nMelt (wide to long):\n{long}")

# Pivot: long to wide
back_to_wide = long.pivot(index="name", columns="subject", values="score")
print(f"\nPivot (long to wide):\n{back_to_wide}")

# Stack and unstack
multi = pd.DataFrame({
    "Q1": [100, 200, 150, 250],
    "Q2": [110, 210, 160, 260],
}, index=pd.MultiIndex.from_tuples([("East", "A"), ("East", "B"), ("West", "A"), ("West", "B")],
                                     names=["region", "product"]))
print(f"\nMulti-index DataFrame:\n{multi}")
print(f"\nUnstack:\n{multi.unstack()}")
print(f"\nStack:\n{multi.unstack().stack()}")

print("=" * 5, "Time series", "=" * 5)

# Create date range
dates = pd.date_range("2025-01-01", periods=10, freq="D")
print(f"Date range (daily):\n{dates}")

# Different frequencies
print(f"\nMonthly: {pd.date_range('2025-01-01', periods=6, freq='ME')}")
print(f"Hourly: {pd.date_range('2025-01-01', periods=6, freq='h')}")
print(f"Business days: {pd.date_range('2025-01-01', periods=6, freq='B')}")

# Time series DataFrame
ts = pd.DataFrame({
    "date": pd.date_range("2025-01-01", periods=30, freq="D"),
    "value": np.random.default_rng(42).standard_normal(30).cumsum() + 100,
})
ts = ts.set_index("date")
print(f"\nTime series:\n{ts.head()}")

# Resample: change frequency
weekly = ts.resample("W").mean()
print(f"\nWeekly resample:\n{weekly.head()}")

monthly = ts.resample("ME").agg({"value": ["mean", "sum", "std"]})
print(f"\nMonthly resample with multiple aggs:\n{monthly.head()}")

# Rolling window
rolling_mean = ts["value"].rolling(window=7).mean()
print(f"\n7-day rolling mean:\n{rolling_mean.head(10)}")

# Shift
ts["value_prev"] = ts["value"].shift(1)
ts["value_next"] = ts["value"].shift(-1)
ts["daily_change"] = ts["value"] - ts["value_prev"]
print(f"\nWith shift:\n{ts.head()}")

# Date components
ts["year"] = ts.index.year
ts["month"] = ts.index.month
ts["day"] = ts.index.day
ts["weekday"] = ts.index.day_name()
print(f"\nDate components:\n{ts[['value', 'year', 'month', 'weekday']].head()}")

# Time delta
td = pd.Timestamp("2025-07-31") - pd.Timestamp("2025-01-01")
print(f"\nTime delta: {td}")  # 181 days
print(f"Days: {td.days}")