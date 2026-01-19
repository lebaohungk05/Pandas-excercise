import pandas as pd
import matplotlib.pyplot as plt

# Step 2
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
        'age': [42, 52, 36, 24, 73], 
        'female': [0, 1, 1, 0, 1],
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'female', 'preTestScore', 'postTestScore'])

# Step 3
plt.scatter(df.preTestScore, df.postTestScore, s=df.age)
plt.xlabel('preTestScore')
plt.ylabel('postTestScore')
plt.title('preTestScore vs postTestScore')
# plt.show()

# Step 4
plt.scatter(df.preTestScore, df.postTestScore, s=df.postTestScore * 4.5, c=df.female)
plt.xlabel('preTestScore')
plt.ylabel('postTestScore')
plt.title('preTestScore vs postTestScore (Color=Sex, Size=PostTestScore)')
# plt.show()
