#In game menu
#When E is pressed a menu is displayed showing the current spell and allows
#the user select a different

from pygame import*

screen = display.set_mode((850,600)) #Game window resolution
display.set_caption("Harry Potter: New Horizons")
mouse.set_cursor(*cursors.tri_left)

#NEW STUFF TO ADD INTO THE LOADING SCREEN**********
openMenu = False
spellMenuBack = image.load ("spellMenuBack.png")
spellMenuBack = transform.scale(spellMenuBack,(700,600))
spellMenuRect = Rect (75,5,700,600)
spellARect = Rect (135,140,80,80)
spellBRect = Rect (135,260,80,80)
spellARect = Rect (135,380,80,80)
spellAPic = image.load ("spellAPic.jpg")
spellAPic = transform.scale(spellAPic,(76,76))
spellBPic = image.load ("spellBPic.jpg")
spellBPic = transform.scale(spellBPic,(76,76))
spellCPic = image.load ("spellCPic.jpg")
spellCPic = transform.scale(spellCPic,(76,76))
closeMenuRect = Rect (635,25,45,55)
font.init()
menuFont = font.SysFont("Verdana", 50) #Font for both menu descriptions and "X" exit button
#This font is only used once at size 50, later resized smaller to text in descriptions
closeMenuText = menuFont.render(("X"), True, (255,0,0))
menuFont = font.SysFont("Verdana", 38)
menuSelectionText = menuFont.render(("INVENTORY"), True, (255,0,0))
menuFont = font.SysFont("Verdana", 22) 
spellAText = menuFont.render(("This is Spell A"), True, (0,0,0))
spellBText = menuFont.render(("This is Spell B"), True, (0,0,0))
spellCText = menuFont.render(("This is Spell C"), True, (0,0,0))
currentSpell = "" #whatever the default is 
#**************************************************

running = True
while running:

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    for e in event.get():       
        if e.type == QUIT:     
            running = False

        if e.type == KEYDOWN and e.key == 101 and openMenu == False:
            openMenu = True #Flag that controls opening the in-game menu

        if openMenu:
            #When E is pressed, the spell menu is opened
            screen.blit(spellMenuBack,(75,5))
            draw.rect(screen,(0,0,0),[135,140,80,80],2) #A
            screen.blit(spellAPic,(137,142))
            draw.rect(screen,(0,0,0),[135,260,80,80],2) #B
            screen.blit(spellBPic,(137,262))
            draw.rect(screen,(0,0,0),[135,380,80,80],2) #C
            screen.blit(spellCPic,(137,382))

            #if collide with spell box, hightight it
            #if mb[0] == 1:
                #currentSpell == "spellA"
            #draw.rect(screen,(0,255,0),[135,140,80,80],2) #A highlight
            #draw.rect(screen,(0,255,0),[135,260,80,80],2) #B highlight
            #draw.rect(screen,(0,255,0),[135,380,80,80],2) #C highlight
            
            screen.blit(spellAText,(230,160))
            screen.blit(spellBText,(230,285))
            screen.blit(spellCText,(230,400))
            screen.blit(menuSelectionText,(168,28)) 
            screen.blit(closeMenuText,(640,20)) # "X" box closes menu
            draw.rect(screen,(255,0,0),[635,25,45,55],3) #red box around X
            
        if mb[0]==1 and closeMenuRect.collidepoint((mx,my)) and openMenu:
            openMenu = False
            #Placeholder, use a subsurface to resume game when menu is closed
            screen.fill ((0,0,0)) #REPLACE LATER
            
    display.flip()
#Remember to add this in the actual file to del fonts
font.quit()
del menuFont
quit()
