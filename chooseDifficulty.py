#Select Difficulty
#this is the screen after the play button is clicked and the grame proceeeds to
#ask the user to choose a difficulty. 

from pygame import*

#USE THE ESC KEY AS THE BACK BUTTON TO RETURN TO THE MAIN MENU
#THAT CODE IS FOUND IN CHOOSE HOUSE AND LOADING 

screen = display.set_mode((850,600)) #Game window resolution
display.set_caption("Harry Potter: New Horizons")
mouse.set_cursor(*cursors.tri_left)

#The following are already loaded in the start screen
difficultyScreen = image.load ("difficulty.jpg")
difficultyEasyIdle = image.load ("EasyIdle.png")
difficultyEasyHighlight = image.load ("EasyHigh.png")
difficultyNormalIdle = image.load ("NormalIdle.png")
difficultyNormalHighlight = image.load ("NormalHigh.png")
difficultyHardIdle = image.load ("HardIdle.png")
difficultyHardHighlight = image.load ("HardHigh.png")

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
difficultyTitle = difficultyFont.render(("Select Difficulty"), True, (0,0,0))
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

        if difficultyEasyButtonRect.collidepoint((mx,my)) and difficultyChosen==False:
            screen.blit(screenGrab,(0,0))
            screen.blit(difficultyEasyHighlight,(285,180))
            if mb[0] == 1:
                difficultyChosen = True
                difficulty = "easy"
            
        elif difficultyNormalButtonRect.collidepoint((mx,my)) and difficultyChosen==False:
            screen.blit(screenGrab,(0,0))
            screen.blit(difficultyNormalHighlight,(275,300))
            if mb[0] == 1:
                difficultyChosen = True
                difficulty = "normal"
            
        elif difficultyHardButtonRect.collidepoint((mx,my)) and difficultyChosen==False:
            screen.blit(screenGrab,(0,0))
            screen.blit(difficultyHardHighlight,(225,420))
            if mb[0] == 1:
                difficultyChosen = True
                difficulty = "hard"

        else:
            screen.blit(screenGrab,(0,0))

    display.flip()
font.quit()
del difficultyFont
quit()
