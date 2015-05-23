#Choose house after the difficulty is chosen 
#Jesse Wang 

#if menu = "play"
from pygame import*
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '25,50' #Opens up in the upper left corner 
screen = display.set_mode((850,600)) #Game window resolution
display.set_caption("Harry Potter: New Horizons")
mouse.set_cursor(*cursors.tri_left)

#This code is ALREADY loaded in the main py
# ***********************************************
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
ravenHouseSelectRect = Rect(430,300,420,300)
blackScreen = image.load ("template.jpg")
textScreen = image.load ("text.jpg")
textComplete = False
#playerHouse == ""
#****************************************************

screen.blit(blackScreen,(0,0)) #Hides gaps between the pictures
#This should be inside the loop with if statement condition in the actual code
#eg. if textComplete==True:
screen.blit(grifHouseSelect,(0,0))
screen.blit(slyHouseSelect,(430,0))
screen.blit(huffHouseSelect,(0,300))
screen.blit(ravenHouseSelect,(430,300))
screen.blit(hogwartsBadge,(275,150))

running = True
while running:

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    for e in event.get():       
        if e.type == QUIT:     
            running = False

        if textComplete == False:
            #Text drops down
            for i in range (-500,0,5):
                screen.blit(textScreen,(0,i+10)) 
                time.wait(2)
                display.flip()
            textComplete = True
            time.wait(1000)
        
        #NOTE TO SELF: FIX THE HIGHLIGHTS USING SUBSURFACE and add in mb[0]==1
            
        #The house selected is highlighted in yellow
        if grifHouseSelectRect.collidepoint((mx,my)):
            draw.rect(screen,(255,255,0),[0,0,420,300],2)
            #The lines are drawn over the crest so the crest must be drawn again overtop
            screen.blit(hogwartsBadge,(275,150))
            #if mb[0]==1:
                #playerHouse == grif
        elif slyHouseSelectRect.collidepoint((mx,my)):
            draw.rect(screen,(255,255,0),[430,0,420,300],2)
            screen.blit(hogwartsBadge,(275,150))
        elif huffHouseSelectRect.collidepoint((mx,my)):
            draw.rect(screen,(255,255,0),[0,300,420,300],2)
            screen.blit(hogwartsBadge,(275,150))
        elif ravenHouseSelectRect.collidepoint((mx,my)):
            draw.rect(screen,(255,255,0),[430,300,420,300],2)
            screen.blit(hogwartsBadge,(275,150))
        
    display.flip()
quit()
