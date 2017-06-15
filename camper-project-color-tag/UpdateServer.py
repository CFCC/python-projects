import socket
import _thread
import select

CVersion = "1.0"

s = socket.socket()
s.bind(("10.0.0.51", 10001))

Sockets = []
Sockets.append(s)

done = False

while not done:
    read = select.select(Sockets, [], [])

    for sock in read:
        if sock == s:
            newS, addr = s.accept()
            Sockets.append(newS)

        else:
            try:
                data = sock.recv(1024)
                if data.decode() == CVersion:
                    sock.send("1".encode())
                else:
                    print("not right version")

            except:
                sock.close()
                Sockets.remove(sock)

