from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open("public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

message = "Hello, RSA!"
cipher = PKCS1_OAEP.new(public_key)
encrypted = cipher.encrypt(message.encode())

with open("private.pem", "wb") as f:
    f.write(encrypted)

print("Encrypted Message (hex):")
print(encrypted.hex())
