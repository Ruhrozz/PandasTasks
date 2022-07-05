import pandas as pd
import numpy as np

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# ============================================= #

# My solution
ser3 = pd.concat([ser1, ser2])
ser_union = ser1[ser1.isin(ser2)]
ser3 = ser3[~ser3.isin(ser_union)]
print(ser3.reset_index(drop=True))

# Author's solution
# ser_u = pd.Series(np.union1d(ser1, ser2))  # union
# ser_i = pd.Series(np.intersect1d(ser1, ser2))  # intersect
# print(ser_u[~ser_u.isin(ser_i)])

# On big data(10.000.000):
# My:       --- 2.615004777908325 seconds ---
# Author's: --- 4.672553300857544 seconds ---
