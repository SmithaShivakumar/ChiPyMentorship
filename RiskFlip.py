
import os
from os import listdir
from os.path import isfile, join, basename
import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
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
        assetname = files_dict[val] #(list(files_dict.keys())[list(files_dict.values()).index(assetkey)])
        # get_data(assetname)
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
        # if val <= 100:  # if not a positive int print message and ask for input again
        #     print("Sorry, input cannot be 0 or less than 0, try again!")
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

        # self.num_of_shares = num_of_shares
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
        print(data)
        return data

    def compute_asset_beta(self):
        returns = self.market_price.shift(1) / self.market_price - 1
        spy_data = pd.read_csv(r'C:\Users\smitha\Documents\Python_Scripts\chipy\chipydata\SPY.csv')
        spy_returns = spy_data['PX_LAST'].shift(1)/spy_data['PX_LAST'] - 1
        asset_beta = sm.ols(formula="spy_returns ~ returns", data=pd.concat([spy_returns, returns], axis =1)).fit()
        return asset_beta

    def returns_data(self):
        self.data['returns'] = self.data['PX_LAST'].shift(1)/self.data['PX_LAST'] - 1
        return self.data['returns']


######################################## POSITION ################################################# 

class Position(object):

    def __init__(self, assetname, num_of_shares):
#         self.assetname = assetname
        self.num_of_shares = num_of_shares
        self.asset = Asset(assetname)
        self.value = self.calc_value()

    def calc_value(self):
        price_of_asset = self.asset.market_price 
        value = self.num_of_shares * price_of_asset
        return value

    def create_position(self):
        position = np.sign(num_of_shares)


        return position

########################################## PORTFOLIO ####################################################

class Portfolio(object):

    def __init__(self):
        # self.assetname = assetname
        # self.num_of_shares = num_of_shares
        self.positions = []

    def add_position(self,asset_name,num_of_shares):
        position = Position(asset_name,num_of_shares)
        self.positions.append(position)


    # def computingBeta(self):
    #     total_returns = Asset.returns * (num_of_assets/total_assets) 
    #     result13 = sm.ols(formula="spy_returns ~ total_returns", data=pd.concat([spy_returns, total_returns], axis =1)).fit()

    #     return beta

    def get_hedge(self,capital_invested,hedge_pct):

        total_returns = self.position.asset.returns* (self.position.num_of_shares/total_assets)
        beta = sm.ols(formula="spy_returns ~ total_returns", data=pd.concat([spy_returns, total_returns], axis =1)).fit()
              
        num_futures = np.round((total_returns * capital_invested * hedge_pct)/(Asset.market_price))
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
    else:


        print("How many shares of the Asset do you want to invest in")
        asset_num_shares = input()
        while not validate_num_shares(asset_num_shares):
            print("Please input an integer!")
            asset_num_shares = input()
        

    return (assetnames, asset_num_shares)


###################################################################################################
######################################### UI RUN ##################################################
###################################################################################################


def userinterface():

    new_user = Portfolio()
    total_shares = 0
    assets = []

    capital_invested, hedge_pct =  get_capital_hedge()
    asset_name, asset_num_shares = get_position_from_user()
    # total_shares += abs(int(asset_num_shares))
    # assets.append(asset_name)
    # total_assets = 1 

    while asset_name:
        # if asset_name == "I am done with adding assets to my portfolio":
        #     break
        new_user.add_position(asset_name, asset_num_shares)
        asset_name, asset_num_shares = get_position_from_user()
        total_assets += 1 
        total_shares += abs(int(asset_num_shares))
        assets.append(asset_name)


    print(assets, total_assets,total_shares)
    # totalreturnsdata = new_user.positions.asset.returns

    hedge_units = new_user.get_hedge(capital_invested,hedge_pct)
    if hedge_units > 0:
        print("To hedge you should buy {} shares".format(hedge_units))
    elif hedge_units < 0:
        print("To hedge you should sell {} shares".format(hedge_units))
    else:
        print("You are fine, perfectly hedged! ")
    # new_user




userinterface()





