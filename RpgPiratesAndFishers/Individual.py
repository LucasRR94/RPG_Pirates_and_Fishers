#!/usr/bin/python3

class Individual(Object):
	"""
		This class Define object type Individual, it is a base for object used for being the base 
		of fishers, and is used for enemies in application.
	"""

	def __init__(self,name,health,attack,defense):
		""" 
		Initializing the class Individual, it's the constructor, assigned 
		the name and three attributes used for create fishers and enemies.
		
		

		@param name : (string) constains the name of Individual
		@param health : (int) attribute for the class represent the health of the individual, 0..100
		@param attack : (int) attribute for the class represent the attack of the individual, 0...100
		@param defense : (int) attribute for the class represent the defense of the individual,0...100


		@return : None
		"""
		self.name = name
		self.health = health
		self.attack = attack
		self.defense = defense


	