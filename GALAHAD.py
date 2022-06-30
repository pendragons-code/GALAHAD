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
    met = input("""
[1]: right click!
[2]: right click and enter!

Tell me my king! What would you like me to do? I shall always be at your behest!: """)
    metter = int (met)
    n = input("Repetitions?: ")
    c = input("Countdown?: ")
    d = input("Delay per click?: ")
    SD = input("Standard Deviation?: ")
    delay = int(d)
    count = int(c)
    reps = int(n)
    STDE = int(SD)
if STDE == 0:
    Deviator = delay
if metter != 2 and metter != 1:
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
        pyautogui.click()
        time.sleep(Deviator)
def clickerEnter():
    for i in range(0, reps):
        pyautogui.click()
        pyautogui.typewrite("\n")
        time.sleep(Deviator)


if metter == 1:
    clicker()
if metter == 2:
    clickerEnter()
