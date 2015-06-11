#enemy generator
#just a snippet of code for randomly choosing an enemy
#after "enemy" is returned, spawn that enemy on screen or something

from random import *

def enemyGenerator ():
    enemiesList = ["knight","spider","goblin"]
    enemyProb = [2,0,1,1,2,2,1,2,0]
    #the elements in the above list refers to the position in enemiesList
    enemySelect = choice(enemyProb) #each has different prob. 
    enemy = enemiesList[enemySelect]
    #print (enemy)
    return enemy

enemyGenerator ()
