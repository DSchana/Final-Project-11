# main.py

from pygame import *
from classes import *

screen = display.set_mode((700, 500))
screen.fill((0, 0, 255))

player1 = player(1.6, 100, 3.2, 400, False, 100, 300)

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

	gameClock.tick(60)
	display.flip()

quit()