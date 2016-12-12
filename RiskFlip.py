
# coding: utf-8

# # User Inputs

# In[46]:

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
        get_data(assetname)
        return True
    else:
        return False
    
def get_data(asset_name):
    assetname_ext = (asset_name + SUFFIX)
    print(asset_name)
    present = pd.read_csv(assetname_ext)
#     print(present)
    return (present)


# # Initiating Portfolio

# In[53]:

class InitiatePortfolio():
    
    def __init__(assetname,num_shares):
        self.assetname = asset_name
        self.num_shares = num_shares
#         self.position = position
        
        
    def add_position(num_shares):
        
        position = np.sign(num_shares)
        if position == 1:
            print ("we are long")
        else:
            print ("we are short")
            
    
#I am not sure how to call the other functions in this
        
        
InitiatePortfolio.add_position(-344) 


# In[48]:

def beta_calc(assetname, market_index):
    s_present = get_data(assetname)
    b_present = get_data(market_index)
    s_present = s_present.dropna()
    b_present = b_present.dropna()
    
    present = pd.concat([s_present,b_present],axis = 1)
    print(present)
"""
Need to refine the data to do the below calculations
"""
    
#     asset_beta = sm.ols(formula="s_present ~ b_present", data=pd.concat([s_present, b_present], axis =1)).fit()
    
#     present[['returns_s','returns_b']] = present[['adjclose_s','adjclose_b']]/\
#     present[['adjclose_s','adjclose_b']].shift(1) -1

#     covmat = np.cov(present["returns_s"],present["returns_b"])

    # calculate measures now
#     asset_beta = covmat[0,1]/covmat[1,1]
#     print(asset_beta)
#     return asset_beta

# beta_calc('GLD ETF','DIA Holdings')

# def weighted_beta_calc(portfolio):
    


# In[49]:

def userinterface():
    asset_dict = create_asset_dict(filelists)
    print("Please select an asset")
    for key, val in asset_dict.items():
        print("{key}: {val}".format(key=key, val=val))
    asset_name = input()
    while not validate_asset_name(asset_name, asset_dict):
        print("that is not a valid asset name!")
        print("Please try again")
        asset_name = input()
        
    print("How many shares of the Asset do you want to invest in")
    asset_num_shares = input()
    while not validate_num_shares(asset_num_shares):
        print("Please input an integer!")
        asset_num_shares = input()
     
    print(asset_name, asset_num_shares)
    
    

#     print(asset_dict[asset_name])
#     get_data(asset_dict.get("asset_name"))
    
userinterface()    


# In[ ]:




# In[ ]:



