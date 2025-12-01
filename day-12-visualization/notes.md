# Day 12 - Data visualization

Topics:
1. Count plots for categorical data (feeding, mood)
2. Line plots for trends over time (sleep_hours)
3. Bar plots, histograms, and distributions
4. Seaborn styling and customization

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

# Count plot
```python
sns.countplot(data=df, x='feeding')
plt.title("Feeding Patterns")
plt.show()
```

# Line plot for sleep
```python
df['sleep_hours'] = df['sleep'].str.replace('h','').astype(float)
df_sorted = df.sort_values('date')
plt.plot(df_sorted['date'], df_sorted['sleep_hours'])
plt.title("Sleep Hours Over Time")
plt.xlabel("Date")
plt.ylabel("Sleep Hours")
plt.show()
```

