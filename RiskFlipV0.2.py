
import pandas as pd
import numpy as np
import datetime as dt
import pandas.io.data as web
import statsmodels.api as sm



START = dt.datetime(2011,1,1)
END = dt.datetime(2016,12,31)

#######################################################################################################

files_dict = {0:'AAPL',
              1:'CSCO',
              2:'BAC',
              3:'GOOGL',
              4:'GS',
              5:'JPM',
              6:'MSFT',
              7:'IBM',
              8:'AMZN',
              9:'GM',
              10:'I am done with adding assets to my portfolio'}



##########################################VALIDATIONS#################################################

def validate_asset_name(userInput,files_dict):
    try:
        val = int(userInput)
    except ValueError:
        return False
    if (val in files_dict):
        assetname = files_dict[val] 
        return True
    else:
        return False
    
    
def validate_num_shares(userInput):
    try:
        val = int(userInput)
        if abs(val) == 0:  # if not a positive int print message and ask for input again
            print("Sorry, input cannot be 0, try again!")
        else:
            position = np.sign(val)
            return True
    except ValueError:
        return False



def validate_hedge_pct(userInput):
    try:
        val = int(userInput)
        if val < 0:  # if not a positive int print message and ask for input again
            print("Sorry, input cannot be negative, try again!")
        elif val > 100:
            print("Sorry, input cannot be greater than 100%, try again!")
        else:
            return True
    except ValueError:
        return False

################################# ASSET ######################################################

class Asset(object):


    def __init__(self,assetname):
        self.assetname = assetname
        self.data = self.pull_data_from_yahoo()
        self.market_price = self.data['Adj Close'][-1]
        self.returns = self.returns_data()


    def pull_data_from_yahoo(self):
        symbol = self.assetname
        data = web.get_data_yahoo(symbol, start=START, end=END)
        # import pdb; pdb.set_trace()
        # print(data)
        return (data)



    def returns_data(self):
        self.data['returns'] = self.data['Adj Close'].shift(1)/self.data['Adj Close'] - 1
        return self.data['returns']


######################################## POSITION ################################################# 

class Position(object):

    def __init__(self, assetname, num_of_shares):
        self.num_of_shares = num_of_shares
        self.asset = Asset(assetname)
        self.value = self.calc_market_value()

    def calc_market_value(self):
        price_of_asset = self.asset.market_price 
        value = self.num_of_shares * price_of_asset
        return value

    def create_position(self):
        position = np.sign(num_of_shares)
        return position

########################################## PORTFOLIO ####################################################

class Portfolio(object):

    def __init__(self):
        self.positions = []

    def add_position(self,asset_name,num_of_shares):
        position = Position(asset_name,num_of_shares)
        self.positions.append(position)

    def market_val_portfolio(self):
        total_market_value = 0
        for position in self.positions:
            total_market_value += position.value
        return total_market_value



    def get_hedge(self):

        percentage_position = 0
        total_returns = 0
        
         
        for position in self.positions:
            percentage_position = position.value/self.market_val_portfolio()
            total_returns += position.asset.returns * (percentage_position)


        spy_data = web.get_data_yahoo('SPY', start=START, end=END)#pd.read_csv(r'C:\Users\smitha\Documents\Python_Scripts\chipy\chipydata\SPY.csv')
        spy_returns = spy_data['Adj Close'].shift(1)/spy_data['Adj Close'] - 1
        
        total_returns.dropna(inplace=True)
        spy_returns.dropna(inplace=True)
        spy_returns.corr(total_returns, method='pearson', min_periods=None)
        total_returns = sm.add_constant(total_returns)
        # print(total_returns)
        
        model = sm.OLS(spy_returns,total_returns).fit()

        beta = model.params[1]
        print("You have {} percent of Beta exposure".format(beta*100))
        # print(model.summary())
        hedge_pct = get_capital_hedge()
        # import pdb; pdb.set_trace()
        num_futures = np.round((beta* self.market_val_portfolio() * (int(hedge_pct)/100))/(spy_data['Adj Close'][-1]))
        
        return num_futures


################################### GETTING USER INPUTS ###############################################

def get_capital_hedge():

    print("\n\nWhat percentage of capital and the Beta exposure do you want to hedge?")
    hedge_pct = input()
    while not validate_hedge_pct(hedge_pct):
        print("Please input a valid integer!")
        hedge_pct = input()

    return hedge_pct 



def get_position_from_user():
    
    asset_dict = files_dict 

    print("\nPlease select an asset from our dictionary of assets")
    for key, val in asset_dict.items():
        print("{key}: {val}".format(key=key, val=val))
    asset_name = input()
    while not validate_asset_name(asset_name, asset_dict):
        print("that is not a valid asset name!")
        print("Please try again")
        asset_name = input()
        
    assetnames = asset_dict[int(asset_name)]
    if assetnames == "I am done with adding assets to my portfolio":
        return (False, 0)

    print("\nHow many shares of the Asset do you want to invest in? (To Buy : positive number, To Sell : negative number)")
    asset_num_shares = input()
    while not validate_num_shares(asset_num_shares):
        print("Please input an integer!")
        asset_num_shares = input()
        
    return (assetnames, int(asset_num_shares))


###################################################################################################
######################################### UI RUN ##################################################
###################################################################################################


def userinterface():

    new_user = Portfolio()

    asset_name, asset_num_shares = get_position_from_user()

    while asset_name:
        new_user.add_position(asset_name, asset_num_shares)
        asset_name, asset_num_shares = get_position_from_user()

    print("\nYour Portfolio is worth: ", new_user.market_val_portfolio(), "\n\n")

    hedge_units = new_user.get_hedge()
    if hedge_units > 0:
        print("\nTo hedge you should buy {} shares of SPDR S&P 500 ETF".format(hedge_units))
    elif hedge_units < 0:
        print("\nTo hedge you should sell {} shares of SPDR S&P 500 ETF".format(hedge_units))
    else:
        print("\nYou are perfectly hedged! ")


userinterface()





