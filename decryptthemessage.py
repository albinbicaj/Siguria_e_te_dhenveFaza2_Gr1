from cryptography.fernet import Fernet
file=open('key.key','rb')
key=file.read()
file.close()
message="Takimi mbahet te premten ne ora 11:00"
encoded = message.encode()
f=Fernet(key)
encrypted=f.encrypt(encoded)
file=open('key.key','rb')
key2=file.read()
file.close()
f2=Fernet(key)
decrypted = decrypted = f2.decrypt(encrypted)
print(decrypted)
original_message = decrypted.decode()
print(original_message)