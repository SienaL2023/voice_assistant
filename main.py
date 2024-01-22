# voice assistant
# take in voice command
# proceed with the action
# 1. function for a timer
# 2. open music (spotify)
# 3. open google (search)
# 4. open yt
# 5. check palindrome
import winsound
import time
import pygame
import pyttsx3
import pyaudio
import speech_recognition as sr
import webbrowser
import urllib
import os

# initialize pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
    # one for female, zero for male voice
# mini project #1: build a timer



def countdown_timer(t):
    # initialize and load music file
    pygame.mixer.init()
    pygame.mixer.music.load("ring tone.mp3")
    # timer starts here
    while t > 0:
        mins, secs = divmod(t, 60) # divmod divides things by 60
        timer = '{:02d}:{:02d}'.format(mins, secs) # format
        #             5:45
        print(timer)
        time.sleep(1)
        # waits one second to make it be like one second passed
        t -= 1
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(100)
    #     #          Hz    msec
    # winsound.Beep(875, 2000)
# countdown_timer(10)

# mini project #2:
# compare 2 stringers to see if equal
wordA = "house"
wordB = "house"
wordC = "water"
# if wordA == wordB:
#     print(True)
# else:
#     print(False)
# create a program to check if a word is a plaidrome
def check_palindrome(word):
    for x in range(int(len(word)/2)):
        if word[x] == word[(len(word)-1) - x]:
            palindrome = True
            continue
        else:
            palindrome = False
            break
    print(palindrome)
# checkPalindrome("dad")

# Mini project #3
# convert speech to text and return text
def speak(audio):
    # just takes in audio
    engine.say(audio)
    engine.runAndWait()

# speak("Hello world")
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
    # indented bc its like with sr.microphone heres what im gonna do with it
        print("Speak")
        r.pause_threshold = .5
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio)
        print(query)
        return query
        # speak(query)
    except:
        print("error")
        return None
        speak("Error try again")
# speech_to_text()

# mini project #4
# navigate/go to a certain website
def web(website):
    # go to website
    webbrowser.open(website)
# web("youtube.com")

def google_search():
    url = "google.com/search?q="
    speak("Would you like to google search anything, please say yes or no")
    answer = speech_to_text()
    if answer == "yes":
        speak("What would you like to search")
        search = speech_to_text()
        search = search.replace(" ", "+")
        final_url = url + search # og + what u spoke
        webbrowser.open(final_url)
    else:
        webbrowser.open("google.com")


# google_search()

# Mini project #5
# access/open a local application
def open_local_applications(application):
    if application == "Spotify":
        speak("Opening spotify!")
    # loc = location
        loc = "C:/Users/xiaop/AppData/Roaming/Spotify/Spotify.exe"
    elif application == "Zoom":
        speak("Opening zoom!")
        loc = "C:/Users/xiaop/AppData/Roaming/Zoom/bin/Zoom.exe"
    os.startfile(loc)
# open_local_applications("Zoom")

# integration of functions
# 1. listen for "python" and activates listening for commmands
# 2. speak and prompt what the user wants to do
# 3. take in speech command and proceed with execution accordingly

answer = None
def main_code():
    activated = False
    answer = None
    while True:
        while(answer != "python"):
            answer = speech_to_text() # either RETURNS what we said OR none
        if answer == "python":
            activated = True
        if activated == True:
            speak("What do you want to do?")
            action = speech_to_text()
            if action == "countdown timer":
                speak("how long do you want this timer to go for? In seconds")
                seconds = int(speech_to_text())
                countdown_timer(seconds)
            elif action == "check palindrome":
                speak("What is the word you wish to check?")
                input = speech_to_text()
                check_palindrome(input)
            elif action == "open YouTube":
                web("youtube.com")
            elif action == "open Wikipedia":
                web("wikipedia.com")
            elif action == "open Canvas":
                web("sandiegounified.instructure.com")
            elif action == "open Google":
                google_search()
            elif action == "open Spotify":
                open_local_applications("Spotify")
            elif action == "open Zoom":
                open_local_applications("Zoom")
            elif action == "stop":
                activated = False
# main_code()

