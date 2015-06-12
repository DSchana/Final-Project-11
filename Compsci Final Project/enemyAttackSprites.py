#attackspirtes for the battle scene
#The actual code for the animations goes with the code from battle.py #*see below 

from pygame import *

#The following lists store the sprites for enemies (attacking and idle)
goblinIdleSpriteList = [] 
for i in range(5):
    goblinIdleSpriteList.append(image.load("goblinIdleSprite\\goblinIdleSprite" + str(i) + ".png"))

goblinAttackSpriteList = []
for i in range(6):
    goblinAttackSpriteList.append(image.load("goblinAttackSprite\\goblinAttackSprite" + str(i) + ".png"))

spiderAttackSpriteList = []
for i in range(3):
    spiderAttackSpriteList.append(image.load("spiderAttackSprite\\spiderAttackSprite" + str(i) + ".png"))

spiderIdleSpriteList = []
for i in range(3):
    spiderIdleSpriteList.append(image.load("spiderIdleSprite\\spiderIdleSprite" + str(i) + ".png"))

knightAttackSpriteList = []
for i in range(6):
    knightAttackSpriteList.append(image.load("enemyAttackSprite3\\enemyAttackSprite3" + str(i) + ".png"))

knightIdleSpriteList = []
for i in range(6):
    knightIdleSpriteList.append(image.load("enemyIdleSprite\\enemyIdleSprite" + str(i) + ".png"))

enemyFrame = 0
enemyIdleFrameLimit =0#controls the frame of the enemy's attack, if over, frame is reset to 0
enemyAttackFrameLimit = 0#controls the frame of the enemy's idle, if over, frame is reset to 0
enemyIdleSpritesList = []
enemyAttackSpritesList = []

#just a snippet of code for randomly choosing an enemy
enemiesList = ["knight","spider","goblin"]
enemyProb = [2,0,1,1,2,2,1,2,0]
#the elements in the above list refers to the position in enemiesList
enemySelect = choice(enemyProb) #each has different prob. 
enemy = enemiesList[enemySelect]

#returns the max number of framces each enemy animations has
#for the animation, if frame is over, it is reset to 0
if enemy == "knight":
    enemyIdleFrameLimit =6
    enemyAttackFrameLimit=6
    #when an enemy is generated, the sprite list to blit is matched accordingly 
    enemyAttackSpritesList = knightAttackSpriteList
    enemyIdleSpritesList = knightIdleSpriteList
elif enemy == "spider":
    enemyIdleFrameLimit=3
    enemyAttackFrameLimit=3
    enemyAttackSpritesList = spiderAttackSpriteList
    enemyIdleSpritesList = spiderIdleSpriteList
elif enemy == "goblin":
    enemyIdleFrameLimit=5
    enemyAttackFrameLimit=6
    enemyAttackSpritesList = goblinAttackSpriteList
    enemyIdleSpritesList = goblinIdleSpriteList
 

#this code would go into this part from battle.py
"""
if turn: #harry's turn, so blit enemy idle

#enemy idle animation *HERE
"""
screen.fill((0,0,0)) #placeholder 
screen.blit(enemyIdleSpritesList[enemyFrame],(80,400)) #or where ever the enemy is blit 
time.wait(80)
enemyFrame +=1
if enemyFrame>enemyIdleFrameLimit: #if frame is over number of frames, reset to frame 0 
    enemyFrame=0

#this code would go into this part from battle.py
"""
elif turn == False: #the enemy's turn
#enemy attack animation *HERE
"""
screen.fill((0,0,0)) #placeholder 
screen.blit(enemyIdleSpritesList[enemyFrame],(80,400))
time.wait(100)
enemyFrame +=1
if enemyFrame>enemyAttackFrameLimit:
    enemyFrame = 0

#def enemyAnimate ():



        




