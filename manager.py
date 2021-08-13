import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#Use the below multiline comment to create the cryptography key by running the function once and hashing it out again
'''def write_key():
    key = base64.urlsafe_b64encode(kdf.derive(password))    
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

salt = os.urandom(16)

kdf = PBKDF2HMAC(
     algorithm=hashes.SHA256(),
     length=32,
     salt=salt,
     iterations=100000,
)

#loads the key created by the write_key function
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
#makes the fernet key usable
key = load_key()
fer = Fernet(key)

#view passwords
def view():
  #opens the file with reading capabilities
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            accttype, user, passw = data.split("|")
            print("Account Type:", accttype, "| User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode()) #decodes the encrypted password
            
#serves no other purpose other than ending the program
def end():
	print("Okay, thanks for using the program.")

#main menu of the program, shows up only if the master password is correct
def menu():		
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        end()
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        menu()

#adds all information to the passwords file
def add():
	atype = str(input('Account Type: '))
	name = str(input('Username: '))
	pwd = str(input('Password: '))
	with open('passwords.txt', 'a') as f:
		f.write(atype + "|" + name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    #writes the password inputted to the file in an encrypted format making it tough to crack

#controls entry or denial into the program menu
def master():
	while(True):
    #user creates a password to use that only they should know 
		password = "ENTER YOU OWN MASTER PASWORD"
		mpwd = str(input('What is the master password (q to quit)? '))
    #grants entry into program
		if(mpwd==password):
			print('Password Correct.')
			menu()
    #quits the program
		elif(mpwd=='q'):
			end()
			break
    #denies program entry
		elif(mpwd!=password):
			print('Password Incorrect, please try again')
			continue


master()
