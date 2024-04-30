import socket
import os
import sys
import threading as thr
import ip

BUFFER_SIZE = 1024
peer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#peer.connect((10.33.16.1,50578))
IP , PORT = ip.get_ip_address(peer)
print(peer.getsockname())
#IP, PORT = ip.get_ip_address(peer)
#peer.bind((IP, PORT))
#peer.send("Member 1".encode())