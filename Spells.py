# Spells.py

from pygame import *
from random import *
from math import *

class Spells:
	def __init__(self, name, power, level, energy):
		self.name = name
		self.power = power
		self.level = level
		self.energy = energy

	def doSpell(self, mx, my, width, height, x, y, attack_radius, camera):
		"Have player perform spell"
		frame_copy = camera.copy()
		sx = x + width//2
		sy = y + height//2
		dx = mx - sx
		dy = my - sy
		d_incx = dx / attack_radius
		d_incy = dy / attack_radius
		while sqrt((sx-x)**2 + (sy-y)**2) < attack_radius:

			camera.blit(frame_copy, (0, 0))
			sx += d_incx
			sy += d_incy
			draw.circle(camera, (218, 135, 4), (int(sx), int(sy)), 3)
			display.flip()

	# spell get methods
	def getName(self):
		"get name of spell"
		return self.name

	def getPower(self):
		"get power level"
		return self.power

	def getLevel(self):
		"get unlock level"
		return self.level

	def getEnergy(self):
		"get required energy"
		return self.energy
