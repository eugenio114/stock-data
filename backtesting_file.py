import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance
import datetime
from scipy.stats import gaussian_kde
from list_stocks import stocks_list, short_list, aapl

ticker = ['A']

stock = pdr.get_data_yahoo(ticker, start=datetime.datetime(2017, 12, 1), end=datetime.date.today())

# Initialize the short and long windows
short_window = 40
long_window = 100

# Initialize the `signals` DataFrame with the `signal` column
signals = pd.DataFrame(index=stock.index)

#signals['Code'] = stock['Ticker']
signals['signal'] = 0.0

# Create short simple moving average over the short window
signals['short_mavg'] = stock['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
signals['long_mavg'] = stock['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:]
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)

# Generate trading orders
signals['positions'] = signals['signal'].diff()


print(stock)
print(signals)

# Initialize the plot figure
fig = plt.figure()

# Add a subplot and label for y-axis
ax1 = fig.add_subplot(111, ylabel='Price in $')

# Plot the closing price
stock['Close'].plot(ax=ax1, color='r', lw=2.)

# Plot the short and long moving averages
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

# Plot the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index,
         signals.short_mavg[signals.positions == 1.0],
         '^', markersize=10, color='b')

# Plot the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index,
         signals.short_mavg[signals.positions == -1.0],
         'v', markersize=10, color='y')

stock['Diff_Open_Close'] = stock.Open - stock.Close

font = {'family': 'sanserif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

plt.title(ticker, fontdict=font)

# Show the plot
plt.show()
print(stock)