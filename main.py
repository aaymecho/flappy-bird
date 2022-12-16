import pygame
from pygame.locals import *
import os
import sys
import math

pygame.init()


window_size = width, height = 1200, 450
screen = pygame.display.set_mode(window_size)
speed = 30

bg = pygame.image.load(os.path.join('images','bg.png')).convert()
bgX = 0
bgX2 = bg.get_width()
clock = pygame.time.Clock()


while True:
    #allows user to close the application
    clock.tick(speed)
    bgX -= 1.5
    bgX2 -= 1.5

    #updates and resets scrolling background
    if (bgX < bg.get_width() * -1):
        bgX = bg.get_width()
    if (bgX2 < bg.get_width() * -1):
        bgX2 = bg.get_width()
        
    screen.blit(bg, (bgX, 0))
    screen.blit(bg, (bgX2, 0))
    pygame.display.update()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: sys.exit()

        