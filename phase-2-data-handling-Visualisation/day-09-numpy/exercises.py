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
arr5= arr + 2
print("\nArray added by 2",arr5)

#4. Aggregations
print("\nAggregations:")
print("Sum of arr",arr.sum())
print("Mean of arr",arr.mean())
print("Max of arr",arr.max())
print("Min of arr",arr.min())

#5. Indexing
print("\nIndexing:")
arr2d = np.array([[1,2,3],[4,5,6]])
print("2D array:\n",arr2d)
print("Element at row0, col2:",arr2d[0,2])
print("Column 1:",arr2d[:,1])
print("Row 1:",arr2d[1:])

#6. Create 2*2 array of zeros
zeros = np.zeros((2,3))
print("\n Array of zeros:\n",zeros)

#7. Array from 0 to 10 step 2 (multiple of 2)
arr3 = np.arange(0,10,2) # array from 0 to 10 step 2
print("\nArray from 0 to 10 step 2",arr3)

#8. 5 numbers from 0 to 1
arr4 = np.linspace(0,1,5) # 5 numbers from 0 to 1
print("\n5 numbers from 0 to 1",arr4)