import socket
import os
import threading

def get_ip_address(s : socket.socket):
    s.connect(("8.8.8.8", 80))
    return s.getsockname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(get_ip_address(s))
# s.bind(get_ip_address(s))
print("Binded")