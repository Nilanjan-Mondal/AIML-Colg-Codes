import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.tree import DecisionTreeRegressor

path = "/Users/nilanjanmondal/Documents/AIML-Colg-Codes/utils/"

# Load dataset
data = pd.read_csv(path + "HeadBrain.csv")

# Features (X) and Target (Y)
X = data[["Head Size(cm^3)"]]  # Independent variable
Y = data["Brain Weight(grams)"]  # Dependent variable

# Split into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4)

# Train Decision Tree Regressor
model = DecisionTreeRegressor()
model.fit(X_train, Y_train)

# Predictions
Y_pred = model.predict(X_test)

# Evaluation Metrics
mse = mean_squared_error(Y_test, Y_pred)
print("Mean Squared Error:", mse)

mae = mean_absolute_error(Y_test, Y_pred)
print("Mean Absolute Error:", mae)

r2 = r2_score(Y_test, Y_pred)
print("R² Score:", r2)

# Visualization
plt.scatter(X_test, Y_test, color='red', label="Actual Data")
plt.scatter(X_test, Y_pred, color='blue', label="Predicted Data")
plt.xlabel("Head Size (cm³)")
plt.ylabel("Brain Weight (grams)")
plt.legend()
plt.title("Decision Tree Regression on HeadBrain Dataset")
#plt.show()
