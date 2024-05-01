import socket
import os
import sys
import threading as thr
import ip

BUFFER_SIZE = 1024
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#IP, PORT = ip.get_ip_address(server_socket)
IP, PORT = "10.33.16.1", 12000
IP = "127.0.0.1"
server_socket.bind((IP, PORT))
print(f'Server ready and listening on {IP}:{PORT}')
clients = {}  #List of clients, values should be tuples of IP and Ports


def remove(address):
    for x in clients.keys():
        if clients.get(x) == address:
            clients.pop(x)
            return 1
    print("Address not found")

def enter(nickname, address):
    clients.update({nickname: address})
    server_socket.sendto('Welcome to the server'.encode(), address)
    print(nickname, "has entered the server at ", address)
try:
    while True:
        message, address = server_socket.recvfrom(BUFFER_SIZE)
        message = message.decode()
        type = message[0]
        print(type)
        if (type == 'S'):
            pass
        elif (type == 'G'):
            print(clients)
            pass
        elif (type == 'A'):
            pass
        elif (type == 'L'):
            remove(address)
        if (not (address in clients)):
            enter(message, address)
        ############################ To be moved to a join function
        nickname = message[2:]
        clients.update({nickname: address})
        server_socket.sendto('Welcome to the server'.encode(), address)
        print(nickname, "has entered the server at ", address)
        ############################ To be moved to a join function

        pass
except KeyboardInterrupt as ki:
    pass


#finally:
#    server_socket.close()
def receive():
    pass


def send():  # Probably gonna need multiple send and receive for each type
    pass
