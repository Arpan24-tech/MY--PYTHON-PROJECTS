#Rock Paper & Scissors

import random
from colorama import Fore
import time 
print(Fore.BLUE+"ROCK PAPER SCISSORS")
print('\n')
time.sleep(1)
name=input(Fore.GREEN+"Enter your Name: ")
print('\n')
time.sleep(2)
print("Welcome "+name+" to the Rock Paper Scissors Game!")
print('\n')
time.sleep(1)
print("Loading...")
print('\n')
time.sleep(3)
print(Fore.RED+"INSTRUCTIONS:\n(i)BETWEEN ROCK AND PAPER->PAPER WINS\n(ii)BETWEEN ROCK AND SCISSORS->ROCK WINS\n(iii)BETWEEN SCISSORS AND PAPER->SCISSORS WINS\nMinimum 5 ROUNDS WILL BE PLAYED.")
print('\n')
print('\n')
time.sleep(4)
print(Fore.YELLOW+"Let's Begin the game :)")
time.sleep(1)
print('\n')
plays=1
__user__score=0
__computer__score=0
count=0
while(plays<=5):
    
    __user__choice=input(Fore.BLUE+"Enter your weapon:").lower()
    time.sleep(1)

    __computer__choice=random.randint(1,3)

    if(__computer__choice==1):__computer__choice="paper"
    elif(__computer__choice==2):__computer__choice="scissors"
    elif(__computer__choice==3):__computer__choice="rock"

    if __user__choice in ["rock","paper","scissors"]:pass
    else:
        while(__user__choice not in ["rock","paper","scissors"]):
            print(Fore.RED+"Enter a correct weapon")
            time.sleep(1)
            __user__choice=input(Fore.BLUE+"Enter your weapon:").lower()
            time.sleep(1)

    winner=""
    
    if(__computer__choice=="rock" and __user__choice=="scissors" or __computer__choice=="paper" and __user__choice=="rock" or __computer__choice=="scissors" and __user__choice=="paper"):
        winner="Computer"
        __computer__score+=1  
    elif(__computer__choice==__user__choice):winner="Draw"  
    else: 
        __user__score+=1
        winner=name
    print(Fore.CYAN+f"You choose {__user__choice} and computer choose {__computer__choice}.\nWinner->{winner} ")
    time.sleep(1)
    print(Fore.CYAN+f"{name} Score={__user__score}          Computer Score={__computer__score}")
    time.sleep(1)
    plays+=1
    count+=1
print(Fore.MAGENTA+f"You have played {count} times.\n")
time.sleep(1)
__user__wish=input(Fore.RED+"Do you want to play more?(Y/N)").lower()
time.sleep(1)
while(__user__wish!="y" and __user__wish!="n"):
    print("Enter (Y/N)")
    time.sleep(1)
    __user__wish=input(Fore.RED+"Do you want to play more?(Y/N)").lower()
    time.sleep(1)
while(__user__wish=="y"):
    __user__choice=input(Fore.BLUE+"Enter your weapon:").lower()
    time.sleep(1)
    __computer__choice=random.randint(1,3)

    if(__computer__choice==1):__computer__choice="paper"
    elif(__computer__choice==2):__computer__choice="scissors"
    elif(__computer__choice==3):__computer__choice="rock"

    if __user__choice in ["rock","paper","scissors"]:pass
    else:
        while(__user__choice not in ["rock","paper","scissors"]):
            print(Fore.RED+"Enter a correct weapon")
            time.sleep(1)
            __user__choice=input(Fore.BLUE+"Enter your weapon:").lower()
            time.sleep(1)
    winner=""
        
    if(__computer__choice=="paper" and __user__choice=="rock" or __computer__choice=="scissors" and __user__choice=="paper" or __computer__choice=="rock" and __user__choice=="scissors"):
        winner="Computer"
        __computer__score+=1  
    elif(__computer__choice==__user__choice):winner="Draw"  
    else: 
        __user__score+=1
        winner=name
    count+=1
    print(Fore.GREEN+f"You choose {__user__choice} and computer choose {__computer__choice}.\nWinner->{winner} ")
    print(Fore.CYAN+f"{name} Score={__user__score}          Computer Score={__computer__score}")
    print(Fore.MAGENTA+f"You have played {count} times.")
    __user__wish=input(Fore.RED+"Do you want to play more?(Y/N)").lower()
    while(__user__wish!="y" and __user__wish!="n"):
        print("Enter (Y/N)")
        time.sleep(1)
        __user__wish=input(Fore.RED+"Do you want to play more?(Y/N)").lower()
        time.sleep(1)
    if(__user__wish=="n"):break
    
if(__computer__score>int(__user__score)):print(Fore.RED+"Computer Wins.")

elif(__computer__score<int(__user__score)):print(Fore.GREEN+"User Wins.")
else:print(Fore.YELLOW+"Its a Draw.")

time.sleep(2)

print(Fore.BLUE+"Thanks for playing.")