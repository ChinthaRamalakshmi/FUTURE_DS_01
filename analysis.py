import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

print("Dataset Loaded Successfully")

print(df.head())

print("Total Sales")
print(df["Sales"].sum())

print("\nRegion Wise Sales:")
print(df.groupby("Region")["Sales"].sum())
print("\nTop 10 Products:")

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)

print(top_products.head(10))
print("\nCategory Wise Sales:")

print(df.groupby("Category")["Sales"].sum())

region_sales = df.groupby("Region")["Sales"].sum()

colors = ["red", "blue", "green", "orange"]

region_sales.plot(
    kind="bar",
    color=colors,
    figsize=(8,5)
)

plt.title("Region Wise Sales Analysis")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.grid(axis="y", linestyle="--")
plt.show()

category_sales = df.groupby("Category")["Sales"].sum()

colors = ["gold", "lightgreen", "skyblue"]

plt.figure(figsize=(7,7))
plt.pie(
    category_sales,
    labels=category_sales.index,
    autopct="%1.1f%%",
    colors=colors
)

plt.title("Category Wise Sales Distribution")
plt.show()

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))

colors = [
    "red", "blue", "green", "orange", "purple",
    "pink", "cyan", "gold", "brown", "magenta"
]

top_products.plot(
    kind="barh",
    color=colors
)

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product Name")
plt.grid(axis="x", linestyle="--")
plt.subplots_adjust(left=0.45)

plt.show()