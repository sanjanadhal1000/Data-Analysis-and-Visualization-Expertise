# Plotting an ROC Curve (Logistic Regression)

# Iris has 3 classes. To plot ROC, we convert it to binary.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import numpy as np

# Load Iris dataset
data = load_iris()
X = data.data
y = data.target

# Convert to binary classification: setosa(0) vs non-setosa(1). setosa and non-setosa are the classes in dataset.
y_binary = (y != 0).astype(int)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2, random_state=42)

# Train the Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predict Probabilities
y_prob = model.predict_proba(X_test)[:,1]

# Compute ROC Curve
fpr, tpr, threshold = roc_curve(y_test, y_prob)

# Compute AUC
auc_roc = auc(fpr, tpr)
print("ROC-AUC:", round(auc_roc,3))

# Plot
plt.plot(fpr, tpr, label="ROC Curve (AUC = %.3f)" % auc_roc)
plt.plot([0,1], [0,1], "--", label="Random Classifier")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()