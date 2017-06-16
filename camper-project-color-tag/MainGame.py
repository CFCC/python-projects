def Game():

    name = input("Choose a player name: ")


    import pygame
    import _thread
    import pickle
    import socket

    s = socket.socket()
    connected = False
    while not connected:
        try:
            server = input("Connect to: ")
            s.connect((server, 10000))
            connected = True
        except Exception as e:
            print("Could not connect")
            print(e)

    def ServerC(s):
        global Information
        dis = False
        s.send(name.encode())
        while (not done) and (not dis):
            try:
                Information[1] = pickle.loads(s.recv(1024))
                s.send(pickle.dumps(Information[0]))
            except:
                dis = True
                Information = "disconnected"


    global Information
    Information = [[None, None, None], []]

    Version = "1.0"

    VersionF = open("ClientVersion.txt", "w")
    VersionF.write(Version)
    VersionF.close()
    class Oplayer(pygame.sprite.Sprite):
        def __init__(self, width, height):
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.team = 0
            self.shield = 0
            self.name = ""
            self.rect = self.image.get_rect()
            self.id = 0

        def update(self):
            if self.team == 0:
                self.image.fill((255, 0, 0))

            elif self.team == 1:
                self.image.fill((255, 255, 0))

            elif self.team == 2:
                self.image.fill((0, 0, 255))


    class player(pygame.sprite.Sprite):
        def __init__(self, team, width, height):
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.team = team
            self.shield = 0
            if self.team == 0:
                self.image.fill((255, 0, 0))

            elif self.team == 1:
                self.image.fill((255, 255, 0))

            elif self.team == 2:
                self.image.fill(0, 0, 255)

            self.change_x = 0
            self.change_y = 0
            self.rect = self.image.get_rect()


        def update(self):
            self.rect.x += self.change_x
            self.rect.y += self.change_y
            Information[0][0] = self.rect.x
            Information[0][1] = self.rect.y

            collideList = pygame.sprite.spritecollide(self, players, False)
            for x in collideList:
                if x.shield == 0 and self.shield == 0:
                    if self.team - x.team == 1 or (x.team == 2 and self.team == 0):
                        Information[0][2] = x.id
                        print("collided with", x.name, self.team, x.team)

            try:
                self.team = Information[1][0][0]
                self.shield = Information[1][0][1]
            except:
                None
            if self.team == 0:
                self.image.fill((255, 0, 0))

            elif self.team == 1:
                self.image.fill((255, 255, 0))

            elif self.team == 2:
                self.image.fill((0, 0, 255))


        def editChange_x(self, num):
            self.change_x += num

        def editChange_y(self, num):
            self.change_y += num

    pygame.init()
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    size = (1000, 800)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Color Tag")

    global done
    done = False

    _thread.start_new_thread(ServerC, (s, ))

    clock = pygame.time.Clock()
    user = player(0, 10, 10)
    player = pygame.sprite.Group()
    player.add(user)
    players = pygame.sprite.Group()
    playersL = []
    while not done:
        try:
            lenI = len(Information[1][1])
            if lenI > len(players):
                for x in range(lenI - len(players)):
                    p = Oplayer(10, 10)
                    players.add(p)
                    playersL.append(p)
            if lenI < len(players):
                for x in range(len(players) - lenI):
                    players.remove(playersL[0])
                    playersL.remove(playersL[0])

        except:
            None

        for z in range(len(playersL)):
            playersL[z].rect.x = Information[1][1][z][2]
            playersL[z].rect.y = Information[1][1][z][3]
            playersL[z].team = Information[1][1][z][4]
            playersL[z].shield = Information[1][1][z][5]
            playersL[z].id = Information[1][1][z][1]
            playersL[z].name = Information[1][1][z][0]


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    user.editChange_x(-1)
                if event.key == pygame.K_RIGHT:
                    user.editChange_x(1)
                if event.key == pygame.K_UP:
                    user.editChange_y(-1)
                if event.key == pygame.K_DOWN:
                    user.editChange_y(1)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    user.editChange_x(1)
                if event.key == pygame.K_RIGHT:
                    user.editChange_x(-1)
                if event.key == pygame.K_UP:
                    user.editChange_y(1)
                if event.key == pygame.K_DOWN:
                    user.editChange_y(-1)
        screen.fill(WHITE)
        player.update()
        player.draw(screen)
        players.update()
        players.draw(screen)

        pygame.display.flip()

        clock.tick(60)
    pygame.quit()

# [[x, y, who was hit], [[team, shield],[[name ,l ,x ,y ,team, shield]]]