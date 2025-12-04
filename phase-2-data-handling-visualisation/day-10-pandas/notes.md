# Day 10 Notes – Pandas Basics
import pandas as pd

# Load CSV
```python
df = pd.read_csv("data/habits.csv")
```

# Inspect data
```python
print(df.head())   # first 5 rows
print(df.info())   # columns and types
print(df.describe())  # numeric summary
print(df.columns)
```

# Selecting data
```python
print(df['feeding'])        # single column
print(df[['date','sleep']]) # multiple columns
```

# Filtering
```python
print(df[df['feeding']=='yes'])
```

# Sorting
```python
print(df.sort_values('date'))
```