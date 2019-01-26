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
		# With the two attributes is calculates the Capacity of attack on character
		self.impact = self.limitsValues(impact)

		self.speed = self.limitsValues(speed)	
	
		
	
	def limitsValues(self,value):

		""" 
		Limits the Values in range between 0 and 10
		
		@param value : (int) contains a number , to be limited
	
		@return : (int) between 0...10
		"""
		if(isinstance(value,int)):
			if(value < 0):
				return 0
			elif(value > 10):
				return 10
			else:
				return value
		else:
			print("Atencao Voce digitou algo diferente de um número inteiro."+str(value))
			return 0
			


	# Get the capacity of attack of the object
	def getAttack(self):
		""" 
		Simple return the number who represent the attack of the object
		
		@return : (int)Number who represent the attack
		"""
		
		return (self.impact * self.speed)
	
	# Get the report of what type of item it is, and what is the capacity
	def getDetail(self):
		""" 
		Return a report for the user, about the object, what is the use, and attributes

		
		@return : (string) contains a report with the attributes of the object,like attack, defense, capacity of heal.
		"""
		return "\n#########################################################\n"+"\nItem of Attack, Name of item:"+self.getName()+"\nCapacity of attack:"+str(self.getAttack())+"\nCapacity de defense:0 \n Capacity of heal:0 \n"+"#########################################################\n"		