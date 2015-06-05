from pygame import*
import os

#Battle Menu 1
#This code displays the menu that appears when harry enters a battle
#eg. options to fight, flee and which spells he can cast 

#Window preferences
os.environ['SDL_VIDEO_WINDOW_POS'] = '25,50' #Opens up in the upper left corner 
screen = display.set_mode((850,600)) #Game window resolution
display.set_caption("Harry Potter: New Horizons")
mouse.set_cursor(*cursors.tri_left)

profilePic = image.load ("profilePic.png")
profilePic = transform.scale(profilePic,(65,65))
screen.fill((255,255,255))    
#battleMenuRect = Rect ()
#
#
#

running = True
while running:

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    for e in event.get():       
        if e.type == QUIT:     
            running = False
    print (mx,my)
    draw.rect(screen,(222,184,135),[0,450,850,600])
    draw.line(screen,(0,0,0),[0,449],[850,449],3)
    screen.blit(profilePic,(750,475))

    draw.rect(screen,(0,0,0),[650,500,100,25]) #Health bar outline
    #draw.rect(screen,(0,0,0),[650,500,100,25])
    draw.rect(screen,(0,0,0),[650,500,100,25]) #Spell bar outline
    #draw.rect(screen,(0,0,0),[650,500,100,25])

    display.flip()
quit()
