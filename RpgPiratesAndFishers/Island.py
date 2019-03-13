#!/usr/bin/python3
# -*- coding: utf-8 -*-

from libGamePiratesAndFishers import assertIfIsWeelFormat
from Item import Item
from Individual import Individual
from Spell import Spell
#from Fisher import Fisher

class Island():
	""" 
		This class Define object type Island, that represent the one scenario possible in application.
		Can have players, items and spell. That is responsible to manage all interactions between players
		with itens, spelll and with other players.
	""" 
	def __init__(self,name):
		""" 
		Initializing the class Island, it's the constructor, of the class island
		that carrier all the attributes of the scenario, and give support to all the 
		actions of the player in the applicationn
		
		@param name : (string) constains the name of Island
		
		@return : None
		"""
		self.name = assertIfIsWeelFormat(name)
		self.itemisland = []
		self.spellisland = None
		self.directions = {} # begins a dictionary on the Island
		self.individualsPresent = [] # begins array of individuals

	def getName(self):
		"""
		This method returns the name of the island
		@param : None
		@return :(String) that represent the name of the island
		"""
		return self.name

	def addItem(self,newitem):
		"""
		This method add an attribute newitem on the obj
		@param newitem :(item) the item that will be add in the attribute itemisland
		@return :(int) 1 if operation sucessed , 0 if fails
			"""
		if(isinstance(newitem,Item)):
			self.itemisland.append(newitem)
			return 1 

		else:
			return 0
	
	def getItem(self,referernameitem):	
		"""
		This method return an specified obj type "Item" from attribute present on the object
		@param referernameitem :(str) is a string the represent the name of obj type Item
		@return :(Item) the Item request if operation succeed , None if fails
		"""
		if(len(self.itemisland)==0):
			return None
		elif(type(referernameitem) is str):
			i=0
			condition = 0 
			while(condition==0):
				if(len(self.itemisland)<(i+1)):
					backup = condition 
					condition= backup + 1
					return None
				else:
					itematual = self.itemisland[i]
					if(itematual.getName() == referernameitem):
						return (self.itemisland.pop(i))
					else:
						backup1 = i
						i = backup1+1

		else:
			return None
	
	def getListItems(self):
		"""
		This method return a array with all the details of items present on the attribute present on itemisland
		@param None:
		@return :(array) array of strings , that carrier the details of all the items present on the island, or None
		if items not found
		"""		
		size = len(self.itemisland)
		if(size==0):
			return None
		else:
			arrayinfo = []

			for i in range(len(self.itemisland)):
				arrayinfo.append(self.itemisland[i].getDetail())
			return arrayinfo
				
	def addSpellIsland(self,newspell):
		"""
		this method ading an Spell object as attribute in class, if already have an obj, it replace
		@param (newspell):(Spell) it's an object type spell
		@return:(int) 1 if operation sucesfull, 0 otherwise
		"""
		if(type(newspell) is Spell):
			self.spellisland = newspell
			return 1
		else:
			return 0
	
	def getSpell(self):
		"""
		This method return the Spell present , on the attribute spellisland, case is empty return None
		, otherwise return the obj
		@param (None):
		@return:(Spell) return an object type Spell if exist, otherwise return None 
		"""		
		if(self.spellisland != None):
			backup = self.spellisland
			self.spellisland = None
			return backup
		else:
			return None

	def statusSpell(self):
		"""
		this method informs if has some Spell obj present that can be collect, if exist return 1, otherwise return 0
		@param None:
		@return :(int) 1 if exist the Spell obj , 0 otherwise
		"""	
		if(self.spellisland == None):
			return 0
		elif(type(self.spellisland) == Spell):
			return 1
		else:
			return 0

	def addIndividual(self, newIndividual):
		"""
		this method adds objects type individuals on the game, if he is successful he returns 1, otherwise 0
		@param newIndividual, (Individual) obj type Individual
		@return ,(int) 1 if successful on insert on the Island, 0 otherwise 
		"""
		if(isinstance(newIndividual,Individual)):
			try:
				self.individualsPresent.index(newIndividual)
			except ValueError:
				self.individualsPresent.append(newIndividual) # added individual on the Island
				return 1
			else:
				# the individual alredy is present the island
				return 0
		else:
			return 0

	
	def getIndividual(self,identification):
		"""
 		This method, uses a key (identification) to search throw the island (individualsPresent) to find a
 		specific individual
 		@param identification:(str) is a string uses to make a search on the vector of individual
 		@return :(Individual or None) if the method find the individual is return the obj Individual, otherwise return None
		"""
		if(type(identification) is str):
			# search
			sizearray = len(self.individualsPresent)
			if(sizearray <=0):
				return None
			else:
				for i in range(sizearray):
					if(self.individualsPresent[i].getName()==identification):
						return self.individualsPresent[i]
				return None
		else:
			return None

	def listIndividuals(self):
		"""
		This method return a list with the names and parameters of all the individuals present on the island
		@param None: None
		@return :(array str) array with string that contains the details of all the individuals present on the island, or None
		"""
		if(len(self.individualsPresent)==0):
			return None
		else:
			emptystr = []
			for actualindividual in self.individualsPresent:
				emptystr.append(actualindividual.getDetail)
			return emptystr

	def verifyIndividuals(self):
		"""
		This method is responsible to verify all the individuals, and exclude from the island 
		all the Individuals that are not lives
		@param None
		@return None
		"""
		if(len(self.individualsPresent)>=0):
			for actualindividual in self.individualsPresent:
				if(actualindividual.getHealth()<=0):
					outofvector = self.individualsPresent.pop()
			return 0

	def adddirection(self,newisland,key):
		"""
		this method add a direction on the island,detail this direction will be used like a key 
		, this means that need to be a string like "center","right","back","left", otherwise will be ignored
		, it receive an object of type island and string that represent the 
		key to dictionary
		@param newisland:(Island) island that will be add in the dictionary of directions
		@param key : (str) key to dictionary
		@return :(int) return 1 if operation sucessful, 0 otherwise
		"""
		if(type(key) == str  and type(newisland) == Island):
			if(key== "left" or key == "center" or key == "right" or key =="back"):
				self.directions[key] = newisland
				return 1	
			else:
				return 0
		else:
			return 0

	def getdirection(self,key):
		"""
		This function return an object type island,present on the attribute on directions
		@param key : (str) a key that links with the obj
		@return :(Island) return an obj type Island if exist the key, or None if does not exist
		"""
		return (self.directions[key])

	def listdirections(self):
		"""
		This function return all the directions of the island, return all 
		the conections(keys) on other islands(obj translated)
		@param None:
		@return :(array) of tuples strings (directions(keys type str) -> islands names(obj type island))
		, if empty return None,None
		"""
		if(len(self.directions) > 0):
			answer = []
			for i in self.directions:
				actualisland = self.directions[i]
				newtuple = (i,self.directions[i].getName())
				answer.append(newtuple)
			return answer
		else:
			answer = (None,None)
			return answer
	
	def changeIndividualForOtherisland(self,presentindividual,newIsland):
		"""
		This method just transfer an individual present on the Island to another island
		@param presentindividual : (Individual) is an Object type Individual that are present on the island
		@param newIsland :(Island) is an Object type Island present on the game
		@return :(int) 1 if operation successful, 0 if is not
		"""
		if(isinstance(presentindividual,Individual) and type(newIsland) is Island):
			position = self.individualsPresent.index(presentindividual)
			objectIndividual = self.individualsPresent.pop(position)
			newIsland.addIndividual(objectIndividual)
			return 1
		else:
			return 0	
	
	
	