import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance
import datetime
from list_stocks import stocks_list

#data = pdr.get_data_yahoo(stocks_list, start=datetime.datetime(2017, 12, 31), end=datetime.datetime(2020, 12, 31))
aapl = pdr.get_data_yahoo('AAPL', start=datetime.datetime(2017, 12, 1), end=datetime.date.today())
print(aapl.head())

#inspect the index
print(aapl.index)
# Inspect the columns
print(aapl.columns)

# Select only the last 10 observations of `Close` and print them
ts = aapl['Close'][-10:]
print(ts)

# Inspect the first rows of November-December 2020
print(aapl.loc[pd.Timestamp('2020-11-01'):pd.Timestamp('2020-12-31')].head())

# Inspect the first rows of 2020
print(aapl.loc['2020'].head())

# Inspect Feb 2018 using iloc
print(aapl.iloc[22:43])

# Inspect the 'Open' and 'Close' values at 2018-02-02 and 2018-03-06
print(aapl.iloc[[22,43], [0, 3]])

# Sample 20 rows
sample = aapl.sample(20)

# Print `sample`
print(sample)

# Resample to monthly level
monthly_aapl = aapl.resample('M')

# Print `monthly_aapl`
print(monthly_aapl)

# Add a column `diff` to `aapl`
aapl['diff'] = aapl.Open - aapl.Close

# Delete the new `diff` column
del aapl['diff']

# Plot the closing prices for `aapl`
aapl['Close'].plot(grid=True)

# Show the plot
plt.show()

# Assign `Adj Close` to `daily_close`
daily_close = aapl[['Adj Close']]

# Daily returns
daily_pct_c = daily_close.pct_change()

# Replace NA values with 0
daily_pct_c.fillna(0, inplace=True)

# Inspect daily returns
print(daily_pct_c)

# Daily log returns
daily_log_returns = np.log(daily_close.pct_change()+1)

# Print daily log returns
print(daily_log_returns)

# Resample `aapl` to business months, take last observation as value
monthly = aapl.resample('BM').apply(lambda x: x[-1])

# Calculate the monthly percentage change
print(monthly.pct_change())

# Resample `aapl` to quarters, take the mean as value per quarter
quarter = aapl.resample("4M").mean()

# Calculate the quarterly percentage change
print(quarter.pct_change())

# Daily returns
daily_pct_c = daily_close / daily_close.shift(1) - 1

# Print `daily_pct_c`
print(daily_pct_c)

# Plot the distribution of `daily_pct_c`
daily_pct_c.hist(bins=50)

# Show the plot
plt.show()

# Pull up summary statistics
print(daily_pct_c.describe())

# Calculate the cumulative daily returns
cum_daily_return = (1 + daily_pct_c).cumprod()

# Print `cum_daily_return`
print(cum_daily_return)