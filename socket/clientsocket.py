import socket
import sys

client_socket = socket.socket()
client_socket.connect(('localhost', 8080))
client_socket.send('Hello world'.encode())
data = client_socket.recv(1024).decode()
client_socket.close()
