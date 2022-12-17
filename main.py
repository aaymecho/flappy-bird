import pygame, os, random
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
clock_speed = 60

screen_size = width, height = 864, 936
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Flappy Bird')


#vars for game
floor_scroll = 0
scroll_speed = 3

#images loaded
bg = pygame.image.load(os.path.join('images', 'bg.png'))
floor = pygame.image.load(os.path.join('images', 'floor.png'))

running = True

while running:
    clock.tick(clock_speed)

    #draws background
    screen.blit(bg, (0,0))

    #draws scrolling floor
    screen.blit(floor, (floor_scroll, height))
    floor_scroll -= scroll_speed

    if (abs(floor_scroll) > 34):
        floor_scroll = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()