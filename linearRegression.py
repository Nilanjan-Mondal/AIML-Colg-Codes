import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = "/Users/nilanjanmondal/Documents/AIML-Colg-Codes/utils/"

data = pd.read_csv(path + "headbrain.csv")

#print(data)

x = data['Head Size(cm^3)'].values

y = data['Brain Weight(grams)'].values

mean_x = np.mean(x)
mean_y = np.mean(y)

coVar = 0
var = 0

for i in range(len(x)):
    coVar += (x[i] - mean_x) * (y[i] - mean_y)
    var += (x[i] - mean_x)**2
    
# y = mx + c.... m is the slope, c is the intercept

m = coVar / var
c = mean_y - (m * mean_x)

max_x = np.max(x) + 100
min_x = np.min(x) - 100

x1 = np.linspace(min_x, max_x, 100)
# y' = m(xi) + c   is the predicted value of y (xi will be input from user)
y1 = (m * x1) + c  

plt.plot(x1, y1, color = "#FF0000") # predicted values line
plt.scatter(x, y, color = "#FF0000", label = "Data Points") # actual data points from the dataSet


# y' = m(xi) + c   is the predicted value of y (xi will be input from user)
value = int(input("insert the head size in cm^3: "))
predict = (m * value) + c
print("Predicted value: ", predict)



