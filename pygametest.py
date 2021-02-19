import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
color = (128, 128, 128)
screen.fill(color)
pygame.display.flip()

circle(screen, (255, 255, 0), (300, 300), 150)
circle(screen, (255, 0, 0), (230, 265), 30)
circle(screen, (255, 0, 0), (370, 265), 24)
circle(screen, (0, 0, 0), (230, 265), 15)
circle(screen, (0, 0, 0), (370, 265), 12)
rect(screen, (0, 0, 0), (220, 375, 160, 30), 0)
rect(screen, (0, 0, 0), (220, 375, 160, 30), 0)
polygon(screen, 'black', [(170, 175), (180, 155), (300, 230), (290, 250)])
polygon(screen, 'black', [(450, 180), (440, 170), (330, 240), (340, 250)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()