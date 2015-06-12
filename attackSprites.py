# attackSprites.py

from pygame import *
import glob

class attackSprite:
	def __init__(self, idle_dir, atk_dir, x, y):
		self.x = x
		self.y = y

		self.idle = []
		self.attack = []

		self.idle_surf = []
		self.attack_surf = []

		self.idle_dir = idle_dir
		self.atk_dir = atk_dir

		self.frame = 0

	def loadImages(self):
		"Load imagess in given directory"
		self.idle.append(glob.glob(self.idle_dir + "*.png"))
		self.attack.append(glob.glob(self.atk_dir + "*.png"))

		self.idle.sort()
		self.attack.sort()

		for i in range(len(self.idle[0])):
			self.idle_surf.append(image.load(self.idle[0][i]))
			self.idle_surf[i] = transform.scale(self.idle_surf[i], (50, 70))

		for i in range(len(self.attack[0])):
			self.attack_surf.append(image.load(self.attack[0][i]))
			self.attack_surf[i] = transform.scale(self.attack_surf[i], (50, 70))

	def showIdle(self, screen):
		"cycly through idle sprites when characters are not doing anything"
		if self.frame < len(self.idle_surf) - 1:
			self.frame += 0.1
		else:
			self.frame = 0

		screen.blit(self.idle_surf[int(self.frame)], (self.x, self.y))

	def showAttack(self, screen, battleScene, other, battle):
		"cycle through attack sprites"
		while self.frame + 0.01 < len(self.attack_surf) - 1:
			screen.blit(battleScene, (0, 0))
			other.showIdle(screen)
			battle.displayHealth(screen)

			self.frame += 0.2
			screen.blit(self.attack_surf[int(self.frame)], (self.x, self.y))
			display.flip()