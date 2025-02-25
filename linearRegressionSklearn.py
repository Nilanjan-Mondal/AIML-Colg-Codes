''' 
- Loads head size & brain weight data.
- Splits it into training (90%) and testing (10%) datasets.
- Fits a linear regression model on training data.
- Predicts values for the test data.
- Evaluates the model using:
- Root Mean Squared Error (RMSE)
- R² Score '''


import pandas as pd  
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split 

path = "/Users/nilanjanmondal/Documents/AIML-Colg-Codes/utils/"


data = pd.read_csv(path + "headbrain.csv")

x = data['Head Size(cm^3)'].values
y = data['Brain Weight(grams)'].values

# Reshape x into a 2D array because scikit-learn expects a 2D array for features
x = x.reshape(len(x), 1)  # Reshapes x from (n,) to (n,1), making it a 2D column vector

# Split the dataset into training (90%) and testing (10%) sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

# Initialize the Linear Regression model
model = LinearRegression()

# Train (fit) the model using the training data
model = model.fit(x_train, y_train)  # Learns the best-fit line (finds m and c in y = mx + c)

# Use the trained model to predict y values for the test set
y_pred = model.predict(x_test)  # Predicts y values based on x_test

# Compute the Root Mean Squared Error (RMSE), which measures the prediction error
rmse = np.sqrt(mean_squared_error(y_test, y_pred))  # Lower RMSE means better accuracy

# Compute the R² (R-squared) value, which indicates how well the model explains the variance in data
rSquareVal = model.score(x_test, y_test)  # Closer to 1 means a better fit

# Print the R-squared value
print(rSquareVal)  # Displays how well the model fits the data
