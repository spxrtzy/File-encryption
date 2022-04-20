from cryptography.fernet import Fernet
import os
import time


#Credits and start-screen
print("""
 _________________________________________________________________________________________
|  _____   _____           ______ _   _  _____ _______     _______ _______ ______ _____   |
| |  __ \ / ____|  /\     |  ____| \ | |/ ____|  __ \ \   / /  __ \__   __|  ____|  __ \  |
| | |__) | (___   /  \    | |__  |  \| | |    | |__) \ \_/ /| |__) | | |  | |__  | |__) | |
| |  _  / \___ \ / /\ \   |  __| | . ` | |    |  _  / \   / |  ___/  | |  |  __| |  _  /  | 
| | | \ \ ____) / ____ \  | |____| |\  | |____| | \ \  | |  | |      | |  | |____| | \ \  |
| |_|  \_\_____/_/    \_\ |______|_| \_|\_____|_|  \_\ |_|  |_|      |_|  |______|_|  \_\ |
|_________________________________________________________________________________________|                                                                                        
MADE BY SPXRTZY                                                                                                                                                                       
                                                                                        """)


#Behind the scenes 😎 (I feel like a real programmer)


def fileEncrypt():
    foldername = input("Enter file folder destination(Lea ve blank for current): ") or '.'
    filename = input("Enter File name: ")

    print("Creating encryption key")
    key = Fernet.generate_key()
    print(f'Your key is {key}')  

    file = open(f"{foldername}/key.key", "wb")
    file.write(key)
    file.close

    print("Finding file...")
    time.sleep(1)

    with open(f"{foldername}/{filename}", "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    #Create the encrypted file
    print("Writing encrypted file")
    with open(f"{foldername}/{filename}.EN", "wb") as f:
        f.write(encrypted)
    
    print('\x1b[6;30;42m' + 'Success! Your file has been Encrypted' + '\x1b[0m')
    print("You may now delete the original file that isn't encrypted")

def fileDecrypt():
    foldername = input("Enter file folder destination(Leave blank for current): ") or '.'
    filename = input("Enter file name: ")
    newfilename = input("New desired name for decrypted file (with ext.): ")
    keyfilename = input("Enter .key file name: ")

    file = open(f"{foldername}/{keyfilename}", "rb")
    key = file.read()
    file.close()

    with open(f"{foldername}/{filename}", "rb") as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)

#Create the encrypted file
    print("Writing decrypted file...")
    with open(f"{foldername}/{newfilename}", "wb") as f:
        f.write(encrypted)
    print('\x1b[6;30;42m' + 'Success! Your file has been decrypted' + '\x1b[0m')




#Give the user options
print("1. Encrypt File")
print("2. Decrypt File")
print("3. HowToUse")
print("4. Exit")

instructions = """
This Script was made by spxrtzy
What it does is it encrypts and decrypts your files of choice.

NOTE: THE KEY TO YOUR FILES THAT WILL BE USED TO DECRYPT IT IS LOCATED IN THE "key.key" FILE BY DEAFULT
IF YOU HAVE ANY ISSUES DON'T HESITATE TO WRITE TO ME(twitter: @lzmogus)

Things you will need for encryption:
There is not much really you need for the encryption part, just keep in mind that the .key file will be created in the same folder as the encrypted file.

Things you will need for decryption:

1. You need to have both the .key file and the encrypted file in the same folder or else it won't work
2. Make sure that the key is correct to the file
3. Make sure that the .key file is not empty.
"""



#While loop asking for input and giving outpuy
runfile = True
while runfile:
    print("Enter Number From Above: ")
    commandlineinput = input(">: ")
    if commandlineinput == "1":
        fileEncrypt()
    elif commandlineinput == "2":
        fileDecrypt()
    elif commandlineinput == "3":
        print(instructions)
    elif commandlineinput == "4":
        print("Exiting...")
        break
    else:
        print("Not a command...")
