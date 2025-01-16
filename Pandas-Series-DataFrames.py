import pandas as pd

# series and dataframe creation

dict = {
        'key1': 1,
        'key2': 2
    }

dtf1 = pd.Series(dict) 
print(dtf1)


# temp = pd.DataFrame(dict) 

# If you pass dict directly to pd.DataFrame(dict), 
# Pandas interprets each key as a column name and expects the values for each key to be iterable 
#(like a list, tuple, or array). But in this case, the values (1 and 2) are integers, not iterables, 
#so you'll get an error.


temp = pd.DataFrame([dict]) 
print(temp)

# To create a DataFrame where the dictionary represents a row, wrap the dictionary in a list ([dict])



dict1 = {
        'name': ['Varun', 'aftab', 'deepika'],
        'email': ['abc.com', 'vsknd.com', 'efij.com']
    
    }

dtf2 = pd.DataFrame(dict1)
print(dtf2)

#In this case, the dictionary values are lists (iterables). Pandas automatically interprets this as:
#Passing dict1 directly to pd.DataFrame(dict1) works because Pandas can map the lists as columns of the DataFrame:

    

dtf2_len = len(dtf2["name"]) # prints the size of 'name' of our data frame
print("Count using len: ", dtf2_len)


count = 0
for n in dict1["name"]:   # manually prints the size of name in the dictionary
    count += 1
print("Count manual: ", count)



# custom indexing in dataframe

customIdxDtf2 = pd.DataFrame(dict1, index=['stu1', 'stu2', 'stu3'])
print(customIdxDtf2)
