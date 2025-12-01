# Install & Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Create a Simple Dataset
data ={
    "Experience":[1,2,3,4,5,6,7,8,9,10],
    "Salary":[30, 35, 40, 47, 52, 60, 65, 70, 78, 85]
} 

df = pd.DataFrame(data)
print(df)

# Split into X and y
X = df[["Experience"]] # features must be 2D. 
# If it was 1D, it would be a Series, not a DataFrame, which isn't allowed in sckit-learn models for X.
y = df["Salary"]

# Train-Test-Split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Build & Train the Model
model = LinearRegression()
model.fit(X_train,y_train)

# Model Outputs (Slope & Intercept)
print(f"Slope (Coefficient): {model.coef_[0]:.2f}")
# In scikit-learn, any value learned from data during training ends with an underscore(_). 
# If we write model.coef, it will throw an error "AttributeError: 'LinearRegression' object has no attribute 'coef'".
#  coef is not a class attribute. Only coef_ is called after you call .fit().
# coef_ is an array even if it has only one feature. 
# If we dont write [0], the result will be an array, not the number or element.
# Formatting with :.2f fails as an array cannot be formatted as a float.
# TypeError: only size-1 arrays can be converted to Python scalars

print(f"Intercept: {model.intercept_:.2f}")

# Make Predictions
y_pred = model.predict(X_test)

print("Predicted:", [round(float(v), 2) for v in y_pred])
print("Actual:", [round(val, 2) for val in y_test])

# Evaluate the Model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Plot Regression Line
plt.scatter(X,y,label="Data Points")
plt.plot(X,model.predict(X),label="Best Fit Line")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (in thousands)")
plt.title("Linear Regression: Salary Prediction")
plt.legend()
plt.show()