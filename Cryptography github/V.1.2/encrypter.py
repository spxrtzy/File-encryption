from cryptography.fernet import Fernet
import time

key = Fernet.generate_key()
print(key)  

file = open("key.key", "wb")
file.write(key)
file.close

time.sleep(2)

file = open("key.key", "rb")
key = file.read()
file.close()

with open("test.txt", "rb") as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

#Create the encrypted file
with open("test.txt.EN", "wb") as f:
    f.write(encrypted)
