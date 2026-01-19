import pandas as pd

# Step 2 & 3
crime = pd.read_csv('student_alcohol.csv')

# Step 4
print(crime.dtypes)

# Step 5
crime.Year = pd.to_datetime(crime.Year, format='%Y')

# Step 6
crime = crime.set_index('Year', drop=True)

# Step 7
del crime['Total']

# Step 8
crimes = crime.resample('10YS').sum()
population = crime['Population'].resample('10YS').max()
crimes['Population'] = population
print(crimes)

# Step 9
print(crimes.idxmax(0))
