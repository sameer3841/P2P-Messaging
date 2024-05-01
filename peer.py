import socket
import os
import sys
import threading as thr
import ip



def member(datatype , nickname):
    BUFFER_SIZE = 1024
    peer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    address, server_address = ip.get_ip_address()
    peer.bind(address)
    print(address)
    print(server_address)
    message = datatype + " " + nickname
    peer.sendto(message.encode(), server_address)
    while True:
        pass
member(input("Enter the type: "), input("Enter a nickname: "))
