import pygame
import random
import time

# Setup
pygame.init()
screen_wight = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_wight, screen_height))
background = pygame.Surface(screen.get_size())


# Rain Drops
class Drop(object):

    __slots__ = ['x', 'y', 'y_speed', 'gravity']

    def __init__(self, x, y, y_speed, gravity):
        self.x = x
        self.y = y
        self.y_speed = y_speed
        self.gravity = gravity

    def fall(self):
        self.y += self.y_speed
        self.y_speed += self.gravity / 10
        if self.y > screen_height:
            self.y = random.randint(-100, 0)
            self.x = random.randint(0, screen_wight)
            self.y_speed = random.randint(3, 10)

    def show(self):
        pygame.draw.line(background,
                         (138, 43, 226),
                         (self.x, self.y),
                         (self.x, self.y + 10))
        screen.blit(background, (0, 0))


# Creating rain drops
all_drops = list()
for i in range(250):
    s_x = random.randint(0, screen_wight)
    s_y = random.randint(-200, 0)
    s_speed = random.randint(3, 10)
    s_gravity = random.randint(0, 2)
    obj = Drop(s_x, s_y, s_speed, s_gravity)
    all_drops.append(obj)


# Main Game Loop
loop = True
while loop:
    start_w = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    background.fill((230, 230, 250))
    background = background.convert()
    start = time.time()
    for drop in all_drops:
        drop.fall()
        drop.show()
    pygame.display.flip()
