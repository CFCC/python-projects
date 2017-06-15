import socket
import pickle

VersionF = open("ClientVersion.txt")
Version = VersionF.read()
Version = pickle.dumps([Version, "Client"])
VersionF.close()

s = socket.socket()

Vf = True

while Vf:
    try:
        s.connect(("10.0.0.51", 10001))
        s.send(Version)
        data = s.recv(1024)
        if data.decode() != "1":
            game = open("MainGame.py", "w")
            game.write(data)
            game.close()
        Vf = False
    except:
        Vf = True

from MainGame import *

Game()
