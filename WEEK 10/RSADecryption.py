from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open("private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

with open("cipher.bin", "rb") as f:
    cipher_text = f.read()

cipher = PKCS1_OAEP.new(private_key)    
decrypted = cipher.decrypt(cipher_text)


print("Decrypted message: ")
print(decrypted.decode())