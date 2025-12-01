# Train a Simple model on the Iris Dataset

# Load the Dataset
from sklearn.datasets import load_iris
data = load_iris()
X = data.data
y = data.target

# Split into Training and Testing Sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Classifier (eg. Logistic Regression)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=200)
model.fit(X_train,y_train)

# Predict
y_pred = model.predict(X_test)

'''
# Confusion Matrix
    - Shows Actual vs. Predicted Classes.
    - Helps see exactly where the model is making mistakes.
    - More detailed than accuracy.
    
'''

# Generate Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)

'''
Interpretation:
    - Rows: Actual labels.
    - Columns: Predicted labels.
    - Diagonal: Correct Predictions.
    - Off-diagonal: Misclassification.

'''

# Visualizing the matrix - optional.
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(cm, annot=True, fmt='d')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Visualization of Confusion Matrix")
plt.show()