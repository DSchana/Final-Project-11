#Harry Potter: New Horizons
#Loading, start screen with menu 

from pygame import*
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '25,50' #Opens up in the upper left corner 
screen = display.set_mode((850,600)) #Game window resolution
display.set_caption("Harry Potter: New Horizons")
mouse.set_cursor(*cursors.tri_left)

#Loading Screen
loadingPic = image.load ("loading.jpg")
loadingComplete = False
screen.blit(loadingPic, (0,0))
display.flip()

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

#rightWalkSpriteList = []
#leftWalkSpriteList = []
#upWalkSpriteList = []
#downWalkSpriteList = []

#rightUpWalkSpriteList = []
#rightDownWalkSpriteList = []
#leftUpWalkSpriteList = []
#leftDownSpriteList = []

blackScreen = image.load ("template.jpg")
homeScreenBlur = image.load ("altHome.jpg")
logo = image.load ("HPlogo.png")
logo = transform.scale(logo,(450,170))
#Used to hide unwated blit objects 
screenGrabRect = Rect(0,0,850,600)
menuGrabRect = Rect(0,0,850,600) 
playButton = image.load ("playButton.png")
playButton = transform.scale(playButton,(200,80))
creditsButton = image.load ("creditsButton.png")
creditsButton = transform.scale(creditsButton,(200,50))
controlsButton = image.load ("controlsButton.png")
controlsButton = transform.scale(controlsButton,(200,50))
#Remember to update these rects 
playButtonRect = Rect(323,217,202,82) 
controlsButtonRect = Rect(325,330,200,50)
creditsButtonRect = Rect(325,410,200,50)

menu = "home" #used to control the rects drawn on different screens 

#Setup
songPlaylist = ["theme.mp3"]
init() #Initialize the mixer
mixer.music.load(songPlaylist[0])  
mixer.music.play()

font.init()
otherFont = font.SysFont("High Tower Text", 28)

running = True
while running:

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    for e in event.get():       
        if e.type == QUIT:     
            running = False
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
quit()
