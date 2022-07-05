import pandas as pd
import numpy as np

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

# ========================================= #

s_list = pd.Series(mylist)
s_arr = pd.Series(myarr)
s_dict = pd.Series(mydict)

print(s_list)
print(s_arr)
print(s_dict)



