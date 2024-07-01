import pytz
from datetime import datetime

def world_clock():
    """
    Continuously prompts the user to enter a city and displays the current time in that city.
    Uses the pytz library to handle timezones.

    Args:
    - None

    Returns:
    - None
    """
    while(True):
        city = input("Enter a city: ")

        try:
            timezone = pytz.timezone(city)  # Retrieve timezone object for the given city
            current_time = datetime.now(timezone)  # Get current time in the specified timezone
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")  # Format time as YYYY-MM-DD HH:MM:SS
            print(f"The current time in {city} is: {formatted_time}")
            print(f"Timezone: {timezone}")
        except pytz.UnknownTimeZoneError:
            print("Invalid city or timezone not found.")

# Start the world clock application
world_clock()
