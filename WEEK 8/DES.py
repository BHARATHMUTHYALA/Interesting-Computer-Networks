def xor_encrypt_decrypt(message, key):
    encrypted = []
    for i in range(len(message)):
        encrypted_char = chr(ord(message[i]) ^ ord(key[i % len(key)]))
        encrypted.append(encrypted_char)
    return ''.join(encrypted)

# Input
key = input("Enter a key (any length): ")
message = input("Enter the message to encrypt: ")

# Encrypt
encrypted_message = xor_encrypt_decrypt(message, key)
print(f"\n Encrypted (raw): {repr(encrypted_message)}")
print(f" Encrypted (hex): {encrypted_message.encode().hex()}")

# Decrypt
decrypted_message = xor_encrypt_decrypt(encrypted_message, key)
print(f" Decrypted: {decrypted_message}")
