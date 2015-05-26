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
	if mode_select == "menu":
		mode_select = loadImages(screen, music["menu"])

	elif mode_select == "controls":
		mode_select = displayControls(screen)

	elif mode_select == "credits":
		mode_select = displayCredits(screen, music["credits"])

	elif mode_select == "play":
		if not gameScreenInit:
			loading1 = image.load("Images/loading/loading1.jpg")
			loading2 = image.load("Images/loading/loading2.jpg")
			loading3 = image.load("Images/loading/loading3.jpg")

			screen.blit(loading1, (0, 0))
			display.flip()

			enemyList = []
			playerList = []
			backgrounds = {}

			harrySprites = Sprites("Images/walking/walkUp/", "Images/walking/walkLeft/", "Images/walking/walkDown/", "Images/walking/walkRight/", "Images/walking/walkUpLeft/", 
					"Images/walking/walkDownLeft/", "Images/walking/walkDownRight/", "Images/walking/walkUpRight/", "Images/attack/castSpellUp/", "Images/attack/castSpellLeft/",
					"Images/attack/castSpellDown/", "Images/attack/castSpellRight/", "Images/attack/castSpellUpLeft/", "Images/attack/castSpellDownLeft/","Images/attack/castSpellDownRight/",
					"Images/attack/castSpellUpRight/")
			harrySprites.loadImages()

			# load backgrounds
			backgrounds["grounds"] = image.load("Images/Backgrounds/Grounds.png")

			screen.blit(loading2, (0, 0))
			display.flip()

			# create usable player
			playerList.append(Player("Jeffery", 100,  "Huflepuff", 0, 1, 1, 1, 200, 100, [], 10, 3, 425, 300))

			# Constant player values
			p_width = playerList[0].getWidth()
			p_height = playerList[0].getHeight()

			screen.blit(loading3, (0, 0))
			display.flip()

			gameClock = time.Clock()

			music["main"].execute(-1)

			gameScreenInit = True

		elif gameScreenInit:
			mx, my = mouse.get_pos()
			pressed = key.get_pressed()

			for e in event.get():
				if e.type == QUIT:
					running = False

				if e.type == KEYDOWN:
					if pressed[K_SPACE]:
						playerList[0].attacking = True
				if e.type == KEYUP:
					playerList[0].attacking = False
			
			playerList[0].analyzeInput(camera, pressed, harrySprites, backgrounds)

			# do enemy methods
			for i in range(len(enemyList)):
				enemyList[i].analyzeInput(camera, playerList[0])

			if playerList[0].getHealth() <= 0:
				running = False

		elif mode_select == "exit":
			running = False

		display.set_caption("Harry Potter: New Horizons " + str(round(gameClock.get_fps(), 2)))
		gameClock.tick(60)
		display.flip()

quit()