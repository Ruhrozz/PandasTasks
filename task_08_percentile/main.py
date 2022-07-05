import pandas as pd
import numpy as np

ser = pd.Series(np.random.normal(10, 5, 25))

# ============================================= #

# Author's solution
percentile = np.percentile(ser, q=[0, 25, 50, 75, 100])

# My solution is equivalent
print(ser.quantile(0) == percentile[0])
print(ser.quantile(0.25) == percentile[1])
print(ser.quantile(0.50) == percentile[2])
print(ser.quantile(0.75) == percentile[3])
print(ser.quantile(1) == percentile[4])
