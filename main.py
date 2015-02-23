# main.py

from pygame import *
from classes import *
from enum import *
from math import *
from random import *

screen = display.set_mode((850, 600))
screen.fill((0, 0, 255))

enemyList = []
playerList = []

playerList.append(player("Jeffery", 100,  "Slytherin", 1, 1, 1, 10, 4, 400, 300, "wasd"))
#playerList.append(player(3, 100, 3.2, 400, False, 600, 200, "wasd"))

enemyList.append(enemy(100, 2, 10, 50, "blob", 10, 20))
enemyList.append(enemy(100, 2, 10, 75, "blob", 100, 400))
enemyList.append(enemy(100, 1, 10, 100, "blob", 100, 200))

gameClock = time.Clock()
running = True

while running:
	screen.fill((0, 168, 64))
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

	for i in range(len(enemyList)):
		rx = playerList[0].getX()
		ry = playerList[0].getY()
		width = playerList[0].getWidth()
		height = playerList[0].getHeight()
		cx = enemyList[i].getX()
		cy = enemyList[i].getY()
		radius = enemyList[i].getAttackRadius()
		if enemyList[i].checkCollision(rx, ry, width, height, cx, cy, radius):
			playerList[0].gotHit()

	if playerList[0].getHealth() <= 0:
		running = False

	print(playerList[0].getHealth())
			

	gameClock.tick(60)
	display.flip()

quit()