import socket
import os
import sys
import threading as thr
import ip

BUFFER_SIZE = 1024
IP, PORT = "127.0.0.1", 12000
clients = {}


def enter(peer_socket):
    nickname = peer_socket.recv(BUFFER_SIZE).decode()
    return nickname


def remove(address):
    for x in clients.keys():
        if clients.get(x) == address:
            clients.pop(x)
            return 1
    print("Address not found")


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print(f'Server ready and listening on {IP}:{PORT}')

    try:
        while True:
            peer_socket, address = server_socket.accept()
            print(f"Connection from {address} has been established.")

            nickname = enter(peer_socket)
            clients.update({nickname: address})
            print(f"{nickname} connected from {address}.")
            peer_socket.send(b"Welcome to the server!\n")
            message = peer_socket.recv(BUFFER_SIZE)
            message = message.decode()
            message_type = message[0].upper()
            message = message[1:]
            if message_type == 'S':
                pass
            elif message_type == 'G':
                peer_socket.send(str(clients).encode())
                pass
            elif message_type == 'A':
                pass
            elif message_type == 'L':
                remove(address)
                peer_socket.send(b'You closed the connection ')
                peer_socket.close()



    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server_socket.close()
        print("Cleaned up all connections.")


if __name__ == "__main__":
    main()


# finally:
#    server_socket.close()
def receive():
    pass


def send():  # Probably gonna need multiple send and receive for each type
    pass
