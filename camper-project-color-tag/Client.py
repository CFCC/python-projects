import socket
import pygame
import pickle
version = "1.0"
pygame.init()
WHITE = (255, 255, 255)
size = (1000, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Color Tag")
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    pygame.display.flip()

    clock.tick(60)
pygame.quit()
