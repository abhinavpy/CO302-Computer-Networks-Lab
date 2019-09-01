import socket

HOST = "127.0.0.1"
PORT = 5005

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    print("Connected successfully to server.")
    data = s.sendto(b'Helloworld', (HOST, PORT))
    print("Message sent successfully.")
    