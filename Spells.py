# Spells.py

from pygame import *
from random import *
from math import *
from enum import *

class spell:
	def __init__(self, name, power, level, energy):
		self.name = name
		self.power = power
		self.level = level
		self.energy = energy

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