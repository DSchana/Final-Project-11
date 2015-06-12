#In game menu
#When E is pressed a menu is displayed showing the current spell and allows
#the user select a different

#UPDATE: CODE HAS BEEN UPDATED WITH THE SAVE AND LOAD FEATURE
#SECTIONS ARE HIGHLIGHTED IN RED  WITH *******************

from pygame import*

screen = display.set_mode((850,600)) #Game window resolution
display.set_caption("Harry Potter: New Horizons")
mouse.set_cursor(*cursors.tri_left)

#NEW STUFF TO ADD INTO THE LOADING SCREEN*
openMenu = False
spellMenuBack = image.load ("spellMenuBack.png")
spellMenuBack = transform.scale(spellMenuBack,(700,600))
spellMenuRect = Rect (75,5,700,600)
spellARect = Rect (135,140,80,80)
spellBRect = Rect (135,260,80,80)
spellCRect = Rect (135,380,80,80)
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
spellAText = menuFont.render(("Alahamoro:"), True, (0,0,0))
spellADescripText = menuFont.render(("Unlocks doors, grants access to new areas"), True, (0,0,0))
spellBText = menuFont.render(("Lumos:"), True, (0,0,0))
spellBDescripText = menuFont.render(("Illuinates dark areas on the map"), True, (0,0,0))
spellCText = menuFont.render(("Wingardium Leviosa:"), True, (0,0,0))
spellCDescripText = menuFont.render(("Lifts obstacles out of the way"), True, (0,0,0))
currentSpell = "" #Keeps track of the selected in-game spell (non-battle spells)
availibleSpells = ["Alahamoro"] #This list keeps track of the spells availible for the player to use 

#NEW CODE FOR SAVE AND LOAD FEATURE **********************************
menuFont = font.SysFont("Verdana", 38)
saveBoxText = menuFont.render(("SAVE"), True, (255,0,0))
loadBoxText = menuFont.render(("LOAD"), True, (255,0,0))
saveButtonRect = Rect (175,520,120,50)
loadButtonRect = Rect (555,520,120,50)
#**************************************************************************

screenGrabRect = Rect(0,0,850,600)

running = True
while running:

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    for e in event.get():       
        if e.type == QUIT:     
            running = False

        if e.type == KEYDOWN and e.key == 101 and openMenu == False:
            openMenu = True #Flag that controls opening the in-game menu
        print (mx,my)
        if openMenu:
            #When E is pressed, the spell menu is opened
            screen.blit(spellMenuBack,(75,5))
            
#NEW CODE FOR SAVE AND LOAD FEATURE **********************************
            screen.blit(saveBoxText,(185,518))
            screen.blit(loadBoxText,(562,518))
            #draw.rect(screen,(255,0,0),[175,520,120,50],2) #save box
            #draw.rect(screen,(255,0,0),[555,520,120,50],2) #load box
            
            if saveButtonRect.collidepoint((mx,my)) : #when the save button is clicked
                screen.blit(screenGrab,(0,0))
                draw.rect(screen,(255,0,0),[175,520,120,50],2) #highlight
                #if mb[0]==1:
                    #The player values variables are updated, i think u have the code that controls player level, experience, etc. 
                
            if loadButtonRect.collidepoint((mx,my)): #when the load button is clicked
                screen.blit(screenGrab,(0,0))
                draw.rect(screen,(255,0,0),[555,520,120,50],2)
                #if mb[0]==1:
                    #the saved changes are blit on-screen, eg. spells that have been unlocked and appear after previous save 
                
#**************************************************************************
            
            #The inventory only displays spells that the player has unlocked 
            if "Alahamoro" in availibleSpells:
                draw.rect(screen,(0,0,0),[135,140,80,80],2) #A
                screen.blit(spellAPic,(137,142))
                screen.blit(spellAText,(230,160))
                screen.blit(spellADescripText,(230,180))

            if  "Lumos" in availibleSpells:
                draw.rect(screen,(0,0,0),[135,260,80,80],2) #B
                screen.blit(spellBPic,(137,262))
                screen.blit(spellBText,(230,285))
                screen.blit(spellBDescripText,(230,305))
                
            if "Wingardium Leviosa" in availibleSpells:
                draw.rect(screen,(0,0,0),[135,380,80,80],2) #C
                screen.blit(spellCPic,(137,382))
                screen.blit(spellCText,(230,400))
                screen.blit(spellCDescripText,(230,420))
            
            screenGrab = screen.subsurface(screenGrabRect).copy()
            
            if spellARect.collidepoint((mx,my)) and "Alahamoro" in availibleSpells:
                screen.blit(screenGrab,(0,0))
                draw.rect(screen,(255,255,0),[135,140,80,80],2) #A highlight
                if mb[0] == 1:
                    currentSpell = "Alahamoro"
                    #When the spell is clicked, the window closes
                    screen.fill ((0,0,0)) #simulates the window closing, replace later 

            elif spellBRect.collidepoint((mx,my)) and "Lumos" in availibleSpells:
                screen.blit(screenGrab,(0,0))
                draw.rect(screen,(255,255,0),[135,260,80,80],2) #B highlight
                if mb[0] == 1:
                    currentSpell = "Lumos"
                    screen.fill ((0,0,0))

            elif spellCRect.collidepoint((mx,my)) and "Wingardium Leviosa" in availibleSpells:
                screen.blit(screenGrab,(0,0))
                draw.rect(screen,(255,255,0),[135,380,80,80],2) #C highlight
                if mb[0] == 1:
                    currentSpell = "Wingardium Leviosa"
                    screen.fill ((0,0,0)) 

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
