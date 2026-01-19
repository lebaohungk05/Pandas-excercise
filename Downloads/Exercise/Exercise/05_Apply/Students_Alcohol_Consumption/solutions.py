import pandas as pd
import numpy as np

# Step 2 & 3
df = pd.read_csv('student_alcohol.csv')

# Step 4
df = df.loc[:, 'school':'guardian']
print(df.head())

# Step 5
capitalize = lambda x: x.capitalize()

# Step 6
df['Mjob'] = df['Mjob'].apply(capitalize)
df['Fjob'] = df['Fjob'].apply(capitalize)

# Step 7
print(df.tail())

# Step 9
def majority(x):
    if x > 17:
        return True
    else:
        return False

df['legal_drinker'] = df['age'].apply(majority)
print(df.head())

# Step 10
def times10(x):
    if np.issubdtype(type(x), np.number):
        return 10 * x
    return x

print(df.map(times10).head(10))
