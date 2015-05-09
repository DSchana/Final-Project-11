from pygame import *
from math import *
from random import *
    
screen = display.set_mode((1024,768))


zap = image.load("zapdos.png")
angle = 0
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            makeTerrain()

    mx,my = mouse.get_pos()

    angle = degrees(atan2(mx-400,my-300))-90
    screen.fill((100,200,200))
    rotPic = transform.rotate(zap,angle)
    screen.blit( rotPic, (400-rotPic.get_width()//2,300-rotPic.get_height()//2))
    display.flip()
    time.wait(10)

quit()
