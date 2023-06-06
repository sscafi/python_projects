import pandas as pd

# Load historical flight data from a CSV file
flight_data = pd.read_csv('historical_flight_data.csv')

# Function to calculate the average price for a given date range
def calculate_average_price(start_date, end_date):
    filtered_flights = flight_data[(flight_data['date'] >= start_date) & (flight_data['date'] <= end_date)]
    average_price = filtered_flights['price'].mean()
    return average_price

# User input for travel details
departure_city = input("Enter departure city: ")
destination_city = input("Enter destination city: ")
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

# Calculate average price for the specified date range
average_price = calculate_average_price(start_date, end_date)

# Display the result
print(f"The average price for flights from {departure_city} to {destination_city} between {start_date} and {end_date} is ${average_price:.2f}")

#In this example,
#  we load historical flight data from a 
# CSV file using the pd.read_csv() function 
# from the pandas library. The flight data is
#  assumed to contain columns such as "date" and "price".