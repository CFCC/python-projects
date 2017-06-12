# Import the necessary libraries
import socket
import sys
import select


# Take message from an host and send it to all others
def shout(sock, message):
    for socket in LIST:
        try:
            # Don't send it back to server and yourself!
            if socket != serv and socket != sock:
                socket.send(message)
        except:
            # Assume client has got disconnected and remove it.
            socket.close
            LIST.remove(socket)


# Declare variables required later.

# To store list of sockets of clients as well as server itself.
LIST = []

# Common buffer for all purposes
buff = 1024

# Declaration of Server socket.
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv.bind(("10.0.0.165", 1356))

# Listen for upto 6 clients. Increase if you need more.
serv.listen(6)

# Add server socket to the LIST
LIST.append(serv)

while 1:
    # Moniter clients all simultaneously
    reads, writes, err = select.select(LIST, [], [])

    for sock in reads:

        # A new client connected?
        if sock == serv:
            sockfd, addr = serv.accept()
            LIST.append(sockfd)

        # Naah, just a new message!
        else:
            try:

                # Get his message.
                data = sock.recv(buff)
                if data:
                    # If he wrote something, send it to shout() function for broadcast.
                    shout(sock, data)
            except:

                # Things just got real. Client kicked by server :3
                sock.close()
                LIST.remove(sock)

                # Do this till the end of time.
                continue
serv.close()