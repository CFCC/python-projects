import socket
import pickle



try:
    VersionF = open("ServerVersion.txt")
    Version = pickle.dumps([VersionF.read(), "Server"])
    VersionF.close()
except:
    open("ServerVersion.txt", "w").close()

s = socket.socket()

Vf = True

update = "Y"

while Vf:
    try:
        s.connect(("10.0.0.51", 10001))
        s.send(Version)
        data = s.recv(7000)
        if data.decode() != "1":
            waiting = True
            update = input("Outdated Client. Permission to update? (Y/N): ").upper()
            while waiting:
                if update == "Y":
                    game = open("MainServer.py", "w")
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

from MainServer import *
if update == "Y":
    print("Starting Server")
    Server()