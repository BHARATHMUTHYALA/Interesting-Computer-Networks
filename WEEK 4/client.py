import socket

def xor(a,b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a,b))


def mod2div(dividend, divisor):
    pick = len(divisor)
    temp = dividend[:pick]
    while pick < len(dividend):
        if temp[0] == '1':
            temp = xor(temp, divisor) + dividend[pick]
        else:
            temp =  xor(temp, '0'*len(divisor)) + dividend[pick]
        temp = temp.lstrip('0')
        pick += 1

    if temp[0] == '1':
        temp = xor(temp, divisor)
    else:
        temp = xor(temp, '0'*len(divisor))
    return temp

def encode_data(data, key):
    padded = data + '0'*(len(key) - 1)
    crc = mod2div(padded, key)
    return data + crc

HOST = 'localhost'
PORT = 65432
POLYNOMIAL = '1001'
DATA = '1101011011'

FULL_DATA = encode_data(DATA, POLYNOMIAL)
print(f"Data to send (Original + CRC): {FULL_DATA}") 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(FULL_DATA.encode())
    response = s.recv(1024).decode()
    print(f"Received response from server: {response}")