# levelRun.py
from pygame import *
import pickle
import os

def drawAll(screen, guyX, guyY):
    screen.blit(back, (0,0))
    draw.circle(screen, (255,0,0), (guyX*20+10, guyY*20+10),8)
    display.flip()

def loadMap(fname):
    if fname in os.listdir("."):
        myPFile = open(fname, "rb")        # load my board that I pickled
        return pickle.load(myPFile)       
    else:
        return [[0]*SCREENY for x in range(SCREENX)]
        
size = width, height = 800, 500
screen = display.set_mode(size)

SCREENX = 40
SCREENY = 25
guyX, guyY = 20, 3

current = 1
back = image.load("map1.bmp")

level = loadMap("level1.p")
running = True
myClock = time.Clock()
while running:
    for evnt in event.get():               
        if evnt.type == QUIT:
            running = False

    oldX, oldY = guyX, guyY
    keys = key.get_pressed()                # Basic arrows    
    if keys[K_LEFT]  : guyX -= 1
    if keys[K_RIGHT] : guyX += 1
    if keys[K_UP]    : guyY -= 1
    if keys[K_DOWN]  : guyY += 1

    if level[guyX][guyY] == 0:          # For now the only values in the grid that matter
        guyX, guyY = oldX, oldY         # are 0/non-0. 0 is impassable
    
    drawAll(screen, guyX, guyY)
    myClock.tick(20)                        
    
quit()

