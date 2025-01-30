import pandas as pd

# reading a csv file using pandas

path = "/Users/nilanjanmondal/Documents/AIML-Colg-Codes/utils/"

data = pd.read_csv(path + "employees-1.csv")


data1 = data.copy()

#this method is used to drop multiple columns at a time 
# here i am not usin data1 = data1.drop because here i am using inplace = true, so it does not return any new DF
data1.drop(data1.columns[[0,1,3]], axis = 1, inplace = True)

print(data)
print(data1)