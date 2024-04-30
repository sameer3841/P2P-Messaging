import socket
import os
import sys
import threading as thr
import ip




BUFFER_SIZE = 1024
peer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

address, server_address = ip.get_ip_address()
peer.bind((address))
print(address)
print(server_address)
peer.sendto("Member 2".encode(), server_address)
print("sent")
while True:
    pass
