#sprites.py

#This file contains the code to control the sprites

#def spriteMovement ():

from pygame import *
import glob

#NOTE: REMEMBER TO ADD IN THE IDLE ANIMATION and also diagonal sprites and put into a function
#Put this in the loading screen to load these sprites

class Sprites:
	def __init__(self, up_directory, left_directory, down_directory, right_directory, upleft_directory, leftdown_directory, downright_directory, upright_directory):
		self.directories = []
		self.directories.append(up_directory)  # sprites[0]
		self.directories.append(left_directory)  # sprites[1]
		self.directories.append(down_directory)  # sprites[2]
		self.directories.append(right_directory)  # sprites[3]
		self.directories.append(upleft_directory)  # sprites[4]
		self.directories.append(leftdown_directory)  # sprites[5]
		self.directories.append(downright_directory)  # sprites[6]
		self.directories.append(upright_directory)  # sprites[7]

		self.sprites = [[]]
		self.idle = []

		self.frame = 0
		self.max_frame = 0

	def loadImages(self):
		for i in range(len(self.directories)):
			if self.directories[i] != False:
				self.sprites.append(glob.glob(self.directories[i] + "*.png"))
				self.sprites[i].sort()

		# Fix the weird error in glob
		del self.sprites[0]
		self.sprites.append(self.directories[7])

		for i in range(8):
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
			
		elif pDirection == "left":
			camera.blit(self.sprites[1][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[1]) - 1: #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2

		elif pDirection == "up":
			camera.blit(self.sprites[0][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[0]) - 1: #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2

		elif pDirection == "down":
			camera.blit(self.sprites[2][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[2]) - 1: #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2

		# diagonal sprites
		elif pDirection == "upleft":
			camera.blit(self.sprites[4][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[4]) - 1: #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2

		elif pDirection == "leftdown":
			camera.blit(self.sprites[5][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[5]) - 1: #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2

		elif pDirection == "downright":
			camera.blit(self.sprites[6][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[6]) - 1: #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2

		elif pDirection == "upright":
			camera.blit(self.sprites[7][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[7]) - 1: #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2

		else:
			self.frame = 0

	def displayIdle(self, Player, camera):
		px = Player.getX()
		py = Player.getY()
		pDirection = Player.getDirection()

		if pDirection == "up":
			camera.blit(self.idle[0], (px, py))
		elif pDirection == "left":
			camera.blit(self.idle[1], (px, py))
		elif pDirection == "down":
			camera.blit(self.idle[2], (px, py))
		elif pDirection == "right":
			camera.blit(self.idle[3], (px, py))
		elif pDirection == "upleft":
			camera.blit(self.idle[4], (px, py))
		elif pDirection == "leftdown":
			camera.blit(self.idle[5], (px, py))
		elif pDirection == "downright":
			camera.blit(self.idle[6], (px, py))
		elif pDirection == "upright":
			camera.blit(self.idle[7], (px, py))