from colorama import Fore
import time
print(Fore.GREEN + "Welcome to the quiz!\nThis Quiz Consists of 5 Questions.\nPlease answer the following questions:\n")
time.sleep(3)
print(Fore.RED+"INSTRUCTIONS:\nEach correct answer gives you +10marks.\nEach Wrong answer gives you -5 answers.\n Lets Begin!")
score=0
correct=0
wrong=0
time.sleep(3)   
answer=input(Fore.CYAN+"What is largest continent on Earth by land area ?\n").lower()
if(answer=="asia"):
    score+=10
    correct+=1
else:
    score-=5
    wrong+=1
time.sleep(1)
answer=input(Fore.CYAN+"What is the chemical symbol for the element Gold?\n").lower()
if(answer=="au"):
    score+=10
    correct+=1
else:
    score-=5
    wrong+=1
time.sleep(1)
answer=input(Fore.CYAN+"Who wrote the famous play Romeo and Juliet?\n").lower()
if(answer=="william shakespeare"):
    score+=10
    correct+=1
else:
    score-=5
    wrong+=1
time.sleep(1)  
answer=input(Fore.CYAN+"Which organ in the human body is responsible for pumping blood?\n").lower()
if(answer=="heart"):
    score+=10
    correct+=1
else:   
    score-=5
    wrong+=1
time.sleep(1)  
answer=input(Fore.CYAN+"Which planet in our solar system is known as the Red Planet?\n").lower()
if(answer=="mars"):
    score+=10
    correct+=1
else:
    score-=5
    wrong+=1
time.sleep(1)   
answer=input(Fore.CYAN+"In which year did World War II end?\n").lower()
if(answer=="1945"):
    score+=10
    correct+=1
else:
    score-=5
    wrong+=1
time.sleep(1)  
answer=input(Fore.CYAN+"What is the tallest animal in the world?\n").lower()
if(answer=="giraffe"):
    score+=10
    correct+=1
else:
    score-=5
    wrong+=1
time.sleep(1)  
answer=input(Fore.CYAN+"What force pulls objects toward the center of the Earth?\n").lower()
if(answer=="gravity"):
    score+=10
    correct+=1
else:
    score-=5
    wrong+=1
time.sleep(1)   
answer=input(Fore.CYAN+"How many players are there on a standard soccer (football) team on the pitch at one time?\n").lower()
if(answer=="11"):
    score+=10
    correct+=1
else:
    score-=5
    wrong+=1
time.sleep(1)   
answer=input(Fore.CYAN+"What is the square root of 144?\n").lower()
if(answer=="12"):
    score+=10
    correct+=1
else:
    score-=5
    wrong+=1
time.sleep(2)
print(Fore.BLUE+"All questions over.\n")
print(Fore.GREEN+"Calculating your score...\n")
time.sleep(5)
print(Fore.YELLOW+"Your score is "+str(score)+" and you got "+str(correct)+" correct and "+str(wrong)+" wrong answers.\n")
print(Fore.WHITE+"THANKS FOR PLAYING :) \n")
time.sleep(3)
ask=input(Fore.MAGENTA+"Do you want to check answers? (Y/N)\n").lower()
time.sleep(1)
if(ask=="y"):
    print(Fore.CYAN+"1. Asia\n2. Au\n3. William Shakespeare\n4. Heart\n5. Mars\n6. 1945\n7. Giraffe\n8. Gravity\n9. 11\n10. 12")    
time.sleep(1)
print(Fore.WHITE+"OKAY, BYE!")