import pandas as pd

# Step 2 & 3
users = pd.read_csv('occupation.csv', sep='|', index_col='user_id')

# Step 4
print(users.head(25))

# Step 5
print(users.tail(10))

# Step 6
print(users.shape[0])

# Step 7
print(users.shape[1])

# Step 8
print(users.columns)

# Step 9
print(users.index)

# Step 10
print(users.dtypes)

# Step 11
print(users.occupation)

# Step 12
print(users.occupation.nunique())

# Step 13
print(users.occupation.value_counts().head(1).index[0])

# Step 14
print(users.describe())

# Step 15
print(users.describe(include='all'))

# Step 16
print(users.occupation.describe())

# Step 17
print(users.age.mean())

# Step 18
print(users.age.value_counts().tail())
