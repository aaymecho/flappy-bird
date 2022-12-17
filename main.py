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


#bird animation
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'images/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.image = pygame.image.load(('images/bird1.png'))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    #controls animation cycle
    def update(self):
        self.counter += 1
        flap_speed = 10

        if self.counter > flap_speed:
            self.counter = 0
            self.index += 1
            if (self.index >= len(self.images)):
                self.index = 0
        self.image = self.images[self.index]



bird_vector = pygame.sprite.Group()
flapping_bird = Bird(100, height/2)
bird_vector.add(flapping_bird)


running = True
while running:
    clock.tick(clock_speed)

    #draws background
    screen.blit(bg, (0,0))

    #draws scrolling floor
    screen.blit(floor, (floor_scroll, 769))
    floor_scroll -= scroll_speed
    if (abs(floor_scroll) > 34):
        floor_scroll = 0

    #draws vector of birds
    bird_vector.draw(screen)
    bird_vector.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()