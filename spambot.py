from colorama import Fore, init, Back, Style
init()

import pyautogui , time , sys  , os , colorama , requests ,discord , asyncio , subprocess ,smtplib ,getpass

from pathlib import Path 
from os import system
from discord.ext import commands, tasks 

#self bot command prefix
colorama.init()
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

def checkinternetconnection():
    respond = True
    try:
        requests.get('https://www.google.com', verify=True)
        respond = True
    except Exception:
        respond = False
    
    if respond == True:
        print(Fore.GREEN + "Internet connection is good" + Fore.RESET)

    if respond == False:
        print(Fore.RED + "Internet connection is bad" + Fore.RESET)

def normalspam():
 
    print("What do you want to spam ? ")
    word = input(Fore.RED + ">>> " + Fore.RESET)
    print("How many time do you want to spam ? ")
    x = int(input(Fore.RED + ">>> " + Fore.RESET))
 
    fivesectimer()
 
    for i in range(x):
        pyautogui.typewrite(word)
        pyautogui.press("enter")
    
    print("Finished spamming")

    conti = input("Do you want to continue ? [ Y / N ] ").lower()

    if conti == ("y"):
        print("restarting...")
        choice()

    elif conti == ("n"):
        tensectimer()
        exit()
    
    else:
        input("Invalid choice press enter to close")
 
 
def wordlistspam():
    print("Enter the .txt file name (without .txt)")
    filename = input(Fore.RED + ">>> " + Fore.RESET)
    filenames = (filename+".txt")
 
    if Path(filenames).exists():
 
        print("Do you wish to start now ? [ Y / N ]")
        yn = input(Fore.RED + ">>> " + Fore.RESET)
        yn = yn.lower()
 
        if yn == ("y"):
            fivesectimer()
 
            f = open(filenames, 'r')
            for i in f:
                pyautogui.typewrite(i)
                pyautogui.press("enter")
 
            input("The task is finish press enter to close")
 
        if yn == ("n"):
            tensectimer()
            exit()
        
        else:
            input("invalid choice press enter to close")
    
    conti = input("Do you want to continue ? [ Y / N ] ").lower()

    if conti == ("y"):
        print("restarting...")
        choice()

    elif conti == ("n"):
        tensectimer()
        exit()
    
    else:
        input("Invalid choice press enter to close")
    
    if not Path(filenames).exists():
        print(filenames + ".txt do not exist do you want to create new .txt with that name ? [ Y / N ]")
        respond = input(Fore.RED + ">>> " + Fore.RESET)
        respond = respond.lower()
 
        if respond == ("y"):
            open(filenames ,'w')
            input("Please write the wordlist in " + filenames + " and run the program again")
 
            tensectimer()
            exit()
        
        if respond == ("n"):
            input("Press enter to close.")
    
    conti = input("Do you want to continue ? [ Y / N ] ").lower()

    if conti == ("y"):
        print("restarting...")
        choice()

    elif conti == ("n"):
        tensectimer()
        exit()
    
    else:
        input("Invalid choice press enter to close")
        
def discordwebhookspam():
    n = 0
    WEBHOOK_URL = str(input("Webhook URL : "))
    WEBHOOK_USERNAME = str(input("Name : "))
    WEBHOOK_AVATAR = str(input("Avatarurl : "))
    WEBHOOK_CONTENT = str(input("What to spam : "))
    SPAM = int(input("How many time to spam : "))
    
    while n < SPAM:
        try:
            payload = {"content":WEBHOOK_CONTENT,"username":WEBHOOK_USERNAME,"avatar_url":WEBHOOK_AVATAR}
            requests.post(WEBHOOK_URL,data=payload)
            n +=1
            print(WEBHOOK_CONTENT + "have been sent to webhook")
        except:
            print("Spam failed")
            pass
    os.system("cls")
    print("Spam finished")

    conti = input("Do you want to continue ? [ Y / N ] ").lower()

    if conti == ("y"):
        print("restarting...")
        choice()

    elif conti == ("n"):
        tensectimer()
        exit()
    
    else:
        input("Invalid choice press enter to close")

def self_bot():
    Token = input("DISCORD TOKEN : ")
    os.system("cls")
    request_url = "https://canary.discordapp.com/api/v6/users/@me"
    
    req = requests.get(request_url, headers={'authorization': Token})

    if req.status_code == 401:
        print(f"The token : {Token} is invalid")
        input("press enter to close")
        exit()
    if req.status_code == 200:
        print(f"The token : {Token} is valid")
    
    checkinternetconnection()
    react = commands.Bot(command_prefix='.r ', self_bot=True)
    react.remove_command("help")

    dot = ['.','..','...','....','.','..','...','....','.','..','...','....','.','..','...','....','.','..','...','....']

    print("status : offline")
    for i in dot:
        sys.stdout.write("\r\x1b[K" + "starting " +i)
        sys.stdout.flush()
        time.sleep(1)
    print('\n')

    @react.event
    async def on_ready():
        os.system("cls")
        print('status : online')
        print("Type .r dmall [message] : Messages every user in that server")
        print("Type .r rnall : Rename every user in that server")
        print("Type .r kall : Kick every user in that server")
        print("Type .r ball : Messages every user in that server")

    try:
        async def self_check(ctx):
            if react.user.id == ctx.message.author.id:
                return True
            else:
                return False

        @commands.check(self_check)
        @react.command(name="dmall")
        async def dmall(ctx, message):
            os.system("cls")
            await ctx.message.delete()
            for member in ctx.guild.members:
                try:
                    await member.create_dm()
                    await member.dm_channel.send(message)
                    print("Message has been sent to "+ member.name)
                except:
                    print("Message failed to sent to "+ member.name)
            
        @commands.check(self_check)
        @react.command(pass_context=True)
        async def rnall(ctx, rename_to):
            os.system("cls")
            await ctx.message.delete()
            for member in list(ctx.guild.members):
                try:
                    await member.edit(name= rename_to)
                    print(f"{member.name} has been renamed to {rename_to} in server {ctx.guild.name}")
                except:
                    print(f"{member.name} has failed to be renamed to {rename_to} in server {ctx.guild.name}")
                
            print("Rename complete")


        @commands.check(self_check)
        @react.command(pass_context=True)
        async def ball(ctx):
            os.system("cls")
            await ctx.message.delete()
            for member in list(ctx.guild.members):
                try:
                    await ctx.guild.ban(member)
                    print (f"{member.name} has been banned from {ctx.guild.name}")
                except:
                    print (f"{member.name} has failed to be banned from {ctx.guild.name}")

            print ("Ban all complete")  

    except:
        pass

        react.run(Token, bot=False, reconnect=True)

def Emailspam():
    print("Choose your email provider")
    print("1. Gmail")
    print("2. Outlook")
    print("3. Yahoo")
    provider = input(Fore.RED + ">>> " + Fore.RESET)
    os.system("cls")
    
    if provider == ("1"):
        smtp_server = 'smtp.gmail.com'
        port = 587
    
    elif provider == ("2"):
        smtp_server = 'smtp.office365.com'
        port = 587
    
    elif provider == ("3"):
        smtp_server = 'smtp.mail.yahoo.com'
        port = 25
    
    else:
        print("Invalid choice")
        input("press enter to close")
        exit()
    checkinternetconnection()
    if Path("accountinfo.txt").exists():
        f = open("accountinfo.txt")
        lines = f.readlines()
        useremail = lines[0]
        userpass = lines[1]
        victimemail = input("Victim email : ")
        Content = input('Message : ')
        Number = int(input("Number of mail to send : "))
        os.system("cls")
        try:
            server = smtplib.SMTP(smtp_server,port)
            server.connect(smtp_server,port)
            server.ehlo()
            server.starttls()
            server.login(useremail,userpass)

            for i in range(0,Number):
                print("Number of Message Sent to " + victimemail + ":" , i+1)
                server.sendmail(useremail,victimemail,Content)
                time.sleep(1)

            print("Finished")
            server.close()

        except Exception as e:
            print(e)
            input("Press enter to close")
            exit()

    if not Path("accountinfo.txt").exists():
        useremail = input("EMAIL : ")
        userpass = input("PASSWORD : ")
        os.system("cls")
        save = input("Do you want to save the email and password ? [ Y / N ] ").lower()

        if save==("y"):
            with open("accountinfo.txt", "w") as writeinfo:
                writeinfo.writelines(
                    [useremail+'\n',
                     userpass +'\n']
                )
            
            print("Data have been save")
        
        elif save == ("n"):
            print("Data have not been save")

        else:
            input("invalid answer")
            exit()

        victimemail = input("Victim email : ")
        Content = input('Message : ')
        Number = int(input("Number of mail to send : "))
        os.system("cls")
        try:
            server = smtplib.SMTP(smtp_server,port)
            server.connect(smtp_server,port)
            server.ehlo()
            server.starttls()
            server.login(useremail,userpass)

            for i in range(0,Number):
                print("Number of Message Sent to " + victimemail + ":" , i+1)
                server.sendmail(useremail,victimemail,Content)
                time.sleep(1)

            print("Finished")
            server.close()

        except Exception as e:
            print(e)
            input("Press enter to close")
            exit()
    conti = input("Do you want to continue ? [ Y / N ] ").lower()

    if conti == ("y"):
        print("restarting...")
        choice()

    elif conti == ("n"):
        tensectimer()
        exit()
    
    else:
        input("Invalid choice press enter to close")

def credit():
    print("")
    print(Fore.BLUE +"                             [*]=----------------------------------------------------------------------------------=[*]" + Fore.RESET)
    print(Fore.BLUE +"                              |                                                                                      |")
    print(Fore.BLUE +"                              |" + Fore.RESET +"                Discord : REACT#1120" + Fore.BLUE + "                                                  |")                     
    print(Fore.BLUE +"                              |" + Fore.RESET +"                Github : https://github.com/reactxsw" + Fore.BLUE + "                                  |")
    print(Fore.BLUE +"                              |" + Fore.RESET +"                steam : https://steamcommunity.com/id/reactswthegod/" + Fore.BLUE + "                  |")
    print(Fore.BLUE +"                              |" + Fore.RESET +"                Youtube : https://www.youtube.com/ANAPAH555" + Fore.BLUE + "                           |")
    print(Fore.BLUE +"                              |                                                                                      |")
    print(Fore.BLUE +"                              |" + Fore.RESET +"                Discord server invite link :" + Fore.BLUE + "                                          |")
    print(Fore.BLUE +"                              |" + Fore.RESET +"               https://discord.com/invite/R8RYXyB4Cg" + Fore.BLUE + "                                  |")
    print(Fore.BLUE +"                              |                                                                                      |")
    print(Fore.BLUE +"                             [*]=----------------------------------------------------------------------------------=[*]")
    print("")
    input("")
 
def choice():
    os.system("cls")
    print()
    print(Fore.BLUE + "                            [*]=--------------------------------------------------=[*]"+ Fore.RESET)
    print(Fore.BLUE + "                             |                                                      |"+ Fore.RESET)
    print(Fore.BLUE + "                             |" + Fore.RESET +" 1. Normal spambot" + Fore.BLUE + "                                    |"+ Fore.RESET)                     
    print(Fore.BLUE + "                             |" + Fore.RESET +" 2. Wordlist spambot" + Fore.BLUE + "                                  |"+ Fore.RESET)
    print(Fore.BLUE + "                             |" + Fore.RESET +" 3. Discord webhook spam" + Fore.BLUE + "                              |"+ Fore.RESET)
    print(Fore.BLUE + "                             |" + Fore.RESET +" 4. Discord self bot" + Fore.BLUE + "                                  |"+ Fore.RESET)
    print(Fore.BLUE + "                             |" + Fore.RESET +" 5. Email spam" + Fore.BLUE + "                                        |"+ Fore.RESET)
    print(Fore.BLUE + "                             |" + Fore.RESET +" 6. credits" + Fore.BLUE + "                                           |"+ Fore.RESET)
    print(Fore.BLUE + "                             |                                                      |"+ Fore.RESET)
    print(Fore.BLUE + "                             |" + Fore.RESET +" 7. close" + Fore.BLUE + "                                             |"+ Fore.RESET)
    print(Fore.BLUE + "                            [*]=--------------------------------------------------=[*]"+ Fore.RESET)
    print("")
    spamchoice = input(Fore.RED + ">>> " + Fore.RESET)
    
    if spamchoice == ("1"):
        os.system("cls")
        normalspam()
           
    elif spamchoice == ("2"):
        os.system("cls")
        wordlistspam()
    
    elif spamchoice == ("3"):
        os.system("cls")
        discordwebhookspam()

    elif spamchoice == ("4"):
        os.system("cls")
        self_bot()
    
    elif spamchoice == ("5"):
        os.system("cls")
        Emailspam()

    elif spamchoice == ("6"):
        os.system("cls")
        credit()

    elif spamchoice == ("7"):
        os.system("cls")
        print("Why do you even run it ? ")
        input("")
        exit()

    else:
        os.system("cls")
        input("Invalid choice press enter to close")
        exit()
        

choice()
