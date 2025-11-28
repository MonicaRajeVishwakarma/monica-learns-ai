# Day 09 Notes – NumPy Basics

import numpy as np

## Create arrays
```python
arr1 = np.array([1, 2, 3, 4])
arr2 = np.zeros((2,3))  # 2x3 zeros
arr3 = np.ones((3,2))   # 3x2 ones
arr4 = np.arange(0,10,2) # array from 0 to 10 step 2
arr5 = np.linspace(0,1,5) # 5 numbers from 0 to 1
```


## Array operations
```python
arr = np.array([1,2,3])
print(arr + 10)  # add 10 to each element
print(arr * 2)   # multiply each element
print(arr ** 2)  # square each element
```

## Aggregations
```python
print(arr.sum())
print(arr.mean())
print(arr.min())
print(arr.max())
```

## Indexing and slicing
```python
arr2d = np.array([[1,2,3],[4,5,6]])
print(arr2d[0,1])    # element at row0, col1
print(arr2d[:,1])    # all rows, column 1
print(arr2d[1,:])    # row1, all columns
```