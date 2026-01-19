import pandas as pd

# Step 2 & 3
euro12 = pd.read_csv('euro.tsv', sep=',')

# Step 4
print(euro12.Goals)

# Step 5
print(euro12.shape[0])

# Step 6
print(euro12.shape[1])

# Step 7
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print(discipline)

# Step 8
print(discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending=False))

# Step 9
print(discipline['Yellow Cards'].mean())

# Step 10
print(euro12[euro12.Goals > 6])

# Step 11
print(euro12[euro12.Team.str.startswith('G')])

# Step 12
print(euro12.iloc[:, :7])

# Step 13
print(euro12.iloc[:, :-3])

# Step 14
print(euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']])
