# Beginner Password Manager
*This is a basic password manager using fernet cryptography*
##### **NOTE: THIS IS NOT RECOMMENDED FOR STORING SENSITIVE DATA**
# 
## Extremely Simple Setup Instructions:
1. First things first, let's make sure the code is set up. Read through it and make changes if you want, but there are a few things you definitely should change in manager.py:

**As the comment says, uncomment the multiline function and run the code while calling the function. This creates the fernet key used to shuffle your passwords and can be commented out once again after one use.**

```python 
#Use the below multiline comment to create the cryptography key by running the function once and hashing it out again
'''def write_key():
    key = base64.urlsafe_b64encode(kdf.derive(password))    
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''
```

**Create your own master password to replace the string - you do not want 'ENTER YOU OWN MASTER PASWORD' to be your password!**

```python
#user creates a password to use that only they should know 
		password = "ENTER YOU OWN MASTER PASWORD"
		mpwd = str(input('What is the master password (q to quit)? '))
```

2. Look through the code to see if you want to make any specific edits in terms of the format, as well as improvements or personal comments. This is to help get a good understanding of what passwords you may want to store in the file and helps you learn a bit more about how it works in general.

3. **Run the program, follow the prompts to use it, and enjoy!** Please feel free to report any issues or submit pull requests as you continue to use it. 
