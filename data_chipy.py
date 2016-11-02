import datetime as dt
# import pandas.io.data as web
import numpy as np
import pandas as pd
from os.path import basename
import os

PATH = r'C:\Users\Tenzan\Documents\Smitha\straddle_test\ForRepo\Smitha\Data\CSVS'
os.chdir(PATH)
files = os.listdir(PATH)

# print(np.array(files))
# print([val for val in files])


print("Choose the number associated with your asset from the following : ")
filename = []


for val in files :
	base = basename(val)
	name = (os.path.splitext(base)[0])
	print(name)
	filename.append(name)
    
# files_dict = (pd.DataFrame(filename)).to_dict
# print(files_dict)

assetname = input()

# print(files_dict['assetname'])

suffix = '.csv'
assetname_ext = os.path.join(assetname + suffix)
present = pd.read_csv(assetname_ext)
print (present)

# x = files_dict.values()
# if (6 in x):
#     assetname_ext = os.path.join(files_dict[assetname] + suffix)
    
#     present = pd.read_csv(assetname_ext)
#     print (present)
# else :
#     raise ValueError("Type out the name of the asset as given in the list!")


#cd = [pd.read_csv(assetname + '.csv') for assetname in files_dict]
#print(dc)




"""wb = pd.read_excel('SP500companies.xlsx')
# print(wb, type(wb))

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

# print(wb.columns)
returns_sp500 = []
assetname = [x for x in wb['Ticker symbol']]


from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

returns_sp500.append(get_data(assetname))

print(returns_sp500)"""