import pandas as pd
import numpy as np

ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

# ========================================== #

print(pd.concat([ser1, ser2], axis="columns"), end='\n\n')
print(pd.concat([ser1, ser2], axis="rows"), end='\n\n')

# Author's solution for vertical concatenation (method is deprecated, don't use it!!!)
# print(ser1.append(ser2))
