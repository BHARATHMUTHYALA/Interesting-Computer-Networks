import socket

def xor(a,b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    return ''.join(str(int(x)^int(y)) for x, y in zip(a,b))


def mod2div(dividend, divisor):
    pick = len(divisor)
    temp = dividend[0:pick]

    while pick < len(dividend):
        if temp[0] == '1':
            temp = xor(temp, divisor) +dividend[pick]
        else:
            temp = xor(temp,'0'*pick) + dividend[pick]
        pick+=1

    if temp[0] == '1':
        temp = xor(temp, divisor)
    else:
        temp = xor(temp, '0'*len(divisor))
    return temp
    
def crc_check(received_data, key):
    remainder = mod2div(received_data, key)
    return remainder == '0' * (len(key)-1)

HOST = 'localhost'
PORT = 65432
POLYNOMIAL = '1001'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr =  server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        received_data = conn.recv(1024).decode()
        print(f"Received data : {received_data}")

        if(crc_check(received_data, POLYNOMIAL)):
            response = "Data is correct"
        else:
            response = "Data is incorrect"

        print(f"CRC check result: {response}")
        conn.send(response.encode())
        print("Response sent to client")