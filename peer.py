import socket
import os
import sys
import threading
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
    return server_address


def receiver(a_socket):
    a_socket.listen()
    sender, address = a_socket.accept()
    nickname = sender.recv(BUFFER_SIZE).decode()  #Receives the nickname
    print(nickname, "from", address, "has established a connection.")
    sender.send(f"Hello {nickname} what did you want say?".encode())# sends to the sender
    message = ""
    while message.upper() != "E":
        message = sender.recv(BUFFER_SIZE).decode()
        print(message)
        response = input()
        sender.send(response.encode())
    sender.close()


def sender(a_socket):
    last_message_type = input("What type of message do you want to send: ")
    a_socket.send(last_message_type.encode())
    message = a_socket.recv(BUFFER_SIZE)#Who would you like to chat with?
    print(message.decode())
    if last_message_type.upper() == 'R':
        msg = a_socket.recv(BUFFER_SIZE).decode()
        print(msg)
    elif last_message_type.upper() == 'S':
        user = input()
        a_socket.send(user.encode())
        message = a_socket.recv(BUFFER_SIZE)
        print(message.decode())
        if not (message == b"Sorry, there is no user by that name."):
            # Connect to the peer
            nickname , peer_ip, peer_port = message.split(" ")
            peer_port = int(peer_port)
            a_socket.connect((peer_ip, peer_port))#########################
    elif last_message_type.upper() == 'L':
        flag = False
    elif last_message_type.upper() == 'NONE':
        pass
    else:
        pass
    pass


enter_network(peer_socket, input("Enter a nickname: "))
message = peer_socket.recv(BUFFER_SIZE)  # Welcome to the server
print(message.decode())
flag = True
while flag:
    send = thr.Thread(target=sender,args=(peer_socket,))
    # receive = thr.Thread(target=receiver,args=(peer_socket,))
    request = input("Do you want to send a message: ")
    if request.upper() == 'Y' or request.upper() == 'YES':
        sender(peer_socket)
    else:
        print("receiver")
        receiver(peer_socket)