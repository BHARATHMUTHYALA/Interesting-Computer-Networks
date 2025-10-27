# from Crypto.Cipher import DES
# from Crypto.Util.Padding import pad, unpad

# def encrypt_des(key, plaintext):
#       cipher = DES.new(key, DES.MODE_ECB)
#       padded_text = pad(plaintext, DES.block_size)
#       cipher_text = cipher.encrypt(padded_text)
#       return cipher_text

# def decrypt_des(key, cipher_text):
#       cipher = DES.new(key, DES.MODE_ECB)
#       decrypted_padded_text = cipher.decrypt(cipher_text)
#       plaintext = unpad(decrypted_padded_text, DES.block_size)
#       return plaintext

# key = b'mysecret'
# message = b"This is a secret message."
# encrypted_message = encrypt_des(key,message)
# print(f"Encrypted Message: {encrypted_message}")

# decrypted_message = decrypt_des(key, encrypted_message)
# print(f"Decrypted Message: {decrypted_message}")


from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad
 
key = b'mysecret'
message = b'This is a secret message'

cipher = DES.new(key, DES.MODE_ECB)
cipher_text = cipher.encrypt(pad(message, DES.block_size))

decipher = DES.new(key, DES.MODE_ECB)
plain_text = unpad(decipher.decrypt(cipher_text), DES.block_size)

print("Encrypted data: ", cipher_text)
print("Decrypted data: ", plain_text)

