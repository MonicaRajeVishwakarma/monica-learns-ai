# Day 12 - Data Visualization using Matplotlib and Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../../data/habits.csv")

# Clean sleep column (if needed)
if 'sleep' in df.columns:
    df['sleep_hours'] = df['sleep'].astype(str).str.extract(r'(\d+\.?\d*)').astype(float)

# ===========================
# 1. Line plot - sleep trend
# ==========================
plt.figure(figsize=(10, 4))
plt.plot(df['date'], df['sleep_hours'])
plt.title("Sleep Hours Over Time")
plt.xlabel("Date")
plt.ylabel("Sleep (hours)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ===========================
# 2. Histogram - Feeding
# ==========================
if 'feeding' in df.columns:
    plt.figure(figsize=(8, 4))
    plt.hist(df['feeding'], bins=20)
    plt.title("Distribution of feeding quantity in ml")
    plt.xlabel("Feeding quantity (ml)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# ===========================
# 3. Scatter Plot - Sleep vs Mood (encoded)
# ==========================
if 'mood' in df.columns:
    df['mood_encoded'] = df['mood'].astype('category').cat.codes

    plt.figure(figsize=(8, 4))
    plt.scatter(df['sleep_hours'], df['mood_encoded'])
    plt.title("Sleep Vs Mood")
    plt.xlabel("Sleep hours")
    plt.ylabel("Mood (encoded)")
    plt.tight_layout()
    plt.show()

# ===========================
# 4. Boxplot - Numerical columns
# ==========================
plt.figure(figsize=(8, 4))
sns.boxplot(data=df.select_dtypes(include='number'))
plt.title("Box plot of numerical features")
plt.tight_layout()
plt.show()

# ===========================
# 5. Correlation Heatmap
# ==========================
plt.figure(figsize=(8, 4))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correaltion Heatmap")
plt.tight_layout()
plt.show()

# ===========================
# 6. Pairplot Seaborn
# ==========================
sns.pairplot(df.select_dtypes(include='number'))
plt.show()