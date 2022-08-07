import time
import math
import pyautogui
import json
import random
pyautogui.FAILSAFE = False

jsoner = input("""
[1]: Import configuration via json file!
[2]: Manually set config via command line entry!

Please select an input method!: """)
if jsoner != "1" and jsoner != "2":
    print("Invalid input selected")
    print("Exiting")
    exit()
if jsoner == "1":
    file = open("config.json")
    config = json.load(file)
    metter = config["metter"]
    reps = config["reps"]
    STDE = config["STDE"]
    delay = config["delay"]
    count = config["count"]
if jsoner == "2":
    metter = int(input("""
[1]: Left click!
[2]: Left click and enter!
[3]: Right click!
[4]: Right click and enter!
[5]: Holding the Left click button down for a specified duration!
[6]: Holding the Right click button down for a specified duration!


Tell me my king! What would you like me to do? I shall always be at your behest!: """))
    reps = int(input("Repetitions?: "))
    count = int(input("Countdown?: "))
    delay = int(input("Delay per click?: "))
    SRDE = int(input("Standard Deviation?: "))
    if metter > 4:
        dur = int(input("How long would you like each click to hold down for?"))
if STDE == 0:
    Deviator = delay
if metter > 6 and metter < 1 or count < 1:
    print("Invalid choice, aborting!")
    exit()
if STDE > 0:
    Deviator = random.randomint(delay - STDE, delay + STDE)
while(count != 0):
    print(count)
    time.sleep(1)
    count -= 1

print("""
  ________    _____  .____       _____    ___ ___    _____  ________   
 /  _____/   /  _  \ |    |     /  _  \  /   |   \  /  _  \ \______ \  
/   \  ___  /  /_\  \|    |    /  /_\  \/    ~    \/  /_\  \ |    |  \ 
\    \_\  \/    |    \    |___/    |    \    Y    /    |    \|    `   \ 
 \______  /\____|__  /_______ \____|__  /\___|_  /\____|__  /_______  /
        \/         \/        \/       \/       \/         \/        \/ 

        """)
def clicker():
    for i in range(0, reps):
        pyautogui.click(button='left', clicks=reps, interval=Deviator)
def clickerEnter():
    for i in range(0, reps):
        pyautogui.click()
        pyautogui.typewrite("\n")
        time.sleep(Deviator)
def clickright():
    for i in range(0, reps):
        pyautogui.click(button='right'. clicks=reps, interval=Deviator)
def clickrightenter():
    for i in range(0, reps):
        pyautogui.click(button='right')
        pyautogui.typewrite("\n")
        time.sleep(Deviator)
def Holddownleft():
    for i in range(0, reps):
        pyautogui.mouseDown(button='left')
        time.sleep(dur)
        pyautogui.mouseUp(button='left')
        time.sleep(Deviator)
def Holddownright():
    for i in range(0, reps):
        pyautogui.mouseDown(button='right')
        time.sleep(dur)
        pyautogui.mouseUp(button='right')
        time.sleep(Deviator)

#filter
if metter == 1:
    clicker()
if metter == 2:
    clickerEnter()
if metter == 3:
    clickright()
if metter == 4:
    clickrightenter()
if metter == 5:
    Holddownleft()
if metter == 6:
    Holddownright()
