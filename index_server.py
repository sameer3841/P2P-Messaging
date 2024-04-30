import socket
import os
import sys
import threading as thr
import ip




BUFFER_SIZE = 1024
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#IP, PORT = ip.get_ip_address(server_socket)
IP , PORT = "10.33.16.1", 12000
IP = "127.0.0.1"
server_socket.bind((IP, PORT))
print(f'Server ready and listening on {IP}:{PORT}')
clients = {}  #List of clients, values should be tuples of IP and Ports
try:
    while True:
        nickname, address = server_socket.recvfrom(BUFFER_SIZE)
        nickname = nickname.decode()
        clients.update({nickname : address})
        server_socket.sendto('Welcome to the server'.encode(), address)
        print(nickname, "has entered the server at ",address)
        print(len(clients))
        print(clients)
        pass
except KeyboardInterrupt as ki:
    pass


#finally:
#    server_socket.close()
def receive():
    pass


def send():  # Probably gonna need multiple send and receive for each type
    pass
