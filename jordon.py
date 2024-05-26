# import Pylance
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import random
import cv2
import pyautogui
import psutil
import pyjokes
import requests
import time
from bs4 import BeautifulSoup as soup
from pynput.keyboard import Key, Controller


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\dawns\\OneDrive\\Pictures\\Screenshots\\ss.png")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at"+usage)
    battery = psutil.sensors_battery()
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_jokes())


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    # speak("I am Jordon your personal assistant. Please tell me how may I help you,Soumyadeep")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('soumyadeepdawn2002@gmail.com', '6291370823')
    server.sendmail('soumyadeepdawn2002@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\dawns\\Music\\Best English 8D Songs collection ever'
            songs = os.listdir(music_dir)
            print(songs)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\dawns\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open notepad' in query:
            notepath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(notepath)

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif 'open wordpad' in query:
            wordpadpath = "C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe"
            os.startfile(wordpadpath)

        elif 'open brave' in query:
            brpath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(brpath)

        elif 'open chrome' in query:
            chpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chpath)

        elif 'open microsft edge' in query:
            msepath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(msepath)

        elif 'open adobe acrobat dc' in query:
            aadpath = "C:\\Program Files (x86)\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
            os.startfile(aadpath)

        elif 'open access' in query:
            apath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\MSACCESS.exe"
            os.startfile(apath)

        elif 'open audacity' in query:
            audpath = "C:\\Program Files\\Audacity\\Audacity.exe"
            os.startfile(audpath)

        elif 'open excel' in query:
            epath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.exe"
            os.startfile(epath)

        elif 'open 1 note' in query:
            o_npath = "C:\\Program Files (x86)\\Microsoft Office\\root\Office16\\ONENOTE.exe"
            os.startfile(o_npath)

        elif 'open outlook' in query:
            opath = "C:\\Program Files (x86)\\Microsoft Office\\root\Office16\\OUTLOOK.exe"
            os.startfile(opath)

        elif 'open powerpoint' in query:
            ppath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.exe"
            os.startfile(ppath)

        elif 'open publisher' in query:
            pupath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\MSPUB.exe"
            os.startfile(pupath)

        elif 'open skype' in query:
            skypath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\lync.exe"
            os.startfile(skypath)

        elif 'open word' in query:
            wpath = "C:\\Program Files (x86)\\Microsoft Office\\root\Office16\\WINWORD.EXE"
            os.startfile(wpath)

        elif 'open unity hub' in query:
            uhpath = "C:\\Program Files\\Unity Hub\\Unity Hub.exe"
            os.startfile(uhpath)

        elif 'open unity' in query:
            upath = "C:\\Program Files\\Unity\\Hub\\Editor\\2020.3.21f1\\Editor\\Unity.exe"
            os.startfile(upath)

        elif 'open bandicam' in query:
            bdpath = "C:\\Program Files\\Bandicam\\bdcam.exe"
            os.startfile(bdpath)

        elif 'open android studio' in query:
            andpath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(andpath)

        elif 'open filmora' in query:
            filpath = "C:\\Program Files\\Wondershare\\Wondershare Filmora\\Wondershare Filmora X.exe"
            os.startfile(filpath)

        elif 'open uniconvertor' in query:
            unipath = "C:\\Program Files\\Wondershare\\UniConverter\\VideoConverterUltimate.exe"
            os.startfile(unipath)

        elif 'open zoom' in query:
            zpath = "C:\\Users\\dawns\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zpath)

        elif 'open wps office' in query:
            wpspath = "C:\\Users\\dawns\\AppData\\Local\\Microsoft\\WindowsApps\\uwp_wpsoffice.exe"
            os.startfile(wpspath)

        elif 'open amd link' in query:
            amdpath = "C:\\Users\\dawns\\AppData\\Local\\Microsoft\\WindowsApps\\amdlinkuwp.exe"
            os.startfile(amdpath)

        elif 'open armoury crate' in query:
            armpath = "C:\\Users\\dawns\\AppData\\Local\\Microsoft\\WindowsApps\\ArmouryCrate.exe"
            os.startfile(armpath)

        elif 'open paint' in query:
            painpath = "C:\\Users\\dawns\\AppData\\Local\\Microsoft\\WindowsApps\\mspaint.exe"
            os.startfile(painpath)

        elif 'open teams' in query:
            teampath = "C:\\Users\\dawns\\AppData\\Local\\Microsoft\\WindowsApps\\msteams.exe"
            os.startfile(teampath)

        elif 'open ss tools' in query:
            snippath = "C:\\Users\\dawns\\AppData\\Local\\Microsoft\\WindowsApps\\SnippingTool.exe"
            os.startfile(snippath)

        elif 'open windows powershell' in query:
            wipath = "C:\\Users\\dawns\\AppData\\Local\\Microsoft\\WindowsApps\\wt.exe"
            os.startfile(wipath)

        elif "remember that" in query:
            speak("what should i remember sir?")
            data = takeCommand()
            speak("you said me to remember that" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'email to seed' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "soumyadepdawn2002@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()
        elif 'go to offline' in query:
            quit()
        elif "log out" in query:
            os.system("shutdown -1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "thank you" in query:
            speak(
                "you are most welcome sir... Should i further help you in any of your work ???")
        elif "weather report" in query:
            speak("Please say me your city sir...")
            weather_city = takeCommand()
            speak("Displaying weather report for "+weather_city)
            url = 'https://wttr.in/{}'.format(weather_city)
            res = requests.get(url)
            print(res.text)
            # speak(res.text)
        elif "today's date" in query:
            today_date = datetime.date.today()
            d = today_date.strftime("%dth%m-%y")
            speak("today's date is "+d)

        elif "news report" in query:
            api_key = "19282c081e074113b43ecbb5dca93793"
            speak("what news do you want national or international news of today???")

            def commandTake():
                # It takes microphone input from the user and returns string output
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    r.pause_threshold = 1
                    audio = r.listen(source, 0, 5)

                try:
                    print("Recognizing...")
                    query = r.recognize_google(audio, language='en-in')
                    print(f"User said: {query}\n")

                except Exception as e:
                    # print(e)
                    print("Say that again please...")
                    return "None"
                return query

            choice = commandTake()
            print(choice)
            try:
                if (choice == 'International'):
                    news_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey="+api_key
                    news = requests.get(news_url).json()
                    article = news['articles']
                    news_article = []
                    speak("today's headlines are.....")
                    # counter=0
                    for arti in article:
                        news_article.append(arti['title'])
                        # counter=counter+1
                        # if counter==3:
                        #     break
                    for i in range(len(news_article)):
                        print(news_article[i])
                        speak(news_article[i])
                elif (choice == 'national'):
                    news_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey="+api_key
                    news = requests.get(news_url).json()
                    article = news['articles']
                    news_article = []
                    speak("today's headlines are.....")
                    for arti in article:
                        news_article.append(arti['title'])
                    for i in range(len(news_article)):
                        print(news_article[i])
                        speak(news_article[i])
                else:
                    speak("please ask for a valid news report sir!")
                    
            finally:
                printCommand="To listen again please tell news report"
                speak(printCommand)
                
        elif "rectangular spiral" in query:
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.write('paint')
            time.sleep(1)
            pyautogui.press('enter')
            pyautogui.moveTo(100, 193, 1)
            pyautogui.rightClick
            pyautogui.moveTo(1181, 122, 1)
            pyautogui.click()
            pyautogui.moveTo(200, 300, 1)
            distance = 500
            while distance > 0:
                pyautogui.dragRel(distance, 0, 0.1, button="left")
                distance = distance - 10
                pyautogui.dragRel(0, distance, 0.1, button="left")
                pyautogui.dragRel(-distance, 0, 0.1, button="left")
                distance = distance - 10
                pyautogui.dragRel(0, -distance, 0.1, button="left")
        elif "minimise the current window" in query:
            press_key = Controller()
            time.sleep(1)
            with press_key.pressed(Key.alt):
                with press_key.pressed(Key.space):
                    press_key.press('n')
        elif "maximize the current window" in query:
            press_key = Controller()
            time.sleep(1)
            with press_key.pressed(Key.alt):
                with press_key.pressed(Key.space):
                    press_key.press('x')
        elif "reopen the current window" in query:
            press_key = Controller()
            time.sleep(1)
            with press_key.pressed(Key.alt):
                press_key.pressed(Key.tab)
        elif "close the current window" in query:
            press_key = Controller()
            time.sleep(1)
            with press_key.pressed(Key.alt):
                press_key.pressed(Key.tab)
        elif "create a file" in query:
            speak("tell me the file name: ")
            filePath="C://Users//dawns//Downloads"
            fileName=takeCommand()
            with open(f"{filePath}//{fileName}",'w') as fp:
                pass