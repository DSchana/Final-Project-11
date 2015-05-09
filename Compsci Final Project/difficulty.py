#Select Difficulty 

from pygame import*

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

screen.blit(difficultyScreen,(0,0))
display.flip()

screen.blit(difficultyEasyIdle,(225,180))
screen.blit(difficultyNormalIdle,(225,300))
screen.blit(difficultyHardIdle,(225,420))

#difficultyEasyButtonRect =
#difficultyEasyButtonRect =
#difficultyEasyButtonRect =

running = True
while running:

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    for e in event.get():       
        if e.type == QUIT:     
            running = False

    display.flip()
quit()
