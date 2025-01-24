import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt

# Step 1: Read and prepare the data
team_flights = pd.read_csv('./team_flights.csv')
fuel_prices = pd.read_csv('./fuel_prices_2101.csv')

# Convert datetime columns to datetime format
team_flights['departure_datetime'] = pd.to_datetime(team_flights['departure_datetime'])
team_flights['landing_datetime'] = pd.to_datetime(team_flights['landing_datetime'])

fuel_prices['date'] = pd.to_datetime(fuel_prices['date'])
fuel_prices = fuel_prices.set_index('date')

# Ensure fuel_prices has a regular frequency
fuel_prices = fuel_prices.asfreq('D')

# Step 2: Calculate maximum number of jets needed
all_times = []
for _, row in team_flights.iterrows():
    all_times.append((row['departure_datetime'], 'start'))
    all_times.append((row['landing_datetime'], 'end'))

# Sort events by time
all_times.sort(key=lambda x: x[0])

# Track flights in progress
in_flight_count = 0
max_jets_needed = 0
for time, event in all_times:
    if event == 'start':
        in_flight_count += 1
    elif event == 'end':
        in_flight_count -= 1
    max_jets_needed = max(max_jets_needed, in_flight_count)

# Step 3: Forecast fuel prices using SARIMAX
# Create SARIMAX model with seasonal parameters
sarimax_model = SARIMAX(fuel_prices['price'], order=(1, 1, 0), seasonal_order=(1, 0, 0, 7), enforce_stationarity=False, enforce_invertibility=False)
model_fit = sarimax_model.fit(disp=True)  # Display optimization details

# Print model summary
print(model_fit.summary())

# Forecast fuel prices for the next 365 days in 2102
forecasted_prices = model_fit.get_forecast(steps=365)
forecast_index = pd.date_range(start='2102-01-01', periods=365, freq='D')
forecasted_prices = pd.DataFrame({
    'date': forecast_index,
    'fuel_price': forecasted_prices.predicted_mean
})
forecasted_prices['date'] = pd.to_datetime(forecasted_prices['date'])

# Step 4: Calculate total fuel spend
# Add departure date to the team flights data
team_flights['departure_date'] = team_flights['departure_datetime'].dt.date
forecasted_prices['date'] = forecasted_prices['date'].dt.date

# Merge forecasted prices with flight data
team_flights = team_flights.merge(forecasted_prices, left_on='departure_date', right_on='date', how='left')

# Calculate distance and fuel cost
team_flights['flight_duration_hours'] = (team_flights['landing_datetime'] - team_flights['departure_datetime']).dt.total_seconds() / 3600
team_flights['travel_distance_miles'] = team_flights['flight_duration_hours'] * 500
team_flights['fuel_cost'] = team_flights['travel_distance_miles'] * team_flights['fuel_price']

# Sum up total fuel costs
total_fuel_spend_2102 = team_flights['fuel_cost'].sum()

# Step 5: Output results
print("Maximum number of jets needed:", max_jets_needed)
print("Total fuel spend for 2102 ($):", total_fuel_spend_2102)

# Step 6: Plot flights in progress over time
time_series = []
current_flights = 0
for time, event in all_times:
    time_series.append((time, current_flights))
    if event == 'start':
        current_flights += 1
    elif event == 'end':
        current_flights -= 1
    time_series.append((time, current_flights))

# Create DataFrame for plotting
flight_data = pd.DataFrame(time_series, columns=['time', 'flights_in_progress'])
flight_data = flight_data.drop_duplicates(subset='time')

# Plot the data
plt.figure(figsize=(12, 7))
plt.step(flight_data['time'], flight_data['flights_in_progress'], where='post', color='blue', linewidth=2, label='Flights in Progress')
plt.scatter(flight_data['time'], flight_data['flights_in_progress'], color='red', s=10, label='Flight Events')
plt.title('Number of Teams in Flight Throughout the 2102 Season', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Flights in Progress', fontsize=14)
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.grid(visible=True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
