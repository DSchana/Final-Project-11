# Battle.py

from pygame import *
from math import *
from random import *

class Battle:
	def __init__(self, Player, Enemy):
		self.Player = Player
		self.Enemy = Enemy
		self.turn = "player"

	def drawBattle(self):
		"Draw battle scene"
