# Player.py

from pygame import *
from random import *
from math import *
from Spells import *
from enum import *

class player:
    def __init__(self, name, health, house, xp, level, spell_level, potion_level, attack_radius, spell_energy, stamina, speed, x, y, moveMode):
        self.name = name
        self.health = health
        self.house = house
        self.level = level
        self.spell_level = spell_level
        self.selected_spell = "Expeliomus"
        self.potion_level = potion_level
        self.attack_radius = attack_radius
        self.stamina = stamina
        self.speed = speed
        self.x = x
        self.y = y
        self.moveMode = moveMode
        self.playerRect = Rect(x, y, 40, 50) 
        self.width = self.playerRect[2]
        self.height = self. playerRect[3]

    def move(self, pressed, screen):
        "Move player"
        if pressed[K_w]:
            self.y -= self.speed
        if pressed[K_s]:
            self.y += self.speed
        if pressed[K_a]:
            self.x -= self.speed
        if pressed[K_d]:
            self.x += self.speed

        self.playerRect = Rect(self.x, self.y, 40, 50)
        draw.rect(screen, (0, 255, 0), self.playerRect)

    def gotHit(self, fireRate):
        "do things for being hit"
        fireChance = randint(1, 100)
        if fireChance % fireRate == 0:
        	self.health -= 1

    def doSpell(self, mx, my, screen):
    	"player performs a spell"
    	sx = int(self.x + self.width/2)
    	sy = int(self.y + self.height/2)
    	dx = mx - sx
    	dy = my - sy
    	d_incx = dx / self.attack_radius
    	d_incy = dy / self.attack_radius
    	while sqrt((sx-self.x)**2 + (sy-self.y)**2) < self.attack_radius:
	    	sx += int(0.5)
	    	sy += int(0.5)
	    	draw.circle(screen, (0, 20, 140), (sx, sy), 3)


    # get meathods
    def getSpeed(self):
        "get speed of object"
        return self.speed
    
    def getX(self):
        "get x position of object"
        return self.x
    
    def getY(self):
        "get y position of object"
        return self.y
    
    def getWidth(self):
        "get width of player"
        return self.width
    
    def getHeight(self):
        "get length of player"
        return self.height
    
    def getRect(self):
        "get the rect of object"
        return self.playerRect
    
    def getHealth(self):
        "get health of player"
        return self.health