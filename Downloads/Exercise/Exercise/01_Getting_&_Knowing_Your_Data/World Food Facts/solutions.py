import pandas as pd

# Step 2 & 3
food = pd.read_csv('products.tsv', sep='\t')

# Step 4
print(food.head())

# Step 5
print(food.shape[0])

# Step 6
print(food.shape[1])

# Step 7
print(food.columns)

# Step 8
print(food.columns[104])

# Step 9
print(food.dtypes[104])

# Step 10
print(food.index)

# Step 11
try:
    print(food.at[18, 'product_name'])
except:
    print("Could not access product_name at index 18")

