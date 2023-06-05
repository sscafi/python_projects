import pytz
from datetime import datetime

def world_clock():
    while(True):
        city = input("Enter a city: ")

        try:
            timezone = pytz.timezone(city)
            current_time = datetime.now(timezone)
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"The current time in {city} is: {formatted_time}")
            print(f"Timezone: {timezone}")
        except pytz.UnknownTimeZoneError:
            print("Invalid city or timezone not found.")

world_clock()
