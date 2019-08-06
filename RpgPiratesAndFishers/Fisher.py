#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Item import Item
from Spell import Spell
from Individual import Individual
from Weapon import Weapon
from Defense import Defense
from Medkit import Medkit
from Island import Island
from libGamePiratesAndFishers import assertFormat
import hashlib
import random

class Fisher(Individual):
	"""
	This class Define object type Fisher, it is a representation of the player
	implemented all the methods and loading all the attributes, for the capacity
	of control and actions in the application.
	"""
	def __init__(self,name,health,itemattack,itemdefense,location,Idplayer):
		"""
		Initializing the class Fisher, it's the constructor, assigned 
		the attributes of inherentance Individual, itens like: defense, attack.
		Actual localation, that is a pointer for an island.
		Idplayer, that is a hash code provided by an ip of the player
		@param name : (string) constains the name of Individual
		@param health : (int) attribute for the class represent the health of the individual, 0..100
		@param itemattack : (Attack) attribute for the class represent an item type attack
		@param itemdefense : (Defense) attribute for the class represent an item type defense
		@param localation : (Island) attribute for the class represent an island that the player is localated
		@param IdPlayer : (hexa code) attribute that identify the player,is provided with by a hash function from an ip
		@return : (None)
		"""
		try:
			assert(type(itemattack) == Weapon)
		except AssertionError:
			print("\033[95mError, the insert item of type weapon not correspond to Weapon object\n")
			self.itemattack = None
		else:
			self.itemattack = itemattack

		try:
			assert(type(itemdefense) == Defense)
		except AssertionError:
			print("\033[95mError, the insert item of type defense not correspond to Defense object\n")
			self.itemdefense = None
		else:
			self.itemdefense = itemdefense	

		try:
			assert(type(location) == Island)
		except AssertionError:
			print("\033[95mError, the insert element of type island not correspond to Island object\n")
			self.actualisland = None
		else:

			self.actualisland = location
			self.actualisland.addIndividual(self) # adding the Fisher on the island 
					
		try:
			assert(type(Idplayer) == str and len(Idplayer) == 64)
		except AssertionError:
			print("\033[95mError, the element Idplayer , not correspond to hash type, generating generic Idplayer")
			objhash = hashlib.sha256()
			randnumb = random.randint(-100000,100000)
			word = bytes(str(randnumb),"latin-1")
			objhash.update(word)
			self.idplayer = objhash.hexdigest()
		else:
			self.idplayer = Idplayer
					
		attack = 0
		defense = 0

		if(type(itemattack) is Weapon):
			attack = itemattack.getAttack()
		if(type(itemdefense) is defense):
			defense = itemdefense.getDefense()
		super().__init__(name,health,attack,defense)
		self.backpack =[]# start backpack of itens, where all the itens will be stored
		self.spellcontainer =[]# start container of spells, where all the spells geted will appear
	
	def getWeapon(self):
		"""
		This method return an object type Weapon that are present in the object Fisher as attribute
		@return : object type Weapon, or None
		"""
		return self.itemattack

	def getDefense(self):
		"""
		This method return an object type Defense that are present in the object Fisher as attribute
		
		@return : object type Defense, or None
		"""	
		return self.itemdefense

	def getactualIsland(self):
		"""
		This method return an object type Island that are present in the object Fisher as attribute
		
		@return : object type Island, or None
		"""
		return self.actualisland
	
	def getNamelocation(self):
		"""
		This method  return an string, that represent the name of the actual island where is located the Fisher

		@return : (str), that represent the name of the actual island of the fisher
		"""
		return self.actualisland.getName()
		
	
	def getIdplayer(self):
		"""
		This method return an object type (string), representing one hashlib_HASH key that are present in the object Fisher as attribute
		
		@return : object type str, or None
		"""
		return self.idplayer
	
	def addItemBackpack(self,item):
		"""
		This method added an object type Item, on the backpack that are an list
		@param item:(uknown) is an object of unknown type, that should be an item obj
		@return : (1) if is successfull the operation, 0 if is fail
		"""
		if(isinstance(item,Item)):
			self.backpack.append(item)
			return 1		
		else:
			return 0

	def listItemBackpack(self):
		"""
		This method list all the itens present on backpack
		
		@return : (list) is a list of strings, that carrier 
		the details of items present on back pack, or None if
		is empty
		"""
		if(len(self.backpack) > 0):
			message = []
			for i in range(len(self.backpack)):
				message.append(self.backpack[i].getDetail())

			return message	
		else:
			return None

	def useItemBackpack(self,choose):
		"""
		This method take a parameter that represent obj 
		of backpack, and using this object in Fisher, 
		and if this replace other, the replaced is 
		stored in backpack.
		
		@param item:(str) is an refer to an obj present of backpack
		
		@return : (1) if is successfull the operation, 0 if is fail
		"""
		condition = 0
		i = 0
		if(type(choose)is str):
			while(condition!=1):
				if(len(self.backpack) < (i+1)):
					condition = 1
					return 0
				else:	
					if(self.backpack[i].getName() == choose):
						itembackup = self.backpack.pop(i) # remove and return to the variable
						if(type(itembackup) is Weapon or type(itembackup) is Defense):
							backup2 = None
							
							if(type(itembackup) is Weapon):
								backup2 = self.__changeItemWeapon(itembackup)
									
							if(type(itembackup) is Defense):
								backup2 = self.__changeItemDefense(itembackup)
							
							if(backup2 != None):
								self.backpack.append(backup2)

							result =[]
							result.append(1)
							result.append(itembackup)
							return result
						else:
							if(type(itembackup) is Medkit):
								backup2 = self.__usingMedKit(itembackup)
								return backup2
							else:		
								return 0	
				
				back = i
				i = back+1

			
		else:	
			return 0

	def __changeItemWeapon(self, newattack):
		"""
		This method take a obj of type Weapon, and 
		replace	on the itemattack, and the replaced 
		is return on the method

		@param newattack:(Weapon) is an object, that is of type Weapon

		@return : (Weapon) if have something previous, it is returned, else return None
		"""
		backup = self.itemattack

		if(backup != None):
			super().changeAttack(newattack.getAttack())
			self.itemattack = newattack
			return backup

		else:
			super().changeAttack(newattack.getAttack())
			self.itemattack = newattack
			return None

	def __changeItemDefense(self, newdefense):
		"""
		This method take a obj of type Defense, and 
		replace	on the itemdefense, and the replaced 
		is return on the method

		@param newdefense:(Defense) is an object, that is of type Defense

		@return : (Defense) if have something previous, it is returned, else return None
		"""
		backup = self.itemdefense
		
		if(backup != None):
			super().changeDefense(newdefense.getDefense())
			self.itemdefense = newdefense
			return backup

		else:
			super().changeDefense(newdefense.getDefense())
			self.itemdefense = newdefense
			return None

	def __usingMedKit(self,itemmedkit):
		"""
		This method take a obj of type Medkit,and add 
		the healing capacity of the item on the fisher
		, and using the method of the Medkit obj call
		useHealing(), that destroy automatic the item

		@param newdefense:(Medkit) is an object, that is of type Medkit

		@return : (int) 1 if operation successful, 0 otherwise.
		"""
		valuehealth = itemmedkit.useHealing()
		return (super().usingMedkit(valuehealth))

	# not tested, and be construction ------

	def collectItem(self,referenameitem):
		"""
		This method add an item from actual position(island) for the back pack
		@param referenameitem:(str) that is the name of the item present on
		island that will be moved for the backpack
		@return :(int) 1 if operation succeed , 0 if fail
		"""
		itemonisland = self.actualisland.getItem(referenameitem)
		if(itemonisland == None):
			return 0
		else:
			self.backpack.append(itemonisland)

	def listItemsfromIsland(self):
		"""	
		This method return a list from items details present on the actual position(island)
		@param None:
		@return :(array) array of strings, that carrier details from items present on actual position
		"""
		
		return(self.actualisland.getListItems())

	def dropItems(self):
		"""
		This method return all the array of the Items present in the object,and deletes the current attribute of items
		@param None:
		@return :(array) contains all the items present on the object
		"""
		backup = self.backpack
		self.backpack = None
		return backup

	def dropSpells(self):
		"""
		This method return all the array of the spells present in the object, and deletes the current attribute of spells
		@param None:
		@return :(array) contains all the spells present on the object
		"""	
		backup = self.spellcontainer
		self.spellcontainer = None
		return backup

	def __addspell(self,newspell):
		"""
		This method just check the type of the element that wants to insert on the spellcontainer, and if the type is right, insert
		otherwise reject
		@param newspell:(Spell) object of the type Spell
		@param :(int) 1 if the insert was sucessfull, 0 otherwise
		"""
		if(type(newspell) == Spell):
			self.spellcontainer.append(newspell)
			return 1 

		else:
			return 0

	def getvalueSpell(self):
		"""
		this method returns the value of the spells present on the spellcontainer, if there is not spell, return 0
		@param None:
		@return :(int) number that represent the value of all the spells summed, or 0 if there is not spell
		"""
		value = 0
		if(len(self.spellcontainer) > 0):
			for spell in self.spellcontainer:
				backup = value
				value = spell.getValue() + backup
				
			return value
		else:
			return 0

	def getinfoaboutSpellonIsland(self):
		"""
		this method informed if have some spell present on the island, if exist return 1, otherwise return 0
		@param None:
		@return :(int) return 1 case exist spell on the island, otherwise return 0
		""" 
		return (self.actualisland.statusSpell())
	
	def changeIsland(self,direction):
		"""
		This method received a key(str) and move the Fisher for other  island, 
		it uses direction present on the actual island
		@param direction:(str) key that will link to other island
		@return:(int) 1 if operation successful, 0 otherwise 
		"""
		pointer = self.actualisland.getdirection(direction)
		if(pointer == None):
			return 0
		elif(type(pointer) == Island):
			backup = self.actualisland
			self.actualisland = pointer
			backup.changeIndividualForOtherisland(self,pointer)
			return 1
		else:
			return 0

	def getDirectionsfromIsland(self):
		"""
		this method returns a list of strings contained, the all the directions present on the island
		in the format"direction and island destination"
		@param None:
		@return :(list) contained "direction and island destination", None if empty
		"""
		tupleisland = self.actualisland.listdirections()
		#return 1
		if(type(tupleisland)== tuple):
			return None
		
		if(type(tupleisland)==list):
			answer = "\n"
			for i in tupleisland:
				key = i[0]
				islandkey = i[1]
				phraseformed = "direction "+str(key)+" the island is: "+ str(islandkey)
				answer+=phraseformed + "\n"
			answer+="\n"
			return answer
		
		else:
			return None

	def collectSpell(self):
		"""
		This method colect from island a obj Spell available, if is not available return 0, otherwise return 1
		@param None:
		@return :(int) 1 if sucessfull colect, 0 otherwise
		"""
		spellcolect = self.actualisland.getSpell()
		if(spellcolect != None):
			if(type(spellcolect)==Spell):
				return(self.__addspell(spellcolect))
			else:
				return 0
		else:
			return 0

	def takeItemsandSpellsDeathplayer(self):
		"""
		This method just returns all the objects type Items and Spells present on the player death
		He do that using the methods:dropItems and dropSpells
		@param None:
		@return :(array) [all the items present, all the spells present], or if just one is present the response still 
		is an array but one is None type, if both are empty the response is None
		"""
		response = []
		first = self.dropItems()
		second = self.dropSpells()
		if(len(first) == len(second) == 0):
			return None
		else:
			if(len(first)==0):
				response.append(None)
				response.append(second)
				return response
			elif(len(second)==0):
				response.append(first)
				response.append(None)
				return response
			else:
				response.append(first)
				response.append(second)
				return response


	# def takeDescriptionIsland(self):

	def attackEnemy(self,referrerIndividual):
		"""
		This method receive a string of a name of one Individual present on the island, and uses for
		make damage on the Individual, if the Individual is not a obj type Fisher he automaticly 
		provide damage to the attacker, if he is a Fisher, that not hapens
		@param referrerIndividual : (str) name of the Individual for attack
		@return :(int) 1 of was successful the attack, 0 if was not
		"""
		if(type(referrerIndividual) is str):
			individualForAttack = self.actualisland.getIndividual(referrerIndividual)
			if(individualForAttack == None):
				return 0
			else:
				if(type(individualForAttack) == Individual):
					location = self.getactualIsland()
					previousattackfromattacker = self.getValueAttack()
					previousattackfromdefender = individualForAttack.getValueAttack()
					individualForAttack.getDamage(previousattackfromattacker)
					self.getDamage(previousattackfromdefender)
					if(self.getHealth() == None and individualForAttack.getHealth() == None):
						result  = location.removeIndividualPresente(self)
						result2 = location.removeIndividualPresente(individualForAttack)
						return (result2 or result)
					elif(self.getHealth() != None and individualForAttack.getHealth() == None):
						result = location.removeIndividualPresente(individualForAttack)
						return (result)
					elif(self.getHealth() == None and individualForAttack.getHealth() != None):
						result = location.removeIndividualPresente(self)
						return (result)	
					elif(self.getHealth() != None and individualForAttack.getHealth() != None):
						return (1)	

				if(type(individualForAttack) == Fisher):
					result2 = 0
					individualForAttack.getDamage(self.getValueAttack())
					location = self.getactualIsland()
					if(individualForAttack.getHealth() == None): #is death
						ItemsSpellsenemy = individualForAttack.takeItemsandSpellsDeathplayer()	
						if(ItemsSpellsenemy != None):
							items = ItemsSpellsenemy.pop(0)
							spells = ItemsSpellsenemy.pop(0)
							if(items != None):

								for i in items:

									self.addItemBackpack(i)
							if(spells != None):		
								for j in spells:
									self.__addspell(j)	

							result2 = location.removeIndividualPresente(individualForAttack)
					#print(individualForAttack.getHealth())			
					#elf.actualisland.verifyIndividuals()
							return result2
					else:
						return 1
				else:
					return 0	
		else:
			return 0

	def listenemies(self):
		"""
		This method return an list of all enemies with their details, if there is not enemies return None
		@param None 
		@return :(array of str OR None) return an array contains details of Individuals present in same 
		island or None
		"""
		return (self.actualisland.listIndividualsforindividual(self))


	# def dropItemsSpeels(self):

	def getDetail(self):
		"""
		it's getting the attributes of the class, providing a report of the object,
		citing the Weapons and the Defense present on the Fisher

		@param None:

		@return (string) : getting an report of the attributes of the object, and report
		on weapon and Defense

		"""
		partialResult  = super().getDetail()
		partialResult1 = None
		partialResult2 = None

		if(self.itemdefense != None):
			partialResult1 = self.itemdefense.getDetail()

		if(self.itemattack != None):
		 	partialResult2 = self.itemattack.getDetail()

		if(partialResult2 != None):
			partialResult+=partialResult2

		if(partialResult1 != None):
			partialResult+=partialResult1

		return partialResult	
