import socket
import os
import sys
import threading as thr
import ip

BUFFER_SIZE = 1024

peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address, server_address = ip.get_ip_address()
print(address, server_address)


def enter_network(peer, nickname):
    peer_socket.connect(server_address)
    peer_socket.send(nickname.encode())
    #Returns a socket representing the server

def receiver():
    peer_socket.listen(1)
    sender, address = peer_socket.accept()
    nickname = sender.recv(BUFFER_SIZE).decode()  #Receives the nickname
    print(nickname, "from", address, "has established a connection.")
    sender.send(f"Hello {nickname} what did you want say?".encode())# sends to the sender
    message = ""
    while (message.upper() != "E"):
        message = sender.recv(BUFFER_SIZE).decode()
        print(message)
        response = input()
        sender.send(response.encode())
    sender.close()


def sender():
    last_message_type = input("What type of message do you want to send: ")
    peer_socket.send(last_message_type.encode())
    message = peer_socket.recv(BUFFER_SIZE)
    print(message.decode())
    if last_message_type.upper() == 'R':
        msg = peer_socket.recv(BUFFER_SIZE).decode()
        print(msg)
    elif last_message_type.upper() == 'S':
        user = input()
        peer_socket.send(user.encode())
        message = peer_socket.recv(BUFFER_SIZE)
        print(message.decode())
        if not (message == b"Sorry, there is no user by that name."):
            # Connect to the peer
            msg = input()
    elif last_message_type.upper() == 'L':
        flag = False
    elif last_message_type.upper() == 'none':
        pass
    else:
        pass
    pass


enter_network(peer_socket, input("Enter a nickname: "))
message = peer_socket.recv(BUFFER_SIZE)  # Welcome to the server
print(message.decode())
last_message_type = ""
flag = True
while flag:
    ######################### All this goes into a sending thread
    pass

    ######################### All this goes into a sending thread
