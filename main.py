import pygame, os, sys, math
from pygame.locals import *

pygame.init()

#-------------------------global variables----------------------------------------
window_size = width, height = 1200, 450
screen = pygame.display.set_mode(window_size)
speed = 30
clock = pygame.time.Clock()

#background globals
bg = pygame.image.load(os.path.join('images','bg.png')).convert()
bg_x = 0
bg_x2 = bg.get_width()

#bird globals
bird = pygame.image.load(os.path.join('images', 'bird.png'))
bird_x = width/3 - bird.get_width()/2
bird_y = height/2 - bird.get_height()/2

#game globals
logo = pygame.image.load(os.path.join('images', 'logo.png'))
play_button = pygame.image.load(os.path.join('images', 'playbtn.png'))
start = True
menu = False
game_over = False


#----------------------functions-------------------------------------------------

#updates bird
def update_bird():
    global bird_x, bird_y
    screen.blit(bird, (bird_x, bird_y))
    if (bird_y <= 0 or bird_y >= height - bird.get_height()): game_over = True
    elif (pygame.key.get_pressed()[pygame.K_SPACE]): bird_y -= 8
    else: bird_y += 5


#def update_pipe():


#updates and resets scrolling background
def update_background():
    global bg_x, bg_x2
    bg_x -= 1.5
    bg_x2 -= 1.5
    if (bg_x < bg.get_width() * -1):
        bg_x = bg.get_width()
    if (bg_x2 < bg.get_width() * -1):
        bg_x2 = bg.get_width()
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x2, 0))

#updates and checks if user closes applicaiton
def check_close():
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

while ~game_over:
    clock.tick(speed)
    update_background()
    update_bird()

    #start menu until space is pressed
    while (start):
        screen.blit(logo, (width/2 - logo.get_width()/2, height/4 - logo.get_height()))
        screen.blit(play_button, (width/2 - play_button.get_width()/2, height - 150))
        if (pygame.key.get_pressed()[pygame.K_SPACE]): start = False;
        check_close()

    check_close()
