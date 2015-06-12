# Battle.py

from pygame import *
from random import *
from math import *

class Battle:
	def __init__(self, Player, Enemy, location):
		self.player = Player
		self.enemy = Enemy
		self.location = location
		self.battleScene = image.load("Images/Backgrounds/Battles/" + location + ".png")
		self.battleScene = transform.scale(self.battleScene, (850, 450))

		# Battle screen images
		self.battleMenu1 = image.load ("Images/battle/battleMenuPic.png")
		self.battleMenu2 = image.load ("Images/battle/battleMenuPic2.png")
		self.healthLogo = image.load ("Images/battle/hpBox.png")
		self.healthLogo = transform.scale(self.healthLogo,(25,25))
		self.energyLogo = image.load ("Images/battle/spellBox.png")
		self.energyLogo = transform.scale(self.energyLogo,(20,30))
		self.profilePic = image.load ("Images/battle/profilePic.png")
		self.profilePic = transform.scale(self.profilePic,(70,70))
		self.battleMenuGrabRect = Rect (0,450,850,150) #The entire bottom of the screen where the menu is displayed
		self.battleMenuFightChoiceRect = Rect (50,500,165,50)
		self.battleMenuFleeChoiceRect = Rect (330,500,145,50)
		self.battleMenuLoaded = False #loads assets only once to avoid slowing down game
		self.enterBattle = ""
		#The followign rects are for the "fight" section of the battle menu 
		self.spell_list = self.player.getAttackSpells()
		self.spell_rects = []
		for i in range(len(self.spell_list)):
			self.spell_rects.append(Rect(45, 460 + 30 * i, 130, 25))
		#controls the lengths of the health/energy bars, also ends game when health = 0 
		self.playerHealth = 100 
		self.playerEnergy = 100
		self.enemyHealth = 100 #though it depends on the enemy 
		self.gameOverScreen = image.load ("Images/battle/gameOver.jpg")
		self.gameOver = False
		self.turn = True
		#These images are the dialogue boxes that appear before/after a battle
		self.dialogueBoxBattle1 = image.load ("Images/battle/dialogueBoxBattle1.png")
		self.dialogueBoxBattle2 = image.load ("Images/battle/dialogueBoxBattle2.png")
		self.dialogueBoxBattle3 = image.load ("Images/battle/dialogueBoxBattle3.png")
		self.dialogueBoxWin1 = image.load ("Images/battle/dialogueBoxWin1.png")
		self.dialogueBoxWin2 = image.load ("Images/battle/dialogueBoxWin2.png")
		self.dialogueList1 = [self.dialogueBoxBattle1, self.dialogueBoxBattle2, self.dialogueBoxBattle3] #stores dialoge for before battle
		self.dialogueList2 = [self.dialogueBoxWin1, self.dialogueBoxWin2] #stores dialoge for after battle
		self.enterBattleScreenGrabRect = Rect (0,0,850,600)
		self.mode = "" #or whatever variable is keeping track of the battle scene
		self.fighting = True

		self.mx, self.my = mouse.get_pos()

	def updateVar(self):
		"Update variables in the battle system"
		for e in event.get():
			if e.type == MOUSEMOTION:
				self.mx, self.my = mouse.get_pos()

	def battleControl(self, screen, music):
		"""Main hub of battle system
		controls what happens in battle based on inputs"""
		self.updateVar()

		music[self.player.getLocation()].halt()
		music[self.player.getLocation() + " battle"].execute()

		while self.fighting:
			screen.blit(self.battleScene, (0, 0))

			if not self.gameOver:
				if self.turn:
					choice = self.fightOrFlight(screen)
					if choice:
						attack = self.chooseAttack(screen)
						self.performAttack(attack, screen)
					elif not choice:
						self.fighting = False
				else:
					attack = self.chooseAttack(screen)
					self.performAttack(attack, screen)

			elif self.gameOver and self.player.getHealth() <= 0:
				# faint animation
				self.fighting = False
			elif self.gameOver and self.enemy.getHealth() <= 0:
				print("Victory")
				# victory animation
				self.fighting = False
				return "victory"
			else:
				self.fighting = False

			display.flip()

	def fightOrFlight(self, screen):
		while True:
			self.updateVar()
			screen.blit(self.battleMenu1, (0,450))#clears previous highlighted option 

			if self.battleMenuFightChoiceRect.collidepoint((self.mx, self.my)): #when mouse is over "fight"
				print(2)
				draw.circle(screen,(0,0,0),(35,525),12)
				for e in event.get():
					if e.type == MOUSEBUTTONDOWN: #When "Fight" is clicked, proceed to battle
						#can't be boolean since false would be automatically triggered, set to empty string as default
						return True

			elif self.battleMenuFleeChoiceRect.collidepoint((self.mx,self.my)):#mouse over "flee"
				draw.circle(screen,(0,0,0),(325,525),12)
				for e in event.get():
					if e.type == MOUSEBUTTONDOWN: #When "Flee" is clicked, exit and go back to game
						return False

			display.flip()


	# FINISH
	def chooseAttack(self, screen):
		while True:
			screen.blit(self.battleMenu2,(0,450))
			self.battleMenuGrab = screen.subsurface(self.battleMenuGrabRect).copy()
			#Player chooses a spell, update enemy health, player status bars
			#battle is over if enemy dies or player dies
			for i in range(len(self.spell_list)):
				self.updateVar()
				if self.spell_rects[i].collidepoint((self.mx, self.my)):
					screen.blit(self.battleMenu2, (0,450))
					draw.circle(screen,(0,0,0),[35,self.spell_rects[i][1]],6)
					for e in event.get():
						if e.type == MOUSEBUTTONDOWN:
							return self.spell_list[i]

			display.flip()

	# FINISH
	def performAttack(self, attack, screen):
		print("performAttack")
		if self.turn:
			self.player.drainEnergy(attack.getEnergy()) #no energy drain for this move
			self.enemy.takeDamage(attack.getPower())
			#ADD: explosion sprite animation over enemy*********
			draw.rect(screen,(0,255,0),[560,564,self.player.getSpellEnergy()*1.51,16]) 
			self.turn = False
		else:
			self.player.takeDamage(attack.getPower())
			self.enemy.drainEnergy(attack.getEnergy())
			# animations
			draw.rect(screen,(255,0,0),[560,500,self.player.getHealth()*1.51,16]) #updates the player's health bar
			self.turn = True






	def doBattle(self, screen):
		"Draw battle scene"
		screen.blit(self.battleScene)
		# draw player and enemy sprites
		running = True
		while running:
			mx, my = mouse.get_pos()
			for e in event.get():
				# Check if user selects fight or flight
				if self.battleMenuFightChoiceRect.collidepoint((mx,my)) and self.gameOver==False: #when mouse is over "fight"
					screen.blit(self.battleMenuGrab,(0,450))#clears previous highlighted option 
					draw.circle(screen,(0,0,0),[35,525],12)
					if MOUSEBUTTONDOWN: #When "Fight" is clicked, proceed to battle
						#can't be boolean since false would be automatically triggered, set to empty string as default
						self.enterBattle = "True"

				elif self.battleMenuFleeChoiceRect.collidepoint((mx,my)) and self.gameOver==False:#mouse over "flee"
					screen.blit(self.battleMenuGrab,(0,450))
					draw.circle(screen,(0,0,0),[325,525],12)
					if mb[0] == 1: #When "Flee" is clicked, exit and go back to game
						self.enterBattle = "False"
						running = False

				else: #when is mouse is hovering over neither
					if self.gameOver==False: #fixes bug when it is blit even after game is over
						screen.blit(self.battleMenuGrab,(0,450))

				# battle functionality
				if self.enterBattle == "True" and self.gameOver==False:
					screen.blit(self.battleMenu2,(0,450))
					self.battleMenuGrab = screen.subsurface(self.battleMenuGrabRect).copy()
					#Player chooses a spell, update enemy health, player status bars
					#battle is over if enemy dies or player dies
					
					if self.battleSpellExpulRect.collidepoint((mx,my)) and self.turn:
						screen.blit(self.battleMenuGrab,(0,450))
						draw.circle(screen,(0,0,0),[38,473],6)
						if MOUSEBUTTONDOWN: #player clicks spell to attack on their turn 
							self.playerEnergy -= 0 #no energy drain for this move
							self.enemyHealth -= 8
							#ADD: explosion sprite animation over enemy*********
							draw.rect(screen,(0,255,0),[560,564,self.playerEnergy*1.51,16]) 
							self.turn = False
							
					elif self.battleSpellImperRect.collidepoint((mx,my)) and self.playerEnergy>=10 and self.turn:
						screen.blit(self.battleMenuGrab,(0,450))
						draw.circle(screen,(0,0,0),[38,507],6)
						if MOUSEBUTTONDOWN:
							self.playerEnergy -= 10
							self.enemyHealth -= 12
							#ADD: explosion sprite animation over enemy*********
							draw.rect(screen,(0,255,0),[560,564,self.playerEnergy*1.51,16]) 
							self.turn = False
							
					elif self.battleSpellCrucioRect.collidepoint((mx,my)) and self.playerEnergy>=15 and self.turn:
						screen.blit(self.battleMenuGrab,(0,450))
						draw.circle(screen,(0,0,0),[38,540],6)
						if MOUSEBUTTONDOWN:
							self.playerEnergy -= 15
							self.enemyHealth -= 16
							#ADD: explosion sprite animation over enemy*********
							draw.rect(screen,(0,255,0),[560,564,self.playerEnergy*1.51,16]) 
							self.turn = False
						
					elif self.battleSpellStupRect.collidepoint((mx,my)) and self.playerEnergy>=8 and self.turn:
						screen.blit(self.battleMenuGrab,(0,450))
						draw.circle(screen,(0,0,0),[38,572],6)
						if MOUSEBUTTONDOWN:
							self.playerEnergy -= 10
							#enemy damage is decreased when this move is used
							self.damage = randint(4,10) #OR HOWEVER the damage system works, you can change this
							draw.rect(screen,(0,255,0),[560,564,self.playerEnergy*1.51,16])
							self.turn = False
							
					#ADD THIS CODE: WHEN THE ENEMY ATTACKS YOU, ENEMY ATTACK ANIMATION 
					elif turn == False: #the enemy's turn
						#enemy attack animation *HERE
						#enemy attacks, deals damage so player health decreases
						self.damage = randint(6,12) #or however damage is calculated 
						self.playerHealth -= self.damage
						draw.rect(screen,(255,0,0),[560,500,self.playerHealth*1.51,16]) #updates the player's health bar
						self.turn = True #back to player's turn
						
				elif self.enterBattle== "Flee":
					screen.blit(self.enterBattleScreenGrab,(0,0))
					self.enterBattle = "" #flag resets
					#mode = "not battle" #or whatever flag is keeping track of the battle scene

				if self.playerHealth <= 0 and self.enterBattle=="True": #if player is killed in battle
					self.gameOver = True #Game over, game ends.
					screen.blit(self.gameOverScreen,(0,0))
					self.enterBattle = ""
					
				if self.enemyHealth <= 0 and self.enterBattle=="True": #player won battle by killing enemy
					#gains some experience and unlock an inventory spell or whatever, eg. append a new spell to the inventory spell list
					#mode = "not battle" #or whatever flag is keeping track of the battle scene
					screen.blit(self.enterBattleScreenGrab,(0,0))
					self.enterBattle = ""
					self.playerHealth = 100 #resets
					self.playerEnergy = 100 #resets 
					#The following displays a dialogue box when the battle is won, eg. "Victory!"
					self.box2 = randint (0,1) #randomly selects a win message
					screen.blit(self.dialogueList2[self.box2],(0,450))
					display.flip()
					time.wait (1200)
					screen.blit(self.enterBattleScreenGrab,(0,0))
					
				display.flip()