#!/usr/bin/python3
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------#

class Item(object):
	""" 
		The super class defines the object type Item,who is inheritance of class , weapon , capacityofdefense.

	"""

	def __init__(self,name):
		""" 
		Initializing the class Item, it's the constructor  
		the name , for the inheritance of subclasses
		

		@param name : (string) constains the name of item
		
		@return : None
		"""
		self.name = name

	def getName(self):
		""" 
		Return the name of the object type Item
		
		@return : (string) constains the name of the object, type item
		"""
		return(self.name)
	
	def getDetail(self):
		""" 
		It's a interface, it's implemented in the subclasses, how return a report of what precisely it's item
		
		"""
		pass

#-------------------------------------------------------------------------------------------------------------------

