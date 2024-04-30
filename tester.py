import socket
import os
import sys
import threading as thr
IP, PORT = "8.8.8.8", 80
BUFFER_SIZE = 1024
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(5)
print(f'Server ready and listening on {IP}:{PORT}')