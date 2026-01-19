import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2 & 3
tips = pd.read_csv('tips.csv')

# Step 4
if 'Unnamed: 0' in tips.columns:
    del tips['Unnamed: 0']

# Step 5
tips.total_bill.plot(kind='hist')
# plt.show()

# Step 6
plt.scatter(x=tips.total_bill, y=tips.tip)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
# plt.show()

# Step 7
sns.pairplot(tips)
# plt.show()

# Step 8
sns.stripplot(x = "day", y = "total_bill", data = tips, jitter = True)
# plt.show()

# Step 9
sns.stripplot(x = "tip", y = "day", hue = "sex", data = tips, jitter = True)
# plt.show()

# Step 10
sns.boxplot(x = "day", y = "total_bill", hue = "time", data = tips)
# plt.show()

# Step 11
g = sns.FacetGrid(tips, col = "time")
g.map(plt.hist, "tip")
# plt.show()

# Step 12
g = sns.FacetGrid(tips, col = "sex", hue = "smoker")
g.map(plt.scatter, "total_bill", "tip", alpha =.7)
g.add_legend()
# plt.show()
