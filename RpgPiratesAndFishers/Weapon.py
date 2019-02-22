#!/usr/bin/python3
# -*- coding: utf-8 -*-




from Item import Item # imports the definitions on item class

class Weapon(Item):
	""" 
		The class defines the object type Weapon,defines capacity of attack of the object in the aplication

	"""

	def __init__(self,name,impact,speed):
		""" 
		Initializing the class Weapon, it's the constructor, assigned 
		the name and two attributes used for calculates the attack of the object
		limit both values in 10.
		

		@param name : (string) constains the name of weapon
		@param impact : (int) attribute for the class represent the impact of weapon
		@param speed : (int) attribute for the class represent the speed of weapon

		@return : None
		"""
		super().__init__(name) # passing to super class parameters
		#With the two attributes is calculates the Capacity of attack on character
		self.impact = super().limitsValues(impact)

		self.speed = super().limitsValues(speed)

	def __del__(self):
		""" 
		it's  destructor from the class, cleaning all the attributes
		

		@param none : 
		

		@return : None
		"""
		super().__del__()
		self.impact = None
		self.speed = None
	
	
	def getAttack(self):
		""" 
		Simple return the number who represent the attack of the object
		
		@return : (int)Number who represent the attack
		"""
		
		return (self.impact * self.speed)
	
	
	def getDetail(self):
		""" 
		Return a report for the user, about the object, what is the use, and attributes

		
		@return : (string) contains a report with the attributes of the object,like attack, defense, capacity of heal.
		"""
		return (super().setParameters(self.getAttack(),0,0))
		
		
