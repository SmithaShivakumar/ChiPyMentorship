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



"""
# SP500 ####################################################################################


returns_sp500 = pd.DataFrame(returns_sp500)

returns_sp500.to_csv('C:/Users/Tenzan/Documents/garch/returns_data.csv')
# print (start, end)
# print (returns)


# DOWJONES ####################################################################################

dowjo = web.get_data_yahoo('^DJI', start=start, end=end)

monthly_dates = pd.date_range(start, end, freq='M')
monthly = dowjo.reindex(monthly_dates, method='ffill')
returns_dowjo = 100 * monthly['Adj Close'].pct_change().dropna()



# NASDAQ ####################################################################################

nasd = web.get_data_yahoo('^IXIC', start=start, end=end)

monthly_dates = pd.date_range(start, end, freq='M')
monthly = nasd.reindex(monthly_dates, method='ffill')
returns_nasd = 100 * monthly['Adj Close'].pct_change().dropna()


# GOOGLE ####################################################################################

gg = web.get_data_yahoo('GOOG', start=start, end=end)

monthly_dates = pd.date_range(start, end, freq='M')
monthly = gg.reindex(monthly_dates, method='ffill')
returns_gg = 100 * monthly['Adj Close'].pct_change().dropna()
# returns_gg = pd.DataFrame(returns_gg)
# print (returns_gg)


# FACEBOOK ####################################################################################

amz = web.get_data_yahoo('AMZN', start=start, end=end)

monthly_dates = pd.date_range(start, end, freq='M')
monthly = amz.reindex(monthly_dates, method='ffill')
returns_amz = 100 * monthly['Adj Close'].pct_change().dropna()
# returns_amz = pd.DataFrame(returns_amz)
# print (returns_amz)


# ICE ####################################################################################

ice = web.get_data_yahoo('ICE', start=start, end=end)

monthly_dates = pd.date_range(start, end, freq='M')
monthly = ice.reindex(monthly_dates, method='ffill')
returns_ice = 100 * monthly['Adj Close'].pct_change().dropna()
# returns_ice = pd.DataFrame(returns_ice)
# print (returns_ice)


# APPLE ####################################################################################

apl = web.get_data_yahoo('AAPL', start=start, end=end)

monthly_dates = pd.date_range(start, end, freq='M')
monthly = apl.reindex(monthly_dates, method='ffill')
returns_apl = 100 * monthly['Adj Close'].pct_change().dropna()
# returns_apl = pd.DataFrame(returns_apl)
# print (returns_apl)


# CUMULATIVE RETURNS ####################################################################################

total_returns = returns_gg + returns_amz + returns_ice + returns_apl

df1 = pd.concat([returns_sp500, total_returns], axis =1)  
df1.columns = ["S&P 500 returns", "Equiweighted Stock returns"]
# print (df1)


df12 = pd.concat([returns_dowjo, total_returns], axis =1) 
df12.columns = ["DOW JONES returns", "Equiweighted Stock returns"]
# print (df12)


df13 = pd.concat([returns_nasd, total_returns], axis =1)  
df13.columns = ["NASDAQ returns", "Equiweighted Stock returns"]
# print (df13)



# REGRESSION ####################################################################################


result1 = sm.ols(formula="returns_sp500 ~ total_returns", data=df1).fit()
# print (result1.params) #, result1.summary())

result12 = sm.ols(formula="returns_dowjo ~ total_returns", data=df12).fit()
# print (result12.params) #, result12.summary())

result13 = sm.ols(formula="returns_nasd ~ total_returns", data=df13).fit()
# print (result13.params) #, result13.summary())


# NUMBER OF FUTURES ##############################################################################

capital_invested = int(input()) # User input of the amount
hedge_pct = float(input())  # User input of the percentage 
symbol = "^GSPC"
history = pd.io.data.DataReader(symbol, "yahoo", start="2014/1/1")

# current_price = (history.Open.tail(1).values)

no_futures = np.round((result1.params.total_returns * capital_invested * hedge_pct)/(history.Open.tail(1).values))











# from pandas.stats.api import ols
# res = ols(y=df['returns'], x=df[['total_returns']])
# print (res)


df = pd.concat([returns_sp500,returns_dowjo,returns_nasd, total_returns], axis =1)  

print (df)

lr1 = LinearRegression()

X1, y1 = df.iloc[:,0].as_matrix(), df.iloc[:,3].as_matrix()
lr1.fit(X1, y1)
LinearRegression(copy_X1=True, fit_intercept=True, normalize=False)

lr2 = LinearRegression()

X2, y2 = df.iloc[:,1].as_matrix(), df.iloc[:,3].as_matrix()
lr2.fit(X2, y2)
LinearRegression(copy_X2=True, fit_intercept=True, normalize=False)

lr3 = LinearRegression()

X3, y3 = df.loc[:,2].as_matrix(), df.loc[:,3].as_matrix()
lr3.fit(X3, y3)
LinearRegression(copy_X3=True, fit_intercept=True, normalize=False)


print (lr1.coef_, lr2.coef_, lr3.coef_)
# lr.intercept_

"""