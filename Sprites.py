#sprites.py
#This file contains the code to control the sprites v

from pygame import *
import glob

#NOTE: REMEMBER TO ADD IN THE IDLE ANIMATION and also diagonal sprites and put into a function
#Put this in the loading screen to load these sprites

class Sprites:
	def __init__(self, up_directory, left_directory, down_directory, right_directory, upleft_directory, leftdown_directory, downright_directory, upright_directory,
		up_attack, left_attack, down_attack, right_attack, upleft_attack, leftdown_attack, downright_attack, upright_attack):
		self.directories = []
		self.directories.append(up_directory)  # sprites[0]
		self.directories.append(left_directory)  # sprites[1]
		self.directories.append(down_directory)  # sprites[2]
		self.directories.append(right_directory)  # sprites[3]
		self.directories.append(upleft_directory)  # sprites[4]
		self.directories.append(leftdown_directory)  # sprites[5]
		self.directories.append(downright_directory)  # sprites[6]
		self.directories.append(upright_directory)  # sprites[7]

		# Attack directories
		self.directories.append(up_attack)  # sprites[8]
		self.directories.append(left_attack)  # sprites[9]
		self.directories.append(down_attack)  # sprites[10]
		self.directories.append(right_attack)  # sprites[11]
		self.directories.append(upleft_attack)  # sprites[12]
		self.directories.append(leftdown_attack)  # sprites[13]
		self.directories.append(downright_attack)  # sprites[14]
		self.directories.append(upright_attack)  # sprites[15]

		self.sprites = [[]]
		self.idle = []

		self.frame = 0
		self.attack_frame = 0
		self.max_frame = 0

		self.attacking = False

		self.last_direction = ""

	def loadImages(self):
		for i in range(len(self.directories)):
			if self.directories[i] != False:
				self.sprites.append(glob.glob(self.directories[i] + "*.png"))
				self.sprites[i].sort()

		# Compensate for the weird error in glob
		del self.sprites[0]
		self.sprites.append(self.directories[len(self.directories)-1])

		for i in range(len(self.directories)):
			for j in range(len(self.sprites[i])):
				self.sprites[i][j] = image.load(self.sprites[i][j])

		# CHANGE later to make it general for all instances of Sprites
		self.idle.append(self.sprites[0][0])
		self.idle.append(self.sprites[1][0])
		self.idle.append(self.sprites[2][0])
		self.idle.append(self.sprites[3][7])
		self.idle.append(self.sprites[4][0])
		self.idle.append(self.sprites[5][7])
		self.idle.append(self.sprites[6][0])
		self.idle.append(self.sprites[7][7])

	def changeSprite(self, Player, camera):
		px = Player.getX()
		py = Player.getY()
		pDirection = Player.getDirection()

		if pDirection == "right":
			camera.blit(self.sprites[3][int(self.frame)],(px,py)) 
			if self.frame > len(self.sprites[3]) - 1: #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2
			self.last_direction = "right"
			
		elif pDirection == "left":
			camera.blit(self.sprites[1][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[1]) - 1: #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2
			self.last_direction = "left"

		elif pDirection == "up":
			camera.blit(self.sprites[0][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[0]) - 1: #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2
			self.last_direction = "up"

		elif pDirection == "down":
			camera.blit(self.sprites[2][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[2]) - 1: #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2
			self.last_direction = "down"

		# diagonal sprites
		elif pDirection == "upleft":
			camera.blit(self.sprites[4][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[4]) - 1: #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2
			self.last_direction = "upleft"

		elif pDirection == "leftdown":
			camera.blit(self.sprites[5][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[5]) - 1: #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2
			self.last_direction = "leftdown"

		elif pDirection == "downright":
			camera.blit(self.sprites[6][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[6]) - 1: #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2
			self.last_direction = "downright"

		elif pDirection == "upright":
			camera.blit(self.sprites[7][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[7]) - 1: #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2
			self.last_direction = "upright"

		else:
			self.frame = 0

	def displayIdle(self, Player, camera):
		px = Player.getX()
		py = Player.getY()

		if self.last_direction == "up":
			camera.blit(self.idle[0], (px, py))
		elif self.last_direction == "left":
			camera.blit(self.idle[1], (px, py))
		elif self.last_direction == "down":
			camera.blit(self.idle[2], (px, py))
		elif self.last_direction == "right":
			camera.blit(self.idle[3], (px, py))
		elif self.last_direction == "upleft":
			camera.blit(self.idle[4], (px, py))
		elif self.last_direction == "leftdown":
			camera.blit(self.idle[5], (px, py))
		elif self.last_direction == "downright":
			camera.blit(self.idle[6], (px, py))
		elif self.last_direction == "upright":
			camera.blit(self.idle[7], (px, py))

	def showBackground(self, back_image, x, y, camera):
		camera.blit(back_image, (x, y))

	def inGameAttack(self, Player, camera, reset):
		"Magic use sprites in game out of battle mode"
		px = Player.getX()
		py = Player.getY()
		if Player.getDirection() == "":
			pDirection = self.last_direction
		else:
			pDirection = Player.getDirection()

		if reset and self.attacking != True:
			self.attack_frame = 0
			self.attacking = True

		if pDirection == "up":
			if self.attack_frame <= len(self.sprites[8]) - 1 and self.attacking:
				camera.blit(self.sprites[8][int(self.attack_frame)], (px, py))
				self.attack_frame += 0.20
			else:
				self.attacking = False

		elif pDirection == "left":
			if self.attack_frame < len(self.sprites[9]) - 1 and self.attacking:
				camera.blit(self.sprites[9][int(self.attack_frame)], (px, py))
				self.attack_frame += 0.20
			else:
				self.attacking = False

		elif pDirection == "down":
			if self.attack_frame < len(self.sprites[10]) - 1 and self.attacking:
				camera.blit(self.sprites[10][int(self.attack_frame)], (px, py))
				self.attack_frame += 0.20
			else:
				self.attacking = False

		elif pDirection == "right":
			if self.attack_frame < len(self.sprites[11]) - 1 and self.attacking:
				camera.blit(self.sprites[11][int(self.attack_frame)], (px, py))
				self.attack_frame += 0.20
			else:
				self.attacking = False

		elif pDirection == "upleft":
			if self.attack_frame < len(self.sprites[12]) - 1 and self.attacking:
				camera.blit(self.sprites[12][int(self.attack_frame)], (px, py))
				self.attack_frame += 0.20
			else:
				self.attacking = False

		elif pDirection == "leftdown":
			if self.attack_frame < len(self.sprites[13]) - 1 and self.attacking:
				camera.blit(self.sprites[13][int(self.attack_frame)], (px, py))
				self.attack_frame += 0.20
			else:
				self.attacking = False

		elif pDirection == "downright":
			if self.attack_frame < len(self.sprites[14]) - 1 and self.attacking:
				camera.blit(self.sprites[14][int(self.attack_frame)], (px, py))
				self.attack_frame += 0.2
			else:
				self.attacking = False

		elif pDirection == "upright":
			if self.attack_frame < len(self.sprites[15]) - 1 and self.attacking:
				camera.blit(self.sprites[15][int(self.attack_frame)], (px, py))
				self.attack_frame += 0.20
			else:
				self.attacking = False

		return self.attacking

	def battle(self):
		"play sprite for battle, including idle, attacking and damaged"