Here's the code with added comments explaining each line:

```python
# Importing necessary libraries
import pyttsx3  # pip install pyttsx3 - Library for text to speech conversion
import speech_recognition as sr  # pip install speechRecognition - Library for speech recognition
import datetime  # Library to handle date and time
import wikipedia  # pip install wikipedia - Library to fetch data from Wikipedia
import webbrowser  # Library to open web browsers
import os  # Library to interact with the operating system
import smtplib  # Library to send emails
import subprocess  # Library to handle subprocesses

# Defining the path to Firefox browser
fire_fox = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
# Registering Firefox as the web browser
webbrowser.register('firefox', None)
print("Initializing Jarvis")  # Initialization message
MASTER = "Sir"  # Setting a variable for user address

# Initializing the text to speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Setting the voice to the first available voice

# Function to make the engine speak the provided text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to wish the user based on the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)  # Getting the current hour
    if hour >= 0 and hour < 12:
        speak("Good Morning " + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon " + MASTER)
    else:
        speak("Good Evening " + MASTER)
    speak("How may I help you ......")

# Function to take voice commands from the user
def takeCommand():
    r = sr.Recognizer()  # Initializing the recognizer
    with sr.Microphone() as source:
        print("Listening.....")  # Indicating that the system is listening
        audio = r.listen(source)  # Listening to the source
    try:
        print("Recognizing.....")  # Indicating that the system is recognizing
        query = r.recognize_google(audio, language='en-GB')  # Recognizing speech using Google
        print(f"user said: {query}\n")  # Printing the recognized text
    except Exception as e:
        print("Please say that again " + MASTER)  # Asking the user to repeat if recognition fails
        query = None
    return query  # Returning the recognized text

# Function to send an email (incomplete implementation)
def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Setting up the SMTP server
    server.ehlo()  # Sending the EHLO command
    server.starttls()  # Starting TLS for security
    server.login('youremail@gmail.com', 'password')  # Logging into the email account
    server.sendmail  # Placeholder for sending the email

# Main function to execute the assistant
def main():
    speak("Initializing Jarvis....")  # Announcing initialization
    wishMe()  # Calling the wishMe function
    query = takeCommand()  # Taking the user's command

    # Handling different commands
    if 'wikipedia' in query.lower():
        speak('Searching Wikipedia...')  # Announcing the search
        query = query.replace("wikipedia", "")  # Removing 'wikipedia' from the query
        results = wikipedia.summary(query, sentences=2)  # Fetching summary from Wikipedia
        print(results)  # Printing the results
        speak(results)  # Speaking the results

    elif 'open youtube' in query.lower():
        webbrowser.register('firefox',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open_new_tab("youtube.com")  # Opening YouTube

    elif 'open facebook' in query.lower():
        url = "facebook.com"
        webbrowser.open(url)  # Opening Facebook

    elif 'open anime' in query.lower():
        webbrowser.register('firefox',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open_new_tab("www3.gogoanime.cm")  # Opening Gogoanime

    elif 'open vumo' in query.lower():
        webbrowser.register('firefox',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open_new_tab("vumoo.to")  # Opening Vumoo

    elif 'open songster' in query.lower():
        webbrowser.register('firefox',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open_new_tab("songsterr.com")  # Opening Songsterr

    elif 'open coding' in query.lower():
        webbrowser.register('firefox',
                            None,
                            webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open_new_tab("w3schools.com")  # Opening W3Schools

    elif 'open notion' in query.lower():
        os.startfile("C:\\Users\\saher\\AppData\\Local\\Programs\\Notion\\Notion.exe")  # Opening Notion

    elif 'play music' in query.lower():
        songs = os.listdir("")  # Listing all songs in the directory

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")  # Getting the current time
        speak(f"{MASTER} THE TIME IS {strTime}")  # Speaking the current time

    elif 'open visual studio' in query.lower():
        os.startfile("C:\\Users\\saher\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")  # Opening Visual Studio Code

    elif 'open spotify' in query.lower():
        os.startfile("spotify")  # Opening Spotify

    elif 'open calculator' in query.lower():
        os.startfile("calculator")  # Opening Calculator

    elif 'open mail' in query.lower():
        os.startfile("Mail")  # Opening Mail

main()  # Calling the main function to start the assistant
```
