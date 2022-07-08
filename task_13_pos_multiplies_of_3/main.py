import pandas as pd
import numpy as np

ser = pd.Series(np.random.randint(1, 10, 7), index=["a", "b", "c", "d", "e", "f", "g"])

# =============================================== #

# My solution
print(ser)
print(ser.reset_index().index[ser % 3 == 0])

# Author's solution
# print(ser)
# print(np.argwhere((ser % 3 == 0).array))
