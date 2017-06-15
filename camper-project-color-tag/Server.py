import socket
import pickle

VersionF = open("ServerVersion.txt")
Version = VersionF.read()
Version = pickle.dumps([Version, "Server"])
VersionF.close()

s = socket.socket()

Vf = True

while Vf:
    try:
        s.connect(("10.0.0.51", 10001))
        s.send(Version)
        data = s.recv(1024)
        if data.decode() != "1":
            game = open("MainServer.py", "w")
            game.write(data.decode())
            game.close()
        Vf = False
    except:
        Vf = True

from MainServer import *

Server()