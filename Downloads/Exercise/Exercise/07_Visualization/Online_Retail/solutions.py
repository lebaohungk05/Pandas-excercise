import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 2 & 3
online_rt = pd.read_csv('online_retail.csv', encoding='latin1')

# Step 4
countries = online_rt.groupby('Country').sum(numeric_only=True)
countries = countries.sort_values(by = 'Quantity',ascending = False)[1:11]
countries['Quantity'].plot(kind='bar')
plt.xlabel('Countries')
plt.ylabel('Quantity')
plt.title('10 Countries with most orders')
# plt.show()

# Step 5
online_rt = online_rt[online_rt.Quantity > 0]

# Step 6
customers = online_rt.groupby(['CustomerID','Country']).sum(numeric_only=True)
customers = customers[customers.UnitPrice > 0]
customers['Country'] = customers.index.get_level_values(1)
top_countries =  ['Netherlands', 'EIRE', 'Germany']
customers = customers[customers['Country'].isin(top_countries)]
for i in top_countries:
    data = customers[customers['Country'] == i]
    plt.scatter(data['UnitPrice'], data['Quantity'], label=i)
plt.legend()

# Step 7 & 8
online_rt['Revenue'] = online_rt.Quantity * online_rt.UnitPrice
price_start = 0 
price_end = 50
price_interval = 1
buckets = np.arange(price_start,price_end,price_interval)
revenue_per_price = online_rt.groupby(pd.cut(online_rt.UnitPrice, buckets)).Revenue.sum()
revenue_per_price.plot()
plt.xlabel('Unit Price (in intervals of '+str(price_interval)+')')
plt.ylabel('Revenue')
# plt.show()
