# Day 10 - Pandas

import pandas as pd

#1. Load CSV
df = pd.read_csv("local_habits.csv")

#2. Preview first 5 rows
print("First 5 rows:\n",df.head())

#3. Inspect data
print("\nInspect Data\n")
print("Info",df.info()) # columns and types
print("Describe",df.describe()) #numeric summary
print("Columns",df.columns)



#4. Filter row where mood is great
print("\nFilter Data\n")
great_df = df[df['mood'] == "great"]
print("\nGreat days",great_df)

#5. Select columns
print("\nSelect Data\n")
print(df['mood'])  # single columns
print(df[['date','sleep']]) # multiple columns

#6. Sorting
print("\nSelect Data\n")
print("Sorting by date",df.sort_values('date'))



