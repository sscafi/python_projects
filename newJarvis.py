import speech_recognition as sr
import mysql.connector

# Function to connect to the database and retrieve the commands
def get_commands():
    # Establish a connection to the database
    db = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="jarvis"
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Retrieve the commands from the database
    cursor.execute("SELECT name, action FROM commands")
    commands = cursor.fetchall()

    # Close the database connection
    db.close()

    # Return the commands as a dictionary
    return dict(commands)

# Initialize the speech recognizer
r = sr.Recognizer()

# Set the microphone as the audio source
mic = sr.Microphone()

# Get the commands from the database
commands = get_commands()

# Continuously listen for voice commands
while True:
    # Listen for voice input
    with mic as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # Use the speech recognizer to convert the audio to text
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)

        # Check if the text matches any of the commands
        for command, action in commands.items():
            if command.lower() in text.lower():
                print("Performing action: " + action)
                # Perform the action associated with the command
                break

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")
    except sr.RequestError as e:
        print("Oops! Couldn't request results from Google Speech Recognition service; {0}".format(e))
