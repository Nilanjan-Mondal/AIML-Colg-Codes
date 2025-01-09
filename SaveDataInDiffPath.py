import numpy as np

path = "C:/Users/User/Desktop/AIML_2A23/TempData/"

arr = np.array([1,2,3,4,5,6])

np.savetxt(path + "data.txt", arr) #concatination

arr1 = np.loadtxt(path + "data.txt")
print(arr1)

