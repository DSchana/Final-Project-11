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

    keys = key.get_pressed()
     
    if keys[K_RIGHT]:
        angle -= 2
    elif keys[K_LEFT]:
        angle += 2
    screen.fill((100,200,200))
    rotPic = transform.rotate(zap,angle)
    screen.blit( rotPic, (200,100))
    display.flip()
    time.wait(10)

quit()
