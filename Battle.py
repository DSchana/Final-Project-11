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
		self.battleScene = image.load("Images/Backgrounds/Battles/" + location + ".png")

	def drawBattle(self, screen):
		"Draw battle scene"
		screen.blit(self.battleScene)
		# draw player and enemy sprites

	def attack(self):
		"Player or Enemy attacks based on turn"