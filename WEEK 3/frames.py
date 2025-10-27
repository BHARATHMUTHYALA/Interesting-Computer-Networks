import socket
HOST = '127.0.0.1'
PORT = 9090
def sender():
    
    data = "Hello, this is a test frame."
    frame = f"{len(data)} {data}"
    with socket.socket() as s:
        print("Sender: Connecting to server...")
        s.connect((HOST,PORT))
        print("Sender: Sending frame.")
        s.send(frame.encode())
        print('Sender: Done')

def receiver():
    print('Receiver: Starting server....')
    with socket.socket() as s:
        s.bind((HOST,PORT))
        s.listen(1)
        print(f"Receiver: Listening on {HOST}:{PORT}...")
        conn, _ =s.accept()
        with conn:
            frame =  conn.recv(1024).decode()
            count , data =  int(frame[:frame.find(" ")]), frame[frame.find(" ") +  1:]
            print(f'Received frame: {frame}')
            print(f'Character count: {count}, Data: {data}')
            print(f'Valid' if len(data) == count else 'Invalid')

if __name__== "__main__":
    import threading
    import time
    threading.Thread(target=receiver,daemon = True).start()
    time.sleep(0.1)
    sender()
    