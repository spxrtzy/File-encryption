from cryptography.fernet import Fernet

file = open("key.key", "rb")
key = file.read()
file.close()

with open("img4.jpg", "rb") as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

#Create the encrypted file
with open("img4.jpg.EN", "wb") as f:
    f.write(encrypted)
