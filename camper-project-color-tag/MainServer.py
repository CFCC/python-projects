def Server():

    Version = "1.0"

    ServerV = open("ServerVersion.txt", "w")
    ServerV.write(Version)
    ServerV.close()
    print("hello world")