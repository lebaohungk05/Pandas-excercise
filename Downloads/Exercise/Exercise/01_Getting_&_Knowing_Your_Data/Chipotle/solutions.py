import pandas as pd

# Step 2 & 3
chipo = pd.read_csv('chipotle.tsv', sep='\t')

# Step 4
print(chipo.head(10))

# Step 5
print(chipo.shape[0])

# Step 6
print(chipo.shape[1])

# Step 7
print(chipo.columns)

# Step 8
print(chipo.index)

# Step 9
item_quants = chipo.groupby(['item_name']).agg({'quantity': 'sum'})
print(item_quants.sort_values('quantity', ascending=False)[:5])
print(item_quants.idxmax()[0])

# Step 10
print(item_quants.max()[0])

# Step 11
choice_quants = chipo.groupby(['choice_description']).agg({'quantity': 'sum'})
print(choice_quants.sort_values('quantity', ascending=False)[:5])
print(choice_quants.idxmax()[0])

# Step 12
print(chipo.quantity.sum())

# Step 13
dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer)
print(chipo.item_price.dtype)

# Step 14
print((chipo['quantity'] * chipo['item_price']).sum())

# Step 15
print(chipo.order_id.value_counts().count())

# Step 16
chipo['revenue'] = chipo['quantity'] * chipo['item_price']
order_grouped = chipo.groupby(by=['order_id']).sum()
print(order_grouped['revenue'].mean())

# Step 17
print(chipo.item_name.value_counts().count())

