import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

path = "/Users/nilanjanmondal/Documents/AIML-Colg-Codes/utils/"

# Load dataset
data = pd.read_csv(path + "Iris_Dataset.csv")

# Features (X) and Target (Y)
X = data.drop("species", axis=1)
Y = data["species"]

# Convert categorical labels to numerical values
le = LabelEncoder()
Y = le.fit_transform(Y)  # Convert categorical labels to numbers

# we do not need to convert x into numpy array because DecisionTreeClassifier support dataframes

# Split into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4)

# Train Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(X_train, Y_train)

# Predictions
Y_pred = model.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(Y_test, Y_pred)
print("Confusion Matrix:\n", cm)

# Accuracy
acc = accuracy_score(Y_test, Y_pred)
print("Accuracy:", acc * 100)

# Precision
precision = precision_score(Y_test, Y_pred, average='weighted')
print("Precision:", precision * 100)

# Recall
recall = recall_score(Y_test, Y_pred, average='weighted')
print("Recall:", recall * 100)

# F1 Score
f1_value = f1_score(Y_test, Y_pred, average='weighted')
print("F1 Score:", f1_value * 100)
