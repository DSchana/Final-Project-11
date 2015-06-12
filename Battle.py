# Battle.py

from pygame import *
from random import *
from math import *
from attackSprites import *

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
		self.enemyHealth = 100 
		self.gameOverScreen = image.load ("Images/battle/gameOver.jpg")
		self.gameOver = False
		self.turn = True
		#These images are the dialogue boxes that appear before/after a battle
		self.dialogue = []
		self.dialogue.append(image.load ("Images/battle/dialogueBoxBattle1.png"))
		self.dialogue.append(image.load ("Images/battle/dialogueBoxBattle2.png"))
		self.dialogue.append(image.load ("Images/battle/dialogueBoxBattle3.png"))

		self.win = []
		self.win.append(image.load ("Images/battle/dialogueBoxWin1.png"))
		self.win.append(image.load ("Images/battle/dialogueBoxWin2.png"))

		self.enterBattleScreenGrabRect = Rect (0,0,850,600)
		self.mode = "" #or whatever variable is keeping track of the battle scene
		self.fighting = True

		self.mx, self.my = mouse.get_pos()

		self.enemySprite = attackSprite("Images/attack/" + self.enemy.getKind() + "IdleSprite/", "Images/attack/" + self.enemy.getKind() + "AttackSprite/", 50, 200)
		self.enemySprite.loadImages()

		self.playerSprite = attackSprite("Images/attack/playerIdleSprite/", "Images/attack/playerAttackSprite/", 700, 200)
		self.playerSprite.loadImages()

	def updateVar(self):
		"Update variables in the battle system"
		self.mx, self.my = mouse.get_pos()
		self.mb = mouse.get_pressed()

		for e in event.get():
			if e.type == MOUSEMOTION:
				self.mx, self.my = mouse.get_pos()

	def battleControl(self, screen, music):
		"""Main hub of battle system
		controls what happens in battle based on inputs"""
		self.updateVar()

		music[self.player.getLocation()].halt()
		music[self.player.getLocation() + " battle"].execute()

		self.showDialogue(screen)
		time.delay(1500)

		while self.fighting:

			screen.blit(self.battleScene, (0, 0))
			self.checkHealth(screen)

			# determine attacker
			if not self.gameOver:
				if self.turn:
					self.choice = self.fightOrFlight(screen)
					if self.choice:
						attack = self.chooseAttack(screen)
						if attack.getEnergy() <= self.player.getSpellEnergy():
							self.performAttack(attack, screen)
						self.turn = False
					elif not self.choice:
						self.fighting = False

				if self.turn == False:
					attack = self.chooseAttack(screen)
					if attack.getEnergy() <= self.enemy.getSpellEnergy():
							self.performAttack(attack, screen)
					self.turn = True

			self.enemySprite.showIdle(screen)
			self.playerSprite.showIdle(screen)
			self.displayHealth(screen)

			display.flip()

	def fightOrFlight(self, screen):
		"Allow user to choose to fight or run away"
		while True:
			screen.blit(self.battleScene, (0, 0))

			self.updateVar()
			screen.blit(self.battleMenu1, (0,450))#clears previous highlighted option 

			if self.battleMenuFightChoiceRect.collidepoint((self.mx, self.my)): #when mouse is over "fight"
				draw.circle(screen,(0,0,0),(35,525),12)
				if self.mb[0] == 1:
					return True
				for e in event.get():
					if e.type == MOUSEBUTTONDOWN: #When "Fight" is clicked, proceed to battle
						#can't be boolean since false would be automatically triggered, set to empty string as default
						return True

			elif self.battleMenuFleeChoiceRect.collidepoint((self.mx,self.my)):#mouse over "flee"
				draw.circle(screen,(0,0,0),(325,525),12)
				if self.mb[0] == 1:
					return False
				for e in event.get():
					if e.type == MOUSEBUTTONDOWN: #When "Flee" is clicked, exit and go back to game
						return False

			self.enemySprite.showIdle(screen)
			self.playerSprite.showIdle(screen)
			self.displayHealth(screen)

			display.flip()

	def chooseAttack(self, screen):
		"Allow user and enemy to choose attack"
		while True:
			screen.blit(self.battleScene, (0, 0))

			if self.turn:
				screen.blit(self.battleMenu2,(0,450))
				self.battleMenuGrab = screen.subsurface(self.battleMenuGrabRect).copy()
				#Player chooses a spell, update enemy health, player status bars
				#battle is over if enemy dies or player dies
				for i in range(len(self.spell_list)):
					self.updateVar()
					if self.spell_rects[i].collidepoint((self.mx, self.my)):
						screen.blit(self.battleMenu2, (0,450))
						draw.circle(screen,(0,0,0),[35, self.spell_rects[i][1] + 15], 6)
						if self.mb[0] == 1:
							return self.spell_list[i]
						for e in event.get():
							if e.type == MOUSEBUTTONDOWN:
								return self.spell_list[i]

			else:
				return self.enemy.chooseSpell()

			self.enemySprite.showIdle(screen)
			self.playerSprite.showIdle(screen)
			self.displayHealth(screen)

			display.flip()

	def performAttack(self, attack, screen):
		"player deals or takes damage"
		screen.blit(self.battleScene, (0, 0))

		if self.turn:
			self.playerSprite.showAttack(screen, self.battleScene, self.enemySprite, self)
			self.enemySprite.showIdle(screen)

			self.player.drainEnergy(attack.getEnergy()) #no energy drain for this move
			self.enemy.takeDamage(attack.getPower())
			#ADD: explosion sprite animation over enemy*********
			self.turn = False

			self.displayHealth(screen)

		elif self.turn == False:
			self.enemySprite.showAttack(screen, self.battleScene, self.playerSprite, self)
			self.playerSprite.showIdle(screen)

			self.player.takeDamage(attack.getPower())
			self.enemy.drainEnergy(attack.getEnergy())
			# animations

			self.displayHealth(screen)

	def displayHealth(self, screen):
		"Show player and enemy info"
		screen.blit(self.profilePic,(755,500)) #harry's face in the corner 
		screen.blit(self.healthLogo,(685,465)) #health cross pic
		screen.blit(self.energyLogo,(685,528)) #energy lightning bolt pic
		draw.rect(screen,(0,0,0),[558,498,155,20]) #Health bar outline
		draw.rect(screen,(0,0,0),[558,562,155,20]) #energy bar outline
		draw.rect(screen,(0,0,0),[28,178,104,20])
		if self.player.getHealth() <= 0:
			draw.rect(screen, (255, 0, 0), [560, 500, 0, 16])
		else:
			draw.rect(screen, (255, 0, 0), [560, 500, self.player.getHealth()*1.51, 16])

		if self.player.getSpellEnergy() <= 0:
			draw.rect(screen, (0, 255, 0), [560, 564, 0, 16])
		else:
			draw.rect(screen, (0, 255, 0), [560, 564, self.player.getSpellEnergy()*1.51, 16])

		if self.enemy.getHealth() <= 0:
			draw.rect(screen, (255, 0, 0), (30, 180, 0, 16))
		else:
			draw.rect(screen, (255, 0, 0), (30, 180, self.enemy.getHealth(), 16))

	def checkHealth(self, screen):
		# game ends when player dies
		if self.player.getHealth() <= 0 or self.enemy.getHealth() <= 0:
			self.fighting = False
			screen.blit(self.gameOverScreen, (0, 0))
			display.flip()
			time.delay(5000)

	def showDialogue(self, screen):
		box_num = randint(0, 2)
		screen.blit(self.dialogue[box_num], (0, 450))
		display.flip()