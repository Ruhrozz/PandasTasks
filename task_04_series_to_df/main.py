import pandas as pd
import numpy as np

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

# ============================================================ #

# Solution 1
df = pd.DataFrame({"ser1": ser1, "ser2": ser2})

# Solution 2
# df = pd.concat([ser1, ser2], axis=1)

print(df)


