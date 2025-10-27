import socket

def xor(a,b):
    result = ""
    for i in range(1, len(a)):
        result +='0' if a[i] == b[i]  else '1'
    return result
    
def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]
    
    while(pick<len(dividend)):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            zeroes = '0'*len(tmp)
            tmp = xor('0'*len(tmp), tmp) + dividend[pick]
        pick+=1
        
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        zeroes = '0'*len(tmp)
        tmp = xor(zeroes, tmp)
        
    return tmp[1:]
        
server_socket = socket.socket()
server_socket.bind(('localhost',12345))
server_socket.listen(1)
print("Server is waiting for connection...")

conn, addr = server_socket.accept()
print(f"Connected to {addr}")

# data = conn.recv(1024).decode()
# print(f"Received Data: {data}")

# generator = conn.recv(1024).decode()
# print(f"Generator Polynomial: {generator}")

data = conn.recv(1024).decode()
parts = data.split('\n')         # Split combined message by newline
received_data = parts[0].strip()
generator = parts[1].strip()

print(f"Received Data: {received_data}")
print(f"Generator Polynomial: {generator}")

remainder = mod2div(received_data, generator)
print(f"Remainder after CRC check:{remainder}")

if "1" in remainder:
    print("Error detected in received data. ")
    conn.send("Error detected".encode())
    
else:
    print("No error detected. Data is received correctly.")
    conn.send("Data received correctly.".encode())



conn.close()
