import os, pygame;from pygame.locals import *
pygame.init();clock=pygame.time.Clock()
os.environ['SDL_VIDEO_WINDOW_POS']='center'
pygame.display.set_caption("Three Surfaces")
pygame.mouse.set_visible(0)
screen=pygame.display.set_mode([400,200],0,32)
sky=pygame.Surface((400,200))
sky.fill((200,255,255))

grass=pygame.Surface((400,100))
grass.fill((50,150,50))

sun=pygame.Surface((40,40))
sun.set_colorkey([0,0,0])
sun.set_alpha(50)
pygame.draw.circle(sun,(255,255,0),(20,20),20)

screen.blit(sky,(0,0))
screen.blit(sun,(180,30))
screen.blit(grass,(0,100))


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    mousex,mousey=pygame.mouse.get_pos()
    screen.blit(sky,(0,0))
    screen.blit(sun,(mousex,mousey))
    screen.blit(grass,(0,100))
    
    pygame.display.update()

pygame.display.update()
pygame.time.wait(10000)
