def Server():

    import pickle
    import _thread
    import random

    Version = "1.0"

    ServerV = open("ServerVersion.txt", "w")
    ServerV.write(Version)
    ServerV.close()

    def Player_Join(s):
        global done
        while not done:
            newS, addr = s.accept()
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

        while (not done) or dis:
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


    _thread.start_new_thread(Player_Join, ())
    while not done:
        for x in All:
            info = Information[x[0]][1]
            if info[2] > -1:
                if info[2] == Information[info[2]][1][2]:
                    newTeam = x[1]+1
                    if newTeam > 2:
                        newTeam = 0
                    All[info[2]][1] = newTeam



# did it colide?
# if so check what it colided with
# it it also colided, change teams and activate a shield
# send it everyone's [team, shield][name ,l ,x ,y ,team, shield]


# recv = [x, y, who was hit]
# all [l, t, name, shield]