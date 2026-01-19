import pandas as pd

# Step 2
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

# Step 3
regiment = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])

# Step 4
print(regiment[regiment['regiment'] == 'Nighthawks'].groupby('regiment').preTestScore.mean())

# Step 5
print(regiment.groupby('company').describe())

# Step 6
print(regiment.groupby('company').preTestScore.mean())

# Step 7
print(regiment.groupby(['regiment', 'company']).preTestScore.mean())

# Step 8
print(regiment.groupby(['regiment', 'company']).preTestScore.mean().unstack())

# Step 9
print(regiment.groupby(['regiment', 'company']).mean(numeric_only=True))

# Step 10
print(regiment.groupby(['regiment', 'company']).size())

# Step 11
for name, group in regiment.groupby('regiment'):
    print(name)
    print(group)
