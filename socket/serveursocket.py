import socket
import sys

serveur_socket = socket.socket()
serveur_socket.bind(('localhost', 8080))
serveur_socket.listen(5)
conn, addr = serveur_socket.accept()
data = conn.recv(1024).decode()
conn.send('Hello, world' .encode())
conn.close()
print(data)
