import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecogniion
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib
import subprocess

fire_fox = 'C:\Program Files\Mozilla Firefox\firefox.exe'
webbrowser.register('firefox' , None)
print("Initializing Jarvis")
MASTER = "Sir"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# speak function will speak the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()
    

#this function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    

    if hour >= 0 and hour < 12: 
        speak("Good Morning" + MASTER)

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    speak(" How may i help you ......")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)
    
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language = 'en-GB')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Please say that again" + MASTER)
        query = None
    return query

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'password')
    server.sendmail

def main():
# will take command from the microphone
    speak("Initializing jarvis....")
    wishMe()
    query=takeCommand()
    

# logic for executing tasks per query , coding the logic here
    if 'wikipedia' in query.lower(): 
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences =2)
        print(results)
        speak (results) 

    elif 'open youtube' in query.lower():
        webbrowser.register('firefox',
	    None,
	    webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open_new_tab("youtube.com") 

    elif 'open facebook' in query.lower(): #needs work
    
        url = "facebook.com"
        webbrowser.open( url) 

    elif 'open anime' in query.lower():
        webbrowser.register('firefox',
	    None,
	    webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open_new_tab("www3.gogoanime.cm") 

    elif 'open vumo' in query.lower():
        webbrowser.register('firefox',
	    None,
	    webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open_new_tab("vumoo.to")

    elif 'open songster' in query.lower():
        webbrowser.register('firefox',
	None,
	webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open_new_tab("songsterr.com")

    elif 'open coding' in query.lower():
        webbrowser.register('firefox',
	    None,
	    webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open_new_tab("w3schools.com")

    elif 'open notion' in query.lower():
        os.startfile("C:\\Users\\saher\\AppData\\Local\\Programs\\Notion\\Notion.exe")
 

    elif ' play music' in query.lower():
        songs = os.listdir("")

    elif ' the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} THE TIME IS {strTime}")
   
    elif 'open visual studio' in query.lower():
   
        os.startfile("C:\\Users\\saher\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif 'open spotify' in query.lower():
        os.startfile("spotify")

    elif 'open calculator' in query.lower():
        os.startfile("calculator")

    elif 'open mail' in query.lower():
        os.startfile("Mail")

main()
