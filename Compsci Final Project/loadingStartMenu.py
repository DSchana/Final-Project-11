#Harry Potter: New Horizons
#Loading, start screen with menu 

from pygame import*
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '25,50' #Opens up in the upper left corner 
screen = display.set_mode((850,600)) #Game window resolution
display.set_caption("Harry Potter: New Horizons")
mouse.set_cursor(*cursors.tri_left)

#Loading Screen
loadingPic1 = image.load ("loading.jpg")
screen.blit(loadingPic1, (0,0))
display.flip()
loadingComplete = False
#The dots appear to be animated as the game loads
loadingPic2 = image.load ("loadingDot.jpg")

#Load the images 
difficultyScreen = image.load ("difficulty.jpg")
difficultyEasyIdle = image.load ("EasyIdle.png")
difficultyEasyHighlight = image.load ("EasyHigh.png")
difficultyNormalIdle = image.load ("NormalIdle.png")
difficultyNormalHighlight = image.load ("NormalHigh.png")
difficultyHardIdle = image.load ("HardIdle.png")
difficultyHardHighlight = image.load ("HardHigh.png")

creditsScreen = image.load ("credits.jpg")
textScreen = image.load ("text.jpg")

grifHouseSelect = image.load ("grifHouse.png")
slyHouseSelect = image.load ("slyHouse.png")
ravenHouseSelect = image.load ("ravenHouse.png")
huffHouseSelect = image.load ("huffHouse.png")
hogwartsBadge = image.load ("HogwartsBadge.png")
grifHouseSelect = transform.scale(grifHouseSelect,(420,300))
slyHouseSelect = transform.scale(slyHouseSelect,(420,300))
ravenHouseSelect = transform.scale(ravenHouseSelect,(420,300))
huffHouseSelect = transform.scale(huffHouseSelect,(420,300))
hogwartsBadge = transform.scale(hogwartsBadge,(300,300))
grifHouseSelectRect = Rect(0,0,420,300)
slyHouseSelectRect = Rect(430,0,420,300)
huffHouseSelectRect = Rect(0,300,420,300)
ravenHouseSelectRect = Rect(275,150,420,300)

screen.blit(loadingPic2, (802,571))
display.flip()

#Load sprites here ********

blackScreen = image.load ("template.jpg")
homeScreenBlur = image.load ("altHome.jpg")
logo = image.load ("HPlogo.png")
logo = transform.scale(logo,(450,170))
#Used to hide unwated blit objects and highlights 
screenGrabRect = Rect(0,0,850,600)
menuGrabRect = Rect(0,0,850,600)

playButton = image.load ("playButton.png")
playButton = transform.scale(playButton,(200,80))
creditsButton = image.load ("creditsButton.png")
creditsButton = transform.scale(creditsButton,(200,50))
controlsButton = image.load ("controlsButton.png")
controlsButton = transform.scale(controlsButton,(200,50))
playButtonRect = Rect(323,217,202,82) 
controlsButtonRect = Rect(325,330,200,50)
creditsButtonRect = Rect(325,410,200,50)

screen.blit(loadingPic2, (812,571))
display.flip()

menu = "home" #used to control the screens drawn depending on the option selected

#These flags control when/if menus drop down
creditsComplete = False
textComplete = False
difficultyChosen = False
goBack = False
difficulty = ""
playerHouse = ""

#In-game menu
#*****HERE

#Setup
songPlaylist = ["theme.mp3"]
init() #Initialize the mixer
mixer.music.load(songPlaylist[0])  
mixer.music.play()

font.init()
otherFont = font.SysFont("High Tower Text", 28)
subtitle = otherFont.render(("New Horizons"), True, (111,127,132))

font.init()
difficultyFont = font.SysFont("Castellar", 52)
difficultyTitle = difficultyFont.render(("Select Difficulty"), True, (0,0,0))
screen.blit(difficultyTitle,(195,80))

running = True
while running:

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    for e in event.get():       
        if e.type == QUIT:     
            running = False
            
        if e.type == KEYDOWN and e.key == 27: #If the esc key is pressed
            goBack = True
        
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
                display.flip()
                
        loadingComplete = True #prevents the screen from sliding down again
        screenGrab = screen.subsurface(screenGrabRect).copy()

        #This black rectangle hides the differences in size between the buttons
        #and the yellow highlight rects for the Play button
        draw.rect(screen,(0,0,0),[323,217,202,82])
        
        screen.blit(playButton,(325,220))
        screen.blit(controlsButton,(325,330))
        screen.blit(creditsButton,(325,410))

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
            screen.blit(menuGrab,(0,0))
            draw.rect(screen,(0,255,0),[322,218,202,82],2)
            menu = "play"
        elif controlsButtonRect.collidepoint((mx,my)):
            screen.blit(menuGrab,(0,0))
            draw.rect(screen,(0,255,0),[325,330,200,50],2)  
            menu = "controls"
        elif creditsButtonRect.collidepoint((mx,my)):
            screen.blit(menuGrab,(0,0))
            draw.rect(screen,(0,255,0),[325,410,200,50],2)
            menu = "credits"
        else:
            screen.blit(menuGrab,(0,0))            

    display.flip()
font.quit()
del otherFont
del difficultyFont
quit()
