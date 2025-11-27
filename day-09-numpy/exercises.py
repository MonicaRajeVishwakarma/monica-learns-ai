# Day 09 - NumPy Basics

import numpy as np

#1. Create a 1D array from 0 to 9
arr = np.arange(10)
print("iD Array:",arr)

#2. Create a 3*3 array of ones
ones = np.ones((3,3))
print("\n3*3 ones\n",ones)

#3. Element wise operation
arr2 = arr * 2
print("\nArray multiplied by 2",arr2)

#4. Aggregations
print("\nSum of arr",arr.sum())
print("\nMean of arr",arr.mean())

#5. Indexing
arr2d = np.array([[1,2,3],[4,5,6]])
print("\n2D array:\n",arr2d)
print("\nElement at row0, col2:",arr2d[0,2])
print("\nColumn 1:",arr2d[:,1])