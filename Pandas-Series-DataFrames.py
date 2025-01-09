import pandas as pd

# series and dataframe creation

dict = {
        'key1': 1,
        'key2': 2
    }

dtf = pd.Series(dict)
temp = pd.DataFrame([dict])

print(dtf)
print(temp)



dict1 = {
        'name': ['Varun', 'aftab', 'deepika'],
        'email': ['abc.com', 'vsknd.com', 'efij.com']
    
    }

dtf = pd.DataFrame(dict1)

print(dtf)