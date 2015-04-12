# Player.py

from pygame import *
from random import *
from math import *
from Spells import *
from enum import *

class Player:
    def __init__(self, name, health, house, xp, level, spell_level, potion_level, attack_radius, spell_energy, spell_list, stamina, speed, x, y, moveMode):
        self.name = name
        self.health = health
        self.house = house
        self.level = level
        self.spell_level = spell_level
        self.spell_energy = spell_energy
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
        self.spell_list = spell_list
        self.learnSpell("Expelliarmus", 10, 1, 10)
        self.selected_spell = self.spell_list[0]

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

    def attack(self, mx, my, screen):
        "player performs a spell"
        self.selected_spell.doSpell(mx, my, self.width, self.height, self.x, self.y, self.attack_radius, screen)
        self.spell_energy -= self.selected_spell.getEnergy()

    def learnSpell(self, name, power, level, energy):
        "Add spell to the player's spell list"
        self.spell_list.append(Spells(name, power, level, energy))


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

    def getSpellList(self):
        "get the list possible spells player can currently cast"
        return self.spell_list

    def getSelectedSpell(self):
        "get the current spell the user has selected"
        return self.selected_spell

    def getStamina(self):
        "get the player's stamina"
        return self.stamina

    def getSpellEnergy(self):
        "get the spell energy of player"
        return self.spell_energy