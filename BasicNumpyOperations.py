import numpy as np

# perform add, sub, mul. div using numpy array

study_duration1 = np.array([4,5,2,3,5,4,6])
study_duration2 = np.array([1,2,5,3,2,2,1])

total_duration1 = study_duration1 + study_duration2
print("Total duration using + operator", total_duration1)

total_duration2 = np.add(study_duration1, study_duration2)
print("Total duration using np add func", total_duration2)

total_duration3 = np.subtract(study_duration1, study_duration2)
print("Total duration using np subtract func", total_duration3)

total_duration4 = np.multiply(study_duration1, study_duration2)
print("Total duration using np multiply func", total_duration4)

total_duration5 = np.divide(study_duration1, study_duration2)
print("Total duration using np divide func", total_duration5)

print("---------------------------------------------------------")


# finding exponential

num_arr = np.array([4,5,6])
num_exp1 = num_arr ** 2

print("Exponent using ** operator", num_exp1)

num_exp2 = np.power(num_arr, 2)
print("Exponent using np power func", num_exp2)

print("---------------------------------------------------------")


# finding mean and median

arr = np.mean([1,2,3,4,4,4,4])
mean = np.mean(arr)
median = np.median(arr)
print("Mean using numpy mean func: ",mean)
print("Median using numpy median func: ",median)

print("---------------------------------------------------------")


# Reshape a numpy array

ar = np.array([4,5,2,3,5,6])
reShapeAr = np.reshape(ar, (3,2))  # 3 is the number of rows and 2 is the number of column
print("Actual arr: ", ar)
print("Reshaped arr: ",reShapeAr)



