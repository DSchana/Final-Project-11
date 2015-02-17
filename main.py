# main.py

from pygame import *
from classes import *
from enum import *
from math import *

screen = display.set_mode((700, 500))
screen.fill((0, 0, 255))

enemyList = []
playerList = []

playerList.append(player(3, 100, 3.2, 400, False, 100, 300, "arrow"))
playerList.append(player(2, 100, 3.2, 400, False, 600, 200, "wasd"))

enemyList.append(enemy(1, 3, 10, "blob", 10, 20))
enemyList.append(enemy(0.5, 3, 10, "blob", 100, 200))

gameClock = time.Clock()
running = True

while running:
	screen.fill((0, 0, 255))
	for e in event.get():
		if e.type == QUIT:
			running = False

	pressed = key.get_pressed()

	# do player meathods
	player1.move(pressed, screen)
	player2.move(pressed, screen)

	# do enemy methods
	if sqrt((player1.getX()-enemy1.getX())**2 + (player1.getY() - enemy1.getY())**2) < sqrt((player2.getX()-enemy1.getX())**2 + (player2.getY() - enemy1.getY())**2):
		enemy1.move(player1.getX(), player1.getY(), screen)
	elif sqrt((player1.getX()-enemy1.getX())**2 + (player1.getY() - enemy1.getY())**2) > sqrt((player2.getX()-enemy1.getX())**2 + (player2.getY() - enemy1.getY())**2):
		enemy1.move(player2.getX(), player2.getY(), screen)

	if sqrt((player1.getX()-enemy2.getX())**2 + (player1.getY() - enemy2.getY())**2) < sqrt((player2.getX()-enemy2.getX())**2 + (player2.getY() - enemy2.getY())**2):
		enemy2.move(player1.getX(), player1.getY(), screen)
	elif sqrt((player1.getX()-enemy2.getX())**2 + (player1.getY() - enemy2.getY())**2) > sqrt((player2.getX()-enemy2.getX())**2 + (player2.getY() - enemy2.getY())**2):
		enemy2.move(player2.getX(), player2.getY(), screen)

	gameClock.tick(60)
	display.flip()

quit()