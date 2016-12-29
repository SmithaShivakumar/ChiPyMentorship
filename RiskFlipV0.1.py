
import os
from os import listdir
from os.path import isfile, join, basename
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression




PATH = r'C:\Users\smitha\Documents\Python_Scripts\chipy\chipydata'  
SUFFIX = '.csv'
filelists = [f for f in listdir(PATH) if isfile(join(PATH, f))]


#######################################################################################################

def create_asset_dict(filelists):
    filename = []
    for val in filelists :
        base = basename(val)
        name = (os.path.splitext(base)[0])
        filename.append(name)
    files_dict = { i : val for i, val in enumerate(filename)} 
    return files_dict


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


def validate_capital_invested(userInput):
    try:
        val = int(userInput)
        if val <= 100:
            print("Sorry, capital invested has to be atleast $100, try again!")
        else:            
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
        self.data = self.get_data()
        self.market_price = self.data['PX_LAST'][0]
        self.returns = self.returns_data()

    def get_data(self):
        assetname_ext = (self.assetname + '.csv')
        print(self.assetname)
        pwd = os.getcwd()
        print(pwd)
        os.chdir(PATH)
        data = pd.read_csv(assetname_ext)
        data.drop_duplicates(subset = ['Date'],keep = 'first',inplace=True)
        data.reset_index(inplace=True)
        del data['index']
        # import pdb; pdb.set_trace()
        return data


    def returns_data(self):
        self.data['returns'] = self.data['PX_LAST'].shift(1)/self.data['PX_LAST'] - 1
        return self.data['returns']


######################################## POSITION ################################################# 

class Position(object):

    def __init__(self, assetname, num_of_shares):
#         self.assetname = assetname
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
        capital_invested,hedge_pct = get_capital_hedge()
         
        for position in self.positions:
            percentage_position = position.value/self.market_val_portfolio()
            total_returns += position.asset.returns * (percentage_position)


        spy_data = pd.read_csv(r'C:\Users\smitha\Documents\Python_Scripts\chipy\chipydata\SPY.csv')
        spy_returns = spy_data['PX_LAST'].shift(1)/spy_data['PX_LAST'] - 1
        
        total_returns.dropna(inplace=True)
        spy_returns.dropna(inplace=True)
        spy_returns.corr(total_returns, method='pearson', min_periods=None)
        total_returns = sm.add_constant(total_returns)
        # print(total_returns)
        
        model = sm.OLS(spy_returns,total_returns).fit()

        beta = model.params
        print(model.summary())
        
        # import pdb; pdb.set_trace()
        num_futures = np.round((beta[1]* self.market_val_portfolio() * (int(hedge_pct)/100))/(spy_data['PX_LAST'][1]))
        
        print(num_futures)
        return num_futures


################################### GETTING USER INPUTS ###############################################

def get_capital_hedge():

    print("How much capital do you want to invest in")
    capital_invested = input()
    while not validate_capital_invested(capital_invested):
        print("Please input a positive integer!")
        capital_invested = input()

    print("What percentage of capital do you want to hedge?")
    hedge_pct = input()
    while not validate_hedge_pct(hedge_pct):
        print("Please input a valid integer!")
        hedge_pct = input()


    return capital_invested, hedge_pct



def get_position_from_user():
    
    asset_dict = create_asset_dict(filelists)
    asset_dict[666] = "I am done with adding assets to my portfolio"
    
    print("Please select an asset")
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

    print("How many shares of the Asset do you want to invest in")
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

    print("Your Portfolio is worth: ", new_user.market_val_portfolio(), "\n\n")

    hedge_units = new_user.get_hedge()
    if hedge_units > 0:
        print("To hedge you should buy {} shares".format(hedge_units))
    elif hedge_units < 0:
        print("To hedge you should sell {} shares".format(hedge_units))
    else:
        print("You are fine, perfectly hedged! ")


userinterface()





