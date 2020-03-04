import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('.btctradeCNY.csv', names=['timestamp', 'price', 'volume'])

data['datetime'] = pd.to_datetime(data['timestamp'], unit='s')
data['month_year'] = data['datetime'].dt.to_period('M')

data = data[~data['price'].isin([0])]
data = data[~data['price'].isnull()]
data = data.drop_duplicates()

data_v = data.groupby('month_year')
data_v = data_v['volume'].sum()

im = data_v.idxmax()

data_max_month = data[data['month_year'].isin([im])]

x = data_max_month['datetime']
y = data_max_month['price']

plt.figure(figsize=(12, 4))
plt.plot(x, y, color="red", linewidth=1)
plt.xlabel("Date Time")
plt.ylabel("Price")
plt.title("Price Curve")
plt.savefig('Curve03.png', dpi=120, bbox_inches='tight')
plt.show()
