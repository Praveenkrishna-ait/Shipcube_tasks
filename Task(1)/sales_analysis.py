import pandas as pd

# 1. Load the sales_data.csv file into a DataFrame
df = pd.read_csv("sales_data.csv")

# 2. Clean the Price column (remove '$' and convert to float)
df["Price"] = df["Price"].replace('[\$,]', '', regex=True).astype(float)

# 3. Fill missing values in ProductCategory with 'Unknown'
df["ProductCategory"] = df["ProductCategory"].fillna("Unknown")

# 4. Convert PurchaseDate to datetime format
df["PurchaseDate"] = pd.to_datetime(df["PurchaseDate"], errors='coerce')

# 5. Calculate total revenue generated from each ProductCategory
revenue_per_category = df.groupby("ProductCategory")["Price"].sum()
print("Total Revenue per Category:\n", revenue_per_category)

# 6. Save the cleaned and processed DataFrame to new CSV
df.to_csv("cleaned_sales_data.csv", index=False)
print("\nCleaned data saved to 'cleaned_sales_data.csv'")
