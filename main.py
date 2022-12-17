import pygame, os, random
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
clock_speed = 60

screen_size = width, height = 864, 936
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Flappy of the Bird')


#vars for game
floor_scroll = 1
scroll_speed = 3
fly_status = False
game_over = False
pipe_distance = 100
pipe_timer = 2000
previous_pipe = pygame.time.get_ticks() - pipe_timer
score = 0
passed_pipe = False
t_font = pygame.font.SysFont('Arial', 50)
white = (255, 255, 255)

#images loaded
bg = pygame.image.load(os.path.join('images', 'bg.png'))
floor = pygame.image.load(os.path.join('images', 'floor.png'))

def display_text(text, t_font, t_color, x, y):
    image = t_font.render(text, True, t_color)
    screen.blit(image, (x, y))
    


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
        self.grav = 0
        self.mouse_trigger = False

    #controls animation cycle
    def update(self):
        if (fly_status == True):
            self.grav += 0.5
            #gravity limiter
            if (self.grav == 6):
                self.grav = 6
            if (self.rect.bottom) < 768:  
                self.rect.y += int(self.grav)
        if (game_over == False):
            #jump control
            if (pygame.mouse.get_pressed()[0] == 1 and self.mouse_trigger == False):
                self.grav = -9
                self.mouse_trigger = True
            if (pygame.mouse.get_pressed()[0] == 0 and self.mouse_trigger == True):
                self.mouse_trigger = False

            self.counter += 1
            flap_speed = 10

            if (self.counter > flap_speed):
                self.counter = 0
                self.index += 1
                if (self.index >= len(self.images)):
                    self.index = 0
            self.image = self.images[self.index]

            #rotation of bird
            self.image = pygame.transform.rotate(self.images[self.index], self.grav * -3)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/pipe.png')
        self.rect = self.image.get_rect()
        #positioning of pipe
        if (position == 1):
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - pipe_distance]
        if (position == -1):
            self.rect.topleft = [x, y + pipe_distance]
    
    def update(self):
        self.rect.x -= scroll_speed
        #deletes pipe when out of bounds
        if (self.rect.right < 0):
            self.kill()


bird_vector = pygame.sprite.Group()
flapping_bird = Bird(100, height/2)
bird_vector.add(flapping_bird)

pipe_vector = pygame.sprite.Group()

running = True
while running:
    clock.tick(clock_speed)

    #draws background
    screen.blit(bg, (0,0))

    #draws vector of birds
    bird_vector.draw(screen)
    bird_vector.update()
    pipe_vector.draw(screen)

    #draws floor
    screen.blit(floor, (floor_scroll, 768))

    #score counter
    if (len(pipe_vector) > 0):
        if (bird_vector.sprites()[0].rect.left > pipe_vector.sprites()[0].rect.left and bird_vector.sprites()[0].rect.right < pipe_vector.sprites()[0].rect.right and passed_pipe == False):
            passed_pipe = True
        if (passed_pipe == True):
            if (bird_vector.sprites()[0].rect.left > pipe_vector.sprites()[0].rect.right):
                score += 1
                passed_pipe = False
    display_text(str(score), t_font, white, width/2, 20)
    print(score)

    #condition for bird touching the ground
    if (flapping_bird.rect.bottom > 769):
        game_over = True
        fly_status = False
    #pipe collision detection
    if (pygame.sprite.groupcollide(bird_vector, pipe_vector, False, False) or flapping_bird.rect.top < 0):
        game_over = True

    if (game_over == False and fly_status == True):
        #generating pipes
        current_timer = pygame.time.get_ticks()
        if (current_timer - previous_pipe > pipe_timer):
            random_height = random.randint(-100, 100)
            bottom_pipe = Pipe(width, height/2 + random_height, -1)
            top_pipe = Pipe(width, height/2 + random_height, 1)
            pipe_vector.add(bottom_pipe, top_pipe)
            previous_pipe = current_timer
            #scroll_speed += 1
        

        #scrolling floor
        floor_scroll -= scroll_speed
        if (abs(floor_scroll) > 34):
            floor_scroll = 0
        pipe_vector.update()

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        if (event.type == pygame.MOUSEBUTTONDOWN and fly_status == False and game_over == False):
            fly_status = True
    pygame.display.update()
pygame.quit()