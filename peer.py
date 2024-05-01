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


# def send_peer_message(message_type, message):
#     message = message_type + " " + message
#     peer_socket.sendto(message.encode(), server_address)


enter_network(peer_socket, input("Enter a nickname: "))
# send_peer_message(input("What type of message do you want to send: "), input("What is the message"))
# message,address = peer_socket.recvfrom(BUFFER_SIZE)
# print(message.decode())
