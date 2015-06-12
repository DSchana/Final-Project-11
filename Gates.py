# objectSprites.py

from pygame import *
from battleBlob import *
import glob

class Gate:
	def __init__(self, Player, dx, dy, width, height, new_location, new_x, new_y, directoryList = False):
		self.frame = 0
		self.directoryList = directoryList

		self.new_x = new_x
		self.new_y = new_y
		self.door_x = Player.getBX() + dx
		self.door_y = Player.getBY() + dy

		self.dx = dx
		self.dy = dy
		self.width = width
		self.height = height

		self.new_location = new_location

		self.sprites = [[]]

	def loadImages(self):
		if self.directoryList != False:
			for i in range(len(self.directoryList)):
				self.sprites.append(glob.glob(self.directoryList[i] + "*.png"))
			
			self.sprites.sort()

			# Compensate for issue with globbing
			del self.sprites[0]

			for i in range(len(self.sprites)):
				for j in range(len(self.sprites[i])):
					self.sprites[i][j] = transform.scale(image.load(self.sprites[i][j]), (self.width, self.height))

	def idle(self, camera, Player):
		"Draws door to background when door is not being interacted with"
		self.door_x = Player.getBX() + self.dx
		self.door_y = Player.getBY() + self.dy

		if self.directoryList != False:
			camera.blit(self.sprites[0][0], (self.door_x, self. door_y))

	def open(self, camera, Player, backgrounds):
		"Opens door when player approaches door"
		self.door_x = Player.getBX() + self.dx
		self.door_y = Player.getBY() + self.dy

		if self.directoryList != False:
			for frame in range(0, len(self.sprites[0])):
				camera.blit(self.sprites[0][int(frame)], (self.door_x, self.door_y))
				time.delay(100)  # timmer slows down animation
				display.flip()

	# Get methods for objectSprites
	def getX(self):
		return self.door_x

	def getY(self):
		return self.door_y

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def getNewLocation(self):
		return self.new_location

	def getNewX(self):
		return self.new_x

	def getNewY(self):
		return self.new_y