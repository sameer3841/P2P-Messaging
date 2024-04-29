import socket
import os
import sys
import threading as thr

IP = '127.0.0.1'
PORT = 12000
BUFFER_SIZE = 1024
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(5)
print(f'Server ready and listening on {IP}:{PORT}')
clients = [] #List of clients, members should be tuples of IP and Ports
try:
    while True:  # section 4 step 6
        (conn_socket, addr) = server_socket.accept()  # section 4 step 3
        clients.append((conn_socket, addr))
        #threader = thr.Thread(target=service_client_connection, args=(conn_socket,))
        #threader.start()
except KeyboardInterrupt as ki:
    pass
finally:
    server_socket.close()
def receive():
    pass
def send():# Probably gonna need multiple send and receive for each type
    pass