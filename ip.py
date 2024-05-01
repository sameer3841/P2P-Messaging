import socket
import os
import sys
import threading as thr


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #s.connect(("8.8.8.8", 80))
    server_address = ("127.0.0.1", 12000)
    s.connect(server_address)
    return s.getsockname() , server_address