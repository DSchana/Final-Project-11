
from pygame import *

size = width, height = 800, 600
screen = display.set_mode(size)

x,y = 400,300
vx= 1
vy = -10
running = True
while running:
    for evnt in event.get():                # checks all events that happen
        if evnt.type == QUIT:
            running = False

    screen.fill((255,255,255))
    x += 1
    y += 1
    x += vx
    vy += 1
    y += vy
    if y>600:
        vy*=-1
    if x<0 or x>800:
        vx*=-1
    draw.circle(screen,(255,0,0),(x,y),10)
    
    display.flip()
    time.wait(20)                        
    
quit()
