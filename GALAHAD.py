import time
import math
import pyautogui
import json
import random
pyautogui.FAILSAFE = False

jsoner = input("""
[1]: Import autoclicker configuration via json file!
[2]: Manually set autoclicker config via command line entry!
[3]: Manual entry of configuring minecraft miner!

Please select an input method!: """)
ACCEPTABLE = ["1", "2", "3", "4"]
if jsoner not in ACCEPTABLE:
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



if jsoner == "3":
    pick = input("""
[1]: wooden
[2]: stone
[3]: gold
[4]: iron
[5]: diamond
[6]: netherite
            
[Warning] The presets are assuming that you have yet to enchant your pickaxe!

Please select a pickaxe type!: """)
    lavaflow = 1.6
    amot = input("""
[Warning] make sure that the pickaxes you have in your hotbar are the same. (Meaning the pickaxes in you hotbar must be of the same type.)
[Warning 2] make sure that he hotbar elector is at the first one!
Amount of pickaxes in your hotbar?: """)
    #yes i am aware that it is in fact 1.5 seconds but it takes another 0.1 second for the stone to form.
    amt = int(amot)
    if amt > 9 or amt < 1:
        print("Invalid choice")
        exit()

    if pick == "1":
        durability = 60
        durator = 1.15
    if pick == "2":
        durability = 131
        durator = 0.75
    if pick == "3":
        durator = 0.25
        durability = 32
    if pick == "4":
        durability = 250
        durator = 0.4
    if pick == "5":
        durability = 1561
        durator = 0.3
    if pick == "6":
        durator = 0.35
        durability = 2031

    def miner(durability, durator, lavaflow, amt):
        for i in range(0, amt):
            for i in range(0, durability):
                time.sleep(lavaflow)
                pyautogui.mouseDown()
                time.sleep(durator)
                pyautogui.mouseUp()
            pyautogui.scroll(-1)
    miner(durability, durator, lavaflow, amt)






if jsoner != "3":



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
            pyautogui.click(button='left', clicks=reps, interval=Deviator)
    def clickerEnter():
        for i in range(0, reps):
            pyautogui.click()
            pyautogui.typewrite("\n")
            time.sleep(Deviator)


    if metter == 1:
        clicker()
    if metter == 2:
        clickerEnter()
