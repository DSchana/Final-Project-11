# pygameRev1.py
from pygame import *
import os
import pickle

def drawAll(screen, level):
    screen.blit(back, (0,0))
    for x in range(SCREENX):
        for y in range(SCREENY):
            c = level[x][y]
            if c > 0:
                draw.rect(screen, col[c], (x*20, y*20, 17, 17))    

def loadMap(fname):
    if fname in os.listdir("."):
        myPFile = open(fname, "rb")        # load my board that I pickled
        return pickle.load(myPFile)       
    else:
        return [[0]*SCREENY for x in range(SCREENX)]
    
def saveMap(level, fname):
    myPFile = open("level1.p", "wb")
    pickle.dump(level, myPFile)
        
size = width, height = 800, 500
screen = display.set_mode(size)
col = [(0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255)]
SCREENX = 40
SCREENY = 25

current = 1     # my current paint colour / contents
back = image.load("map1.bmp")

level = loadMap("level1.p")
running = True
myClock = time.Clock()
while running:
    for evnt in event.get():                # checks all events that happen
        if evnt.type == QUIT:
            running = False
            
    keys = key.get_pressed()                # get numbers from KB
    for i in range(8):
        if keys[i+48]:
            current = i
        
    if mouse.get_pressed()[0]==1:
        mx, my = mouse.get_pos()
        gx = mx // 20
        gy = my // 20
        level[gx][gy] = current
        draw.rect(screen, col[level[gx][gy]], (gx*20, gy*20, 17, 17))
        
    drawAll(screen, level)
    display.flip()

    myClock.tick(60)                        
    
quit()
saveMap(level, "level1.p")
