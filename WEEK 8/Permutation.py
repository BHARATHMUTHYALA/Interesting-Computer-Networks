IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17,  9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41,  9, 49, 17, 57, 25]

def permute(bits, table, label = 'PERM'):
    result =  ''.join(bits[i-1] for i in table)

    print(f"\n[{label}] Resulting Bits: \n{result}\n")
    return result

def string_to_bits(data):
    bits = ''.join(f"{byte:08b}" for byte in data)
    
    print("[BIT CONVERSION] Input bytes to bits: ")

    for i, byte in enumerate(data):
        print(f"  {chr(byte)}: {byte:08b} ")
    print(f"\nFull bit string: \n{bits}\n")

    return bits

def bits_to_bytes(bits):
    b = bytes(int(bits[i:i+8], 2) for i in range(0,len(bits), 8))

    print("[BYTE CONVERSION] bits to bytes: ")

    for i in range(0, len(bits), 8):
        print(f" {bits[i:i+8]} --> {int(bits[i:i+8], 2):02x}")
    print(f"\nFinal byte output: \n{b}\n")

    return b

data = b'ABCDEFGH'

print("Original: ",data)

bit_str = string_to_bits(data)

ip_bits = permute(bit_str,IP,label = 'IP')

fp_bits = permute(ip_bits,FP, label = 'FP')

final_output = bits_to_bytes(fp_bits)

print("After IP --> FP: ", final_output)