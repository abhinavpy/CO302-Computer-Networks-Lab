import socket

HOST = "127.0.0.1"
PORT = 5005
MESSAGE = "Hello World!"

with socket.socket(socket.AF_INET, socket.SOCK_DGAM) as s:
    s.bind((HOST, PORT))
    
    while True:
        data, addr = sock.recvfrom(1024)
        print("Received message: ", data)
        print("Received Message from: ", addr)
