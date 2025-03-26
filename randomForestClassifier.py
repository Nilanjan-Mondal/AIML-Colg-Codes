import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score

path = "/Users/nilanjanmondal/Documents/AIML-Colg-Codes/utils/"

# Load dataset
data = pd.read_csv(path + "Iris_Dataset.csv")

# Features (X) and Target (Y)
X = data.drop("species", axis=1)  
Y = data["species"]  

# Convert categorical labels to numerical values
le = LabelEncoder()
Y = le.fit_transform(Y)

# Split into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4)

# Train Random Forest Classifier
random_forest = RandomForestClassifier()
random_forest.fit(X_train, Y_train)

# Predictions
Y_pred = random_forest.predict(X_test)

# Confusion Matrix & Accuracy
cm = confusion_matrix(Y_test, Y_pred)
acc = accuracy_score(Y_test, Y_pred)

# Output Results
print("Confusion Matrix:\n", cm)
print("Accuracy:", acc * 100)
