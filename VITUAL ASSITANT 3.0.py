
from traceback import print_list
import pyttsx3 
import speech_recognition as sr  
import datetime
import wikipedia  
import webbrowser

import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! surjeet")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! surjeet")

    else:
        speak("Good Evening!sutjeet")

    speak(" how are bro. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('surjeetroy016@gmail.com', 'Kum@r123$')
    server.sendmail('mukeshpajiyar999@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        #  if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'rajat' in query:
            speak('Searching Wikipedia...')
            url='https://en.wikipedia.org/wiki/'
            query = query.replace("rajat", "")
            search_url=url+query
            webbrowser.open(search_url)
            # results = wikipedia.summary(query, sentences=2)
            # speak("According to Wikipedia")
            # print(results)
            # speak(results)


        if 'satnam' in query:
            url='https://www.google.co.in/search?q='
            query= query.replace("satnam","")
            search_url=url+query
            webbrowser.open(search_url)
        # except:
        #     print("can't recognise")   
        if 'yadveer' in query:
            url='https://www.youtube.com/results?search_query='
            query= query.replace("yadveer","")
            search_url=url+query
            webbrowser.open(search_url)
           
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            #  music_dir = 'music.youtube.com'
            music_dir = 'D:\playsound'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\Downloads"
            os.startfile(codePath)

        elif 'email to mukesh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "surjeetroy016@gmail.com "
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry ! I am not able to send this email")
