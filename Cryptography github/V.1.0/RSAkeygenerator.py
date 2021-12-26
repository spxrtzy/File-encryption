from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)  

file = open("token.key", "wb")
file.write(key)
file.close

