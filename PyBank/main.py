

import pandas as pd

df = pd.read_csv('./resources/budget_data.csv')
months = df['Date'].count()
total = df['Profit/Losses'].sum()
change = df['Profit/Losses']
average = df['Profit/Losses']
#prints out months and total
print(f'Total Months : {months}')
print(f'Total : {total}')
# creates a new column change, which measures the change from this row compared to previous row
for i in range(1, len(df)):
    lastrow = 867884
    df['change'] = pd.Series(df['Profit/Losses'] - lastrow)
    lastrow = df['Profit/Losses']

# prints mean, max and min
print(f'Average Change : {int(df.change.mean())}')
print(f'Greatest increase in profits : {df.change.max()}')
print(f'Greatest decrease in profits : {df.change.min()}')
