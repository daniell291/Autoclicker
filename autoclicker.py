#Importing libraries
import pyautogui as pg
import time
import keyboard as kb

#Setting defaults
on = False
key = "F8"
pg.PAUSE = 0.01

print(f"Press {key} to Start/Stop the autoclicker")

#Main program loop
while True:
    #This loop runs while the autoclicker is activated
    while on:
        pg.click()
        #Check if the toggle key is pressed
        if kb.is_pressed(key):
            print("Deactivated")
            on = False
            #Wait until the key is released
            while kb.is_pressed(key):
                time.sleep(0.1)
    #Check if the toggle key is pressed to activate
    if kb.is_pressed(key):
        print("Activated")
        on = True
        #Wait until the key is released
        while kb.is_pressed(key):
            time.sleep(0.1)
    time.sleep(0.1)
#Created by Daniell291 2026.