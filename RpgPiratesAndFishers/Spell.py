#!/usr/bin/python3
# -*- coding: utf-8 -*-
from libGamePiratesAndFishers import *

class Spell(object):
	"""
	This class Define object type Spell, it is a base for object used for spell in the application.
	"""
	def __init__(self, name , value):
		""" 
		Initializing the class Spell, it's the constructor, assigned 
		the name and one attribute, the represente the value of defense 
		Value is limite 0...100	

		@param name : (string) constains the name of Spell, between 5~32 caracters
		@param value : (int) attribute for the class represent the value of the spell in the object
		
		@return : None
		"""
		self.name  = assertIfIsWeelFormat(name)
		self.value = makeSureThatIsnumberLimited(value,100)


	def getName(self): 
		""" 
		Return the name of the object type Item
		
		@return : (string) contains the name of the object, type item
		"""
		return self.name
	
	def getValue(self):
		"""
		Return the value of the spell.

		@return : (string) contains the value of the speel, type spell
		"""
		return self.value
