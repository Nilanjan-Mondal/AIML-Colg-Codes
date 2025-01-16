# create a numpy array, arr1 which contains 9 integer values.
# Reshape arr1 into an order of 3 x 3
# Perform exponential operation on reshaped numpy array

import numpy as np

arr = np.array([4,5,2,3,5,6,7,8,9])

reShapeArr = np.reshape(arr, (3,3))

print(reShapeArr)

powerArr = np.power(reShapeArr, 2)
print(powerArr)

