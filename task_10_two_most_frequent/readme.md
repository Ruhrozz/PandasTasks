# How to keep only top 2 most frequent values as it is and replace everything else as ‘Other’?

From `ser`, keep the top 2 most frequent items as it is and replace everything else as ‘Other’.

## Input:

```
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
```