import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Dummy data creation (replace this with your actual dataset)
data = pd.DataFrame({
    'CB_FLOW': np.random.uniform(0, 100, 100),
    'CB_PRESS': np.random.uniform(0, 100, 100),
    'CO2': np.random.uniform(0, 20, 100),
    'H2': np.random.uniform(0, 5, 100),
    'TEMP': np.random.uniform(300, 1500, 100),
    'O2': np.random.uniform(0, 10, 100),
    'N2': np.random.uniform(60, 80, 100),
    'hour': np.random.randint(0, 24, 100),
    'target': np.random.uniform(0, 1, 100)  # CO:CO₂ Ratio
})

X = data.drop('target', axis=1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
accuracy = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Save model
joblib.dump(model, 'model.pkl')
joblib.dump({'accuracy': accuracy, 'mse': mse}, 'metrics.pkl')

print("✅ Model and metrics saved!")
