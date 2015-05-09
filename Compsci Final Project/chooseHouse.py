#Choose difficulty screen, house and enter player name 

#if menu = "play"

from pygame import*
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '25,50' #Opens up in the upper left corner 
screen = display.set_mode((850,600)) #Game window resolution
display.set_caption("Harry Potter: New Horizons")
mouse.set_cursor(*cursors.tri_left)

#The images are already loaded in the main py
grifHouseSelect = image.load ("grifHouse.png")
slyHouseSelect = image.load ("slyHouse.png")
ravenHouseSelect = image.load ("ravenHouse.png")
huffHouseSelect = image.load ("huffHouse.png")

#These need to be copied over to main py
grifHouseSelect = transform.scale(grifHouseSelect,(260,260))
slyHouseSelect = transform.scale(slyHouseSelect,(250,250))
ravenHouseSelect = transform.scale(ravenHouseSelect,(235,235))
huffHouseSelect = transform.scale(huffHouseSelect,(260,260))
#grifHouseSelectRect = Rect()
#slyHouseSelectRect = Rect()
#ravenHouseSelectRect = Rect()
#huffHouseSelectRect = Rect()

blackScreen = image.load ("template.jpg")

running = True
while running:

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    for e in event.get():       
        if e.type == QUIT:     
            running = False
        screen.blit(blackScreen,(0,0)) #Hides gaps between the pictures
        screen.blit(grifHouseSelect,(100,30))
        screen.blit(slyHouseSelect,(455,30))
        screen.blit(ravenHouseSelect,(120,320))
        screen.blit(huffHouseSelect,(460,305))
        
        
    display.flip()
quit()
