import statsmodels.api as sm
import pandas as pd
from pandas import tseries
import numpy as np
import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance
import datetime
from scipy.stats import gaussian_kde
from list_stocks import stocks_list, short_list, aapl


tickers = stocks_list

def get(tickers, startdate, enddate):
    def data(tickers):
        return (pdr.get_data_yahoo(tickers, start=startdate, end=enddate))
    datas = map (data, tickers)
    return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))


stock = get(tickers, datetime.datetime(2018, 1, 1), datetime.date.today())

#add Difference from open to close column in the data
stock['Diff_Open_Close'] = stock.Open - stock.Close

daily_close_px = stock[['Adj Close']]


# Calculate the daily percentage change for `daily_close_px`
daily_pct_change = daily_close_px.pct_change()

stock['Daily_PC_Change'] = daily_pct_change

min_periods = 75

# Calculate the volatility VIX indicator to exploit market's fear
#https://www.forex.in.rs/volatility-75-index/
vol = daily_pct_change.rolling(min_periods).std() * np.sqrt(min_periods)

stock['75_Vol_VIX'] = vol

short_window = 40
long_window = 100

# Initialize the `signals` DataFrame with the `signal` column

stock['signal'] = 0.0

# Create short simple moving average over the short window
stock['short_mavg'] = stock['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
stock['long_mavg'] = stock['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
stock['signal'][short_window:] = np.where(stock['short_mavg'][short_window:]
                                            > stock['long_mavg'][short_window:], 1.0, 0.0)

# Generate trading orders
stock['positions'] = stock['signal'].diff()


####stock.to_csv("/Users/carpanie/Desktop/Stocks/stock.csv")
print(stock)
print(stock.columns)

# Buy a 100 shares when signal turns positive
stock['Pos'] = 1*stock['signal']

#print(stock)

# Initialize the portfolio with value owned
stock['Portfolio'] = stock['Pos'].multiply(stock['Adj Close'], axis=0)

# Store the difference in shares owned
stock['Pos_diff'] = stock['Pos'].diff()

# Add `holdings` to portfolio

stock.loc[stock['positions'] == 1, 'Buy'] = stock['Portfolio']
stock.loc[stock['positions'] == -1, 'Sell'] = stock['Portfolio'].shift(1)

stock['Returns'] = (stock['Sell'].sum() + stock['Portfolio'][-1]) - stock['Buy'].sum()


# Print CAGR


print(stock)


stock.to_csv("apple.csv")

