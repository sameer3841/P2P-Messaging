import socket
import os
import sys
import threading as thr


def get_ip_address(s: socket.socket):
    #s.connect(("8.8.8.8", 80))
    s.connect(("10.33.16.1", 1200))
    return s.getsockname()