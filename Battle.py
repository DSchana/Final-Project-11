# Battle.py

from pygame import *
from random import *
from math import *

class Battle:
	def __init__(self, Player, Enemy, location):
		self.player = Player
		self.enemy = Enemy
		self.turn = "player"
		self.location = location
		self.battleScene = image.load("Images/Backgrounds/Battles/" + location + ".png")

		# Battle screen images
		self.battleMenu1 = image.load ("Images/battle/battleMenuPic.png")
		self.battleMenu2 = image.load ("Images/battle/battleMenuPic2.png")
		self.healthLogo = image.load ("Images/battle/hpBox.png")
		self.healthLogo = transform.scale(healthLogo,(25,25))
		self.energyLogo = image.load ("Images/battle/spellBox.png")
		self.energyLogo = transform.scale(energyLogo,(20,30))
		self.profilePic = image.load ("Images/battle/profilePic.png")
		self.profilePic = transform.scale(profilePic,(70,70))
		self.battleMenuGrabRect = Rect (0,450,850,150) #The entire bottom of the screen where the menu is displayed
		self.battleMenuFightChoiceRect = Rect (50,500,165,50)
		self.battleMenuFleeChoiceRect = Rect (330,500,145,50)
		self.battleMenuLoaded = False #loads assets only once to avoid slowing down game
		self.enterBattle = ""
		#The followign rects are for the "fight" section of the battle menu 
		self.battleSpellExpulRect = Rect (45,462,130,23)
		self.battleSpellImperRect = Rect (45,495,130,25)
		self.battleSpellCrucioRect = Rect (45,530,108,23)
		self.battleSpellStupRect = Rect (45,560,125,25)
		#controls the lengths of the health/energy bars, also ends game when health = 0 
		self.playerHealth = 100 
		self.playerEnergy = 100
		self.enemyHealth = 100 #though it depends on the enemy 
		self.gameOverScreen = image.load ("Images/battle/gameOver.jpg")
		self.gameOver = False
		#These images are the dialogue boxes that appear before/after a battle
		self.dialogueBoxBattle1 = image.load ("Images/battle/dialogueBoxBattle1.png")
		self.dialogueBoxBattle2 = image.load ("Images/battle/dialogueBoxBattle2.png")
		self.dialogueBoxBattle3 = image.load ("Images/battle/dialogueBoxBattle3.png")
		self.dialogueBoxWin1 = image.load ("Images/battle/dialogueBoxWin1.png")
		self.dialogueBoxWin2 = image.load ("Images/battle/dialogueBoxWin2.png")
		self.dialogueList1 = [dialogueBoxBattle1,dialogueBoxBattle2,dialogueBoxBattle3] #stores dialoge for before battle
		self.dialogueList2 = [dialogueBoxWin1,dialogueBoxWin2] #stores dialoge for after battle
		self.enterBattleScreenGrabRect = Rect (0,0,850,600)
		self.mode = "" #or whatever variable is keeping track of the battle scene

	def drawBattle(self, screen):
		"Draw battle scene"
		screen.blit(self.battleScene)
		# draw player and enemy sprites
		running = True
		while running:
			for e in event.get():
				# Check if user selects fight or flight
				if battleMenuFightChoiceRect.collidepoint((mx,my)) and gameOver==False: #when mouse is over "fight"
					screen.blit(battleMenuGrab,(0,450))#clears previous highlighted option 
					draw.circle(screen,(0,0,0),[35,525],12)
					if MOUSEBUTTONDOWN: #When "Fight" is clicked, proceed to battle
						#can't be boolean since false would be automatically triggered, set to empty string as default
						enterBattle = "True"

				elif battleMenuFleeChoiceRect.collidepoint((mx,my)) and gameOver==False:#mouse over "flee"
					screen.blit(battleMenuGrab,(0,450))
					draw.circle(screen,(0,0,0),[325,525],12)
					if mb[0] == 1: #When "Flee" is clicked, exit and go back to game
						enterBattle = "False"
						running = False

				else: #when is mouse is hovering over neither
					if gameOver==False: #fixes bug when it is blit even after game is over
						screen.blit(battleMenuGrab,(0,450))

				# battle functionality
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