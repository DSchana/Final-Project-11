# main.py

import os
from pygame import *
from math import *
from random import *
from Sound import *
from Player import *
from Enemy import *
from Battle import *
from Sprites import *
from Menu import *

os.environ['SDL_VIDEO_WINDOW_POS'] = '25,50' #Opens up in the upper left corner 
screen = display.set_mode((850, 600))
display.set_caption("Harry Potter: New Horizons")
mouse.set_cursor(*cursors.tri_left)

# create subsurface of a camera
camera = screen.subsurface((0, 0, 850, 600))

# main music
music = {}
music["main"] = Sound("Audio/main.mp3")
music["menu"] = Sound("Audio/menu.mp3")
music["credits"] = Sound("Audio/credits.mp3")

mode_select = loadImages(screen, music["menu"])

# Variable checks if the game has been drawn so it does not draw again
gameScreenInit = False
running = True

while running:
	if mode_select == "controls":
		print("Controls")

	if mode_select == "credits":
		displayCredits(screen, music["credits"])
		mode_select = loadImages(screen, music["menu"])

	if mode_select == "play":
		if not gameScreenInit:
			enemyList = []
			playerList = []

			harrySprites = Sprites("Images/walking/walkUp/", "Images/walking/walkLeft/", "Images/walking/walkDown/", "Images/walking/walkRight/", "Images/walking/walkUpLeft/", 
					"Images/walking/walkDownLeft/", "Images/walking/walkDownRight/", "Images/walking/walkUpRight/")
			harrySprites.loadImages()

			# create usable player
			playerList.append(Player("Jeffery", 100,  "Huflepuff", 0, 1, 1, 1, 200, 100, [], 10, 4, 400, 300))

			# Constant player values
			p_width = playerList[0].getWidth()
			p_height = playerList[0].getHeight()

			gameClock = time.Clock()

			music["main"].execute(0)

			gameScreenInit = True

		elif gameScreenInit:
			mx, my = mouse.get_pos()
			pressed = key.get_pressed()

			camera.fill((0, 168, 64))  # replace with blit background
			for e in event.get():
				# do player stuff
				#playerList[0].analyzeInput(camera, pressed, e, harrySprites)
				if e.type == QUIT:
					running = False

			# do player stuff
			playerList[0].analyzeInput(camera, pressed, False, harrySprites)

			# do enemy methods
			for i in range(len(enemyList)):
				enemyList[i].analyzeInput(camera, playerList[0])

			if playerList[0].getHealth() <= 0:
				running = False

			display.flip()
			gameClock.tick(60)

		if mode_select == "exit":
			running = False

quit()