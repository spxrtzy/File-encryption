from cryptography.fernet import Fernet
import time

key = Fernet.generate_key()
print(key)  

file = open("token.key", "wb")
file.write(key)
file.close

time.sleep(2)


#Open the file and read the info that is stored
file = open("token.key", "rb")
key = file.read()
file.close()

#With th e code that is in the file token.key
with open("test.txt", "rb") as f:
    data = f.read()

#Use it to encrypt the data
fernet = Fernet(key)
encrypted = fernet.encrypt(data)

#Create the encrypted file
with open("test.txt.EN", "wb") as f:
    f.write(encrypted)
