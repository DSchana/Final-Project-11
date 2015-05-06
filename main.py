# main.py

from pygame import *
from math import *
from random import *
from Sound import *
from Player import *
from Enemy import *

screen = display.set_mode((850, 600))

# create subsurface of a camera
camera = screen.subsurface((0, 0, 850, 600))

# main music
main_theme = Sound("Audio/main.mp3")

# play main sound track
main_theme.execute(0)

# create usable player
self.enemyList = []
self.playerList = []

self.playerList.append(Player("Jeffery", 100,  "Huflepuff", 0, 1, 1, 1, 200, 100, [], 10, 4, 400, 300, "wasd"))

for i in range(5):
	self.enemyList.append(Enemy(100, "Slytherin", randint(1, 3), randint(1, 10), randint(50, 150), randint(5, 10), "Death eater", randint(10, 800), randint(10, 550)))

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
		if e.type == QUIT:
			running = False

	# do player stuff
	playerList[0].analyzeInput(camera, False, pressed)

	# do enemy methods
	for i in range(len(enemyList)):
		enemyList[i].analyzeInput(camera, playerList[0])

	if playerList[0].getHealth() <= 0:
		running = False

	# temporary
	print(round(playerList[0].getHealth(), 0), round(playerList[0].getSpellEnergy(), 0), round(playerList[0].getStamina(), 0), playerList[0].getX(), playerList[0].getY())

	# draw stuff
	display.flip()
	gameClock.tick(60)

quit()