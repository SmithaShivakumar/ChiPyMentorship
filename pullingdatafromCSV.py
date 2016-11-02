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


