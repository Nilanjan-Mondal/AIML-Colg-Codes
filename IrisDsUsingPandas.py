import pandas as pd

# reading a csv file using pandas

path = "/Users/nilanjanmondal/Documents/AIML-Colg-Codes/utils/"

data = pd.read_csv(path + "Iris_Dataset.csv")

#print(data)


# add one extra column by calculating from one existing column

data1 = data

data1 = data1.assign(total_length = data1['sepal_length'] + data1['petal_length'])
data1 = data1.assign(total_width = data1['sepal_width'] + data1['petal_width'])

print(data1)

