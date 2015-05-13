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

os.environ['SDL_VIDEO_WINDOW_POS'] = '25,50' #Opens up in the upper left corner 

screen = display.set_mode((850, 600))

# create subsurface of a camera
camera = screen.subsurface((0, 0, 850, 600))

# main music
main_theme = Sound("Audio/main.mp3")

# play main sound track
main_theme.execute(0)

enemyList = []
playerList = []

harrySprites = Sprites("Images/walking/walkUp/", "Images/walking/walkLeft/", "Images/walking/walkDown/", "Images/walking/walkRight/", "Images/walking/walkUpLeft/", 
		"Images/walking/walkDownLeft/", "Images/walking/walkDownRight/", "Images/walking/walkUpRight/")
harrySprites.loadImages()

# create usable player
playerList.append(Player("Jeffery", 100,  "Huflepuff", 0, 1, 1, 1, 200, 100, [], 10, 4, 400, 300, "wasd"))

for i in range(5):
	enemyList.append(Enemy(100, "Slytherin", randint(1, 3), randint(1, 10), randint(50, 150), randint(5, 10), "Death eater", randint(10, 800), randint(10, 550)))

# Constant player values
p_width = playerList[0].getWidth()
p_height = playerList[0].getHeight()

gameClock = time.Clock()
running = True

while running:
	mx, my = mouse.get_pos()
	pressed = key.get_pressed()

	camera.fill((0, 168, 64))
	for e in event.get():
		# do player stuff
		playerList[0].analyzeInput(camera, pressed, e, harrySprites)
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

quit()
