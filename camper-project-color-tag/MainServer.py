def Server():

    import pickle
    import _thread
    import random
    import socket
    import select

    s = socket.socket()
    s.bind((socket.gethostname(), 10000))
    s.listen(0)

    Version = "1.0"

    ServerV = open("ServerVersion.txt", "w")
    ServerV.write(Version)
    ServerV.close()

    def Player_Join(s):
        global done
        while not done:
            read = select.select([s], [], [])[0]

            for x in read:
                newS, addr = x.accept()
                _thread.start_new_thread(Comunicate, (newS, addr))
                print(addr)




    def Comunicate(s, addr):
        global Information
        global done
        dis = False
        name = s.recv(1024).decode()
        l = len(Information)
        Information.append([None, None])
        T = random.randint(0,2)
        All.append([l, T, name, 0])

        print(name)

        while (not done) and (not dis):
            try:
                s.send(pickle._dumps(Information[l][0]))
                Information[l][1] = pickle.loads(s.recv(1024))
            except:
                s.close()
                Information[l] = ["disconnected", "disconnected"]
                dis = True

    All = []

    global Information
    Information = []

    global done
    done = False

    _thread.start_new_thread(Player_Join, (s, ))
    while not done:
        for x in All:
            try:
                if Information[x[0]] != [None, None] and Information[x[0]] != ["disconnected", "disconnected"]:
                    print(Information)
                    info = Information[x[0]][1]
                    if info[2] != None:
                        if info[2] == Information[info[2]][1][2]:
                            newTeam = x[1]+1
                            if newTeam > 2:
                                newTeam = 0
                            All[info[2]][1] = newTeam
            except:
                None



# did it colide?
# if so check what it colided with
# it it also colided, change teams and activate a shield
# send it everyone's [team, shield],[[name ,l ,x ,y ,team, shield],...]


# recv = [x, y, who was hit]
# all [l, t, name, shield]
