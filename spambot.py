import pyautogui , time , sys  , os
from pathlib import Path
  
import requests
from os import system


def fivesectimer():
    num = ['5',
           '4',
           '3',
           '2',
           '1']
    
    for i in num:
        sys.stdout.write("\r\x1b[K" + "starting in " + i + " second")
        sys.stdout.flush()
        time.sleep(1)

    os.system("cls")

def tensectimer():
    num = ['10',
            '9',
            '8',
            '7',
            '6',
            '5',
            '4',
            '3',
            '2',
            '1']
    
    for i in num:
        sys.stdout.write("\r\x1b[K" + "Program is closing in " + i + " second")
        sys.stdout.flush()
        time.sleep(1)
    
    os.system("cls")

def normalspam():

    print("What do you want to spam ? ")
    word = input(">>> ")
    print("How many time do you want to spam ? ")
    x = int(input(">>> "))

    fivesectimer()

    for i in range(x):
        pyautogui.typewrite(word)
        pyautogui.press("enter")


def wordlistspam():
    print("Enter the .txt file name (without .txt)")
    filename = input(">>> ")
    filenames = (filename+".txt")

    if Path(filenames).exists():

        print("Do you wish to start now ? [ Y / N ]")
        yn = input(">>> ")
        yn = yn.lower()

        if yn == ("y"):
            fivesectimer()

            f = open(filenames, 'r')
            for i in f:
                pyautogui.typewrite(i)
                pyautogui.press("enter")

            fin = input("The task is finish press enter to close")
            exit()

        if yn == ("n"):
            tensectimer()
            exit()
        
        else:
            v = input("invalid choice press enter to close")


    
    if not Path(filenames).exists():
        print(filenames + ".txt do not exist do you want to create new .txt with that name ? [ Y / N ]")
        respond = input(">>> ")
        respond = respond.lower()

        if respond == ("y"):
            file = open(filenames ,'w')
            w = input("Please write the wordlist in " + filenames + " and run the program again")

            tensectimer()
            exit()
        
        if respond == ("n"):
            c = input("Press enter to close.")

def discordwebhookspam():
    x = 0
    WEBHOOK_URL = str(input("Webhook URL : "))
    WEBHOOK_USERNAME = str(input("Name : "))
    WEBHOOK_AVATAR = str(input("Avatarurl : "))
    WEBHOOK_CONTENT = str(input("What to spam : "))
    SPAM = int(input("How many time to spam : "))
    while x < SPAM:
        try:
            payload = {"content":WEBHOOK_CONTENT,"username":WEBHOOK_USERNAME,"avatar_url":WEBHOOK_AVATAR}
            r = requests.post(WEBHOOK_URL,data=payload)
            x +=1
            print(WEBHOOK_CONTENT + "have been sent to webhook")
        except:
            print("Spam failed")
            pass
    os.system("cls")
    print("Spam finished")

def credit():
    print("               [*]=----------------------------------------------------------------------------------=[*]")
    print("                |                                                                                      |")
    print("                |                 Discord : REACT#1120                                                 |")                     
    print("                |                 Github : https://github.com/reactxsw                                 |")
    print("                |                 steam : https://steamcommunity.com/id/reactswthegod/                 |")
    print("                |                                                                                      |")
    print("                |                 Discord server invite link :                                         |")
    print("                |                 https://discord.com/invite/R8RYXyB4Cg                                |")
    print("                |                                                                                      |")
    print("               [*]=----------------------------------------------------------------------------------=[*]")
    print("")
    ic = input("")

def choice():
    print("               [*]=--------------------------------------------------=[*]")
    print("                |                                                      |")
    print("                |                 1. Normal spambot                    |")                     
    print("                |                 2. Wordlist spambot                  |")
    print("                |                 3. Discord webhook spam              |")
    print("                |                 4. credits                           |")
    print("                |                                                      |")
    print("               [*]=--------------------------------------------------=[*]")
    print("")
    spamchoice = input(">>> ")
    
    if spamchoice == ("1"):
        os.system("cls")
        normalspam()

    if spamchoice == ("2"):
        os.system("cls")
        wordlistspam()
    
    if spamchoice == ("3"):
        os.system("cls")
        discordwebhookspam()
    
    if spamchoice == ("4"):
        os.system("cls")
        credit()

    else:
        ic = input("Invalid choice press enter to close")



choice()

    


