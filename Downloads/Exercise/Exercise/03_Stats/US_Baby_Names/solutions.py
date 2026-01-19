import pandas as pd

# Step 2 & 3
baby_names = pd.read_csv('us_baby.tsv', sep=',')

# Step 4
print(baby_names.head(10))

# Step 5
if 'Unnamed: 0' in baby_names.columns:
    del baby_names['Unnamed: 0']
if 'Id' in baby_names.columns:
    del baby_names['Id']

# Step 6
print(baby_names['Gender'].value_counts())

# Step 7
names = baby_names.groupby('Name').sum()
if 'Year' in names.columns:
    del names['Year']
print(names.head())

# Step 8
print(len(names))

# Step 9
print(names.Count.idxmax())

# Step 10
print(len(names[names.Count == names.Count.min()]))

# Step 11
print(names.Count.median())

# Step 12
print(names.Count.std())

# Step 13
print(names.Count.describe())
