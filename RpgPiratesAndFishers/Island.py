#!/usr/bin/python3
# -*- coding: utf-8 -*-

from libGamePiratesAndFishers import assertFormat
from Item import Item

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
		self.name = assertFormat(name)
		self.itemisland = []
		
	
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
			for i in range(self.itemisland):
				arrayinfo.append(self.itemisland[i].getDetal())
			return arrayinfo
				
	# def addIndividual(self):

	# def getIndividual(self):

	# def addSpell(self):

	# def getSpell(self):

	# def adddirection(self):

	# def getdirection(self):

	# def getListdirections(self):

	# def getDetailIsland(self):

	