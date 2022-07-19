from os import system



system("cls")
print("Welcome to the stroop test game\nrules are very simple you have to detect of colour in which the colour is printed \ninstead which colour is printed\nyou have 10 chances and you can select your speed mode\nThis is the test of your concentration \nALL THE BEST !!!")
import random
import time
import colorama
colorama.init()
from colorama import Fore

color=["BLACK","BLUE","GREEN","PINK","RED","YELLOW","VIOLET","INDIGO","ORANGE","GREY"]
hub=["BLACK","BLUE","GREEN","PINK","RED","YELLOW","VIOLET","INDIGO","ORANGE","GREY"]



n=int(input("enter your level:"
"\nfor easy press 3 key "
"\nfor moderate press 2 key"
"\nfor hard press 1 key\nentry:"))



for i in range(10):
    choice = random.randint(1, 7)
    X = random.choice(color)
    y = random.choice(hub)
    a=choice
    system("cls")
    if(a==1):
        print(Fore.YELLOW + X)
        time.sleep(n)
    
    elif (a==2):
        print(Fore.BLUE + y)
        time.sleep(n)
        
    elif (a==3):
        print(Fore.GREEN+ X)
        time.sleep(n)
        
    elif (a==4):
        print(Fore.RED+ X)
        time.sleep(n)
        
    elif (a == 5):
        print(Fore.WHITE + y)
        time.sleep(n)
        
    elif(a>7):
        print(Fore.MAGENTA + y)# you can call it as purple 
        time.sleep(n)
        
    else:
        print(Fore.CYAN + X) # you can call it as sky blue 
        time.sleep(n)
        
