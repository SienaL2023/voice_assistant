# voice assistant
# take in voice command
# proceed with the action
# 1. function for a timer
# 2. open music (spotify, Youtube music)
# 3. open google (search)
# 4. open yt
import winsound
import time
import pygame

# mini project #1: build a timer



def countdown_timer(t):
    # initilize and load music file
    pygame.mixer.init()
    pygame.mixer.music.load("ring tone.mp3")
    # timer starts here
    while t > 0:
        mins, secs = divmod(t, 60)
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
# countdown_timer(5)

# mini project #2:
# compare 2 stringers to see if equal
word1 = "racecar"
word2 = "anna"
word3 = "moon"

for x in range(len(word3)):
    if word3[x] == word3[(len(word2)-1) - x]:
        palidrome = True
        continue
    else:
        palidrome = False
        break
print(palidrome)
