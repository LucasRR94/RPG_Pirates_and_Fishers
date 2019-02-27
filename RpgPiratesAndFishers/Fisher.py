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

		self.backpack = [] # start backpack of itens, where all the itens will be stored

	def getWeapon(self):
		'''
		This method return an object type Weapon that are present in the object Fisher as attribute
		
		@return : object type Weapon, or None
		'''
		return self.itemattack
	
	def getDefense(self):
		'''
		This method return an object type Defense that are present in the object Fisher as attribute
		
		@return : object type Defense, or None
		'''	
		return self.itemdefense

	def getactualIsland(self):
		'''
		This method return an object type Island that are present in the object Fisher as attribute
		
		@return : object type Island, or None
		'''
		return self.actualisland
	
	def getIdplayer(self):
		'''
		This method return an object type (string), representing one hashlib_HASH key that are present in the object Fisher as attribute
		
		@return : object type str, or None
		'''
		return self.idplayer
	
	# not tested, and be construction ------

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

	def addItemBackpack(self,item):
		'''
		This method added an object type Item, on the backpack that are an list
		@param item:(uknown) is an object of unknown type, that should be an item obj
		@return : (1) if is successfull the operation, 0 if is fail
		'''
		if(isinstance(item,Item)):
			self.backpack.append(item)
			return 1		
		else:
			return 0

	def listItemBackpack(self):
		'''
		This method list all the itens present on backpack
		
		@return : (list) is a list of strings, that carrier 
		the details of items present on back pack, or None if
		is empty
		'''
		if(len(self.backpack) > 0):
			message = []
			for i in range(len(self.backpack)):
				message.append(self.backpack[i].getDetail())

			return message	
		else:
			return None

	def useItemBackpack(self,choose):
		'''
		This method take a parameter that represent obj 
		of backpack, and using this object in Fisher, 
		and if this replace other, the replaced is 
		stored in backpack.
		
		@param item:(str) is an refer to an obj present of backpack
		
		@return : (1) if is successfull the operation, 0 if is fail
		'''
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

							return 1
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
		'''
		This method take a obj of type Weapon, and 
		replace	on the itemattack, and the replaced 
		is return on the method

		@param newattack:(Weapon) is an object, that is of type Weapon

		@return : (Weapon) if have something previous, it is returned, else return None
		'''
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
		'''
		This method take a obj of type Defense, and 
		replace	on the itemdefense, and the replaced 
		is return on the method

		@param newdefense:(Defense) is an object, that is of type Defense

		@return : (Defense) if have something previous, it is returned, else return None
		'''
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
		'''
		This method take a obj of type Medkit,and add 
		the healing capacity of the item on the fisher
		, and using the method of the Medkit obj call
		useHealing(), that destroy automatic the item

		@param newdefense:(Medkit) is an object, that is of type Medkit

		@return : (int) 1 if operation successful, 0 otherwise.
		'''
		valuehealth = itemmedkit.useHealing()
		return (super().usingMedkit(valuehealth))

	
	# def setAttack(self , attackobj):
	# 	'''
	# 	This method set an attribute itemattack, that will be testes if is right type is insert
	# 	@param attackobj:(uknown) is an  object of unknown type
	# 	@return : (int) case of item is type Attack return 1, return 0 otherwise
	# 	'''
	# 	if(type(attackobj)is attackobj):
	# 		self.itemattack =  attackobj

	# 	else:
	# 		print("Error, Obj not correspond to item Attack \n")
	
	# def getSpell(self):
	# 	'''
	# 	This method return an object type Spell that are present in the object Fisher as attribute
		
	# 	@return : object type spell , or None
	# 	'''

	# 	return self.spell		
	
	


	

	

	# def useItem(self):

	# def collectItem(self):

	# def listItems(self):

	# def listSpell(self):

	# def dropSpell(self):

	# def dropItems(self):

	# def changeIsland(self):

	# def getDirectionsfromIsland(self):

	# def takeDescriptionIsland(self):

	# def takeItemIsland(self):

	# def takeSpellIsland(self):

	# def attackEnemy(self):

	
