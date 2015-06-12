# battleBlob.py
#This file controls the animations for the blue blobs on the ground that launch
#battle sequences 

from pygame import *
from random import *
import glob

class Blob:
        #The blue blobs' positions are randomly generated 
	def __init__(self, Player, backgrounds):
		self.player = Player
		self.x = randint(50, backgrounds[Player.getLocation()].get_rect()[2] - 50)
		self.y = randint(50, backgrounds[Player.getLocation()].get_rect()[3] - 50)
		self.width = 15
		self.height = 11

		self.frame = 0 #default 
		self.image_list = glob.glob("Images/battleBlob/*.png")

		for i in range(len(self.image_list)): #load all sprites 
			self.image_list[i] = image.load(self.image_list[i])

		self.rect = Rect(self.x, self.y, self.width, self.height)

	def show(self, camera, masks):
		show_x = self.x + self.player.getBX()
		show_y = self.y + self.player.getBY()

                #the animation loops if the frame is over the number of existing frames
		if self.frame < len(self.image_list)-1:
			self.frame += 0.2
		else:
			self.frame = 0
		if masks[self.player.getLocation()].get_at((self.x, self.y)) != (255, 0, 0) and masks[self.player.getLocation()].get_at((self.x, self.y)) != (255, 255 , 0):
			camera.blit(self.image_list[int(self.frame)], (show_x,  show_y))

	# Get methods
	def getRect(self):
		return self.rect
