import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
data = pd.read_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf_kneighbor_v2.csv')

# Create feature matrix (X) and target vector (y)
X = data[['stfdem', 'stfgov', 'stfeco']]  # Replace with your feature names
y = data['educational_level']  # Replace with your target variable name

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the logistic regression model
logreg = LogisticRegression()

# Train the model
logreg.fit(X_train, y_train)

# Make predictions
y_pred = logreg.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Generate confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print(f'Confusion Matrix:\n{conf_matrix}')

# Get a more detailed classification report
class_report = classification_report(y_test, y_pred)
print(f'Classification Report:\n{class_report}')
