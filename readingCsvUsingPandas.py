import pandas as pd

# reading a csv file using pandas

path = "/Users/nilanjanmondal/Documents/AIML-Colg-Codes/utils/"

data = pd.read_csv(path + "employees-1.csv")

#print(data)


# add one extra column by calculating from one existing column

data1 = data.copy()  #.copy is used to create a seperate copy independent of the original dataframe

data1 = data1.assign(commission_yearly = data1['salary'] * 0.2) # 20 percent commission

print(data1)