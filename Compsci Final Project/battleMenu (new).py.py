from pygame import*
import os

#NOTE: THIS IS BASICALLY DONE, I HAVE LEFT NOTES FOR WHERE YOUR CODE SHOULD GO. THANKS.
#I ALSO HAVE ADDED THE SPRITES FOR DIFFERENT ENEMIES, EG. SPIDER, KNIGHT, GOBLIN
#I FOUND THE BLUE BLOB, IT DOESNT HAVE TO ANIMATE
#THE EXPLOSION SPRITES ARE THERE TOO, EG. WHEN PLAYER ATTACKS, EXPLOSION OVER ENEMY SPRITE

#Battle Menu 1
#This code displays the menu that appears when harry enters a battle
#eg. options to fight, flee and which spells he can cast 

#Window preferences
os.environ['SDL_VIDEO_WINDOW_POS'] = '25,50' #Opens up in the upper left corner 
screen = display.set_mode((850,600)) #Game window resolution
display.set_caption("Harry Potter: New Horizons")

#DONT FORGET TO ADD THE FOLLOWING INTO THE LOADING PART************
from random import *
battleMenu1 = image.load ("battleMenuPic.png")
battleMenu2 = image.load ("battleMenuPic2.png")
healthLogo = image.load ("hpBox.png")
healthLogo = transform.scale(healthLogo,(25,25))
energyLogo = image.load ("spellBox.png")
energyLogo = transform.scale(energyLogo,(20,30))
profilePic = image.load ("profilePic.png")
profilePic = transform.scale(profilePic,(70,70))
screen.fill((255,255,255))    
battleMenuGrabRect = Rect (0,450,850,150) #The entire bottom of the screen where the menu is displayed
battleMenuFightChoiceRect = Rect (50,500,165,50)
battleMenuFleeChoiceRect = Rect (330,500,145,50)
battleMenuLoaded = False #loads assets only once to avoid slowing down game
enterBattle = ""
#The followign rects are for the "fight" section of the battle menu 
battleSpellExpulRect = Rect (45,462,130,23)
battleSpellImperRect = Rect (45,495,130,25)
battleSpellCrucioRect = Rect (45,530,108,23)
battleSpellStupRect = Rect (45,560,125,25)
#controls the lengths of the health/energy bars, also ends game when health = 0 
playerHealth = 100 
playerEnergy = 100
enemyHealth = 100 #though it depends on the enemy 
gameOverScreen = image.load ("gameOver.jpg")
gameOver = False
#These images are the dialogue boxes that appear before/after a battle
dialogueBoxBattle1 = image.load ("dialogueBoxBattle1.png")
dialogueBoxBattle2 = image.load ("dialogueBoxBattle2.png")
dialogueBoxBattle3 = image.load ("dialogueBoxBattle3.png")
dialogueBoxWin1 = image.load ("dialogueBoxWin1.png")
dialogueBoxWin2 = image.load ("dialogueBoxWin2.png")
dialogueList1 = [dialogueBoxBattle1,dialogueBoxBattle2,dialogueBoxBattle3] #stores dialoge for before battle
dialogueList2 = [dialogueBoxWin1,dialogueBoxWin2] #stores dialoge for after battle
turn = True #keeps track of player or enemy's turn to attack
enterBattleScreenGrabRect = Rect (0,0,850,600)
mode = "" #or whatever variable is keeping track of the battle scene
#******************************************************************

harryWalksintoTheBlueBlob = True #This is just a place holder for the actual code when harry walks into the blue blob

running = True
while running:

	mb = mouse.get_pressed()
	mx,my = mouse.get_pos()

	for e in event.get():       
		if e.type == QUIT:     
			running = False
			
	print (mx,my)

	#ADD THIS CODE: when harry walks into the blue blob 
	if harryWalksintoTheBlueBlob: #placeholder
		battleMenuLoaded == False
		#mode = "battle" #or whatever flag is keeping track of the battle scene
		
		#Takes a copy of the screen before battle, blits it back after battle
		enterBattleScreenGrab = screen.subsurface(enterBattleScreenGrabRect).copy() 
		box1 = randint (0,2) #randomly selects a pre-battle message
		#A dialogue box appears, time.wait to giver user time to read
		screen.blit(dialogueList1[box1],(0,450))
		display.flip()
		time.wait (1200)
		harryWalksintoTheBlueBlob = False #reverse the flag afterwards 
	
	#Once player enters battle, the battle menu appears as long as the player health is not 0
	if gameOver==False and (battleMenuLoaded == False or enterBattle == "True"):
		#This if statement ensures the assets are only loaded once to avoid
		#slowing down the game 
		screen.blit(battleMenu1,(0,450)) #the beige background 
		screen.blit(profilePic,(755,500)) #harry's face in the corner 
		screen.blit(healthLogo,(685,465)) #health cross pic
		screen.blit(energyLogo,(685,528)) #energy lightning bolt pic
		#just the length of the black bars changes, looks like colored bars are decreasing 
		draw.rect(screen,(0,0,0),[558,498,155,20]) #Health bar outline
		draw.rect(screen,(0,0,0),[558,562,155,20]) #energy bar outline
		#"playerHealth*1.51" scales the numerical value of health to the length of coloured bars 
		draw.rect(screen,(255,0,0),[560,500,playerHealth*1.51,16]) #actual health coloured in
		draw.rect(screen,(0,255,0),[560,564,playerEnergy*1.51,16]) #actual energy coloured in
		#move this later to fit in colored bars 
		battleMenuGrab = screen.subsurface(battleMenuGrabRect).copy()
		
		battleMenuLoaded = True
	
	if battleMenuFightChoiceRect.collidepoint((mx,my)) and gameOver==False: #when mouse is over "fight"
		screen.blit(battleMenuGrab,(0,450))#clears previous highlighted option 
		draw.circle(screen,(0,0,0),[35,525],12)
		if mb[0] == 1: #When "Fight" is clicked, proceed to battle
			#can't be boolean since false would be automatically triggered, set to empty string as default
			enterBattle = "True" 
		
	elif battleMenuFleeChoiceRect.collidepoint((mx,my)) and gameOver==False:#mouse over "flee"
		screen.blit(battleMenuGrab,(0,450))
		draw.circle(screen,(0,0,0),[325,525],12)
		if mb[0] == 1: #When "Flee" is clicked, exit and go back to game
			enterBattle = "False"

	else: #when is mouse is hovering over neither
		if gameOver==False: #fixes bug when it is blit even after game is over
			screen.blit(battleMenuGrab,(0,450))

	#FIX ERROR WHEN THE MOUSE IS HELD DOWN, THE SPELLS ARE CAST MULTIPLE TIMES 
	if enterBattle == "True" and gameOver==False:
		screen.blit(battleMenu2,(0,450))
		battleMenuGrab = screen.subsurface(battleMenuGrabRect).copy()
		#Player chooses a spell, update enemy health, player status bars
		#battle is over if enemy dies or player dies
		
		if battleSpellExpulRect.collidepoint((mx,my)) and turn:
			screen.blit(battleMenuGrab,(0,450))
			draw.circle(screen,(0,0,0),[38,473],6)
			if mb[0] == 1: #player clicks spell to attack on their turn 
				playerEnergy -= 0 #no energy drain for this move
				enemyHealth -= 8
				#ADD: explosion sprite animation over enemy*********
				draw.rect(screen,(0,255,0),[560,564,playerEnergy*1.51,16]) 
				turn = False
				
		elif battleSpellImperRect.collidepoint((mx,my)) and playerEnergy>=10 and turn:
			screen.blit(battleMenuGrab,(0,450))
			draw.circle(screen,(0,0,0),[38,507],6)
			if mb[0] == 1:
				playerEnergy -= 10
				enemyHealth -= 12
				#ADD: explosion sprite animation over enemy*********
				draw.rect(screen,(0,255,0),[560,564,playerEnergy*1.51,16]) 
				turn = False
				
		elif battleSpellCrucioRect.collidepoint((mx,my)) and playerEnergy>=15 and turn:
			screen.blit(battleMenuGrab,(0,450))
			draw.circle(screen,(0,0,0),[38,540],6)
			if mb[0] == 1:
				playerEnergy -= 15
				enemyHealth -= 16
				#ADD: explosion sprite animation over enemy*********
				draw.rect(screen,(0,255,0),[560,564,playerEnergy*1.51,16]) 
				turn = False
			
		elif battleSpellStupRect.collidepoint((mx,my)) and playerEnergy>=8 and turn:
			screen.blit(battleMenuGrab,(0,450))
			draw.circle(screen,(0,0,0),[38,572],6)
			if mb[0] == 1:
				playerEnergy -= 10
				#enemy damage is decreased when this move is used
				damage = randint(4,10) #OR HOWEVER the damage system works, you can change this
				draw.rect(screen,(0,255,0),[560,564,playerEnergy*1.51,16])
				turn = False
				
		#ADD THIS CODE: WHEN THE ENEMY ATTACKS YOU, ENEMY ATTACK ANIMATION 
		elif turn == False: #the enemy's turn
			#enemy attack animation *HERE
			#enemy attacks, deals damage so player health decreases
			damage = randint(6,12) #or however damage is calculated 
			playerHealth -= damage
			draw.rect(screen,(255,0,0),[560,500,playerHealth*1.51,16]) #updates the player's health bar
			turn = True #back to player's turn
			
	elif enterBattle== "Flee":
		screen.blit(enterBattleScreenGrab,(0,0))
		enterBattle = "" #flag resets
		#mode = "not battle" #or whatever flag is keeping track of the battle scene

	if playerHealth <= 0 and enterBattle=="True": #if player is killed in battle
		gameOver = True #Game over, game ends.
		screen.blit(gameOverScreen,(0,0))
		enterBattle = ""
		
	if enemyHealth <= 0 and enterBattle=="True": #player won battle by killing enemy
		#gains some experience and unlock an inventory spell or whatever, eg. append a new spell to the inventory spell list
		#mode = "not battle" #or whatever flag is keeping track of the battle scene
		screen.blit(enterBattleScreenGrab,(0,0))
		enterBattle = ""
		playerHealth = 100 #resets
		playerEnergy = 100 #resets 
		#The following displays a dialogue box when the battle is won, eg. "Victory!"
		box2 = randint (0,1) #randomly selects a win message
		screen.blit(dialogueList2[box2],(0,450))
		display.flip()
		time.wait (1200)
		screen.blit(enterBattleScreenGrab,(0,0))
		
	display.flip()
quit()
