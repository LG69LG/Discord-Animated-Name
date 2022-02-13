import webbrowser
import requests
import time
from colorama import Fore, Back, Style
import os

clear = lambda: os.system('cls')
color4 = lambda: os.system('color 4')
color4()

print('Im not resposible for getting banned because of API abuse!')
print('Im not resposible for getting banned because of API abuse!')
print('Im not resposible for getting banned because of API abuse!')
time.sleep(5)
print("Opening Discord...")
time.sleep(5)
webbrowser.open('https://discord.com/login', new=2)

color5 = lambda: os.system('color 5')
color5()

ServerID = input("please provide a server ID... If you dont know how, say help ")
if ServerID == "help":
	webbrowser.open('https://www.alphr.com/discord-find-server-id/', new=2)
	
Token = input("please provide your Discord Token... If you dont know how, say help ")
if Token == "help":
	webbrowser.open('https://www.youtube.com/watch?v=YEgFvgg7ZPI', new=2)


url = f"https://discord.com/api/v9/guilds/{ServerID}/members/@me"


print("!quit to get out of the names")
names = []
index = 0
while True:
    index += 1;
    if index == 1:
        names.append(input("Name " + str(index) + ":"))
    else:
        i = input("Name " + str(index) + ":")
        if i == "!quit":
            break
        names.append(i)

headers = {
	    "Content-Type": "application/json",
	    "authorization": f"{Token}",
	    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36"
	    }

print("Press Ctrl + C to quit.")
time.sleep(1)
clear()
print("Press Ctrl + C to quit..")
time.sleep(1)
clear()
print("Press Ctrl + C to quit...")
time.sleep(1)
clear()


while True:
	for name in names:
		payload = {"nick": name}
		requests.request("PATCH", url, json=payload, headers=headers)
		time.sleep(3)
		break



