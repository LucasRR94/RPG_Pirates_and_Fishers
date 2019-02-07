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


	def treatedInputtoInt(self,enter):
		""" 
			it's treat the enters , to make shure that are number's
			

			@param enter : (string) 
			
			@return a: integer.
		"""
		try:
			a = int(enter) # try convert to integer
		except ValueError:
			print("it's not a integer, seted for default value")
			a = 0
		else:
			a = enter
		finally:
			return a


	def treatedNumberForStandardEnter(self,enter):
		""" 
			it's treat the number , to make shure that are between 0 and 10
			

			@param enter : (int) should bee a integer
			
			@return a: integer, standard
		"""
		try:
			if (enter>10 or enter <0):
				raise Exception("It's number bigger then 10 our less then 0")
		except Exception:
			a = 0
		else:
			a = enter
		finally:
			return a

	def limitsValues(self,value):
		""" 
		Limits the Values in range between 0 and 10
		
		@param value : (int)value contains a number , to be limited
	
		@return : (int) between 0...10
		"""
		return(self.treatedNumberForStandardEnter(int(self.treatedInputtoInt(value))))

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

