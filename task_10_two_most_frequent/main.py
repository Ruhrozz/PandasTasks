import pandas as pd
import numpy as np

np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

# ================================= #

# My solution:
# top_two = ser.value_counts().index[:2]
# ser = pd.Series(np.where(ser.isin(top_two), ser, 'other'))
# print(ser)

# Better (author's) solution:
top_two = ser.value_counts().index[:2]
ser[~ser.isin(top_two)] = 'other'
print(ser)
