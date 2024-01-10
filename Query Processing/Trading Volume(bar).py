import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Date': '01-04-2020', 'Volume': 2343100, 'Close': 1105.62},
    {'Date': '02-04-2020', 'Volume': 1964900, 'Close': 1120.84},
    {'Date': '03-04-2020', 'Volume': 2313400, 'Close': 1097.88},
    {'Date': '06-04-2020', 'Volume': 2664700, 'Close': 1186.92},
    {'Date': '07-04-2020', 'Volume': 2387300, 'Close': 1186.51},
    {'Date': '08-04-2020', 'Volume': 1975100, 'Close': 1210.28},
    {'Date': '09-04-2020', 'Volume': 2175400, 'Close': 1211.45},
    {'Date': '13-04-2020', 'Volume': 1739800, 'Close': 1217.56},
    {'Date': '14-04-2020', 'Volume': 2470400, 'Close': 1269.23},
    {'Date': '15-04-2020', 'Volume': 1671700, 'Close': 1262.47},
    {'Date': '16-04-2020', 'Volume': 2518100, 'Close': 1263.47},
    {'Date': '17-04-2020', 'Volume': 1949000, 'Close': 1283.25},
    {'Date': '20-04-2020', 'Volume': 1695500, 'Close': 1266.61},
    {'Date': '21-04-2020', 'Volume': 2153000, 'Close': 1216.34},
    {'Date': '22-04-2020', 'Volume': 2093100, 'Close': 1263.21},
    {'Date': '23-04-2020', 'Volume': 1566200, 'Close': 1276.31},
    {'Date': '24-04-2020', 'Volume': 1640400, 'Close': 1279.31},
    {'Date': '27-04-2020', 'Volume': 1600600, 'Close': 1275.88},
    {'Date': '28-04-2020', 'Volume': 2951300, 'Close': 1233.67},
    {'Date': '29-04-2020', 'Volume': 3793600, 'Close': 1341.48},
    {'Date': '30-04-2020', 'Volume': 2665400, 'Close': 1320.61},
    {'Date': '01-05-2020', 'Volume': 2072500, 'Close': 1320.61}
]

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Specify the start and end dates for the bar plot
start_date = '2020-04-01'
end_date = '2020-04-20'

filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

plt.bar(filtered_data['Date'], filtered_data['Volume'], color='blue')
plt.xlabel('Date')
plt.ylabel('Trading Volume')
plt.title(f'Trading Volume of Alphabet Inc. ({start_date} to {end_date})')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
