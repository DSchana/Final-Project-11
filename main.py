# main.py

from pygame import *
from classes import *
from enum import *
from math import *
from random import *

screen = display.set_mode((700, 500))
screen.fill((0, 0, 255))

enemyList = []
playerList = []
blockList = []

playerList.append(player(4, 100, 3.2, 400, False, 100, 300, "arrow"))
playerList.append(player(3, 100, 3.2, 400, False, 600, 200, "wasd"))

enemyList.append(enemy(1.5, 3, 10, "blob", 10, 20))
enemyList.append(enemy(0.5, 3, 10, "blob", 100, 400))
enemyList.append(enemy(1, 3, 10, "blob", 100, 200))

for i in range(8):
	blockList.append(block(5, True, "stone", False, 100 + i*60, 300))

gameClock = time.Clock()
running = True

while running:
	screen.fill((0, 0, 255))
	for e in event.get():
		if e.type == QUIT:
			running = False

	pressed = key.get_pressed()

	# do player meathods
	for i in range(len(playerList)):
		playerList[i].move(pressed, screen)

	# do enemy methods
	if len(playerList)>1:
		for i in range(len(enemyList)):
			if sqrt((playerList[0].getX()-enemyList[i].getX())**2 + (playerList[0].getY() - enemyList[i].getY())**2) < sqrt((playerList[1].getX()-enemyList[i].getX())**2 + (playerList[1].getY() - enemyList[i].getY())**2):
				enemyList[i].move(playerList[0].getX(), playerList[0].getY(), screen)
			elif sqrt((playerList[0].getX()-enemyList[i].getX())**2 + (playerList[0].getY() - enemyList[i].getY())**2) > sqrt((playerList[1].getX()-enemyList[i].getX())**2 + (playerList[1].getY() - enemyList[i].getY())**2):
				enemyList[i].move(playerList[1].getX(), playerList[1].getY(), screen)
	else:
		for i in range(len(enemyList)):
			enemyList[i].move(playerList[0].getX(), playerList[0].getY(), screen)

	for i in range(len(blockList)):
		blockList[i].show(screen)

	gameClock.tick(60)
	display.flip()

quit()