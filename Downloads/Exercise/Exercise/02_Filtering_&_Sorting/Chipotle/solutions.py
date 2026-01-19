import pandas as pd

# Step 2 & 3
chipo = pd.read_csv('chipotle.tsv', sep='\t')
# Clean item_price
dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer)

# Step 4
# "How many products cost more than $10.00?"
chipo['unit_price'] = chipo['item_price'] / chipo['quantity']
print(chipo[chipo['unit_price'] > 10].item_name.nunique())

# Step 5
print(chipo[['item_name', 'unit_price']].drop_duplicates().sort_values(by='unit_price', ascending=False))

# Step 6
print(chipo.sort_values(by='item_name'))

# Step 7
print(chipo.sort_values(by='item_price', ascending=False).head(1))

# Step 8
print(len(chipo[chipo.item_name == "Veggie Salad Bowl"]))

# Step 9
print(len(chipo[(chipo.item_name == "Canned Soda") & (chipo.quantity > 1)]))

