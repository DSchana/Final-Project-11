# classes.py

from pygame import *

class player:
	def __init__(self, speed, tongue_range, tongue_speed, shoot_range, is_loaded, x, y):
		self.x = x
		self.y = y
		self.playerRect = Rect(x, y, 20, 50)
		self.speed = speed
		self.tongue_range = tongue_range
		self.tongue_speed = tongue_speed
		self.shoot_range = shoot_range
		self.is_loaded = is_loaded

	def move(self, pressed, screen):
		"Move player"
		if pressed[K_UP]:
			self.y -= self.speed
		elif pressed[K_DOWN]:
			self.y += self.speed
		elif pressed[K_LEFT]:
			self.x -= self.speed
		elif pressed[K_RIGHT]:
			self.x += self.speed

		self.playerRect = Rect(self.x, self.y, 20, 50)
		draw.rect(screen, (255, 255, 255), self.playerRect)

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

class enemy:
	def __init__(self, speed, ko_time, AI_level, kind):
		self.speed = speed
		self.ko_time = ko_time
		self.AI_level = AI_level
		self.kind = kind

	def move(self):
		"Move enemy"

	def knock_out(self):
		"Enemy is knocked out"

	def AI(self):
		"AI for enemies"

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