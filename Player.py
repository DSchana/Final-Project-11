# Player.py

from pygame import *
from random import *
from math import *
from Spells import *
from Sprites import *
from Gates import *

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
		self.bx = -2000
		self.by = -2000
		self.playerRect = Rect(x, y, 22, 45) 
		self.width = self.playerRect[2]
		self.height = self. playerRect[3]
		self.spell_list = spell_list
		self.learnSpell("lumos", "illuminate the tip of the caster's wand", 0, 1, 0)
		self.selected_spell = self.spell_list[0]
		self.direction = "left"
		self.location = "grounds"
		self.attacking = False
		self.sprint_multiplyer = 2
		self.hit_box = Rect(self.x, self.y + 26, self.width, 20)

	def analyzeInput(self, camera, pressed, sprite, gates, background, collision_mask, music):
		"Centralized method that analyzes inputs and calls adequate functions"

		self.hit_box = Rect(self.x, self.y + 26, self.width, 20)

		sprite.showBackground(background[self.location], self.bx, self.by, camera)

		# coordinates to check players location relative to the map, not screen
		check_x = self.x + self.width/2 - self.bx
		check_y = self.y + self.height/2 - self.by

		# draw door depending on player's location
		for i in range(len(gates)):
			gates[i].idle(camera, self)

		if self.attacking == False:
			if self.direction == "":
				sprite.displayIdle(self, camera)
			else:
				sprite.changeSprite(self, camera)
		else:
			self.attacking = sprite.inGameAttack(self, camera, self.attacking)
			self.attack(camera)
			
		self.changeDirection(pressed)
		if not self.getCollision(collision_mask[self.location], background[self.location], gates, camera, music):
			self.move(pressed, camera, sprite, background[self.location])

		self.regenerate()

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

	def move(self, pressed, camera, sprite, back_image):
		"Move player"

		# Moving left and right
		if self.bx > 0 or self.x < 415:
			if self.bx >= 0:
				self.bx = 0

			if pressed[K_LSHIFT] and self.stamina > 1.0:
				if self.direction.find("left") != -1:
					self.x -= self.speed * self.sprint_multiplyer
					self.stamina -= 0.05
				if self.direction.find("right") != -1:
					self.x += self.speed * self.sprint_multiplyer
					self.stamina -= 0.05
			else:
				if self.direction.find("left") != -1:
					self.x -= self.speed
				if self.direction.find("right") != -1:
					self.x += self.speed

		elif self.bx < -back_image.get_width()+camera.get_width() or self.x > 435:
			if self.bx <= -back_image.get_width()+camera.get_width():
				self.bx = -back_image.get_width()+camera.get_width()

			if pressed[K_LSHIFT] and self.stamina > 1.0:
				if self.direction.find("left") != -1:
					self.x -= self.speed * self.sprint_multiplyer
					self.stamina -= 0.05
				if self.direction.find("right") != -1:
					self.x += self.speed * self.sprint_multiplyer
					self.stamina -= 0.05
			else:
				if self.direction.find("left") != -1:
					self.x -= self.speed
				if self.direction.find("right") != -1:
					self.x += self.speed

		else:
			if pressed[K_LSHIFT] and self.stamina > 1.0:
				if self.direction.find("left") != -1:
					self.bx += self.speed * self.sprint_multiplyer
					self.stamina -= 0.05
				if self.direction.find("right") != -1:
					self.bx -= self.speed * self.sprint_multiplyer
					self.stamina -= 0.05
			else:
				if self.direction.find("left") != -1:
					self.bx += self.speed
				if self.direction.find("right") != -1:
					self.bx -= self.speed


		# Moving up and down
		if self.by > 0 or self.y < 290:
			if self.by >= 0:
				self.by = 0

			if pressed[K_LSHIFT] and self.stamina > 1.0:
				if self.direction.find("up") != -1:
					self.y -= self.speed * self.sprint_multiplyer
					self.stamina -= 0.05
				if self.direction.find("down") != -1:
					self.y += self.speed * self.sprint_multiplyer
					self.stamina -= 0.05
			else:
				if self.direction.find("up") != -1:
					self.y -= self.speed
				if self.direction.find("down") != -1:
					self.y += self.speed

		elif self.by < -back_image.get_height()+camera.get_height() or self.y > 310:
			if self.by <= -back_image.get_height()+camera.get_height():
				self.by = -back_image.get_height()+camera.get_height()

			if pressed[K_LSHIFT] and self.stamina > 1.0:
				if self.direction.find("up") != -1:
					self.y -= self.speed * self.sprint_multiplyer
					self.stamina -= 0.05
				if self.direction.find("down") != -1:
					self.y += self.speed * self.sprint_multiplyer
					self.stamina -= 0.05
			else:
				if self.direction.find("up") != -1:
					self.y -= self.speed
				if self.direction.find("down") != -1:
					self.y += self.speed

		else:
			if pressed[K_LSHIFT] and self.stamina > 1.0:
				if self.direction.find("up") != -1:
					self.by += self.speed * self.sprint_multiplyer
					self.stamina -= 0.05
				if self.direction.find("down") != -1:
					self.by -= self.speed * self.sprint_multiplyer
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
			print("up")
		if self.direction == "left":
			print("left")
		if self.direction == "down":
			print("down")
		if self.direction == "right":
			print("right")

		# diagonal facing spells
		if self.direction == "upleft":
			print("upleft")
		if self.direction == "leftdown":
			print("leftdown")
		if self.direction == "downright":
			print("downright")
		if self.direction == "upright":
			print("upright")
		
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

	def getCollision(self, collision_mask, back_image, gates, camera, music):
		check_x = self.hit_box[0] + self.hit_box[2]/2 - self.bx
		check_y = self.hit_box[1] + self.hit_box[3]/2 - self.by

		if self.direction.find("up") != -1:
			check_y -= self.hit_box[3]/2
		if self.direction.find("left") != 1:
			check_x -= self.hit_box[2]/2
		if self.direction.find("down") != -1:
			check_y += self.hit_box[3]/2
		if self.direction.find("right") != 1:
			check_x += self.hit_box[2]/2

		# Left and right checking is weird, this compensates for that
		if self.direction.find("right") != -1:
			mask_col = collision_mask.get_at((int(check_x) + 9, int(check_y)))
		elif self.direction.find("left") != -1:
			mask_col = collision_mask.get_at((int(check_x) - 9, int(check_y)))
		else:
			mask_col = collision_mask.get_at((int(check_x), int(check_y)))

		# Check for wall collisions
		if mask_col == (255, 0, 0, 255):
			return True
		# Check for door collisions
		elif mask_col == (255, 255, 0, 255):
			self.interactDoor(gates, camera, music)
		else:
			return False

	def interactDoor(self, gates, camera, music):
		"Check which door the player has collided with and act accordingly"
		for i in range(len(gates)):
			if self.x > gates[i].getX() and self.x < gates[i].getX()+gates[i].getWidth():
				gates[i].open(camera, self)
				self.location = gates[i].getNewLocation()
				self.bx = -(gates[i].getNewX() - 425)
				self.by = -(gates[i].getNewY() - 300)
		music[self.location].halt()
		music[self.location].execute()

	def learnSpell(self, name, description, power, level, energy):
		"Add spell to the player's spell list"
		self.spell_list.append(Spells(name, description, power, level, energy))

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

	def getBX(self):
		"get bx of player"
		return self.bx

	def getBY(self):
		"get by of player"
		return self.by
	
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

	def getHouse(self):
		"get the house of player"
		return self.house

	def getLocation(self):
		"""get the current location of the player
		Location is used to determine backgrounds and sounds"""
		return self.location