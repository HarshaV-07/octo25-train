import pandas as ps
import numpy as ny
import matplotlib.pyplot as pt

# Read the dataset
aq = ps.read_csv('air.csv')
print(aq.head())

# Convert 'End Date' to datetime format (fix format string if necessary)
aq['End Date'] = ps.to_datetime(aq['End Date'], format='mixed')

print(aq.info())

# Plotting the NO2 levels
pt.figure()
pt.plot(aq['End Date'], aq['NO2'], marker='.', label='NO2')
pt.xticks(fontsize=20)
pt.yticks(fontsize=20)
pt.xlabel('Date', fontsize=20)
pt.ylabel('NO2 Concentration', fontsize=20)
pt.legend(fontsize=25)
pt.title('Actual NO2 readings in Coventry', fontsize=32)
pt.show()

# Convert NO2 column to NumPy array for computation
aq1 = aq['NO2'].to_numpy()
print(aq1)

alpha = 0.5  # Smoothing parameter for level
gamma = 0.5  # Smoothing parameter for seasonality
m = 92       # Seasonality period (e.g., monthly data with yearly seasonality)

# Initialize variables
Level = ny.empty(len(aq1))
Seasonal = ny.empty(len(aq1))
Forecast = ny.empty(len(aq1))

# Initial values (can be adjusted based on your data)
Level[0] = aq1[0]  # Initial level can be set to the first observation
Seasonal[:m] = aq1[:m] - aq1[:m].mean()  # Initial seasonal component

# Holt-Winters Smoothing (without Trend)
for i in range(m, len(aq1)):
    # Level update (simplified without trend)
    Level[i] = alpha * (aq1[i] - Seasonal[i - m]) + (1 - alpha) * Level[i - 1]
    
    # Seasonal update
    Seasonal[i] = gamma * (aq1[i] - Level[i]) + (1 - gamma) * Seasonal[i - m]
    
    # Forecast calculation
    Forecast[i] = Level[i] + Seasonal[i - m]

# Convert to a DataFrame for better visualization
summary = ps.DataFrame({
    'Actual': aq1,
    'Level': Level,
    'Seasonal': Seasonal,
    'Forecast': Forecast
})

# Print summary DataFrame
print(summary)

# Plot the actual vs forecasted data
pt.figure(figsize=(12, 6))
pt.plot(aq['End Date'], aq1, label='Actual NO2', color='blue', marker='.')
pt.plot(aq['End Date'], Forecast, label='Forecasted NO2', color='red', linestyle='-', marker='x')
pt.xticks(fontsize=16)
pt.yticks(fontsize=20)
pt.title('Actual vs Forecasted NO2 levels', fontsize=32)
pt.xlabel('Date', fontsize=20)
pt.ylabel('NO2 Concentration', fontsize=20)
pt.legend(fontsize=12)
pt.grid(True)
pt.show()
