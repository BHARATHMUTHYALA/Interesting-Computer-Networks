from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

with open("private.pem", "wb") as f:
    f.write(private_key)

with open("public.pem", "wb") as f:
    f.write(public_key)

print("Keys are generated and saved to 'public.pem' and 'private.pem'. ")

message = "Hello, RSA!"
public_key = RSA.import_key(open("public.pem", "rb").read())

cipher = PKCS1_OAEP.new(public_key)
cipher_text = cipher.encrypt(message.encode())

with open("cipher.bin","wb") as f:
    f.write(cipher_text)

print("Encrypted Message (hex):")
print(cipher_text.hex())


private_key = RSA.import_key(open("private.pem","rb").read())
cipher_rsa = PKCS1_OAEP.new(private_key)

with open("cipher.bin", "rb") as f:
    cipher_data = f.read()
 
decrypted = cipher_rsa.decrypt(cipher_data)
print("Decrypted message: ")
print(decrypted.decode())


