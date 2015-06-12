# Enemy.py
#stores the AI and the attacks for the enemy
#please note that not all of the following code is actually used in the game since
#it changed from a dungeon crawler to a turn-based game 

from pygame import *
from random import *
from math import *
from Spells import *

class Enemy:
	def __init__(self, AI_level):
                #enemies have 100 hp and they are spawned randomly 
		self.health = 100
		self.house = "slytherin"
		self.AI_level = AI_level
		type_list = ["goblin", "enemy", "goblin", "enemy", "spider", "enemy"] #note "enemy" is the knight 
		#randomly choose enemy from the list, each has a different probaility 
		self.kind = choice(type_list)
		self.spell_energy = 100

		self.attack_spells = []
                #enemy's attacks 
		self.attack_spells.append(self.learnSpell("Expulso", "Light dameage, no energy drain", 10, 1, 0))
		self.attack_spells.append(self.learnSpell("Imerio", "Moderate damage, low energy", 15, 1, 5))
		self.attack_spells.append(self.learnSpell("Crucio", "Heavy damage, costs more energy", 20, 1, 15))
		self.attack_spells.append(self.learnSpell("Stupefy", "Weakens next enemy attack", 0, 1, 10))

	def analyzeInput(self, camera, player):
		"Centralized method that analyzes inputs and calls functions"
		# Check attack
		rx = player.getX()
		ry = player.getY()

	def show(self, camera):
		"Draw enemy"  # use only when enemy will not be moving
		draw.rect(camera, (255, 0, 0), self.enemyRect)

	def gotHit(self):
		"Damage to ememies"
		self.health -= 1

	#def attack(self, x, y, camera, player):
		#"emeny performs a spell"

	def learnSpell(self, name, description, power, level, energy):
		"Add spell to the player's spell list"
		return (Spells(name, description, power, level, energy))

	def chooseSpell(self):
		"choose spell for enemy in battle"
		return choice(self.attack_spells)


	# get methods
	def getX(self):
		"get x position of object"
		return self.x

	def getY(self):
		"get y position of object"
		return self.y

	def getSpellEnergy(self):
                #returns the energy of the enemy after attack is used
		return self.spell_energy

	#def getAttackRadius(self):
	#	"get the attack radius"
	#	return self.attack_radius

	def getHealth(self):
		"get health of enemy"
		return self.health

	def getKind(self):
		"get type of enemy to show"
		return self.kind

	def takeDamage(self, damage):
		"Reduce enemy health based on attack"
		self.health -= damage

	def drainEnergy(self, energy):
		"drains the enemy energy when an attack is used"
		self.spell_energy -= energy
