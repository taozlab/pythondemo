import pygame, random
from pygame.locals import *
pygame.init()
clock=pygame.time.Clock()

screen=pygame.display.set_mode([800,600],FULLSCREEN)
pygame.mouse.set_visible(False)
pygame.display.set_caption("Fish Game")

rotate=pygame.transform.rotozoom

fish=pygame.image.load("e.gif").convert_alpha()
fishes=[rotate(fish,0,1),rotate(fish,90,2),rotate(fish,180,3),rotate(fish,270,0.5)]
bkcol=[0,0,0]
fx=0;fy=0
delta=20

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:run=False
            if event.key==pygame.K_LEFT:fish=fishes[0]
            if event.key==pygame.K_RIGHT:fish=fishes[2]
            if event.key==pygame.K_UP:fish=fishes[3]
            if event.key==pygame.K_DOWN:fish=fishes[1]
        if event.type==pygame.KEYUP:
            fx+=delta;fy+=delta
            if fx>=800: fx=0
            if fy>=600: fy=0 

    screen.fill(bkcol)
    screen.blit(fish,[fx,fy]) 
    pygame.display.update();clock.tick(100)
pygame.quit()
