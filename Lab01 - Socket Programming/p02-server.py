import socket
from datetime import date 

today = date.today()
print("Today's date is: ", today)

HOST = '127.0.0.1'
PORT = 65436

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by ', addr)
        while True:
            data = conn.recv(1024)
            if data:
                print("Message from client (", addr, ") : ", data)
            if not data:
                break
            conn.sendall(b'' + str(date))