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


def receiver(a_socket: socket.socket):
    msgg = a_socket.recv(BUFFER_SIZE)
    return msgg.decode()

def sender(person):
    peer_socket.send(person.encode())
    return person


enter_network(peer_socket, input("Enter a nickname: "))
message = peer_socket.recv(BUFFER_SIZE)
print(message.decode())
last_message_type = ""
flag = True
while flag:

    last_message_type = sender(input("What type of message do you want to send: "))
    message = peer_socket.recv(BUFFER_SIZE)
    print(message.decode())
    if last_message_type.upper() == 'R':
        msg = receiver(peer_socket)
        print(msg)
    elif last_message_type.upper() == 'S':
        user = sender(input())
        message = peer_socket.recv(BUFFER_SIZE)
        print(message.decode())
        msg = input()
    elif last_message_type.upper() == 'L':
        flag = False