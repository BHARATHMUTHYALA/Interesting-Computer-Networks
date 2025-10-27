from Crypto.Cipher import DES 
from Crypto.Util.Padding import unpad
key = b"8bytekey"
plaintext = b"HelloDES"
cipher = DES.new(key, DES.MODE_ECB)

ciphertext = cipher.encrypt(plaintext)
print("Decrypted Bytes: ", plaintext)
print("Decrypted Text: ", plaintext.hex())
