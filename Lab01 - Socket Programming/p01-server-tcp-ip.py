#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'	# standard loopback interface address (localhost)
PORT = 65432		# port to listen on (non - privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Connected by ', addr)
		if True:
			data = b"hello world!"
			conn.sendall(data) 
		