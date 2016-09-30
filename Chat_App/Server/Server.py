# main()

from socket import *
import select, time
# import User, Broadcast

def broadcast(sock, message):
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock: #not master or sender
            try:
                socket.send(message)
            except:
                # Socket connection broken
                socket.close()
                CONNECTION_LIST.remove(socket)


if __name__ == "__main__": #Back to main()
                           #This checks if we are in fact in main(), if so..:

    CONNECTION_LIST = []
    RECV_BUFFER = 4096 # Max amount of packets able to receive.. Don't want an overflow
    PORT = 13337

    #socket(IPv4, TCP)
    server_sock = socket(AF_INET, SOCK_STREAM)
    server_sock.bind(('',PORT))
    server_sock.listen(10)
