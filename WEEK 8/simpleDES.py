def generate_keys(key):
    bits = []

    for char in  key[:8]:
        bits.extend([int (b) for b in format(ord(char), '08b')])
    return bits


def initial_permutation(data):
    return data[::-1] 

def final_permutation(data):
    return data[::-1]

data = "12345678"
print("Initial Permutation: ", initial_permutation(data))
print("Final Permutation: " , final_permutation(data))

EXPANSION_TABLE = [0,1,3,2,1,3]


S_BOXES = [
    [[1,0],[3,2],[0,1],[2,3]],
    [[0,3],[2,1],[3,0],[1,2]]
]

P_BOX = [2,0,3,1]

def expand(bits, table):
    return [bits [i] for i in table]

def xor(bits1, bits2):
    return [b1^b2 for b1, b2 in zip(bits1, bits2)]

def s_box_substitution(bits):
    result = []
    for i in range(0, len(bits) , 3):
        block = bits[i:i+3]

        if len(block) < 3:  continue

        row = block[0]
        col = (block[1] << 1) | block[2]
        sbox_index = i // 3

        if sbox_index >= len(S_BOXES): continue 

        sbox = S_BOXES[sbox_index]
        if row >= len(sbox) or col >= len(sbox[row]):
            continue
        val = sbox[row][col]
        result.extend([(val >> 1) & 1 , val & 1])
    return result 

def permute(bits, table):
    return [bits[i] if i < len(bits) else 0 for i in table]

def fiestel_function(right_half, round_keys):
    expanded = expand(right_half,EXPANSION_TABLE)
    xored = xor(expanded, round_keys)
    substitued = s_box_substitution(xored)
    result = permute(substitued, P_BOX)
    return result


keys = "12345678"
round_keys = generate_keys(keys)[:6]
print("Round Key: ", round_keys)


right_half = [1, 0 ,1, 1]
output = fiestel_function(right_half, round_keys)
print("Output of F-function: ", output)

# round_key = [1, 1, 0, 0 ,1, 0]
# output = fiestel_function(right_half, round_key)
# print(f"Output of F-function : {output}")


