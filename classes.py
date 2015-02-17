# classes.py

from pygame import *
from enum import *

class player:
	def __init__(self, speed, tongue_range, tongue_speed, shoot_range, is_loaded, x, y, moveMode):
		self.x = x
		self.y = y
		self.moveMode = moveMode
		self.playerRect = Rect(x, y, 20, 50)
		self.speed = speed
		self.tongue_range = tongue_range
		self.tongue_speed = tongue_speed
		self.shoot_range = shoot_range
		self.is_loaded = is_loaded

	def move(self, pressed, screen):
		"Move player"
		if self.moveMode == "arrow":  # temporary use enumerations
			if pressed[K_UP]:
				self.y -= self.speed
			elif pressed[K_DOWN]:
				self.y += self.speed
			elif pressed[K_LEFT]:
				self.x -= self.speed
			elif pressed[K_RIGHT]:
				self.x += self.speed

		if self.moveMode == "wasd":
			if pressed[K_w]:
				self.y -= self.speed
			elif pressed[K_s]:
				self.y += self.speed
			elif pressed[K_a]:
				self.x -= self.speed
			elif pressed[K_d]:
				self.x += self.speed

		self.playerRect = Rect(self.x, self.y, 20, 50)
		draw.rect(screen, (0, 255, 0), self.playerRect)

	def suck(self):
		"Use tongue to obtain block"

	def shoot(self):
		"Shoot block from player"

	# get meathods
	def getSpeed(self):
		"get speed of object"
		return self.speed
	def tongueSpeed(self):
		"get spped of tongue"
		return self.tongue_speed
	def getX(self):
		"get x position of object"
		return self.x
	def getY(self):
		"get y position of object"
		return self.y

class enemy:
	def __init__(self, speed, ko_time, AI_level, kind, x, y):
		self.x = x
		self.y = y
		self.enemyRect = Rect(x, y, 20, 50)
		self.speed = speed
		self.ko_time = ko_time
		self.AI_level = AI_level
		self.kind = kind

	def move(self, px, py, screen):
		"Move enemy"
		if px > self.x:
			self.x += self.speed
		elif px < self.x:
			self.x -= self.speed
		elif py > self.y:
			self.y += self.speed
		elif py < self.y:
			self.y -= self.speed

		self.enemyRect = Rect(self.x, self.y, 20, 50)
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

class block:
	def __init__(self, speed, can_pull, kind, can_break):
		self.speed = speed
		self.can_pull = can_pull
		self.kind = kind
		self.can_break = can_break

	def pull(self):
		"Change how the block interacts with the player"

	def throw(self):
		"Change how block moves while moving"

# enum
class playerMode(Enum):
	player_1 = True
	player_2 = True