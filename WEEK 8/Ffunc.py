SBOX = [
    [ [1, 3, 0 ,2], [2, 1 , 3, 0], [3, 0 ,1, 2], [0, 2, 3, 1]],
    [ [3, 1, 2, 0], [0, 2, 1, 3], [1, 3, 0, 2], [2, 0, 3, 1]]
]

P = [2, 4, 6, 8, 1, 3, 5, 7]


def expand(r):
    return r[0:4] + r[2:6] + r[4:8]

def xor(a, b):
    return ''.join('1' if i!=j else '0' for i,j in zip(a, b))

def sbox_lookup(bits6, box):
    row = int(bits6[0]  + bits6[5], 2)
    col = int(bits6[1:5], 2) % 4
    return f"{SBOX[box][row][col]:04b}"

def permute(bits, table):
    return ''.join(bits[i - 1] for i in table)


def simplified_f(r, k):
    print("\n [F-FUNCTION START]")
    print("Input R: ", r)

    r_exp = expand(r);
    print("Expanded R: ", r_exp)

    xored = xor(r_exp, k)
    print("XOR with key: ", xored)

    s1_out = sbox_lookup(xored[:6],0)
    s2_out = sbox_lookup(xored[6:], 1)
    print("S1 Output: ", s1_out)
    print("S2 Output: ", s2_out)

    combined  = s1_out + s2_out
    print("Combined S-box output: ", combined)

    permuted = permute(combined, P)
    print("Permuted Ouput: ", permuted)

    print("[F-FUNCTION END]\n")
    return permuted

def fiestel_round(L, R, key):
    f_out = simplified_f(R, key)
    new_L = R 
    new_R = xor(L, f_out)
    return new_L, new_R


def fiestel_encrypt(block8bit, key12bit, rounds = 1):
    assert len(block8bit) == 16
    assert len(key12bit) == 12

    L = block8bit[:8]
    R = block8bit[8:]
    print("Initial Block: L = ", L, ", R =",R)

    for i in range(rounds):
        print(f"\n[ROUND {i+1}]")
        L,R  = fiestel_round(L, R, key12bit)

    cipher_text = L + R 
    print("\nFinal Ciphertext (binary): ", cipher_text)
    return cipher_text

plaintext = '1100110011001100'
key = '101010101010'

cipher_text = fiestel_encrypt(plaintext, key, rounds = 1)
print(f"\nEncrypted Ciphertext: ", cipher_text)
