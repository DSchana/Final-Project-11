#credits screen
#display this screen after the credits options is clicked

from pygame import*

#USE THE ESC KEY AS THE BACK BUTTON TO RETURN TO THE MAIN MENU
#THAT CODE IS FOUND IN CHOOSE HOUSE AND LOADING 

screen = display.set_mode((850,600)) #Game window resolution
display.set_caption("Harry Potter: New Horizons")
mouse.set_cursor(*cursors.tri_left)

creditsScreen = image.load ("credits.jpg")

creditsComplete = False

running = True
while running:

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    for e in event.get():       
        if e.type == QUIT:     
            running = False
        #if menu = "credits"
        if creditsComplete == False:
            for i in range (-600,0,10):
                screen.blit(creditsScreen,(0,i+10)) 
                time.wait(3)
                display.flip()
            creditsComplete = True
   
    display.flip()
quit()
