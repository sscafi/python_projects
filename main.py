import requests
import pywhatkit as kit
from datetime import datetime, timedelta
import random


# Function to fetch a random cat image URL
def fetch_random_cat_image():
    # URL of the Cat API endpoint
    url = 'https://api.thecatapi.com/v1/images/search'

    try:
        # Send a GET request to the API
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract the URL of the random cat image
        image_url = data[0]['url']
        return image_url
    except requests.RequestException as e:
        print(f"Error fetching cat image: {e}")
        return None


# Fetch a random cat image URL
cat_image_url = fetch_random_cat_image()

# Check if the image URL was successfully fetched
if cat_image_url:
    # Your phone number with country code
    number = 'xxxxxxxxxx'
    message = 'Check out this random cat image!'

    # Get the current time and add a minute to it
    now = datetime.now()
    send_time = now + timedelta(minutes=1)
    hour = send_time.hour
    minute = send_time.minute

    # Send the WhatsApp message with the cat image URL
    kit.sendwhatmsg(number, message, hour, minute)
    kit.sendwhats_image(number, cat_image_url, message, 15)  # 15 seconds delay to ensure message is sent
else:
    print("Failed to fetch cat image.")
