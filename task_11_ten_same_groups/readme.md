# How to bin a numeric series to 10 groups of equal size?

Bin the series ser into 10 equal deciles and replace the values with the bin name.

## Input:

``` 
ser = pd.Series(np.random.random(20))
```

## Desired output:

``` 
# First 5 items
0    7th
1    9th
2    7th
3    3rd
4    8th
dtype: category
Categories (10, object): [1st < 2nd < 3rd < 4th ... 7th < 8th < 9th < 10th]
```