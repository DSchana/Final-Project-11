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

		self.frame = 0
		self.max_frame = 0

	def loadImages(self):
		for i in range(len(self.directories)):
			if self.directories[i] != False:
				self.sprites.append(glob.glob(self.directories[i] + "*.png"))  ## shits not working
				self.sprites[i].sort()

		for i in range(8):
			for j in range(len(self.sprites[i])):
				self.sprites[i][j] = image.load(self.sprites[i][j])

	def changeSprite(self, Player, camera):
		px = Player.getX()
		py = Player.getY()
		pDirection = Player.getDirection()

		if pDirection == "right":
			camera.blit(self.sprites[3][int(self.frame)],(px,py)) 
			if self.frame > len(self.sprites[3]): #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2
			
		elif pDirection == "left":
			camera.blit(self.sprites[1][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[1]): #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2

		elif pDirection == "up":
			camera.blit(self.sprites[0][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[0]): #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2

		elif pDirection == "down":
			camera.blit(self.sprites[2][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[2]): #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2

		# diagonal sprites
		elif pDirection == "upleft":
			camera.blit(self.sprites[4][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[4]): #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2

		elif pDirection == "leftdown":
			camera.blit(self.sprites[5][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[5]): #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2

		elif pDirection == "downright":
			camera.blit(self.sprites[6][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[6]): #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2

		elif pDirection == "upright":
			camera.blit(self.sprites[7][int(self.frame)],(px,py))
			if self.frame > len(self.sprites[7]): #8 frames total for this animation
				self.frame = 0
			self.frame += 0.2

		else:
			self.frame = 0

		display.flip()
