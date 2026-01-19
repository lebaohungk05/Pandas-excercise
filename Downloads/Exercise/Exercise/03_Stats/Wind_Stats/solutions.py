import pandas as pd
import datetime

# Step 2 & 3
data = pd.read_csv('wind_stats.tsv', sep='\s+', parse_dates=[[0, 1, 2]])

# Step 4
def fix_century(x):
    year = x.year - 100 if x.year > 1989 else x.year
    return datetime.date(year, x.month, x.day)

data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix_century)

# Step 5
data['Yr_Mo_Dy'] = pd.to_datetime(data['Yr_Mo_Dy'])
data = data.set_index('Yr_Mo_Dy')

# Step 6
print(data.isnull().sum())

# Step 7
print(data.notnull().sum().sum())

# Step 8
print(data.mean().mean())

# Step 9
loc_stats = data.describe(percentiles=[])
print(loc_stats)

# Step 10
day_stats = pd.DataFrame()
day_stats['min'] = data.min(axis=1)
day_stats['max'] = data.max(axis=1)
day_stats['mean'] = data.mean(axis=1)
day_stats['std'] = data.std(axis=1)
print(day_stats.head())

# Step 11
print(data.loc[data.index.month == 1].mean())

# Step 12
print(data.resample('A').mean())

# Step 13
print(data.resample('M').mean())

# Step 14
print(data.resample('W').mean())

# Step 15
weekly = data.resample('W').agg(['min','max','mean','std'])
print(weekly.iloc[1:53].head())
