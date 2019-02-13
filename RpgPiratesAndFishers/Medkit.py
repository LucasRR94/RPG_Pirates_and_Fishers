#!/usr/bin/python3
# -*- coding: utf-8 -*-
from Item import Item
class Medkit(Item):
	"""
		This class Defines object type Medkit, it is a base for object used for Medkit in the application
	"""

	def __init__(self,name,healing):
		""" 
		Initializing the class Medkit, it's the constructor, assigned 
		the name and one attribute used for calculates the capacity of healing
		of the object
		limit value in 100, that is a value could be add in case the player desire to recover health.

		
		
		@param name : (string) constains the name of healing object
		@param healing : (int) attribute for the class represent the healing capacity of the object
		
		@return : None
		"""
		super().__init__(name)

		#self.healing = super().limitsValuesMedkit(healing) # value is between 0 ... 100
		self.healing = self.__limitsValuesMedkit(healing) # value is between 0 ... 100
	
	def __del__(self):
		""" 
		it's destroy the object.
		
		@param  : None
		@return : None

		"""
		self.name = ''
		self.healing = 0		
	
	def __treatedInputtoIntMedkit(self,enter):
		""" 
			it's treat the enters , to make shure that are number's
			

			@param enter : (string) 
			
			@return a: integer.
		"""
		try:
			a = int(enter) # try convert to integer
		except (ValueError,TypeError) as e:
			print("it's not a integer, seted for default value")
			a = 0
		else:
			a = enter
		finally:
			return a

	
	def __treatedNumberForStandardEnterMedkit(self,enter):
		""" 
			it's treat the number , to make shure that are between 0 and 100
			

			@param enter : (int) should bee a integer
			
			@return a: integer, standard
		"""
		try:
			if (enter > 100 or enter < 0):
				raise Exception("It's number bigger then 10 our less then 0")
		except Exception:
			a = 0
		else:
			a = enter
		finally:
			return a


	def __limitsValuesMedkit(self,value):
		""" 
		Limits the Values in range between 0 and 100
		
		@param value : (int)value contains a number , to be limited
	
		@return : (int) between 0...100
		"""
		return(self.__treatedNumberForStandardEnterMedkit(int(self.__treatedInputtoIntMedkit(value))))


	def getHealing(self):
		"""
		Simple return the number who represent the Healing capacity of the object

		@return : (int) Number who represent the healing capacity of the object
		"""
		return(self.healing)


	def useHealing(self):
		"""
		Consume the attributes, and destroy's the object

		@return : (int) Number who represent the healing capacity of the object
		"""
		backup = self.getHealing()
		self.__del__()
		return backup

	def getDetail(self):
		"""
		Return a report for the user, about the object, what is the use, and attributes

		
		@return : (string) contains a report with the attributes of the object,like attack, defense, capacity of heal.
		
		"""
		return (super().setParameters(0,0,self.getHealing()))
		
		#return "\n#########################################################\n"+"\nItem Medical Kit, Name of item:"+self.getNome()+"\nCapacidade of healing of Item:"+str(self.getHealing())+"\nCapacidade of Attack:0, Capacidade of defense:0\n"+"#########################################################\n"	
		
