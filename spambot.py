import pyautogui , time , sys  , os , colorama , requests ,discord , asyncio , subprocess
from pathlib import Path 
from os import system
from discord.ext import commands, tasks 

 
#self bot command prefix
 
CEND      = '\33[0m'
CGREEN2  = '\33[92m'
CBLUE   = '\33[34m'
CRED    = '\33[31m'
CYELLOW = '\33[33m'
 
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
    word = input(CRED + ">>> " + CEND)
    print("How many time do you want to spam ? ")
    x = int(input(CRED + ">>> " + CEND))
 
    fivesectimer()
 
    for i in range(x):
        pyautogui.typewrite(word)
        pyautogui.press("enter")
 
 
def wordlistspam():
    print("Enter the .txt file name (without .txt)")
    filename = input(CRED + ">>> " + CEND)
    filenames = (filename+".txt")
 
    if Path(filenames).exists():
 
        print("Do you wish to start now ? [ Y / N ]")
        yn = input(CRED + ">>> " + CEND)
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
        respond = input(CRED + ">>> " + CEND)
        respond = respond.lower()
 
        if respond == ("y"):
            file = open(filenames ,'w')
            w = input("Please write the wordlist in " + filenames + " and run the program again")
 
            tensectimer()
            exit()
        
        if respond == ("n"):
            c = input("Press enter to close.")
 
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
            r = requests.post(WEBHOOK_URL,data=payload)
            x +=1
            print(WEBHOOK_CONTENT + "have been sent to webhook")
        except:
            print("Spam failed")
            pass
    os.system("cls")
    print("Spam finished")

def self_bot():
    Token = input("DISCORD TOKEN : ")
    os.system("cls")
    request_url = "https://canary.discordapp.com/api/v6/users/@me"
    
    req = requests.get(request_url, headers={'authorization': Token})

    if req.status_code == 401:
        print(f"The token : {Token} is invalid")
        inv = input("press enter to close")
        exit()
    if req.status_code == 200:
        print(f"The token : {Token} is valid")
        
    react = commands.Bot(command_prefix='.r ', self_bot=True)
    react.remove_command("help")

    dot = ['.','..','...','....','.','..','...','....','.','..','...','....','.','..','...','....']

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
            await ctx.message.delete()
            for member in list(ctx.guild.members):
                try:
                    await member.edit(name= rename_to)
                    print(f"{member.name} has been renamed to {rename_to} in server {ctx.guild.name}")
                except:
                    print(f"{member.name} has failed to be renamed to {rename_to} in server {ctx.guild.name}")
                
            print ("Rename complete")

        @commands.check(self_check)
        @react.command(pass_context=True)
        async def ball(ctx):
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
        
def credit():
    print("")
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
    print("                |                 4. Discord self bot                  |")
    print("                |                 5. Credit                            |")
    print("                |                                                      |")
    print("                |                                                      |")
    print("               [*]=--------------------------------------------------=[*]")
    print("")
    spamchoice = input(CRED + ">>> " + CEND)
    
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
        self_bot()
    
    if spamchoice == ("5"):
        os.system("cls")
        credit()

choice()
