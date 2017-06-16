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
    change_x = 0
    change_y = 0
    player_x = 0
    player_y = 0
    class player(pygame.sprite.Sprite):
        def __init__(self, color, width, height):
            super.__init__()
            self.image=pygame.Surface([width, height])
            self.image.fill(WHITE)
        def update(self):
            player_x+=change_x
            player_y+=change_y
            pygame.draw.rect(self.image, color, [player_x, player_y, width, height])

    pygame.init()
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    size = (1000, 800)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Color Tag")
    done = False
    global done
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x -= 1
                if event.key == pygame.K_RIGHT:
                    change_x += 1
                if event.key == pygame.K_UP:
                    change_y -= 1
        screen.fill(WHITE)

        pygame.display.flip()

        clock.tick()