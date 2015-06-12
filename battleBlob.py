# battleBlob.py

from pygame import *
from random import *
import glob

class Blob:
	def __init__(self, Player, backgrounds):
		self.player = Player
		self.x = randint(50, backgrounds[Player.getLocation()].get_rect()[2] - 50)
		self.y = randint(50, backgrounds[Player.getLocation()].get_rect()[3] - 50)
		self.width = 15
		self.height = 11

		self.frame = 0
		self.image_list = glob.glob("Images/battleBlob/*.png")

		for i in range(len(self.image_list)):
			self.image_list[i] = image.load(self.image_list[i])

		self.rect = Rect(self.x, self.y, self.width, self.height)

	def show(self, camera, masks):
		show_x = self.x + self.player.getBX()
		show_y = self.y + self.player.getBY()

		if self.frame < len(self.image_list)-1:
			self.frame += 0.2
		else:
			self.frame = 0
		if masks[self.player.getLocation()].get_at((self.x, self.y)) != (255, 0, 0) and masks[self.player.getLocation()].get_at((self.x, self.y)) != (255, 255 , 0):
			camera.blit(self.image_list[int(self.frame)], (show_x,  show_y))

	# Get methods
	def getRect(self):
		return self.rect