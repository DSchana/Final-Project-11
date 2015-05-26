#Cast Spell Sprites
#This code controls the animations for the player when he casts spells

#Load the sprites in the loading screen ******

from pygame import*
screen = display.set_mode((850,600))

#The following lists store the sprites for casting spells (attacking) 
castSpellRightSpriteList = []
for i in range(6):
    castSpellRightSpriteList.append(image.load("castSpellRight\\castSpellRight" + str(i) + ".png"))
    
castSpellLeftSpriteList = []
for i in range(6):
    castSpellLeftSpriteList.append(image.load("castSpellLeft\\castSpellLeft" + str(i) + ".png"))
    
castSpellUpSpriteList = []
for i in range(6):
    castSpellUpSpriteList.append(image.load("castSpellUp\\castSpellUp" + str(i) + ".png"))
    
castSpellDownSpriteList = []
for i in range(6):
    castSpellDownSpriteList.append(image.load("castSpellDown\\castSpellDown" + str(i) + ".png"))
    
castSpellUpRightSpriteList = []
for i in range(6):
    castSpellUpRightSpriteList.append(image.load("castSpellUpRight\\castSpellUpRight" + str(i) + ".png"))
    
castSpellUpLeftSpriteList = []
for i in range(6):
    castSpellUpLeftSpriteList.append(image.load("castSpellUpLeft\\castSpellUpLeft" + str(i) + ".png"))
    
castSpellDownRightSpriteList = []
for i in range(6):
    castSpellDownRightSpriteList.append(image.load("castSpellDownRight\\castSpellDownRight" + str(i) + ".png"))
    
castSpellDownLeftSpriteList = []
for i in range(6):
    castSpellDownLeftSpriteList.append(image.load("castSpellDownLeft\\castSpellDownLeft" + str(i) + ".png"))

playerX, playerY = 400,300 #placeholder values
screen.fill((255,255,255))
direction = "right"
frame = 0

#I assume you have some variable that keeps track of the direction that the player is facing,
#in this file I just called it "direction" 

running = True
while running:

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    
    for e in event.get():       
        if e.type == QUIT:     
            running = False
    
    if key.get_pressed()[K_SPACE]:
        if direction == "left":
            screen.fill((255,255,255)) #Replace fill with subsurface
            screen.blit(castSpellLeftSpriteList[int(frame)],(playerX,playerY))
            time.wait(20) #Find better way to delay animations 
            frame += 0.2
            if frame>5: 
                frame = 0

        elif direction == "right":
            screen.fill((255,255,255)) 
            screen.blit(castSpellRightSpriteList[int(frame)],(playerX,playerY))
            time.wait(20) 
            frame += 0.2
            if frame>5: 
                frame = 0

        elif direction == "up":
            screen.fill((255,255,255))
            screen.blit(castSpellUpSpriteList[int(frame)],(playerX,playerY))
            time.wait(20)
            frame += 0.2
            if frame>5: 
                frame = 0

        elif direction == "down":
            screen.fill((255,255,255)) 
            screen.blit(castSpellDownSpriteList[int(frame)],(playerX,playerY))
            time.wait(20)
            frame += 0.2
            if frame>5: 
                frame = 0

        elif direction == "upRight":
            screen.fill((255,255,255))
            screen.blit(castSpellUpRightSpriteList[int(frame)],(playerX,playerY))
            time.wait(20) 
            frame += 0.2
            if frame>5: 
                frame = 0
                
        elif direction == "upLeft":
            screen.fill((255,255,255)) 
            screen.blit(castSpellUpLeftSpriteList[int(frame)],(playerX,playerY))
            time.wait(20) 
            frame += 0.2
            if frame>5:
                frame = 0
                
        elif direction == "downRight":
            screen.fill((255,255,255)) 
            screen.blit(castSpellDownRightSpriteList[int(frame)],(playerX,playerY))
            time.wait(20) 
            frame += 0.2
            if frame>5:
                frame = 0
                
        elif direction == "downLeft":
            screen.fill((255,255,255)) 
            screen.blit(castSpellDownLeftSpriteList[int(frame)],(playerX,playerY))
            time.wait(20) 
            frame += 0.2
            if frame>5:
                frame = 0
                
    display.flip()
quit()

