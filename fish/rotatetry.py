import pygame, random
from pygame.locals import *
pygame.init()
clock=pygame.time.Clock()

screen=pygame.display.set_mode([800,600])

pygame.display.set_caption("Eye Testing")
bkcol=[0,0,0]

font=pygame.font.Font(None,120)
Eat=font.render("E",1,(255,255,255))
angle=0
run=True

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:angle=180
            if event.key==pygame.K_RIGHT:angle=0
            if event.key==pygame.K_UP:angle=270
            if event.key==pygame.K_DOWN:angle=90
            Eat=pygame.transform.rotate(Eat,angle)
        screen.fill(bkcol)
        screen.blit(Eat,[36,150])
    pygame.display.update();clock.tick(100)
pygame.quit()
