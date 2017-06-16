def Game():

    name = input("Choose a player name: ")
    server = input("Connect to: ")


    import pygame
    import _thread
    import pickle
    import socket

    s = socket.socket()
    s.connect((server, 10000))

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

    class player(pygame.sprite.Sprite):
        def __init__(self, team, width, height):
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.team = team
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
            try:
                self.team = Information[1][0][0]
            except:
                None
            if self.team == 0:
                self.image.fill((255, 0, 0))

            elif self.team == 1:
                self.image.fill((255, 255, 0))

            elif self.team == 2:
                self.image.fill(0, 0, 255)

            if self.team == 0:
                self.image.fill((255, 0, 0))

            elif self.team == 1:
                self.image.fill((255, 255, 0))

            elif self.team == 2:
                self.image.fill(0, 0, 255)


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
    players = pygame.sprite.Group()
    players.add(user)
    while not done:
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
        screen.fill(BLACK)

        players.update()
        players.draw(screen)

        pygame.display.flip()

        clock.tick()
    pygame.quit()

# [[x, y, who was hit], [[team, shield],[name ,l ,x ,y ,team, shield]]]
