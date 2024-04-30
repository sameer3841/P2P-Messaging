import socket
import os
import sys
import threading as thr

def get_ip_address(s : socket.socket):
    s.connect(("8.8.8.8", 80))
    return s.getsockname()

# s.bind(get_ip_address(s))

BUFFER_SIZE = 1024
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IP , PORT = get_ip_address(server_socket)
#server_socket.listen(5)
print(f'Server ready and listening on {IP}:{PORT}')
clients = {} #List of clients, values should be tuples of IP and Ports
try:
    while True:
        pass
except KeyboardInterrupt as ki:
    pass
#finally:
#    server_socket.close()
def receive():
    pass
def send():# Probably gonna need multiple send and receive for each type
    pass