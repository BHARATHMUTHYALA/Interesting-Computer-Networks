from Crypto.Cipher import DES 
from Crypto.Util.Padding import pad, unpad

key = b'8bytekey'
plaintext = b'This is a secret message'

padded_text = pad(plaintext, DES.block_size)

cipher  = DES.new(key, DES.MODE_ECB)

ciphertext = cipher.encrypt(padded_text)

print("Plaintext: ", plaintext)
print("Padded text: ", padded_text)
print("Cipher Text (bytes): ", ciphertext)


decipher = DES.new(key, DES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), DES.block_size)

print("Decrypted Text: ", decrypted)
