# Player.py

from pygame import *
from random import *
from math import *
from Spells import *
from Sprites import *

class Player:
	def __init__(self, name, health, house, xp, level, spell_level, potion_level, attack_radius, spell_energy, spell_list, stamina, speed, x, y):
		# initialize all variables
		self.name = name
		self.health = health
		self.max_health = health
		self.house = house
		self.level = level
		self.spell_level = spell_level
		self.spell_energy = spell_energy
		self.max_spell_energy = spell_energy
		self.potion_level = potion_level
		self.attack_radius = attack_radius
		self.stamina = stamina
		self.max_stamina = stamina
		self.angle_speed = speed * cos(radians(45))
		self.straight_speed = speed
		self.x = x
		self.y = y
		self.bx = -300
		self.by = -400
		self.playerRect = Rect(x, y, 22, 45) 
		self.width = self.playerRect[2]
		self.height = self. playerRect[3]
		self.spell_list = spell_list
		self.learnSpell("Expelliarmus", 10, 1, 10)
		self.selected_spell = self.spell_list[0]
		self.direction = "left"
		self.location = "grounds"

	def analyzeInput(self, camera, pressed, e, sprite, background):
		"Centralized method that analyzes inputs and calls adequett functions"

		sprite.showBackground(background[self.location], self.bx, self.by, camera)

		if self.direction == "":
			sprite.displayIdle(self, camera)
		else:
			sprite.changeSprite(self, camera)
			
		self.changeDirection(pressed)
		self.move(pressed, camera, sprite, background[self.location])
		self.regenerate()
		# if e.type == KEYDOWN and pressed[K_SPACE]:
		#	self.attack(camera)

	def changeDirection(self, pressed):
		"Change the direction used to affect player"

		self.direction = ""

		if pressed[K_w]:
			self.direction += "up"
		if pressed[K_a]:
			self.direction += "left"
		if pressed[K_s]:
			self.direction += "down"
		if pressed[K_d]:
			self.direction += "right"
		if pressed[K_a] and pressed[K_d] or pressed[K_w] and pressed[K_s]:
			self.direction = ""

		if len(self.direction) >= 6:
			self.speed = self.angle_speed
		else:
			self.speed = self.straight_speed

	def changeLocation(self):
		"Change the location ex. main entrance, grounds"

	def move(self, pressed, camera, sprite, back_image):
		"Move player"

		if self.bx == -back_image.get_width()+camera.get_width() or self.bx == 0:
			if pressed[K_LSHIFT] and self.stamina > 1.1:
				if self.direction.find("left") != -1:
					self.x -= self.speed*2
					self.stamina -= 0.05
				if self.direction.find("right") != -1:
					self.x += self.speed*2
					self.stamina -= 0.05
			else:
				if self.direction.find("left") != -1:
					self.x -= self.speed
				if self.direction.find("right") != -1:
					self.x += self.speed

		else:
			if pressed[K_LSHIFT] and self.stamina > 1.1:
				if self.direction.find("left") != -1:
					self.bx += self.speed*2
					self.stamina -= 0.05
				if self.direction.find("right") != -1:
					self.bx -= self.speed*2
					self.stamina -= 0.05
			else:
				if self.direction.find("left") != -1:
					self.bx += self.speed
				if self.direction.find("right") != -1:
					self.bx -= self.speed

		if self.by == -back_image.get_height()+camera.get_height() or self.by == 0:
			if pressed[K_LSHIFT] and self.stamina > 1.1:
				if self.direction.find("up") != -1:
					self.y -= self.speed*2
					self.stamina -= 0.05
				if self.direction.find("down") != -1:
					self.y += self.speed*2
					self.stamina -= 0.05
			else:
				if self.direction.find("up") != -1:
					self.y -= self.speed
				if self.direction.find("down") != -1:
					self.y += self.speed

		else:
			if pressed[K_LSHIFT] and self.stamina > 1.1:
				if self.direction.find("up") != -1:
					self.by += self.speed*2
					self.stamina -= 0.05
				if self.direction.find("down") != -1:
					self.by -= self.speed*2
					self.stamina -= 0.05
			else:
				if self.direction.find("up") != -1:
					self.by += self.speed
				if self.direction.find("down") != -1:
					self.by -= self.speed

	def gotHit(self):
		"do things for being hit"
		self.health -= 1

	def attack(self, camera):
		"player performs a spell"

		# straight facing spells
		if self.direction == "up":
			# do up spell animation
			print("up")
		if self.direction == "left":
			# do left spell animation
			print("up")
		if self.direction == "down":
			# do down spell animation
			print("up")
		if self.direction == "right":
			# do right animation
			print("up")

			# diagonal facing spells
		if self.direction == "upleft":
			# do upleft animation
			print("up")
		if self.direction == "leftdown":
			# do leftdown animation
			print("up")
		if self.direction == "downright":
			# do downright animation
			print("up")
		if self.direction == "upright":
			# do rightup anumation
			print("up")
		
		# Turns out the game has a turn based attack system similar to pokemon
		# if self.spell_energy > self.selected_spell.getEnergy():
		#     if self.direction == "left":
		#         self.selected_spell.doSpell((self.x+self.width/2)-self.attack_radius, (self.y+self.height/2), self.width, self.height, self.x, self.y, self.attack_radius, camera)
		#     if self.direction == "right":
		#         self.selected_spell.doSpell((self.x+self.width/2)+self.attack_radius, (self.y+self.height/2), self.width, self.height, self.x, self.y, self.attack_radius, camera)
		#     if self.direction == "up":
		#         self.selected_spell.doSpell((self.x+self.width/2), (self.y+self.height/2)-self.attack_radius, self.width, self.height, self.x, self.y, self.attack_radius, camera)
		#     if self.direction == "down":
		#         self.selected_spell.doSpell((self.x+self.width/2), (self.y+self.height/2)+self.attack_radius, self.width, self.height, self.x, self.y, self.attack_radius, camera)

		#     self.spell_energy -= self.selected_spell.getEnergy()

	def learnSpell(self, name, power, level, energy):
		"Add spell to the player's spell list"
		self.spell_list.append(Spells(name, power, level, energy))

	def regenerate(self):
		"regenerate health, stamina, and energy over time"
		if self.stamina < self.max_stamina:
			self.stamina += 0.04
		if self.spell_energy < self.max_spell_energy:
			self.spell_energy += 0.09


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

	def getDirection(self):
		"get the direction of the player"
		return self.direction
