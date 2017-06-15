import socket
import select
import pickle

CVersion = "1.0"

s = socket.socket()
s.bind((socket.gethostname(), 10001))
s.listen(0)

Sockets = []
Sockets.append(s)

done = False

while not done:
    read = select.select(Sockets, [], [])[0]
    for sock in read:
        if sock == s:
            newS, addr = s.accept()
            Sockets.append(newS)
            print(addr)

        else:
            try:
                data = pickle.loads(sock.recv(1024))
                print(data)
                if data[0] == CVersion:
                    sock.send("1".encode())
                    print("correct version")
                else:
                    if data[1] == "Client":
                        print("incorrect client")
                        Game = open("MainGame.py")
                        GameC = Game.read()
                        Game.close()
                        sock.send(GameC.encode())
                    else:
                        Server = open("MainServer.py")
                        print("incorrect server")
                        ServerC = Server.read()
                        Server.close()
                        sock.send(ServerC.encode())

                sock.close()
                Sockets.remove(sock)

            except:
                sock.close()
                Sockets.remove(sock)

