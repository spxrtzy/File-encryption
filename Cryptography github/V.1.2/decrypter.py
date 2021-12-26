from cryptography.fernet import Fernet

file = open("token.key", "rb")
key = file.read()
file.close()

with open("test.txt.EN", "rb") as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

#Create the encrypted file
with open("test.txt.DE", "wb") as f:
    f.write(encrypted)
