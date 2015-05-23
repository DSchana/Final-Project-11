#sprites.py
#This file contains the code to control the sprites

#def spriteMovement ():

from pygame import*
screen = display.set_mode((850,600))

#NOTE TO SELF: REMEMBER TO ADD IN THE IDLE ANIMATION and also diagonal sprites and put into a function
#Put this in the loading screen to load these sprites. fix sprites using clock and tick 

#The following lists store the sprites for movement 
rightWalkSpriteList = []
for i in range(9):
    rightWalkSpriteList.append(image.load("walkRight\\walkRight" + str(i) + ".png"))
leftWalkSpriteList = []
for i in range(9):
    leftWalkSpriteList.append(image.load("walkLeft\\walkLeft" + str(i) + ".png"))
upWalkSpriteList = []
for i in range(9):
    upWalkSpriteList.append(image.load("walkUp\\walkUp" + str(i) + ".png"))
downWalkSpriteList = []
for i in range(9):
    downWalkSpriteList.append(image.load("walkDown\\walkDown" + str(i) + ".png"))
rightUpWalkSpriteList = []
for i in range(9):
    rightUpWalkSpriteList.append(image.load("walkUpRight\\walkUpRight" + str(i) + ".png"))
rightDownWalkSpriteList = []
for i in range(9):
    rightDownWalkSpriteList.append(image.load("walkDownRight\\walkDownRight" + str(i) + ".png"))
leftUpWalkSpriteList = []
for i in range(9):
    leftUpWalkSpriteList.append(image.load("walkUpLeft\\walkUpLeft" + str(i) + ".png"))
leftDownSpriteList = []
for i in range(9):
    leftDownSpriteList.append(image.load("walkDownLeft\\walkDownLeft" + str(i) + ".png"))

playerX, playerY = 400,300
screen.fill((255,255,255))
frame = 0 #for the sprite being blitted 

running = True
while running:

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    
    for e in event.get():       
        if e.type == QUIT:     
            running = False
    
    if key.get_pressed()[K_RIGHT]:
        playerX += 2
        screen.fill((255,255,255)) #Replace fill with subsurface
        screen.blit(rightWalkSpriteList[frame],(playerX,playerY))
        time.wait(20) #Find better way to delay animations 
        frame += 1
        if frame>8: #8 frames total for this animation
            frame = 0
        
    elif key.get_pressed()[K_LEFT]:
        playerX -= 2
        screen.fill((255,255,255)) #Replace fill with subsurface 
        screen.blit(leftWalkSpriteList[frame],(playerX,playerY))
        time.wait(20) #Find better way to delay animations 
        frame += 1
        if frame>8: #8 frames total for this animation
            frame = 0
    elif key.get_pressed()[K_UP]:
        playerY -= 2
        screen.fill((255,255,255)) #Replace fill with subsurface
        screen.blit(upWalkSpriteList[frame],(playerX,playerY))
        time.wait(20) #Find better way to delay animations 
        frame += 1
        if frame>8: #8 frames total for this animation
            frame = 0
    elif key.get_pressed()[K_DOWN]:
        playerY += 2
        screen.fill((255,255,255)) #Replace fill with subsurface
        screen.blit(downWalkSpriteList[frame],(playerX,playerY))
        time.wait(20) #Find better way to delay animations 
        frame += 1
        if frame>8: #8 frames total for this animation
            frame = 0
            
    print (playerX,playerY) #just prints the coordinates of the player         
    display.flip()
quit()

