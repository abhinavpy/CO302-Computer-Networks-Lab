import socket

HOST = "127.0.0.1"
PORT = 5005

with socket.socket(socket.AF_INET, socket.SOCK_DGAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    