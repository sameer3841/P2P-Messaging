import socket
import os
import sys
import threading as thr
import ip


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #s.connect(("8.8.8.8", 80))
    server_address = ("127.0.0.1", 12000)
    s.connect(server_address)
    return s.getsockname() , server_address

BUFFER_SIZE = 1024
peer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

address, server_address = get_ip_address()
peer.bind((address))
print(address)
print(server_address)
peer.sendto("Member 1".encode(), server_address)
print("sent")
