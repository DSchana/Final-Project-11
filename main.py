# main.py

# THINGS TO DO:
# Hogwarts
# Story
# Characters

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
from Gates import *
from battleBlob import *

#Window preferemces 
os.environ['SDL_VIDEO_WINDOW_POS'] = '25,50'  # Opens up in the upper left corner 
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
music["grounds"] = Sound("Audio/grounds.mp3")
music["grounds battle"] = Sound("Audio/grounds battle.mp3")
music["hagrid's hut"] = Sound("Audio/grounds.mp3")
music["hagrid's hut battle"] = Sound("Audio/grounds battle.mp3")
music["entrance hall"] = Sound("Audio/entrance hall.mp3")
music["entrance hall battle"] = Sound("Audio/entrance hall battle.mp3")

mode_select = loadImages(screen, music["menu"])

#defaults 
house = ""
difficulty = ""

gameClock = time.Clock()

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
			if difficulty == "":
				difficulty = chooseDifficulty(screen)

			elif house == "":
				house = chooseHouse(screen)

			else:
				loading1 = image.load("Images/loading/loading1.jpg")
				loading2 = image.load("Images/loading/loading2.jpg")
				loading3 = image.load("Images/loading/loading3.jpg")

				screen.blit(loading1, (0, 0))
				display.flip()

				enemyList = []
				playerList = []
				gates = []
				blob_list = []
				backgrounds = {}
				back_mask = {}

				harrySprites = Sprites("Images/walking/walkUp/", "Images/walking/walkLeft/", "Images/walking/walkDown/", "Images/walking/walkRight/", "Images/walking/walkUpLeft/", 
						"Images/walking/walkDownLeft/", "Images/walking/walkDownRight/", "Images/walking/walkUpRight/", "Images/attack/castSpellUp/", "Images/attack/castSpellLeft/",
						"Images/attack/castSpellDown/", "Images/attack/castSpellRight/", "Images/attack/castSpellUpLeft/", "Images/attack/castSpellDownLeft/","Images/attack/castSpellDownRight/",
						"Images/attack/castSpellUpRight/")
				harrySprites.loadImages()

				screen.blit(loading2, (0, 0))
				display.flip()

				# load backgrounds
				backgrounds["grounds"] = image.load("Images/Backgrounds/grounds.png")
				backgrounds["entrance hall"] = image.load("Images/Backgrounds/entrance hall.png")
				backgrounds["hagrid's hut"] = image.load("Images/Backgrounds/hagrid's hut.png")

				back_mask["grounds"] = image.load("Images/Backgrounds/grounds_mask.png")
				back_mask["entrance hall"] = image.load("Images/Backgrounds/entrance hall_mask.png")
				back_mask["hagrid's hut"] = image.load("Images/Backgrounds/hagrid's hut_mask.png")

				# create usable player
				playerList.append(Player("Jeffery", 100,  house, 0, 1, 1, 1, 100, 10, 1.5, 425, 300, backgrounds, difficulty))

				# create gates for player to travle through buildings
				gates.append(Gate(playerList[0], 1771, 462, 169, 184, "entrance hall", 870, 1130, ["Images/gate/"]))
				gates.append(Gate(playerList[0], 841, 1177, 71, 10, "grounds", 1868, 654))
				gates.append(Gate(playerList[0], 2881, 3112, 33, 41, "hagrid's hut", 480, 590))
				gates.append(Gate(playerList[0], 465, 641, 48, 11, "grounds", 2886, 3142))

				for i in range(len(gates)):
					gates[i].loadImages()

				# Constant player values
				p_width = playerList[0].getWidth()
				p_height = playerList[0].getHeight()

				screen.blit(loading3, (0, 0))
				display.flip()

				music[playerList[0].getLocation()].execute()

				gameScreenInit = True

		elif gameScreenInit:
			mx, my = mouse.get_pos()
			pressed = key.get_pressed()
			test = "good"
			for e in event.get():
				if e.type == QUIT:
					running = False

				# Display in game menu
				if e.type == KEYDOWN and e.key == 101:
					inGameMenu(camera, playerList[0], music)

			if pressed[K_SPACE]:
				playerList[0].attacking = True

			playerList[0].analyzeInput(camera, pressed, harrySprites, gates, backgrounds, back_mask, music)

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
