import pandas as pd

# Step 2 & 3
users = pd.read_csv('occupation.csv', sep='|', index_col='user_id')

# Step 4
print(users.groupby('occupation').age.mean())

# Step 5
# Male ratio
def gender_to_numeric(x):
    if x == 'M':
        return 1
    if x == 'F':
        return 0

users['gender_n'] = users['gender'].apply(gender_to_numeric)
a = users.groupby('occupation').gender_n.sum() / users.occupation.value_counts() * 100
print(a.sort_values(ascending=False))

# Step 6
print(users.groupby('occupation').age.agg(['min', 'max']))

# Step 7
print(users.groupby(['occupation', 'gender']).age.mean())

# Step 8
gender_occup_count = users.groupby(['occupation', 'gender']).agg({'gender': 'count'})
occup_count = users.groupby(['occupation']).agg('count')
occup_gender = gender_occup_count.div(occup_count, level='occupation') * 100
print(occup_gender.loc[:, 'gender'])
