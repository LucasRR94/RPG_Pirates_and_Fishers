#!/usr/bin/python3
# -*- coding: utf-8 -*-

from libGamePiratesAndFishers import assertIfIsWeelFormat,makeSureThatIsnumberLimited

class Individual(object):
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
		self.name = assertIfIsWeelFormat(name)
		self.health = makeSureThatIsnumberLimited(health,100) 
		self.attack = makeSureThatIsnumberLimited(attack,100)
		self.defense = makeSureThatIsnumberLimited(defense,100)

	def __del__(self):
		""" 
		it's  destructor from the class, cleaning all the attributes
		

		@param none : 
		

		@return : None
		"""
		self.name = ''
		self.health = None
		self.attack = None
		self.defense = None

	def getName(self):
		"""
		it's return an attribute of the class call Name, that represent the name of the individual in game

		@param none:

		@return : (string) return a attribute name of the object
		"""
		return self.name


	def getHealth(self):
		"""
		it's return an attribute of the class that represent the health of the individual in the game

		@param none:

		@return : (int) return a attribute that is the health, between 0 ... 100
		"""

		return self.health

	def getDefense(self):	
		"""
		it's return an attribute of the class that represent the defense of the individual in the game

		@param none:

		@return : (int) return a attribute that is the defense, between 0 ... 100
		"""
		return self.defense

	def getAttack(self,attack):
		"""
		it's return an attribute of the class that represent the attack of the individual in the game

		@param none:

		@return : (int) return a attribute that is the attack, between 0 ... 100
		"""
		return self.attack	

	def __setAttack(self,attack):
		"""
		it's seting an attribute of the class, the attribute named attack

		@param attack:(int)  a integer between 0..100, that will be sum in the attribute

		@return None : 
		"""
		self.attack = attack


	def __setDefense(self,defense):
		"""
		it's seting an attribute of the class, the attribute named defense

		@param defense:(int)  a integer between 0..100, that will be sum in the attribute

		@return None : 
		"""
		self.defense = defense

	def __setHealth(self,health):
		"""
		it's seting an attribute of the class, the attribute named health

		@param health:(int)  a integer between 0..100, that will replace the attribute

		@return None : 
		"""
		if(health == 0):
			self.__del__()
		else:
			self.health = health

	def _changeAttackOrDefense(self,newvalue,option):
		"""
		it's change the attribute attack or defense by other number, when the player want exchange the weapon
		or the defense
		when option is : 1 --> attack
					   : 2 --> defense

		@param newvalue:(int)  a integer between 0..100, that will replace the attribute

		@return oldavalue :(int or tuple) integer that represent the old capacity of attack or defense,
		or None plus a message of error
		"""
		answer = None
		if(type(newvalue) is int):
			newnumb = newvalue
			if(newnumb > 100):
					newnumb = 100

			if(newnumb < 0):
				newnumb = 0

			if((type(option) is int)):
				
				if(option >=1 and option <= 2):
					
					if(option == 1):
						answer = self.getAttack()
						self.__setAttack(newnumb) # change the values
						return answer

					else:
						answer = self.getDefense()
						self.__setDefense(newnumb) # change the values
						return answer

				else:
					resptuple = (None,"error, this is not an supported option")
					answer = resptuple

			else:
				resptuple = (None,"error, this is not an supported option")
				answer = resptuple

		
		if(type(newvalue) is str): # try to make conversion between str -> int
			try:
				newnumb = int(newvalue)
			except ValueError:
				resptuple = (None,"error, this is not an supported type")
				answer = resptuple
			else:
				
				if(newnumb > 100):
					newnumb = 100

				if(newnumb < 0):
					newnumb = 0

				if((type(option) is int)):
				
					if(option >=1 and option <= 2):
						
						if(option == 1):
							answer = self.getAttack()
							self.__setAttack(newnumb) # change the values
							return answer

						else:
							answer = self.getDefense()
							self.__setDefense(newnumb) # change the values
							return answer

					else:
						resptuple = (None,"error, this is not an supported option")
						answer = resptuple

				else:
					resptuple = (None,"error, this is not an supported option")
					answer = resptuple


			finally:
				return answer
		
		else:
			resptuple = (None,"error, this is not an supported type")
			return resptuple


	def usingMedkit(self, valuehealth):
		"""
		it's adding one medkit in health.If the health is on max, it's discarded, and maintaining health in 100

		@param valuehealth:(int)  a integer between 0..100, that will added in health attribute

		@return (int): return 1 , when sucessfull use, 0 when it's not possible the use of medkit
		"""
		if(type(valuehealth) is int):
			newnumb = valuehealth

			if(newnumb > 100):
				newnumb = 100

			if(newnumb < 0):
				newnumb = 0
			
			backuphealth = self.getHealth()
			updatevalue = newnumb + backuphealth
			if(updatevalue>=100):
				self.__setHealth(100)
				return 1
			else:
				self.__setHealth(newvalue)
				return 1

		if(type(valuehealth) is str):
			try:
				newnumb = int(valuehealth)
			except ValueError:
				answer = 0
			else:
				if(newnumb > 100):
					newnumb = 100

				if(newnumb < 0):
					newnumb = 0
				backuphealth = self.getHealth()
				updatevalue = newnumb + backuphealth
				if(updatevalue>=100):
					self.__setHealth(100)
					answer = 1
				else:
					self.__setHealth(newvalue)
					answer = 1

			finally:
				return answer
		else:
			return 0

			
	def changeAttack(self,newAttack):
		"""
		it's change the attribute attack,calling the methodchangeAttackOrDefense with the appropriated 
		parameters

		@param newattack:(int)  a integer between 0..100, that will replace the attribute

		@return oldavalue :(int or tuple) integer that represent the old capacity of attack,
		or None plus a message of error
		"""
		return _changeAttackOrDefense(newAttack,1)	
	
	def changeDefense(self,newDefense):
		"""
		it's change the attribute defense,calling the methodchangeAttackOrDefense with the appropriated 
		parameters

		@param newDefense:(int)  a integer between 0..100, that will replace the attribute

		@return oldavalue :(int or tuple) integer that represent the old capacity of defense,
		or None plus a message of error
		"""
		return _changeAttackOrDefense(newDefense,2)	
		

	def getDamage(self, valuehit):
		"""
		it's repass the hit's from enemy, that means check values of health and defense, 
		updating the values of this two attributes

		@param valuehit:(int)  a integer between 0..100, that represent the value of an attack that need to be passed to defense and health

		@return int: 1 is value hit was correcty repass , 0 if is not.
		"""
		if(type(valuehit) is int):
			newnumb = valuehit
			if(newnumb > 100):
				newnumb = 100

			if(newnumb < 0):
				newnumb = 0
			defenseBackup = self.getDefense()
			healthbackup = self.getHealth()
			defensevalue = valuehit - defenseBackup
			if(defensevalue > 0): # no more defense
				if(defensevalue> self.getHealth()):
					self.__del()
					return 1
				else:
					self.__setDefense(0)
					newvaluehealth = healthbackup - defensevalue
					self.__setHealth(newvaluehealth)
					return 1 
			else:
				newvaluedefense = defensevalue * -1
				self.__setDefense(newvaluedefense)


		if(type(valuehit) is str):
			try:
				newnumb = int(valuehit)
			except ValueError:
				answer = 0
			else:
				newnumb = valuehit
				if(newnumb > 100):
					newnumb = 100

				if(newnumb < 0):
					newnumb = 0
				defenseBackup = self.getDefense()
				healthbackup = self.getHealth()
				defensevalue = valuehit - defenseBackup
				if(defensevalue > 0): # no more defense
					if(defensevalue> self.getHealth()):
						self.__del()
						return 1
					else:
						self.__setDefense(0)
						newvaluehealth = healthbackup - defensevalue
						self.__setHealth(newvaluehealth)
						return 1 
				else:
					newvaluedefense = defensevalue * -1
					self.__setDefense(newvaluedefense)


		else:
			return 0	


	def getDetail(self):
		"""
		it's getting the attributes of the class, providing a report of the object

		@param None:

		@return (string) : getting an report of the attributes of the object

		"""

		resposta += "\n #########################################################\n "+"Name of individual :" + self.getName() + "\n Health of individual:" + str(self.getHealth())+"\nAttack of individual:"+str(self.getAttack())+"\nDefense of individual:"+str(self.getDefense())+"\n#########################################################\n"