import socket
import pickle



try:
    VersionF = open("ClientVersion.txt")
    Version = VersionF.read()
    Version = pickle.dumps([Version, "Client"])
    VersionF.close()
except:
    open("ClientVersion.txt", "w").close()

VersionF = open("ClientVersion.txt")
Version = VersionF.read()
Version = pickle.dumps([Version, "Client"])
VersionF.close()


s = socket.socket()

Vf = True

update = "Y"

while Vf:
    try:
        s.connect(("192.168.0.13", 10001))
        s.send(Version)
        data = s.recv(7000)
        if data.decode() != "1":
            waiting = True
            update = input("Outdated Client. Permission to update? (Y/N): ").upper()
            while waiting:
                if update == "Y":
                    game = open("MainGame.py", "w")
                    game.write(data.decode())
                    game.close()
                    waiting = False
                elif update == "N":
                    waiting = False
                else:
                    update = input("That was not an option. Please choose a (Y/N): ")

        Vf = False
    except:
        Vf = True

from MainGame import *

if update == "Y":
    print("Client Starting")
    Game()
