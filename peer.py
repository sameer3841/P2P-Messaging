import socket
import os
import sys
import threading as thr
import ip

BUFFER_SIZE = 1024

peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address, server_address = ip.get_ip_address()

print(server_address)


def enter_network(peer, nickname):
    peer.connect(server_address)
    peer.send(nickname.encode())


def send_message_type(message_type):
    peer_socket.send(message_type.encode())
    return message_type


enter_network(peer_socket, input("Enter a nickname: "))
message = peer_socket.recv(BUFFER_SIZE)
print(message.decode())
last_message_type = ""
flag = True
while flag:
    last_message_type = send_message_type(input("What type of message do you want to send: "))
    message = peer_socket.recv(BUFFER_SIZE)
    print(message.decode())
    if last_message_type.upper() == 'L':
        flag = False



