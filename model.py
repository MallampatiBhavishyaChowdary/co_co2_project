import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Generate sample CO/CO2 data
np.random.seed(42)
co_levels = np.random.uniform(0, 100, 500)  # Simulated CO levels
co2_levels = 2.5 * co_levels + np.random.normal(0, 10, 500)  # Simulated CO2 levels

# Create a DataFrame
data = pd.DataFrame({'CO': co_levels, 'CO2': co2_levels})

# Split data into train and test sets
X = data[['CO']]
y = data['CO2']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"Model Performance: MAE={mae:.2f}, MSE={mse:.2f}")

# Save model
joblib.dump(model, "co_co2_model.pkl")
print("Model saved as co_co2_model.pkl")
