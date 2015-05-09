# Battle.py

from pygame import *
from random import *
from math import *

class Battle:
	def __init__(self, Player, Enemy, location):
		self.player = Player
		self.enemy = Enemy
		self.turn = "player"
		self.location = location

	def drawBattle(self):
		"Draw battle scene"

	def attack(self):
		"Player or Enemy attacks based on turn"