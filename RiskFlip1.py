import os
from os import listdir
from os.path import isfile, join, basename
import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
from sklearn.linear_model import LinearRegression


PATH = r'C:\Users\smitha\Downloads\Python Scripts\Smitha\straddle_test\ForRepo\Smitha\Data\CSVS'  
SUFFIX = '.csv'
filelists = [f for f in listdir(PATH) if isfile(join(PATH, f))]


def create_asset_dict(filelists):
    filename = []
    for val in filelists :
        base = basename(val)
        name = (os.path.splitext(base)[0])
        filename.append(name)
    files_dict = { i : val for i, val in enumerate(filename)} 
    return files_dict

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

#################################################################################################

class Asset():


    def __init__(self,assetname):

        # self.num_of_shares = num_of_shares
        self.assetname = assetname
        self.data = self.get_data()
        self.market_price = self.data['Adj Close'][0]

    def get_data(asset_name):
        assetname_ext = (asset_name + '.csv')
        print(asset_name)
        present = pd.read_csv(assetname_ext)
        print(present)
        return (present)


    def compute_asset_beta(present):


        return asset_beta



#################################################################################################

class Position():

    def __init__(self, assetname, num_of_shares):
        # self.assetname = assetname
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


#################################################################################################


class Portfolio():

    def __init__(self):
        # self.assetname = assetname
        # self.num_of_shares = num_of_shares
        self.positions = []

    def add_position(self,asset_name,num_of_shares):
        position = Position(asset_name,num_of_shares)
        self.positions.append(position)


    def computingBeta(self):
        return beta









#################################################################################################
#################################### RUN ########################################################
#################################################################################################

def get_position_from_user()
    asset_dict = create_asset_dict(filelists)
    print("Please select an asset")
    for key, val in asset_dict.items():
        print("{key}: {val}".format(key=key, val=val))
    asset_name = input()
    while not validate_asset_name(asset_name, asset_dict):
        print("that is not a valid asset name!")
        print("Please try again")
        asset_name = input()

     assetnames = asset_dict[int(asset_name)]
        
    print("How many shares of the Asset do you want to invest in")
    asset_num_shares = input()
    while not validate_num_shares(asset_num_shares):
        print("Please input an integer!")
        asset_num_shares = input()
     
    return (asset_name, asset_num_shares)


def userinterface():

    new_user = Portfolio()
    asset_name, num_of_shares = get_position_from_user()
    while asset_name:
        new_user.add_position(asset_name, num_of_shares)
        asset_name, num_of_shares = get_position_from_user()
    
    hedge_units = portfolio.get_hedge()
    if hedge_units > 0:
        print("To hedge you should buy {} shares".format(hedge_unitts))
    elif hedge_units < 0:
        print("To hedge you should sell {} shares".format(hedge_unitts))
    else:
        print("You are fine, perfectly hedged! ")
    # new_user
