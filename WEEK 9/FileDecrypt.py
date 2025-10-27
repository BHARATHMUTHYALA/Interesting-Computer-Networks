from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

key = b"8bytekey"
input_file = 'ciphertext.bin'
output_file = 'decrypted.txt'
with open(input_file, 'rb') as f:
    ciphertext = f.read()

cipher = DES.new(key, DES.MODE_ECB)
plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)

with open(output_file, 'wb') as f:
    f.write(plaintext)

print(f"Decryption Complete. Decrypted file {output_file}")