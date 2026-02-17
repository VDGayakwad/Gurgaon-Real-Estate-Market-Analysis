"""
Gurgaon Real Estate Data Analysis
Author: Vaishnavi Gayakwad

This project analyzes residential property listings in Gurgaon
to generate insights for buyers, investors, and developers.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load Dataset
df = pd.read_csv("data.csv")


# Data Cleaning

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Convert numerical columns
df["price"] = df["price"].astype(str).str.replace(",", "").astype(float)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)

# Clean categorical columns
df["status"] = df["status"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower()
df["flat_type"] = df["flat_type"].str.strip().str.lower()

# Remove duplicates
df = df.drop_duplicates()


# Exploratory Data Analysis

# 1. Costliest Property
costliest_property = df.loc[df["price"].idxmax()]
print(
    f"The most expensive property is a {costliest_property['flat_type']} "
    f"in {costliest_property['locality']} priced at "
    f"{costliest_property['price'] / 1e7:.2f} crore "
    f"with an area of {costliest_property['area']} sqft."
)

# 2. Locality with Highest Average Price
highest_avg_price_locality = df.groupby("locality")["price"].mean().idxmax()
print(f"Locality with highest average price: {highest_avg_price_locality}")

# 3. Locality with Highest Rate per Sqft
highest_rate_locality = df.groupby("locality")["rate_per_sqft"].mean().idxmax()
print(f"Locality with highest rate per sqft: {highest_rate_locality}")

# 4. Ready-to-move vs Under-construction
ready_avg = df[df["status"] == "ready to move"]["price"].mean()
under_avg = df[df["status"] == "under construction"]["price"].mean()

if ready_avg > under_avg:
    print("Ready-to-move properties cost more on average.")
else:
    print("Under-construction properties cost more on average.")

# 5. RERA Premium Analysis
rera_avg = df[df["rera_approval"] == "approved by rera"]["price"].mean()
non_rera_avg = df[df["rera_approval"] == "not approved by rera"]["price"].mean()

if rera_avg > non_rera_avg:
    print("RERA-approved properties command a price premium.")
else:
    print("RERA-approved properties do not command a price premium.")

# 6. Area vs Price Visualization
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="area", y="price")
plt.title("Area vs Price")
plt.xlabel("Area (sqft)")
plt.ylabel("Price (INR)")
plt.show()

# 7. Most Expensive BHK by Average Price
expensive_bhk = df.groupby("bhk_count")["price"].mean().idxmax()
print(f"Most expensive BHK configuration by price: {expensive_bhk}")

# 8. Most Expensive BHK by Rate per Sqft
expensive_bhk_rate = df.groupby("bhk_count")["rate_per_sqft"].mean().idxmax()
print(f"Most expensive BHK by rate per sqft: {expensive_bhk_rate}")

# 9. Costliest Property Type
costliest_property_type = df.groupby("flat_type")["rate_per_sqft"].mean().idxmax()
print(f"Costliest property type: {costliest_property_type}")

# 10. Top 5 Premium Builders
top_builders = (
    df.groupby("company_name")["rate_per_sqft"]
    .mean()
    .sort_values(ascending=False)
    .head(5)
)

print("Top 5 Premium Builders:")
for builder in top_builders.index:
    print(builder)

# 11. Area vs Rate per Sqft
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="area", y="rate_per_sqft")
plt.title("Area vs Rate per Sqft")
plt.xlabel("Area (sqft)")
plt.ylabel("Rate per Sqft")
plt.show()
