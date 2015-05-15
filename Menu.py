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

	grifHouseSelect = image.load ("Images/loading/grifHouse.png")
	slyHouseSelect = image.load ("Images/loading/slyHouse.png")
	ravenHouseSelect = image.load ("Images/loading/ravenHouse.png")
	huffHouseSelect = image.load ("Images/loading/huffHouse.png")

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

	music.execute(0)

	while menu == "home":
		mb = mouse.get_pressed()
		mx,my = mouse.get_pos()

		for e in event.get():
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
					return "play"
			elif controlsButtonRect.collidepoint((mx,my)):
				draw.rect(screen,(0,255,0),[325,330,200,50],2)
				if mb[0]:
					return "controls"
			elif creditsButtonRect.collidepoint((mx,my)):
				draw.rect(screen,(0,255,0),[325,410,200,50],2)
				if mb[0]:
					return "credits"

		display.flip()

def displayCredits(screen, music):
	creditsScreen = image.load ("Images/loading/credits.jpg")
	screen.blit(creditsScreen, (0, 0))
	display.flip()
	music.execute(0)
	while True:
		pressed = key.get_pressed()
		if pressed[K_ESCAPE]:
			return -1