import socket
import os
import sys
import threading as thr
import ip

BUFFER_SIZE = 1024
IP, PORT = "127.0.0.1", 12000


# def remove(address):
#     for x in clients.keys():
#         if clients.get(x) == address:
#             clients.pop(x)
#             return 1
#     print("Address not found")


def enter(peer_socket):
    """Receive the client's nickname from the socket."""
    nickname = peer_socket.recv(1024).decode('utf-8')
    return nickname.strip()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print(f'Server ready and listening on {IP}:{PORT}')

    clients = {}

    try:
        while True:
            peer_socket, address = server_socket.accept()
            print(f"Connection from {address} has been established.")

            nickname = enter(peer_socket)
            clients.update({nickname: address})
            print(f"{nickname} connected from {address}.")
            peer_socket.send(b"Welcome to the server!\n")

            # Here, add handling for additional data from clients if necessary
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server_socket.close()
        for nickname, (sock, _) in clients.items():
            sock.close()
        print("Cleaned up all connections.")


if __name__ == "__main__":
    main()


# finally:
#    server_socket.close()
def receive():
    pass


def send():  # Probably gonna need multiple send and receive for each type
    pass
