import pandas as pd
import numpy as np

ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]

# ======================================================= #

# My solution
# print(ser[ser.reset_index().index.isin(pos)])

# Better (author's) solution
# print(ser.get(pos))
print(ser.take(pos))
