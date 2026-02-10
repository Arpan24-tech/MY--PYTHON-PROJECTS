import random
import time
from colorama import Fore

__number__range__=random.randint(10,100)
print(Fore.YELLOW+"Welcome to the Random Number Guessing Game!")
time.sleep(2)
print(Fore.CYAN+"I have selected a random number between 0 and "+str(__number__range__)+". \nCan you guess it?")
time.sleep(2)
n=random.randint(0,__number__range__)
chance=0
flag=True

while(flag):
    answer=int(input(Fore.GREEN+"Make guess:"))
    time.sleep(2)
    if(answer<0):
        chance+=1
        print(Fore.RED+"Enter a positive number.")
        time.sleep(1)
        continue
    if(answer==n):
        print(Fore.LIGHTRED_EX+"You got it right.")
        print(Fore.YELLOW+"You guessed the number in "+str(chance)+" chances.")
        time.sleep(3)
        flag=False
        break
    elif(answer>n):
        print(Fore.LIGHTMAGENTA_EX+"You guessed higher. Try again!")
        time.sleep(2)
        chance+=1
    else:
        print(Fore.LIGHTMAGENTA_EX+"You guessed lower. Try again!")
        time.sleep(2)
        chance+=1
    
print(Fore.LIGHTBLUE_EX+"THE GAME IS OVER.")
