import pandas as pd
import numpy as np

ser = pd.Series(np.random.random(20))

# ========================================= #

# My solution
# bins = 10
# categories = pd.cut(ser, bins)
#
# categories.cat.categories = [f"{i} group" for i in range(1, bins+1)]
#
# print(categories)

# Author's solution:
bins = 10
categories = pd.cut(ser, bins, labels=["1th", "2nd", "3rd"] + [f"{i}th" for i in range(4, 11)])

print(categories)
