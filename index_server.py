import socket
import threading

BUFFER_SIZE = 1024
IP, PORT = "127.0.0.1", 12000
clients = {}


def enter(peer_socket):
    nickname = peer_socket.recv(BUFFER_SIZE).decode()
    return nickname


def remove(address):  # We could make this target the peer instead of the address
    for x in clients.keys():
        if clients.get(x) == address:
            print(x + " left the network")
            clients.pop(x)
            break


def sender(message, recv_IP, recv_PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # To be deleted
    sock.connect((recv_IP, recv_PORT))
    sock.sendto(message.encode(), (recv_IP, recv_PORT))


# def connect_peer(peer_address):
#     a_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     a_socket.bind(peer_address)
#     return a_socket


def service_peer_connection(a_socket, address):
    nickname = enter(a_socket)
    clients.update({nickname: address})
    print(f"{nickname} connected from {address}.")
    a_socket.send(b"Welcome to the server!\n")

    while True:
        message = a_socket.recv(BUFFER_SIZE)
        message = message.decode().upper()

        if message == 'S':
            print("Sending Message")
            a_socket.send(b"Who would you like to chat with?")
            user = a_socket.recv(BUFFER_SIZE)
            user = user.decode()
            print(user)
            peer_address = clients.get(user)
            if (peer_address == None):
                a_socket.send(b"Sorry, there is no user by that name.")
            else:
                peer_ip, peer_port = peer_address
                # connect_peer((peer_ip, peer_port))
                ########################################################
                a_socket.send(f"{user} {peer_ip} {peer_port}".encode())
                ########################################################
        elif message == 'G':
            a_socket.send(str(clients).encode())
        elif message == 'A':
            pass
        elif message == 'L':
            remove(address)
            a_socket.close()
            break
        else:
            pass


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print(f'Server ready and listening on {IP}:{PORT}')

    try:
        while True:
            peer_socket, address = server_socket.accept()
            print(f"Connection from {address} has been established.")
            t1 = threading.Thread(target=service_peer_connection, args=(peer_socket, address,))
            t1.start()

    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server_socket.close()
        print("Cleaned up all connections.")


if __name__ == "__main__":
    main()


# finally:
#    server_socket.close()
def receive(a_socket):
    msg = a_socket.recv(BUFFER_SIZE)


def send():  # Probably gonna need multiple send and receive for each type
    pass
