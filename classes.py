# classes.py

from pygame import *
from math import *
from enum import *

class player:
	def __init__(self, name, house, level, spell_level, potion_level, stamina, speed, x, y, moveMode):
		self.name = name
		self.house = house
		self.level = level
		self.spell_level = spell_level
		self.potion_level = potion_level
		self.stamina = stamina
		self.speed = speed
		self.x = x
		self.y = y
		self.moveMode = moveMode
		self.playerRect = Rect(x, y, 40, 50)

	def move(self, pressed, screen):
		"Move player"
		if self.moveMode == "wasd":  # temporary use enumerations
			if pressed[K_UP]:
				self.y -= self.speed
			if pressed[K_DOWN]:
				self.y += self.speed
			if pressed[K_LEFT]:
				self.x -= self.speed
			if pressed[K_RIGHT]:
				self.x += self.speed

		if self.moveMode == "arrow":
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

	def suck(self):
		"Use tongue to obtain block"

	def shoot(self):
		"Shoot block from player"

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
	def getRect(self):
		"get the rect of object"
		return self.playerRect

class enemy:
	def __init__(self, speed, ko_time, AI_level, attack_radius, kind, x, y):
		self.x = x
		self.y = y
		self.attack_radius = attack_radius
		self.enemyRect = Rect(x, y, 40, 50)
		self.speed = speed
		self.ko_time = ko_time
		self.AI_level = AI_level
		self.kind = kind

	def move(self, px, py, screen):
		"Move enemy"
		#draw.circle(screen, (148, 0, 0, 30), (int(self.x)+20, int(self.y)+25), self.attack_radius)
		#draw.circle(screen, (150, 0, 0, 255), (int(self.x)+20, int(self.y)+25), self.attack_radius, 10)
		if sqrt((px-self.x)**2 + (py - self.y)**2) < self.attack_radius:
			if abs(py - self.y) == abs(px - self.x):
				if py > self.y:
					self.y += self.speed
				elif py < self.y:
					self.y -= self.speed
			elif abs(py - self.y) > abs(px - self.x):
				if py > self.y:
					self.y += self.speed
				elif py < self.y:
					self.y -= self.speed
			elif abs(py - self.y) < abs(px - self.x):
				if px > self.x:
					self.x += self.speed
				elif px < self.x:
					self.x -= self.speed

		self.enemyRect = Rect(self.x, self.y, 40, 50)
		draw.rect(screen, (255, 0, 0), self.enemyRect)

	def knock_out(self):
		"Enemy is knocked out"

	def AI(self):
		"AI for enemies"

	# get methods
	def getX(self):
		"get x position of object"
		return self.x
	def getY(self):
		"get y position of object"
		return self.y

	def checkCollision(self, player_rect):
		"check if player dies"
		return self.enemyRect.colliderect(player_rect)

# enumeration
class playerMode(Enum):
	player_1 = 1
	player_2 = 2