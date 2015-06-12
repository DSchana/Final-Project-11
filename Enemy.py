# Enemy.py

from pygame import *
from random import *
from math import *
from Spells import *

class Enemy:
	def __init__(self, AI_level):
		self.health = 100
		self.house = "slytherin"
		self.AI_level = AI_level
		type_list = ["goblin", "spider", "knight"]
		self.kind = choice(type_list)
		self.spell_energy = 100

	def analyzeInput(self, camera, player):
		"Centralized method that analyzes inputs and calls adequett functions"
		# Check attack
		rx = player.getX()
		ry = player.getY()

	def show(self, camera):
		"Draw enemy"  # use only when enemy will not be moving
		draw.rect(camera, (255, 0, 0), self.enemyRect)

	def AI(self):
		"AI for enemies"

	def checkCollision(self, rleft, rtop, width, height, center_x, center_y, radius):
		"Detect collision between a rectangle and circle (playerRect and attack_radius)"

		# complete boundbox of the rectangle
		rright, rbottom = rleft + width/2, rtop + height/2

		# bounding box of the circle
		cleft, ctop     = center_x-radius, center_y-radius
		cright, cbottom = center_x+radius, center_y+radius

		# trivial reject if bounding boxes do not intersect
		if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
			return False  # no collision possible

		# check whether any point of rectangle is inside circle's radius
		for x in (rleft, rleft+width):
			for y in (rtop, rtop+height):
				# compare distance between circle's center point and each point of
				# the rectangle with the circle's radius
				if hypot(x-center_x, y-center_y) <= radius:
					return True  # collision detected

		# check if center of circle is inside rectangle
		if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
			return True

		return False  # no collision detected

	def gotHit(self):
		"Damage to ememies"
		self.health -= 1

	def attack(self, x, y, camera, player):
		"emeny performs a spell"

		# Not how it works, it is like pokemon, need to fix dis shit
		'''
		x += randint(-10, 10)
		y += randint(-10, 10)
		fireChance = randint(1, 50)
		if fireChance % self.fireRate == 0:
			self.selected_spell.doSpell(x, y, self.width, self.height, self.x, self.y, self.attack_radius, camera)
			player.gotHit()'''


	# get methods
	def getX(self):
		"get x position of object"
		return self.x

	def getY(self):
		"get y position of object"
		return self.y

	def getAttackRadius(self):
		"get the attack radius"
		return self.attack_radius

	def getHealth(self):
		"get health of enemy"
		return self.health

	def getFireRate(self):
		"get fire rate of enemy"
		return self.fireRate

	def takeDamage(self, damage):
		"Reduce enemy health based on attack"
		self.health -= damage

	def drainEnergy(self, energy):
		"drains the enemy energy when an attack is used"
		self.spell_energy -= energy