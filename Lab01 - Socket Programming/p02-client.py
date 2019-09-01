import socket

HOST = '127.0.0.1'
PORT = 65436

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Tell me todays date.')
    data = s.recv(1024)

if data:
    print('Received', repr(data))
else:
    print('No data received.')