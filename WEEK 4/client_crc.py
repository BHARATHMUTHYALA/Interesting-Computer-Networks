import socket

def xor(a, b):
    result = ""
    for i in range(1, len(b)):
        result +='0' if a[i] == b[i]  else '1'
    return result
    
def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]
    
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*len(tmp) , tmp) + dividend[pick]
        pick +=1 
        
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
        
    return tmp
    
    
data = input("Enter the data bits:")
generator = input("Enter the generator polynomial: ")

append_data = data + '0'*(len(generator) - 1)

remainder = mod2div(append_data, generator)
print(f"Remainder after CRC check :{remainder}")

codeword = data + remainder 
print(f"Transmitted data (Data + CRC): {codeword}")

client_socket = socket.socket()
client_socket.connect(('localhost', 12345))

# client_socket.send(codeword.encode())
# client_socket.send(generator.encode())


message = codeword + '\n' + generator  # Join with newline
client_socket.send(message.encode())


response = client_socket.recv(1024).decode()
print(f"Server Response: {response}")

client_socket.close()