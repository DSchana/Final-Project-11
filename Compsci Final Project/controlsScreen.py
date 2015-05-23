#controls Screen
#displays this screen after the controls button is clicked from the menu 

from pygame import*

screen = display.set_mode((850,600)) #Game window resolution
display.set_caption("Harry Potter: New Horizons")
mouse.set_cursor(*cursors.tri_left)

controlsScreen = image.load ("controls.jpg")

controlsComplete = False #a flag that controls the scrolling of the page

running = True
while running:

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    for e in event.get():       
        if e.type == QUIT:     
            running = False
        #if menu = "credits"
        if controlsComplete == False:
            for i in range (-600,0,10):
                screen.blit(controlsScreen,(0,i+20)) 
                time.wait(2)
                display.flip()
            controlsComplete = True
        #Add option to go back when the esc key is pressed        
    display.flip()
quit()
