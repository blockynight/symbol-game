# Trying out some pygame stuff.

import sys, pygame
pygame.init()

size = width, height = 600, 200
speed = [1, 1]
black = 0, 0, 0
grey = 100, 100, 100
red = (255, 0, 0)
boxh = 50
boxw = 50
box = width / 2 - boxw / 2, height / 2 - boxh / 2, boxh, boxw

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.draw.rect(screen, grey, box)
    pygame.display.flip()

