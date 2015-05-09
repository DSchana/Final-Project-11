from pygame import *

screen = display.set_mode((1024,768))
back = image.load("city.jpg")
cover = Surface((200,200),SRCALPHA)
draw.circle(cover,(255,0,0,111),(100,100),100)
running = True

while running:
    for evnt in event.get():               
        if evnt.type == QUIT:
            running = False

    mx,my = mouse.get_pos()
    screen.blit(back,(0,0))
    screen.blit(cover,(mx-100,my-100))
    display.flip()
                  
    
quit()
