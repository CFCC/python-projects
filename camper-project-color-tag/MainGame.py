def Game():

    import pygame
    import _thread
    import pickle

    def ServerC(s):
        global Information
        dis = False
        while not done or not dis:
            try:
                Information[1] = pickle.loads(s.recv(1024))
                s.send(pickle.dumps(Information[0]))
            except:
                dis = True
                Information = "disconnected"


    Information = [[], []]
    global Information

    Version = "1.0"

    VersionF = open("ClientVersion.txt", "w")
    VersionF.write(Version)
    VersionF.close()

    class player(pygame.sprite.Sprite):
        def __init__(self, color, width, height, team):
            super.__init__()
            self.image=pygame.Surface([width, height])
            self.image.fill(WHITE)
            self.change_x = 0
            self.change_y = 0
            self.rect = self.image.getRect()
            self.team = team

        def update(self):
            self.rect.x += self.change_x
            self.rect.y += self.change_y

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
    done = False
    global done
    clock = pygame.time.Clock()
    user = player(WHITE, 10, 10, 0)
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

        pygame.display.flip()

        clock.tick()
    pygame.quit()