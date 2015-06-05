#Harry Potter: New Horizons
#Loading, start screen with menu 

from pygame import *
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '25,50' #Opens up in the upper left corner 
screen = display.set_mode((850,600)) #Game window resolution

def loadImages(screen, music):
	#Loading Screen
	loadingPic1 = image.load ("Images/loading/loading1.jpg")
	screen.blit(loadingPic1, (0,0))
	display.flip()
	loadingComplete = False
	#The dots appear to be animated as the game loads
	loadingPic2 = image.load ("Images/loading/loading2.jpg")
	loadingPic3 = image.load ("Images/loading/loading3.jpg")

	#Load the images 
	difficultyScreen = image.load ("Images/loading/difficulty.jpg")
	difficultyEasyIdle = image.load ("Images/loading/EasyIdle.png")
	difficultyEasyHighlight = image.load ("Images/loading/EasyHigh.png")
	difficultyNormalIdle = image.load ("Images/loading/NormalIdle.png")
	difficultyNormalHighlight = image.load ("Images/loading/NormalHigh.png")
	difficultyHardIdle = image.load ("Images/loading/HardIdle.png")
	difficultyHardHighlight = image.load ("Images/loading/HardHigh.png")

	creditsScreen = image.load ("Images/loading/credits.jpg")
	textScreen = image.load ("Images/loading/text.jpg")

	screen.blit(loadingPic2, (0,0))
	display.flip()

	#rightWalkSpriteList = []
	#leftWalkSpriteList = []
	#upWalkSpriteList = []
	#downWalkSpriteList = []

	#rightUpWalkSpriteList = []
	#rightDownWalkSpriteList = []
	#leftUpWalkSpriteList = []
	#leftDownSpriteList = []

	blackScreen = image.load ("Images/loading/template.jpg")
	homeScreenBlur = image.load ("Images/loading/altHome.jpg")
	logo = image.load ("Images/loading/HPlogo.png")
	logo = transform.scale(logo,(450,170))
	#Used to hide unwated blit objects 
	screenGrabRect = Rect(0,0,850,600)
	menuGrabRect = Rect(0,0,850,600) 
	playButton = image.load ("Images/loading/playButton.png")
	playButton = transform.scale(playButton,(200,80))
	creditsButton = image.load ("Images/loading/creditsButton.png")
	creditsButton = transform.scale(creditsButton,(200,50))
	controlsButton = image.load ("Images/loading/controlsButton.png")
	controlsButton = transform.scale(controlsButton,(200,50))

	screen.blit(loadingPic3, (0,0))
	display.flip()

	playButtonRect = Rect(323,217,202,82) 
	controlsButtonRect = Rect(325,330,200,50)
	creditsButtonRect = Rect(325,410,200,50)

	menu = "home" #used to control the rects drawn on different screens 

	font.init()
	otherFont = font.SysFont("High Tower Text", 28)

	music.execute(-1)

	while menu == "home":
		mb = mouse.get_pressed()
		mx,my = mouse.get_pos()

		for e in event.get():
			if e.type == QUIT:
				return "exit"
			if loadingComplete == False:
				screen.blit(blackScreen,(0,0))
				display.flip()
				#Background drops down
				for i in range (-500,0,5):
					screen.blit(homeScreenBlur,(-120,i)) 
					time.wait(2)
					display.flip()
				screenGrab = screen.subsurface(screenGrabRect).copy()
				#Logo slides up
				for i in range (-600,0,10):
					screen.blit(screenGrab,(0,0))
					screen.blit(logo,(200,-i+15)) #Arbitrary 15px offset
					#350
					display.flip()
			loadingComplete = True #prevents the screen from sliding down again
			screenGrab = screen.subsurface(screenGrabRect).copy()

			#This black rectangle hides the differences in size between the buttons
			#and the yellow highlight rects for the Play button
			draw.rect(screen,(0,0,0),[323,217,202,82])
			
			screen.blit(playButton,(325,220))
			screen.blit(controlsButton,(325,330))
			screen.blit(creditsButton,(325,410))

			subtitle = otherFont.render(("New Horizons"), True, (111,127,132))
			screen.blit(subtitle,(460,145))
			
			#Fix the coordinates for the yellow rect to match the black rectangles
			draw.rect(screen,(255,255,0),[322,218,202,82],2)
			draw.rect(screen,(255,255,0),[325,330,200,50],2)
			draw.rect(screen,(255,255,0),[325,410,200,50],2)
			menuGrab = screen.subsurface(menuGrabRect).copy()
			screen.blit(menuGrab,(0,0))
			#Highlights the selected box when mouse is over it
			#Clears previous highlights when mouse is moved
			if playButtonRect.collidepoint((mx,my)):
				draw.rect(screen,(0,255,0),[322,218,202,82],2)
				if mb[0]:
					music.halt()
					return "play"
			elif controlsButtonRect.collidepoint((mx,my)):
				draw.rect(screen,(0,255,0),[325,330,200,50],2)
				if mb[0]:
					music.halt()
					return "controls"
			elif creditsButtonRect.collidepoint((mx,my)):
				draw.rect(screen,(0,255,0),[325,410,200,50],2)
				if mb[0]:
					music.halt()
					return "credits"
			elif e.type == KEYDOWN:
				if key.get_pressed()[K_ESCAPE]:
					music.halt()
					return "exit"
				if key.get_pressed()[K_RETURN]:
					music.halt()
					return "play"

		display.flip()

def displayCredits(screen, music):
	creditsScreen = image.load ("Images/loading/credits.jpg")
	screen.blit(creditsScreen, (0, 0))
	display.flip()
	music.execute(0)
	while True:
		for e in event.get():
			if e.type == KEYDOWN:
				if key.get_pressed()[K_ESCAPE]:
					music.halt()
					return "menu"

def displayControls(screen):
	controlsScreen = image.load("Images/loading/controls.jpg")
	screen.blit(controlsScreen, (0, 0))
	display.flip()
	while True:
		for e in event.get():
			if e.type == KEYDOWN:
				if key.get_pressed()[K_ESCAPE]:
					return "menu"

def chooseHouse(screen):
	grifHouseSelect = image.load ("Images/loading/grifHouse.png")
	slyHouseSelect = image.load ("Images/loading/slyHouse.png")
	ravenHouseSelect = image.load ("Images/loading/ravenHouse.png")
	huffHouseSelect = image.load ("Images/loading/huffHouse.png")
	hogwartsBadge = image.load("Images/loading/HogwartsBadge.png")

	blackScreen = image.load ("Images/loading/template.jpg")
	textScreen = image.load("Images/loading/text.jpg")
	screenGrabRect = Rect(0, 0, 850, 600)

	grifHouseSelect = transform.scale(grifHouseSelect,(420,300))
	slyHouseSelect = transform.scale(slyHouseSelect,(420,300))
	ravenHouseSelect = transform.scale(ravenHouseSelect,(420,300))
	huffHouseSelect = transform.scale(huffHouseSelect,(420,300))
	hogwartsBadge = transform.scale(hogwartsBadge,(300,300))

	grifHouseSelectRect = Rect(0,0,420,300)
	slyHouseSelectRect = Rect(430,0,420,300)
	huffHouseSelectRect = Rect(0,300,420,300)
	ravenHouseSelectRect = Rect(430,300,420,300)

	playerHouse = ""
	goBack = False
	textComplete = False

	screen.blit(blackScreen,(0,0)) #Hides gaps between the pictures
	#This should be inside the loop with if statement condition in the actual code
	#eg. if textComplete==True:
	screen.blit(grifHouseSelect,(0,0))
	screen.blit(slyHouseSelect,(430,0))
	screen.blit(huffHouseSelect,(0,300))
	screen.blit(ravenHouseSelect,(430,300))
	screen.blit(hogwartsBadge,(275,150))
	screenGrab = screen.subsurface(screenGrabRect).copy()

	running = True
	while running:

		mb = mouse.get_pressed()
		mx,my = mouse.get_pos()

		for e in event.get():       
			if e.type == QUIT:     
				running = False
				
			#The house selected is highlighted in yellow
			#The previous highlights are hidden with a clean image, screenGrab  
			if grifHouseSelectRect.collidepoint((mx,my)) and playerHouse=="":
				screen.blit(screenGrab,(0,0))
				draw.rect(screen,(255,255,0),[0,0,420,300],2)
				#The lines are drawn over the crest so the crest must be drawn again overtop
				screen.blit(hogwartsBadge,(275,150))
				if mb[0]==1:
					playerHouse = "gryffindor"
					
			elif slyHouseSelectRect.collidepoint((mx,my)) and playerHouse=="":
				screen.blit(screenGrab,(0,0))
				draw.rect(screen,(255,255,0),[430,0,420,300],2)
				screen.blit(hogwartsBadge,(275,150))
				if mb[0]==1:
					playerHouse = "slytherin"
					
			elif huffHouseSelectRect.collidepoint((mx,my)) and playerHouse=="":
				screen.blit(screenGrab,(0,0))
				draw.rect(screen,(255,255,0),[0,300,420,300],2)
				screen.blit(hogwartsBadge,(275,150))
				if mb[0]==1:
					playerHouse = "hufflepuff"
					
			elif ravenHouseSelectRect.collidepoint((mx,my)) and playerHouse=="":
				screen.blit(screenGrab,(0,0))
				draw.rect(screen,(255,255,0),[430,300,420,300],2)
				screen.blit(hogwartsBadge,(275,150))
				if mb[0]==1:
					playerHouse = "ravenclaw"
	
			if textComplete == False and playerHouse != "": 
				#Text drops down when a house is chosen
				for i in range (-500,0,5):
					screen.blit(textScreen,(0,i+10)) 
					time.wait(2)
					display.flip()
				textComplete = True

			if textComplete and e.type == MOUSEBUTTONDOWN:
				return playerHouse
			
		display.flip()

def chooseDifficulty(screen):
	difficultyScreen = image.load ("Images/loading/difficulty.jpg")
	difficultyEasyIdle = image.load ("Images/loading/EasyIdle.png")
	difficultyEasyHighlight = image.load ("Images/loading/EasyHigh.png")
	difficultyNormalIdle = image.load ("Images/loading/NormalIdle.png")
	difficultyNormalHighlight = image.load ("Images/loading/NormalHigh.png")
	difficultyHardIdle = image.load ("Images/loading/HardIdle.png")
	difficultyHardHighlight = image.load ("Images/loading/HardHigh.png")

	#relevant to this screen only
	screen.blit(difficultyScreen,(-10,0))
	display.flip()

	draw.rect(screen,(0,0,0),[223,178,420,75]) 
	draw.rect(screen,(0,0,0),[223,298,420,75])
	draw.rect(screen,(0,0,0),[223,418,420,85])

	draw.rect(screen,(255,255,255),[225,180,415,70]) 
	draw.rect(screen,(255,255,255),[225,300,415,70])
	draw.rect(screen,(255,255,255),[225,420,415,70])

	screen.blit(difficultyEasyIdle,(285,180))
	screen.blit(difficultyNormalIdle,(275,300))
	screen.blit(difficultyHardIdle,(225,420))

	difficultyEasyButtonRect = Rect(225,180,415,70) #same rects as above
	difficultyNormalButtonRect = Rect(225,300,415,70)
	difficultyHardButtonRect = Rect(225,420,415,70)

	#The following is already defined in the main program start.py
	difficultyChosen = False
	font.init()
	difficultyFont = font.SysFont("Castellar", 52)
	difficultyTitle = difficultyFont.render(("Select Difficulty"), True, (255,255,0))
	screen.blit(difficultyTitle,(162,75))
	difficulty = ""

	screenGrabRect = Rect(0,0,850,600)
	screenGrab = screen.subsurface(screenGrabRect).copy()

	running = True
	while running:

		mb = mouse.get_pressed()
		mx,my = mouse.get_pos()

		for e in event.get():
			if e.type == QUIT:
				running = False

			screen.blit(difficultyEasyIdle, (285, 180))
			screen.blit(difficultyNormalIdle, (275, 300))
			screen.blit(difficultyHardIdle, (225, 420))

			if difficultyEasyButtonRect.collidepoint((mx,my)) and difficultyChosen==False:
				screen.blit(screenGrab,(0,0))
				screen.blit(difficultyEasyHighlight,(285,180))
				if mb[0] == 1:
					time.delay(200)
					difficultyChosen = True
					difficulty = "easy"
					return difficulty
				
			elif difficultyNormalButtonRect.collidepoint((mx,my)) and difficultyChosen==False:
				screen.blit(screenGrab,(0,0))
				screen.blit(difficultyNormalHighlight,(275,300))
				if mb[0] == 1:
					time.delay(200)
					difficultyChosen = True
					difficulty = "normal"
					return difficulty
				
			elif difficultyHardButtonRect.collidepoint((mx,my)) and difficultyChosen==False:
				screen.blit(screenGrab,(0,0))
				screen.blit(difficultyHardHighlight,(225,420))
				if mb[0] == 1:
					time.delay(200)
					difficultyChosen = True
					difficulty = "hard"
					return difficulty

		display.flip()