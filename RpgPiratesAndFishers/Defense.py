#!/usr/bin/python3

from Item import *

class Defense(Item):
	""" 
		This class Define object type Defense, it is a base for object used for defense in application.
	""" 

	def __init__(self,name,maneuverability,protection):
		""" 
		Initializing the class Defense, it's the constructor, assigned 
		the name and two attributes used for calculates the capacity of defend
		of the object
		limit both values in 10.
		

		@param name : (string) constains the name of Defense
		@param maneuverability : (int) attribute for the class represent the capacity of movability of the object
		@param protection : (int) attribute for the class represent the attack resistence

		@return : None
		"""
		super().__init__(name)
		self.maneuverability = super().limitsValues(maneuverability)
		self.protection = super().limitsValues(protection)


	def getDefense(self):
		""" 
		Simple return the number who represent the capacity of defense of the object
		
		@return : (int)Number who represent the defense of the object
		"""
		
		return(self.maneuverability * self.protection)
	
	def reportDamage(self,damage):
		""" 
		When someone attack the Object  type defense, this method update the new attributes values

		@param damage : (string) contains the value that will be used for calculated update for the attributes
		
		@return : None
		"""
		defense = self.getDefense()
		if(defense <= damage):
			self.impenetrabilidade = 0
		if(defense > damage):
			recalculateddefense = self.getDefense() -  damage
			self.maneuverability = 1
			self.protection = recalculateddefense

	def getDetail(self):
		""" 
		Return a report for the user, about the object, what is the use, and attributes

		
		@return : (string) contains a report with the attributes of the object,like attack, defense, capacity of heal.
		"""
		return "\n#########################################################\n"+"\nItem of Defense, Name of item:"+self.getName()+"\nCapacity of defense:"+str(self.getDefense())+"\nCapacity of attack:0 \n Capacity of heal:0 \n"+"#########################################################\n"
		