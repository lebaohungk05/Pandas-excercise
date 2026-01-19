import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Step 2 & 3
chipo = pd.read_csv('chipotle.tsv', sep='\t')
dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer)

# Step 4
print(chipo.head(10))

# Step 5
x = chipo.item_name
letter_counts = Counter(x)
df = pd.DataFrame.from_dict(letter_counts, orient='index')
df = df[0].sort_values(ascending = True)[-5:]
df.plot(kind='bar')
plt.xlabel('Items')
plt.ylabel('Quantity')
plt.title('Most ordered Chipotle\'s Items')
# plt.show()

# Step 6
chipo['unit_price'] = chipo.item_price / chipo.quantity
orders = chipo.groupby('order_id').sum()
plt.scatter(x = orders.item_price, y = orders.quantity, s = 50, c = 'green')
plt.xlabel('Order Price')
plt.ylabel('Items ordered')
plt.title('Number of items ordered per order price')
# plt.show()

