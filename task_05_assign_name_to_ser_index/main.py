import pandas as pd
import numpy as np

ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))

# ==================================================== #

ser.name = "alphabets"
print(ser)
