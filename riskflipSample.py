import datetime as dt
import pandas as pd
import numpy as np
import pandas.io.data as web
import statsmodels.formula.api as sm
from sklearn.linear_model import LinearRegression


# GETTING DATA #################################################################################

def get_data(symbol):
	start = dt.datetime(2011,1,1)
	end = dt.datetime(2016,1,1)
	symbol_df = web.get_data_yahoo(symbol, start=start, end=end)
	start = symbol_df.index.min()
	end = symbol_df.index.max()

	monthly_dates = pd.date_range(start, end, freq='M')
	monthly = symbol_df.reindex(monthly_dates, method='ffill')
	returns_symbol = 100 * monthly['Adj Close'].pct_change().dropna()

	return (returns_symbol)


returns_sp500 = get_data('^GSPC')
returns_dowjo = get_data('^DJI')
returns_nasd = get_data('^IXIC')


returns_gg = get_data('GOOG')
returns_amz = get_data('AMZN')
returns_ice = get_data('ICE')
returns_apl = get_data('AAPL')


# CUMULATIVE RETURNS ####################################################################################

total_returns = returns_gg + returns_amz + returns_ice + returns_apl

# REGRESSION ####################################################################################


result1 = sm.ols(formula="returns_sp500 ~ total_returns", data=pd.concat([returns_sp500, total_returns], axis =1)).fit()

result12 = sm.ols(formula="returns_dowjo ~ total_returns", data=pd.concat([returns_dowjo, total_returns], axis =1) ).fit()

result13 = sm.ols(formula="returns_nasd ~ total_returns", data=pd.concat([returns_nasd, total_returns], axis =1)).fit()


# NUMBER OF FUTURES ##############################################################################

capital_invested = 60000   #int(input()) # User input of the amount
hedge_pct = 0.6   #float(input())  # User input of the percentage
symbol = "^GSPC"
history = pd.io.data.DataReader(symbol, "yahoo", start="2014/1/1")
# current_price = (history.Open.tail(1).values)

no_futures = np.round((result1.params.total_returns * capital_invested * hedge_pct)/(history.Open.tail(1).values))

print (no_futures)

