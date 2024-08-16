import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import pyautogui
import sys
import random
import requests
import data
import wolframalpha
import pywhatkit
import pyaudio
import psutil
from bs4 import BeautifulSoup
import pywikihow


engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('Your_App_ID') 
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%I:%M %p")
    if hour>=4 and hour<12:
        print(f"Good Morning,Sir!, its {strTime}")
        speak(f"Good Morning,Sir!, its {strTime}")

    elif hour>=12 and hour<16:
        print(f"Good Afternoon,Sir!, its {strTime}")
        speak(f"Good Afternoon,Sir!, its {strTime}")

    elif hour>=16 and hour<20:
        print(f"Good Evening,Sir!, its {strTime}")
        speak(f"Good Evening,Sir!, its {strTime}")
    else:

        print(f"Good Night,Sir!, its {strTime}")
        speak(f"Good Night,Sir!, its {strTime}")
    try:
        search = "weather in surat"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        speak(f"the {search} is {temp}")
        print(f"the {search} is {temp}")
    except Exception as e:
                speak("sorry sir, i can't find the weather")
                pass
    

    
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"Sir, battery at {percentage} percent now")
    print(battery.percent)
    if percentage>=60:
      speak("Sir, we have enought power for our work")

    elif percentage>=40 and percentage<=59:
      speak("Sir, we should connect our system to charging point to charge our battery") 
    elif percentage>30 and percentage<40:
        speak("Sir, we should probably connect our system with charging ")
        
    elif percentage>=20 and percentage<=30:
       speak("Sir, we must connect our system with charging")

    elif percentage<20:
       speak("Sir, we have no more power to run our system so please sir connect system with charging point otherwise the system will be shutdown very soon!")


    print("I am Jarvis Sir. Please tell me how may I help you, Sir?")
    speak("I am Jarvis Sir. Please tell me how may I help you, Sir?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

        if 'jarvis' in query:
            query = query.replace('jarvis', '')
            print(query)


    except Exception as e:
        print("Say that again please...")
        return "none"
    
    return query



def TaskExecution():
    wishMe()
    while True:

        query = takeCommand().lower()

    # logic for executing tasks based on query
        if 'wikipedia' in query:
            print('Searching wikipedia...')
            speak('Searching wikipedia...')
            try:
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            
            except Exception as e:
                speak("sorry sir, i can't found this on wikipedia")
                pass

        elif 'open google' in query:
            print("Sir, what should i search on google..?")
            speak("Sir, what should i search on google ..?")
            search_Term = takeCommand().lower()
            speak("Searching...")
            webbrowser.open('https://www.google.com/search?q='+search_Term)

        elif 'date' in query:
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            date = datetime.datetime.now().day
            speak("Sir, the date is")
            speak(date)
            speak(month)
            speak(year)

        elif 'play' in query:
            song = query.replace('play','')
            speak('Sir!, playing '+ song)
            pywhatkit.playonyt(song)

        elif 'translate' in query:
            stMsgs = ["hey you go,sir", "Sure sir!", "Opening Google translate sir!"]
            speak(random.choice(stMsgs))
            webbrowser.open("https://translate.google.com/?hl=en-GB&tab=rT")
        
        elif 'introduce' in query or 'tell me about' in query:
            speak("Ok, now i am introduce myself. I am a jarvis. A Virtual artificial intelligence, And i am here to assist you, the variety of task that i can, 24 hours a day, 7 days of week. And you know that, I am created by Keval! ")
        
        elif 'what are you doing' in query:
            speak("I am assist you,sir!")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            print(f"Sir,the time is {strTime}")
            speak(f"Sir,the time is {strTime}")

        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com/accounts/onetap/?next=%2F")
            speak("sir!, your profile is open. You should Check it.")
        
        if 'open zoom' in query:
            zoomPath = "C:\\Users\keval\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoomPath)

        elif 'open maths pdf' in query:
            mathsPath = "C:\\Users\\keval\\OneDrive\\Desktop\\Maths"
            os.startfile(mathsPath)
            speak("sure,sir!")

        elif "open command promp" in query:
            os.system("start cmd")
            speak("yes,sir!")

        elif "open notepad" in query:
            os.system("start notepad")
            speak("yes,sir!")

        elif "sleep" in query:
            stMsgs = ["Okay sir!, i am going to sleep you can call me anytime", "As you wish Sir!"]
            speak(random.choice(stMsgs))
            break

        elif "thanks" in query:
            stMsgs = ['No problem sir!','Welcome sir!',"It's my Pleasure Sir!", "It's Jarvis!"]
            speak(random.choice(stMsgs))

        elif "hello" in query or  "hey" in query or "hi" in query:
            stMsgs = ['hello sir.','hi sir.']
            speak(random.choice(stMsgs))

        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing Sir!, and what about you sir?', 'I am fine Sir!, and what about you sir?', "I'm Nice Sir!, and what about you, sir?"]
            speak(random.choice(stMsgs))
        
        elif "also good" in query or "fine" in query:
            stMsgs = ["It's so good, sir!", 'So nice, sir!']
            speak(random.choice(stMsgs))

        elif "good morning" in query:
            print("Good morning,sir!")
            speak("Good morning,sir!")

        elif "good afternoon" in query:
            print("Good Afternoon,sir!")
            speak("Good Afternoon,sir!")
        
        elif "good evening" in query:
            print("Good Evenning,sir!")
            speak("Good Evenning,sir!")

        elif "good night" in query:
            print("Good Night,sir!")
            speak("Good Night,sir!")
        
        elif "cpu" in query or "battery" in query or "laptop" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir, battery at {percentage} percent now")
            print(battery.percent)
            
            if percentage>=70:
                speak("Sir, we have enought power for our work")
            elif percentage>=40 and percentage<=70:
                speak("Sir, we should connect our system to charging point to charge our battery") 

            elif percentage>=20 and percentage<=30:
                speak("Sir, we should probably connect our system with charging")

            elif percentage<20:
                speak("Sir, we have no more power to run our system so please sir connect system with charging point otherwise the system will be shutdown very soon!")
                
        elif 'open youtube' in query:
            speak("what do i search on youtube, sir?")
            search_Term = takeCommand().lower()
            speak("Hey we go sir!")
            webbrowser.open('https://www.youtube.com/results?search_query='+search_Term)

        elif "i am going for sleep" in query:
            print("Good night sir, we will meet tomorrow")
            speak("Good night sir, we will meet tomorrow")

        elif "close notepad" in query:
            speak("Okay sir, closing notepad")
            print("Okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "visual" in query:
             visualPath = "C:\\Users\\keval\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
             os.startfile(visualPath)
             speak("sure,sir!")
            
        elif "hard" in query:
            speak("Sir, I think it's possible for ordinary people to choose to be extraordinary")

        elif "happy" in query:
            speak("Yeah. I know this feeling Sir!")

        elif 'play music' in query or 'play song' in query or "hit some muisc" in query:
            music = 'C:\\Users\\keval\\Music\\Playlists'
            speak("Sure sir")
            songs = os.listdir(music)
            rd = random.choice(songs)
            os.startfile(os.path.join(music, rd))

        elif "hit some music" in query:
            speak("Would you like this, Sir?")
            print("would you like this, Sir?")
            webbrowser.open("https://www.youtube.com/watch?v=pAgnJDJN4VA")

        elif "find my location" in query or "where i am" in query or "location" in query:
            speak("sir, i am checking your location......")
            print("sir i am checking your location......")
            try:
                r = requests.get('https://get.geojs.io/')
                ip_requests = requests.get("https://get.geojs.io/v1/ip.json")
                ipAdd = ip_requests.json()['ip']
                print(ipAdd)

                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                region = geo_data['region']
                country = geo_data['country']
                print(f"sir i'm not sure, but i think we are in {city} city of, {region} region in, {country} country")
                speak((f"sir i'm not sure, but i think we are in {city} city of {region} region in {country} country"))
            except Exception as e:
                speak("sorry sir, Due to network issue i am not able to find where we are")
                pass

        elif "weather" in query or "temperature" in query:
            search = "weather in surat"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"the {search} is {temp}")

        elif "shutdown" in query:
            speak("Sir!, you really want to shutdown the system")
            reply = takeCommand().lower()
            if "yes" in reply or "of course" in reply:
                speak("Good bye sir")
                os.system('shutdown /s /t 1')
                sys.exit()
            else:
                speak("As your wish sir!")

        elif "restart" in query:
            
            speak("Do you really want to shutdown the system")
            reply = takeCommand().lower()
            if "yes" in reply:
                os.system('shutdown /r /t 1')
            else:
                speak("As your wish sir!")

        elif "wait" in query:
          stMsgs = ['Ok sir! I am waiting for you!', 'Sure sir! I am eagerly waiting for you!']
          speak(random.choice(stMsgs))
          break

        elif "take a screenshot"  in query:
            speak("sir, please tell me the name forthis screenshot folder")
            name = takeCommand().lower()
            speak("please sir hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            print("i am done sir, the screenshot is saved in your main folder. Now i am ready for new command")
            speak("i am done sir, the screenshot is saved in your main folder. Now i am ready for new command")

        elif "quit" in query or "bye" in query:
            speak("thanks for using me sir, have a good day!!")
            print("thanks for using me sir, have a good day!!")
            sys.exit()
        
        elif "search" in query or "tell me about" in query:
            speak('Searching....')
            print('Searching....')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('sir i found this...')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Sir, i found this...')
                    speak('WIKIPEDIA says - ')
                    print(results)
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        elif "hear me" in query:
            speak("Yes Sir. Sometimes slow network and other problems i can't hear you!, But now i can hear you sir!")
            print("Yes Sir. Sometimes slow network and other problems i can't hear you!, But now i can hear you sir!")
        
        elif "ok" in query:
            speak("It's Jarvis!")
        
        elif 'wake up' in query:
             stMsgs = ["Sir, i am online and ready!", "I am always here for you, sir!", "Jarvis, At your service sir!", "I'm always Ready,Sir!"]
             speak(random.choice(stMsgs))

        elif "volume up" in query:
            speak("sure,sir!")
            pyautogui.hotkey('volumeup')

        elif "volume down" in query:
            speak("sure")
            pyautogui.hotkey('volumedown')
        
        elif "activate how to do mod"  in query:
            speak("Sir, how to do mod is activated")
            while True:
                speak("Sir, can you tell me what do you want  to know?")
                how = takeCommand()
                try:
                    if "exit" in how or "close" in how:
                        speak(" Okay sir, how to mod is closed")
                        break
                    else:
                        max_results = 1
                        how_to = pywikihow.search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("I am sorry sir, i am not able to find this!")
    
if __name__ == "__main__": 
    while True:
        permission = takeCommand()
        if "wake up" in permission or "online" in permission or "is there" in permission or "you up" in permission:
            stMsgs = ["Sir, i am online and ready!", "I am always here for you, sir!", "You're welcome sir!", "For you Sir,always!", "I'm always Ready,Sir!"]
            speak(random.choice(stMsgs))
            TaskExecution()
        elif "goodbye" in permission:
            speak("thanks for using me sir, have a good day!")
            print("thanks for using me sir, have a good day!")
            sys.exit()