import pandas as pd

import matplotlib.pyplot as plt

from scipy.stats import linregress

#Link do teste: https://replit.com/@LuizSinx/boilerplate-sea-level-predictor#main.py

# Read data from file
df = pd.read_csv('epa-sea-level.csv')


# Create scatter plot
fig, ax = plt.subplots(figsize=(16, 8))

dy = pd.Series([int(i) for i in range(1880, 2051)])
print(dy.head())
df.plot(x='Year', y='CSIRO Adjusted Sea Level', kind='scatter', ax=ax, label="Original Date")


# Create first line of best fit
line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
ax.plot(dy, line.intercept+line.slope*dy, label='Before 2000')

# Create second line of best fit
line = linregress(df['Year'][df['Year'] >= 2000], df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000])

ax.plot(dy[dy >= 2000], line.intercept+line.slope*dy[dy >= 2000], label="After 2000")

# Add labels and title
ax.set_title('Rise in Sea Level')
ax.legend()


plt.show()