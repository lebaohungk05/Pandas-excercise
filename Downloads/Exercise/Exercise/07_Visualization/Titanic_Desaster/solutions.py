import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2 & 3
titanic = pd.read_csv('titanic.csv')

# Step 4
titanic.set_index('PassengerId', inplace=True)

# Step 5
males = (titanic['Sex'] == 'male').sum()
females = (titanic['Sex'] == 'female').sum()
proportions = [males, females]
plt.pie(proportions, labels = ['Males', 'Females'], shadow = False, colors = ['blue', 'red'], explode = (0.15 , 0), startangle = 90, autopct = '%1.1f%%')
plt.axis('equal')
plt.title("Sex Proportion")
# plt.show()

# Step 6
groups = titanic.groupby("Sex")
for name, group in groups:
    plt.plot(group["Age"], group["Fare"], marker="o", linestyle="", label=name)
plt.legend()
plt.xlabel("Age")
plt.ylabel("Fare")
# plt.show()

# Step 7
print(titanic.Survived.sum())

# Step 8
titanic.Fare.hist()
plt.xlabel("Fare")
plt.ylabel("Frequency")
# plt.show()
