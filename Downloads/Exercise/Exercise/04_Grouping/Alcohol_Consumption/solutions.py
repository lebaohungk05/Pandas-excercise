import pandas as pd

# Step 2 & 3
drinks = pd.read_csv('drinks.csv')

# Step 4
print(drinks.groupby('continent').beer_servings.mean().idxmax())

# Step 5
print(drinks.groupby('continent').wine_servings.describe())

# Step 6
print(drinks.groupby('continent').mean())

# Step 7
print(drinks.groupby('continent').median())

# Step 8
print(drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max']))
