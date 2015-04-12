# main.py

from pygame import *
from enum import *
from math import *
from random import *
from Sound import *
from Player import *
from Enemy import *

screen = display.set_mode((850, 600))
screen.fill((0, 0, 255))

# main music
## main_theme = Sound("Audio/main.mp3")

# play main sound track
## main_theme.execute(-1)

enemyList = []
playerList = []

playerList.append(Player("Jeffery", 100,  "Huflepuff", 0, 1, 1, 1, 200, 100, [], 10, 4, 400, 300, "wasd"))

enemyList.append(Enemy(100, "Slytherin", 2, 5, 50, 4, "Beletrix", 10, 20))
enemyList.append(Enemy(100, "Slytherin", 2, 5, 75, 6, "Lucius", 100, 400))
enemyList.append(Enemy(100, "Slytherin", 1, 10, 100, 10, "Voldemort", 100, 200))

# Constant player values
p_width = playerList[0].getWidth()
p_height = playerList[0].getHeight()

gameClock = time.Clock()
running = True

while running:
	screen.fill((0, 168, 64))
	for e in event.get():
		if e.type == QUIT:
			running = False
		if e.type == MOUSEBUTTONDOWN:
			playerList[0].attack(mx, my, screen)

	mx, my = mouse.get_pos()
	pressed = key.get_pressed()

	for i in range(len(playerList)):
		playerList[i].move(pressed, screen)

	# do enemy methods
	for i in range(len(enemyList)):
		rx = playerList[0].getX()
		ry = playerList[0].getY()
		cx = enemyList[i].getX()
		cy = enemyList[i].getY()
		radius = enemyList[i].getAttackRadius()
		if enemyList[i].checkCollision(rx, ry, p_width, p_height, cx, cy, radius):
			playerList[0].gotHit(enemyList[i].getFireRate())
			enemyList[i].show(screen)
		else:
			enemyList[i].move(playerList[0].getX(), playerList[0].getY(), screen)

	if playerList[0].getHealth() <= 0:
		running = False

	print(playerList[0].getHealth(), playerList[0].getSpellEnergy())
			

	gameClock.tick(60)
	display.flip()

quit()