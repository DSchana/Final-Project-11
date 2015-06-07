#Battle Menu 2
#The code for the menu that appears when Harry enters a battle with enemies
#displays the actions he can take

from pygame import*
import os

#Window preferences
os.environ['SDL_VIDEO_WINDOW_POS'] = '25,50' #Opens up in the upper left corner 
screen = display.set_mode((850,600)) #Game window resolution
display.set_caption("Harry Potter: New Horizons")
mouse.set_cursor(*cursors.tri_left)

#Already Loaded in main
profilePic = image.load ("profilePic.png")
#*******

#Load idle sprites, these lists hold the sprites for the animations of the enemies
#during battle screens 
enemyIdleSpritesList = []
enemyAttackSpritesList = [] 
enemyFrame = 0

enemyMode = "Attack" #change to default Idle 

for i in range (6):
    enemyIdleSpritesList.append(image.load("enemyIdleSprite\\enemyIdleSprite"+str(i)+".png"))
    enemyIdleSpritesList[i] = transform.scale(enemyIdleSpritesList[i],(50,60))

for i in range (6):
    enemyAttackSpritesList.append(image.load("enemyAttackSprite\\enemyAttackSprite"+str(i)+".png"))
    enemyAttackSpritesList[i] = transform.scale(enemyAttackSpritesList[i],(50,60))

screen.fill((0,0,0)) #replace later 

running = True
while running:

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    for e in event.get():       
        if e.type == QUIT:     
            running = False
            
    #Some variable that keeps track of whether or not harry in is a battle
    #Eg. triggered when harry walks into the blue blob 
    #if gameMode == "Battle":

    if enemyMode == "Attack": #if the enemy is attacking:
        screen.fill((0,0,0))
        screen.blit(enemyAttackSpritesList[enemyFrame],(80,400))
        time.wait(100)
        enemyFrame +=1
        if enemyFrame>5:
            enemyFrame = 0
            enemyMode="Idle" 
    #Add code when harry finishes his move, the enemy attacks again
            
    elif enemyMode == "Idle": #if the enemy is not attacking:
        screen.fill((0,0,0))
        screen.blit(enemyIdleSpritesList[enemyFrame],(80,400))
        time.wait(80)
        enemyFrame +=1
        if enemyFrame>5:
            enemyFrame=0
            
    display.flip()
quit()
