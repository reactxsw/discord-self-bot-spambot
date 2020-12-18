import pyautogui , time , sys 
from pathlib import Path

def normalspam():

    print("What do you want to spam ? ")
    word = input(">>> ")
    print("How many time do you want to spam ? ")
    x = int(input(">>> "))

    num = ['5',
    '4',
    '3',
    '2',
    '1']
    
    for i in num:
        sys.stdout.write("\r\x1b[K" + "starting in " + i + " second")
        sys.stdout.flush()
        time.sleep(1)

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
            num = ['5',
                '4',
                '3',
                '2',
                '1']
    
            for i in num:
                sys.stdout.write("\r\x1b[K" + "starting in " + i + " second")
                sys.stdout.flush()
                time.sleep(1)

            f = open(filenames, 'r')
            for i in f:
                pyautogui.typewrite(i)
                pyautogui.press("enter")

            fin = input("The task is finish press enter to close")
            exit()

        if yn == ("n"):
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
            
            exit()
        
        if respond == ("n"):
            c = input("Press enter to close.")


def choice():
    print("               [*]=--------------------------------------------------=[*]")
    print("                |                                                      |")
    print("                |                 1. normal spambot                    |")                     
    print("                |                 2. wordlist spambot                  |")
    print("                |                                                      |")
    print("               [*]=--------------------------------------------------=[*]")
    print("")
    spamchoice = input(">>> ")
    
    if spamchoice == ("1"):
        normalspam()

    else:
        wordlistspam()



choice()

    


