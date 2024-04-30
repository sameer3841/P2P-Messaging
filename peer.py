import socket
import os
import sys
import threading as thr
import ip

server_address = ("10.33.16.1", 1200)
BUFFER_SIZE = 1024
peer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IP, PORT = ip.get_ip_address(peer)
print(IP, PORT)
peer.sendto("Member 1".encode(), server_address)
