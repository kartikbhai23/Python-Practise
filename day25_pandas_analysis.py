# Day 25: Pandas GroupBy
# grouping, handling missing null data values in pandas dataframes

import pandas as pd
import numpy as np

# database of sales data
sales_data = {
    "Store": ["East", "West", "East", "North", "West", "East", "North"],
    "Product": ["Apples", "Bananas", "Apples", "Apples", "Bananas", "Oranges", "Oranges"],
    "Sales": [120, 80, np.nan, 150, 95, 200, 110],
    "Quantity": [10, 8, 12, 15, np.nan, 20, 11]
}
df = pd.DataFrame(sales_data)
print("Sales database:\n", df)

# filling empty values with statistics
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
df["Quantity"] = df["Quantity"].fillna(0)
print("\nFilled empty cells:\n", df)

# group sales by store sum
store_sales = df.groupby("Store")["Sales"].sum().reset_index()
print("\nStore Summed Sales:\n", store_sales)

# multiple aggregates grouped by product
product_stats = df.groupby("Product").agg({"Sales": "mean", "Quantity": "sum"})
print("\nProduct aggregations:\n", product_stats)

# exercise 1: simple filter oranges
oranges = df[df["Product"] == "Oranges"]
print("\nOranges list:\n", oranges)

# challenge: sort values and reset index index
sorted_df = df.sort_values(by="Sales", ascending=False).reset_index(drop=True)
print("\nSorted by Sales:\n", sorted_df)

# sorted results by store total sales
