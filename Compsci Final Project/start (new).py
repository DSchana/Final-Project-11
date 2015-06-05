#Opening Screen
#The programs for the loading screen, the main menu and the screens that
#appear afterwards are all put together in this file.
#MAJOR EDIT: BACK BUTTON (ESC) HAS BEEN ADDED
#Includes the following:
#loadingScreen.py
#creditsScreen.py
#controlsScreen.py
#chooseHouse.py
#chooseDifficulty

from pygame import*
import os

#Window preferences
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
controlsScreen = image.load ("controls.jpg")

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
controlsComplete = False 
difficultyChosen = False
chooseHouseScreenLoaded = False
houseScreenGrabRect = Rect(0,0,850,600)
goBack = False

difficulty = ""
diffScreenLoaded = False
diffScreenGrabRect = Rect(0,0,850,600)
#Rects for the difficulty buttons
difficultyEasyButtonRect = Rect(225,180,415,70) 
difficultyNormalButtonRect = Rect(225,300,415,70)
difficultyHardButtonRect = Rect(225,420,415,70)

playerHouse = ""

#In-game Menu
#*****HERE

#Battle Menu
profilePic = image.load ("profilePic.png")

#Music
songPlaylist = ["theme.mp3"]
init() #Initialize the mixer
mixer.music.load(songPlaylist[0])  
mixer.music.play()

#Fonts
font.init()
otherFont = font.SysFont("High Tower Text", 28)
subtitle = otherFont.render(("New Horizons"), True, (111,127,132))

font.init()
difficultyFont = font.SysFont("Castellar", 28)
difficultyTitle = difficultyFont.render(("Select Difficulty and Choose House"), True, (255,255,0))
difficultyTitle2 = difficultyFont.render(("(R. Click to choose house or ESC to re-choose)"), True, (255,255,0))

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

        if menu == "home":
            #This black rectangle hides the differences in size between the buttons
            #and the yellow highlight rects for the Play button
            draw.rect(screen,(0,0,0),[323,217,202,82])
            
            screen.blit(playButton,(325,220))
            screen.blit(controlsButton,(325,330))
            screen.blit(creditsButton,(325,410))

            screen.blit(subtitle,(460,145)) #"New Horizons" text
            
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
                if mb[0]==1:
                    menu = "play"
            elif controlsButtonRect.collidepoint((mx,my)):
                screen.blit(menuGrab,(0,0))
                draw.rect(screen,(0,255,0),[325,330,200,50],2)
                if mb[0]==1:
                    menu = "controls"
            elif creditsButtonRect.collidepoint((mx,my)):
                screen.blit(menuGrab,(0,0))
                draw.rect(screen,(0,255,0),[325,410,200,50],2)
                if mb[0]==1:
                    menu = "credits"
            else:
                screen.blit(menuGrab,(0,0))
                
        elif menu == "play":
            if difficultyChosen == False:
                #The following only needs to be blit once, eg. the buttons and stuff
                if diffScreenLoaded == False:
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
                    screen.blit(difficultyTitle,(120,60))
                    screen.blit(difficultyTitle2,(25,90))
                    diffScreenLoaded = True #flag controls this being blit only once
                    diffScreenGrab = screen.subsurface(diffScreenGrabRect).copy()

                if difficultyEasyButtonRect.collidepoint((mx,my)) and difficultyChosen==False:
                    screen.blit(diffScreenGrab,(0,0))
                    screen.blit(difficultyEasyHighlight,(285,180))
                    if mb[0] == 1:
                        difficultyChosen = True
                        difficulty = "easy"
                
                elif difficultyNormalButtonRect.collidepoint((mx,my)) and difficultyChosen==False:
                    screen.blit(diffScreenGrab,(0,0))
                    screen.blit(difficultyNormalHighlight,(275,300))
                    if mb[0] == 1:
                        difficultyChosen = True
                        difficulty = "normal"
                
                elif difficultyHardButtonRect.collidepoint((mx,my)) and difficultyChosen==False:
                    screen.blit(diffScreenGrab,(0,0))
                    screen.blit(difficultyHardHighlight,(225,420))
                    if mb[0] == 1:
                        difficultyChosen = True
                        difficulty = "hard"
                        
                else: #Highlight dissappears when mouse is not over any button
                    screen.blit(diffScreenGrab,(0,0))
                    
            if difficultyChosen:
                #The following only needs to be blit once, eg. the buttons and stuff
                if chooseHouseScreenLoaded == False:
                    screen.blit(blackScreen,(0,0)) #Hides gaps between the pictures
                    screen.blit(grifHouseSelect,(0,0))
                    screen.blit(slyHouseSelect,(430,0))
                    screen.blit(huffHouseSelect,(0,300))
                    screen.blit(ravenHouseSelect,(430,300))
                    screen.blit(hogwartsBadge,(275,150))
                    chooseHouseScreenLoaded = True
                    houseScreenGrab = screen.subsurface(houseScreenGrabRect).copy()

                #The house selected is highlighted in yellow
                #The previous highlights are hidden with a clean image, screenGrab  
                if grifHouseSelectRect.collidepoint((mx,my)) and playerHouse=="":
                    screen.blit(houseScreenGrab,(0,0))
                    draw.rect(screen,(255,255,0),[0,0,420,300],2)
                    #The lines are drawn over the crest so the crest must be drawn again overtop
                    screen.blit(hogwartsBadge,(275,150))
                    #Had to change mb[0] and replaced with mb[2] due to both the difficulty selection
                    #and the house selection used left click which caused bugs, assigning a house
                    #simultanously when a diffculty was chosen.
                    if mb[2]==1:
                        playerHouse = "grif"
                
                elif slyHouseSelectRect.collidepoint((mx,my)) and playerHouse=="":
                    screen.blit(houseScreenGrab,(0,0))
                    draw.rect(screen,(255,255,0),[430,0,420,300],2)
                    screen.blit(hogwartsBadge,(275,150))
                    if mb[2]==1:
                        playerHouse = "sly"
                
                elif huffHouseSelectRect.collidepoint((mx,my)) and playerHouse=="":
                    screen.blit(houseScreenGrab,(0,0))
                    draw.rect(screen,(255,255,0),[0,300,420,300],2)
                    screen.blit(hogwartsBadge,(275,150))
                    if mb[2]==1:
                        playerHouse = "huff"
                
                elif ravenHouseSelectRect.collidepoint((mx,my)) and playerHouse=="":
                    screen.blit(houseScreenGrab,(0,0))
                    draw.rect(screen,(255,255,0),[430,300,420,300],2)
                    screen.blit(hogwartsBadge,(275,150))
                    if mb[2]==1:
                        playerHouse = "raven"

                if goBack:
                    #Resets previouly selected items and the flags are reversed 
                    playerHouse = ""
                    textComplete = False
                    chooseHouseScreenLoaded = False
                    goBack = False

                if textComplete == False and playerHouse !="": 
                    #Text drops down when a house is chosen
                    for i in range (-500,0,5):
                        screen.blit(textScreen,(0,i+10)) 
                        time.wait(2)
                        display.flip()
                    textComplete = True
                    time.wait(1000)

        elif menu == "controls":
            if controlsComplete == False:
                for i in range (-600,0,10):
                    screen.blit(controlsScreen,(0,i+20)) 
                    time.wait(2)
                    display.flip()
                controlsComplete = True

            if goBack:
                controlsComplete = False
                loadingComplete = False
                menu = "home"
                goBack = False

        elif menu == "credits":
            if creditsComplete == False:
                for i in range (-600,0,10):
                    screen.blit(creditsScreen,(0,i+10)) 
                    time.wait(3)
                    display.flip()
                creditsComplete = True

            if goBack:
                creditsComplete = False
                loadingComplete = False
                menu = "home"
                goBack = False

    display.flip()
font.quit()
del otherFont
del difficultyFont
quit()
