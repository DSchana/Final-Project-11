# attackSprites.py

from pygame import *
import glob

class attackSprite:
	def __init__(self, idle_dir, atk_dir, x, y):
		self.x = x
		self.y = y

		self.idle = []
		self.attack = []

		self.idle_dir = idle_dir
		self.atk_dir = atk_dir

		self.frame = 0

	def loadImages(self):
		self.idle.append(glob.glob(self.idle_dir + "*.png"))
		self.attack.append(glob.glob(self.atk_dir + "*.png"))

		self.idle.sort()
		self.attack.sort()

		print(self.idle)
		print(self.attack)

		for i in range(len(self.idle)):
			self.idle[0][i] = image.load(self.idle[0][i])
			self.idle[0][i] = transform.scale(self.idle[0][i], (50, 70))

		for i in range(len(self.attack)):
			self.attack[0][i] = image.load(self.attack[0][i])
			self.attack[0][i] = transform.scale(self.attack[0][i], (50, 70))

	def showIdle(self, screen):
		print("idling")
		if self.frame < len(self.idle)-1:
			self.frame += 0.2
		else:
			self.frame = 0
		print(self.frame)

		screen.blit(self.idle[0][int(self.frame)], (self.x, self.y))

	def showAttack(self, screen):
		while self.frame + 0.2 < len(self.attack) - 1:
			print("attacking")
			self.frame += 0.2
			screen.blit(self.attack[0][int(self.frame)], (self.x, self.y))
			display.flip()