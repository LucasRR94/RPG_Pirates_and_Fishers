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

		super().__init__(assertFormat(name),health,attack,defense)


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
	def setAttack(self , attackobj):
		'''
		This method set an attribute itemattack, that will be testes if is right type is insert
		@param attackobj:(uknown) is an  object of unknown type
		@return : (int) case of item is type Attack return 1, return 0 otherwise
		'''

	# def changeItemattack(self):

	# def changeItemDefense(self):

	# def getDetail(self):

	# def useItem(self):

	# def collectItem(self):

	# def listItems(self):

	def getSpell(self):
		'''
		This method return an object type Spell that are present in the object Fisher as attribute
		
		@return : object type spell , or None
		'''

		return self.spell 

	# def listSpell(self):

	# def dropSpell(self):

	# def dropItems(self):

	# def getIdPlayer(self):

	# def changeIsland(self):

	# def getDirectionsfromIsland(self):

	# def takeDescriptionIsland(self):

	# def takeItemIsland(self):

	# def takeSpellIsland(self):

	# def attackEnemy(self):

	
