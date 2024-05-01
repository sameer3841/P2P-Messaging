import socket
import os
import sys
import threading as thr
import ip

BUFFER_SIZE = 1024
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# IP, PORT = ip.get_ip_address(server_socket)
IP, PORT = "10.33.16.1", 12000
IP = "127.0.0.1"
server_socket.bind((IP, PORT))
print(f'Server ready and listening on {IP}:{PORT}')
clients = {}  # List of clients, values should be tuples of IP and Ports


def remove(address):
    for x in clients.keys():
        if clients.get(x) == address:
            clients.pop(x)
            return 1
    print("Address not found")


def enter(a_socket):
    nickname, address = a_socket.recvfrom(BUFFER_SIZE)
    server_socket.sendto('Welcome to the server'.encode(), address)
    print(nickname.decode(), "has entered the server at ", address)
    return nickname, address


try:
    nickname, address = enter(server_socket)
    clients.update({nickname: address})
    while True:
        message, peer_address = server_socket.recvfrom(BUFFER_SIZE)
        message_type = message.decode()[0].upper()
        message = message.decode()[1:]
        if message_type == 'S':
            pass
        elif message_type == 'G':
            server_socket.sendto(str(clients).encode(), peer_address)
            pass
        elif message_type == 'A':
            pass
        elif message_type == 'L':
            remove(address)

        pass
except KeyboardInterrupt as ki:
    pass


# finally:
#    server_socket.close()
def receive():
    pass


def send():  # Probably gonna need multiple send and receive for each type
    pass
