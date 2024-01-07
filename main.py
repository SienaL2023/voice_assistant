# voice assistant
# take in voice command
# proceed with the action
# 1. function for a timer
# 2. open music (spotify, Youtube music)
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
    engine.say(audio)
    engine.runAndWait()

# speak("Hello world")
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
    # indented bc its like with sr.microphone heres what im gonna do with it
        print("Speak")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio)
        print(query)
    except:
        print("error")
        speak("Error try again")
# speech_to_text()

# mini project #4
# navigate/go to a certain website
def web(website):
    # go to website
    webbrowser.open(website)
web("google.com")
