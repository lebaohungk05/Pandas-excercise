import pandas as pd
import numpy as np

# Step 2 & 3
iris = pd.read_csv('iris.csv')

# Step 4
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Step 5
print(iris.isnull().sum())

# Step 6
iris.iloc[10:30, 2] = np.nan

# Step 7
iris.petal_length.fillna(1, inplace=True)

# Step 8
del iris['class']

# Step 9
iris.iloc[0:3, :] = np.nan

# Step 10
iris = iris.dropna(how='any')

# Step 11
iris = iris.reset_index(drop=True)
print(iris.head())
