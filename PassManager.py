import os
import base64
from cryptography.fernet import Fernet
import getpass
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from colorama import Fore
import time
#To create master key for unlocking my file
print(Fore.YELLOW+"Welcome to the Password Manager!")
time.sleep(2)
print(Fore.CYAN+"This program will help you securely store your passwords. \nLet's get started!")
time.sleep(2)
def generate_key(password,salt):
    """Turns your password + salt into a Fernet-compatible key."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1_200_000,
    )
    # kdf.derive returns raw bytes; we base64 encode them for Fernet
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))
SALT_FILE = "salt.bin"
if os.path.exists(SALT_FILE):
    with open(SALT_FILE, "rb") as s_file:
        salt = s_file.read()
else:
    # Create a permanent salt if it doesn't exist
    salt = os.urandom(16)
    with open(SALT_FILE, "wb") as s_file:
        s_file.write(salt)
    print(Fore.GREEN+f"[*] Created new salt file: {SALT_FILE}")

user_password = getpass.getpass(Fore.CYAN+"Enter your Master Password: ")
key = generate_key(user_password, salt)
fer = Fernet(key)

LOGIN_FILE = "login.bin"

if not os.path.exists(LOGIN_FILE):
    # First time setup: Encrypt a 'secret' word to verify later
    with open(LOGIN_FILE, "wb") as f:
        f.write(fer.encrypt(b"success"))
    print(Fore.GREEN+"Master Password set!")
else:
    # Attempt to verify the password
    try:
        with open(LOGIN_FILE, "rb") as f:
            encrypted_data = f.read()
        print(Fore.YELLOW+"Verifying Master Password...")
        time.sleep(2)
        
        # This will fail if the key is wrong
        if fer.decrypt(encrypted_data) == b"success":
            print(Fore.GREEN+"Access Granted!")
            time.sleep(1)
        else:
            print(Fore.RED+"Access Denied!")
            time.sleep(1)
            quit()
    except Exception:
        # If decryption fails (InvalidToken), the password was wrong
        print(Fore.RED+"Incorrect Master Password. Access Denied.")
        quit()


def view():
    file=open("password.txt","r")
    for line in file.readlines():
        data=line.rstrip()
        user,password=data.split(":",1)
        print(Fore.LIGHTBLUE_EX+f"user:{user}\npassword:{fer.decrypt(password.encode()).decode()}")
        time.sleep(2)
def add():
    name=input(Fore.LIGHTGREEN_EX+"Enter username: \n")
    time.sleep(1)
    password=getpass.getpass(Fore.LIGHTYELLOW_EX+"Enter the password: \n")
    time.sleep(1)
    file="password.txt"
    if(os.path.exists(file)):
        with open("password.txt","a") as f:
            f.write(name+":"+fer.encrypt(password.encode()).decode()+"\n")
    else:
        with open("password.txt","w") as f:
            f.write(name+":"+fer.encrypt(password.encode()).decode()+"\n")
        print(Fore.GREEN+"Created new password.txt file.") 
        time.sleep(1)    
   
    


Flag="y"
while(Flag=="y"):
    flag=input(Fore.LIGHTCYAN_EX+"Do you want to save or view a password?(Y/N)").lower()
    time.sleep(1)
    while flag not in ["y","n"]:
        flag=input(Fore.RED+"Enter correct option:")
        time.sleep(1)
    if(flag=="n"):quit()
    
    choice=input(Fore.LIGHTMAGENTA_EX+"You want to add or view the passwords?(ADD/View)").lower()
    time.sleep(1)
    
    while choice not in ["view","add"]:
        choice=input(Fore.RED+"Enter correct choice:")
        time.sleep(1)
    if(choice=="add"):
        add()
    else:
        view()