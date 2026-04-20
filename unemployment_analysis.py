# ================================
# STEP 1: Import Libraries
# ================================
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# ================================
# STEP 2: Set Working Directory
# ================================
os.chdir(r"C:\Users\sethu\Documents\CA&DS")

# ================================
# STEP 3: Load Dataset
# ================================
df = pd.read_csv("Unemployment in India.csv")

# ================================
# STEP 4: Data Understanding
# ================================
print("First 5 Rows:\n", df.head())
print("\nDataset Info:\n")
print(df.info())

# ================================
# STEP 5: Data Cleaning
# ================================
# Remove extra spaces in column names
df.columns = df.columns.str.strip()

# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Drop missing values
df = df.dropna()

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# ================================
# STEP 6: Statistical Summary
# ================================
print("\nStatistical Summary:\n", df.describe())

# ================================
# STEP 7: Overall Unemployment Trend
# ================================
plt.figure(figsize=(12,6))
plt.plot(df['Date'], df['Estimated Unemployment Rate (%)'])
plt.title("Overall Unemployment Trend")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ================================
# STEP 8: Covid-19 Impact Analysis
# ================================
pre_covid = df[df['Date'] < '2020-03-01']
covid = df[df['Date'] >= '2020-03-01']

print("\nPre-Covid Average Unemployment:",
      pre_covid['Estimated Unemployment Rate (%)'].mean())

print("Covid Period Average Unemployment:",
      covid['Estimated Unemployment Rate (%)'].mean())

# Plot comparison
plt.figure(figsize=(12,6))

plt.plot(pre_covid['Date'],
         pre_covid['Estimated Unemployment Rate (%)'],
         label='Pre-Covid')

plt.plot(covid['Date'],
         covid['Estimated Unemployment Rate (%)'],
         label='Covid Period')

plt.title("Impact of Covid-19 on Unemployment")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ================================
# STEP 9: Monthly Trend Analysis
# ================================
df['Month'] = df['Date'].dt.month

monthly_trend = df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()

plt.figure()
monthly_trend.plot(kind='bar')
plt.title("Monthly Average Unemployment Rate")
plt.xlabel("Month")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# ================================
# STEP 10: Yearly Trend Analysis
# ================================
df['Year'] = df['Date'].dt.year

yearly_trend = df.groupby('Year')['Estimated Unemployment Rate (%)'].mean()

plt.figure()
yearly_trend.plot(kind='line', marker='o')
plt.title("Yearly Average Unemployment Rate")
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# ================================
# STEP 11: Region-wise Analysis
# ================================
region_trend = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

print("\nTop 10 Regions with Highest Unemployment:\n")
print(region_trend.sort_values(ascending=False).head(10))

plt.figure()
region_trend.sort_values(ascending=False).head(10).plot(kind='bar')
plt.title("Top 10 Regions by Unemployment Rate")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# ================================
# STEP 12: Urban vs Rural Analysis
# ================================
area_trend = df.groupby('Area')['Estimated Unemployment Rate (%)'].mean()

print("\nUrban vs Rural:\n", area_trend)

plt.figure()
area_trend.plot(kind='bar')
plt.title("Urban vs Rural Unemployment")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# ================================
# STEP 13: Key Insights
# ================================
print("\n--- KEY INSIGHTS ---")
print("1. Unemployment increased significantly during Covid-19.")
print("2. Highest spike observed around April-May 2020.")
print("3. Pre-Covid unemployment was relatively stable.")
print("4. Some regions are more affected than others.")
print("5. Urban and rural areas both show impact.")