import pandas as pd
import numpy as np

# Step 2 & 3
wine = pd.read_csv('wine.csv')

# Step 4
wine = wine.drop(wine.columns[[0,3,6,8,11,12,13]], axis = 1)

# Step 5
wine.columns = ['alcohol', 'malic_acid', 'alcalinity_of_ash', 'magnesium', 'flavanoids', 'proanthocyanins', 'hue']

# Step 6
wine.iloc[0:3, 0] = np.nan

# Step 7
wine.iloc[2:4, 3] = np.nan

# Step 8
wine.alcohol.fillna(10, inplace=True)
wine.magnesium.fillna(100, inplace=True)

# Step 9
print(wine.isnull().sum())

# Step 10
random = np.random.randint(10, size = 10)

# Step 11
wine.alcohol[random] = np.nan

# Step 12
print(wine.isnull().sum())

# Step 13
wine = wine.dropna(axis = 0, how = "any")

# Step 14
print(wine.alcohol.notnull().sum())

# Step 15
wine = wine.reset_index(drop=True)
print(wine.head())
