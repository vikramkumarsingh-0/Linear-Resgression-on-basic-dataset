
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the data
data = pd.read_csv("practice.csv")

# Reshape the data
data = data.melt(id_vars='Brands', var_name='Year', value_name='Sales')
print(data)
data['Year'] = data['Year'].astype(int)
print("------------------------------------------------------")
print(data)

# Initialize variables
brands = data['Brands'].unique()
predictions = {}

# Loop over each brand
for i in range(len(brands)):
    # Filter data for the current brand
    brand_data = data[data['Brands'] == brands[i]]
    
    # Prepare the data for the model
    X = brand_data['Year'].values.reshape(-1, 1)
    y = brand_data['Sales']
    
    # Create and fit the model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict the next five years and store the predictions
    future_years = np.array([2024, 2025, 2026, 2027, 2028]).reshape(-1, 1)
    predictions[brands[i]] = model.predict(future_years)

# Print the predictions
for brand, prediction in predictions.items():
    print(f"Predicted sales for {brand} for the next five years: {prediction}")
