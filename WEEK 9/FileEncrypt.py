from Crypto.Cipher import DES
from Crypto.Util.Padding import pad 
key = b"8bytekey"
input_file = 'plaintext.txt'
output_file = 'ciphertext.bin'

with open(input_file, 'rb') as f:
    plaintext = f.read()

cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))

with open(output_file, "wb") as f:
    f.write(ciphertext)

print(f"Encryption has been complete, Encrypted File: ",output_file)
