#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Fisher import *
import random
import hashlib
from Item import Item
from Spell import Spell
from Individual import Individual
from Weapon import Weapon
from Defense import Defense
from Medkit import Medkit
from Island import Island
from libGamePiratesAndFishers import assertFormat


def accepttypeWeapon(objectWeapon):
	'''
	this function assert if the objectWeapon is of the type Weapon
	
	@param objectWeapon : (unknown) an object that don't have type defined

	@return  : (int) 0 if is not of type Weapon, 1 if is type Weapon

	'''
	if(type(objectWeapon) is Weapon):
		return 1
	else:
		return 0

def accepttypeDefense(objectDefense):
	'''
	this function assert if the objectdefense is of the type Defense
	
	@param objectdefense : (unknown) an object that don't have type defined

	@return  : (int) 0 if is not of type Defense, 1 if is type Defense

	'''
	if(type(objectDefense) is Defense):
		return 1
	else:
		return 0

def accepttypeIsland(objectisland):
	'''
	this function assert if the objectisland is of the type Island
	
	@param objectisland : (unknown) an object that don't have type defined

	@return  : (int) 0 if is not of type Island, 1 if is type Island

	'''
	if(type(objectisland) is Island):
		return 1
	else:
		return 0

def accepttypeHash256(objectIdplayer):
	'''
	this function assert if the objectIdplayer is of the type str with size of 64 characters
	
	@param objectIdplayer : (unknown) an object that don't have type defined

	@return  : (int) 0 if is not of type Island, 1 if is type Island
	'''
	if((type(objectIdplayer) is str)):
		if(len(objectIdplayer) == 64):
			return 1
		else:
			return 0
	else:
		return 0

def test_ParametersofFisher(fisherobj,objattack,objdefense,objisland,objectidplayer,CaseStudy):
	resultobjweapon = accepttypeWeapon(objattack)
	resultobjdefense = accepttypeDefense(objdefense)
	resultobjisland = accepttypeIsland(objisland)
	resultidplayerhash  = accepttypeHash256(objectidplayer)
	
	if(resultobjweapon == 1):
		try:
			assert(fisherobj.getWeapon() == objattack)
		except AssertionError:
			print("\033[91mError, the object Weapon don't was insert correcly,Case Study:",CaseStudy)
			exit()
	
	if(resultobjweapon == 0):
		try:
			assert(fisherobj.getWeapon() == None)
		except AssertionError:
			print("\033[91mError,Was inserted an object type weapon incorrecly, Case Study: ", CaseStudy)
			exit()
	
	if(resultobjdefense == 1):
		try:
			assert(fisherobj.getDefense() == objdefense)
		except AssertionError:
			print("\033[91mError, the object Defense don't was insert correcly,Case Study:",CaseStudy)
			exit()
	
	if(resultobjdefense == 0):
		try:
			assert(fisherobj.getDefense() == None)
		except AssertionError:
			print("\033[91mError,Was inserted an object type Defense incorrecly, Case Study: ", CaseStudy)
			exit()
	
	if(resultobjisland == 1):
		try:
			assert(fisherobj.getactualIsland() == objisland)
		except AssertionError:
			print("\033[91mError, the object Island don't was insert correcly,Case Study:",CaseStudy)
			exit()
	
	if(resultobjisland == 0):
		try:
			assert(fisherobj.getactualIsland() == None)
		except AssertionError:
			print("\033[91mError,Was inserted an object type Island incorrecly, Case Study: ", CaseStudy)
			exit()
	
	if(resultidplayerhash == 1):
		try:
			assert(fisherobj.getIdplayer() == objectidplayer)
		except AssertionError:
			print("\033[91mError, the object Hash sha256 don't was insert correcly,Case Study:",CaseStudy)
			exit()
	
	if(resultidplayerhash == 0):
		try:
			assert(type(fisherobj.getIdplayer()) == str and len(fisherobj.getIdplayer()) == 64)
		except AssertionError:
			print("\033[91mError,Was inserted an object type Hash sha256 incorrecly, Case Study: ", CaseStudy)
			exit()
	
	if(True):
		print("\033[92mTest was sucessfull, case Study: "+str(CaseStudy))		

def checkUseItem(fisherobj,itemusing,refereitem,caseStudy):
	'''
	Assert that item was used, immediately stopping in case of error
	Assert the integrity of the backpack 
	Assert the Attack,Defense and Health
	@param fisherobj:(Fisher) Obj of type fisher
	@param itemusing:(Str) string that represent an reference to an item
	@param refereitem:(Item) obj type item that will be used
	@param caseStudy:(Int) int number, that represent the study case
	@return : (list of str) object that should be on the backpack
	'''
	if(isinstance(refereitem,Item)):
		if(type(refereitem) is Medkit): # if is is necessary diminish the health of the character's to observe the effect of Medkit
			actualhealth   = fisherobj.getHealth()
			efectsfromItem = refereitem.getHealing()
			summoffactors = actualhealth + efectsfromItem
			finalsummm= summoffactors
			if(summoffactors > 100):
				fisherobj.health = 1
				finalsummm = 1+efectsfromItem

			# verify if the item will be used correcly
			try:
				assert(fisherobj.useItemBackpack(itemusing)==1)
			except AssertionError:
				print("Error, medkit was not summed, case Study:\n",caseStudy)
				exit()
			else:		
				try:
				#	print(fisherobj.health,sumcalculated)
				#	exit()
					assert(fisherobj.health == finalsummm)
				except AssertionError:
					print("Error, the medkit was not summed, case Study:\n",caseStudy)
					exit()
				else:
					try:
						assert(fisherobj.backpack.index(refereitem)==-1)
					except AssertionError:
						print("Error, the item keep on the backpack,case Study\n",caseStudy)
						exit()
					except ValueError:
						print("Test sucessfull, case Study: \n",caseStudy)
						return 1

		else: # just observe pratical efects as placing another  weapon of defense on the fisher	
			if(type(refereitem) is Weapon):
				actualweapon = fisherobj.getWeapon()
				if(actualweapon != None):
					try:
						assert(fisherobj.useItemBackpack(itemusing) == 1)
					except AssertionError:
						print("Error, was not insert correcly the new weapon,case Study:",caseStudy)
						exit()
					else:
						try:
							assert(fisherobj.itemattack == refereitem and fisherobj.backpack.index(actualweapon)>-1 and fisherobj.backpack.index(refereitem)==-1)
						except AssertionError:
							print("Error, not found new weapon added, or not insert on back the previous weapon, Case Study:",CaseStudy)
							exit()
						except ValueError:
							print("Test sucessfull, case study :\n", caseStudy)	
							return 1
						else:
							print("Test sucessfull, case study :\n", caseStudy)	
							return 1	

				if(actualweapon == None):
					try:
						assert(fisherobj.useItemBackpack(itemusing)==1)
					except AssertionError:
						print("Error the new weapon, don't was insert correcly, case of study:\n",caseStudy)
						exit()
					else:
						try:
							assert(fisherobj.itemattack == refereitem)
						except AssertionError:
							print("Error, the item not was insert correcly, case study:\n",caseStudy)
							exit()
						else:
							try:
								assert(fisherobj.backpack.index(refereitem)>=0)
							except (AssertionError,ValueError) as e :
								print("Test sucessfull, case study:\n",caseStudy)
								return 1
							else:
								print("Error, the item continue on the back pack, case study:\n",caseStudy)
								exit()

			if(type(refereitem) is Defense):	
				actualdefense = fisherobj.getDefense()
				if(actualdefense != None):
					try:
					#	print(fisherobj.useItemBackpack(itemusing))
					#	exit()
						assert(fisherobj.useItemBackpack(itemusing) == 1)
					except AssertionError:
						print("Error, was not insert correcly the new defense,case Study:",caseStudy)
						exit()
					else:
						try:
							assert(fisherobj.itemdefense == refereitem and fisherobj.backpack.index(actualdefense)>-1 and fisherobj.backpack.index(refereitem)==-1)
						except AssertionError:
							print("Error, not found new defense added, or not insert on back the previous defense, Case Study:",CaseStudy)
							exit()
						except ValueError:
							print("Test sucessfull, case study :\n", caseStudy)	
							return 1
						else:
							print("Test sucessfull, case study :\n", caseStudy)	
							return 1	

				if(actualdefense == None):
					try:
						assert(fisherobj.useItemBackpack(itemusing)==1)
					except AssertionError:
						print("Error the new defense, don't was insert correcly, case of study:\n",caseStudy)
						exit()
					else:
						try:
							assert(fisherobj.itemdefense == refereitem)
						except AssertionError:
							print("Error, the item defense not was insert correcly, case study:\n",caseStudy)
							exit()
						else:
							try:
								assert(fisherobj.backpack.index(refereitem)>=0)
							except (AssertionError,ValueError) as e :
								print("Test sucessfull, case study:\n",caseStudy)
								return 1
							else:
								print("Error, the item defense continue on the back pack, case study:\n",caseStudy)
								exit()
			else:
				print("Happened an error, case study:",caseStudy)
				exit()					

	else: # check if he is not avaliable

		try:
			assert(fisherobj.backpack.index(refereitem)>=0)
		
		except ValueError:
			print("Test sucessfull, case study:", caseStudy)
			
		else:
			print("Error, object of unknown type is present list of back pack, study case:\n", caseStudy)	
			exit()	

def checkaddItem(fisherobj,iteminsert,caseStudy):
	'''
	Assert that item was insert, immediately stopping in case of error
	@param fisherobj:(Fisher) Obj of type fisher
	@param iteminsert:(Item) Obj of type Item that will be insert on fisher backpack
	@param caseStudy:(int) the case of study that is study
	@return :None
	'''
	try:
		assert(fisherobj.backpack.index(iteminsert))
	except ValueError:
		
		if(type(iteminsert)!=Item):
			try:
				assert(fisherobj.addItemBackpack(iteminsert)==1)
			except AssertionError:
				print("Error, not be inserted on de backpack, case study:\n",caseStudy)
				exit()
			else:
				try:
					assert(fisherobj.backpack.index(iteminsert)>=0)
				except (AssertionError,ValueError) as e:
					print("Error, instability on backpack, object not found, case study:\n",CaseStudy)
					exit()
				else:
					print("Test sucessfull, case study:\n",caseStudy)
		
		if(type(iteminsert)==Item):
			try:
				assert(fisherobj.addItemBackpack(iteminsert)==0)
			except AssertionError:
				print("Error, an object that is not an item was insert incorrecly, case Study:\n",CaseStudy)	
				exit()
			else:
				print("Test sucessfull, case study:\n",caseStudy)
	else:
		print("Error the element was previous on the backpack, case study: \n"+str(caseStudy))
		exit()

def gerandoItem(numb):
	'''
	Return a number of items and their names, that was generated
	@param numb:(int) is an int that informs how much elements has to be generated
	@return :(list) return an list composed by all the [objects, names of objects]
	'''
	items = []
	names = []
	resp = [items,names]
	for i in range(numb):
		whatitemis = random.randint(1,3)
		if(whatitemis == 1): # created med kit whatitemis = 1
			genname = "Medkit"+str(i)
			genparam1 = random.randint(0,95)
			names.append(genname)
			genmedkit = Medkit(genname,genparam1)
			items.append(genmedkit)

		if(whatitemis == 2): # created Weapon  whatitemis = 2
			genname = "Weapon"+str(i)
			genparam1 = random.randint(0,10)
			genparam2 = random.randint(0,10)
			names.append(genname)
			genweapon = Weapon(genname,genparam1,genparam2)
			items.append(genweapon)

		if(whatitemis == 3): # created Defense whatitemis = 3
			genname = "Defense"+str(i)
			genparam1 = random.randint(0,10)
			genparam2 = random.randint(0,10)
			names.append(genname)
			gendefense = Defense(genname,genparam1,genparam2)
			items.append(gendefense)
	
	return resp

def test_colectandlisItemsIsland(objFisher,itempassed,caseStudy):
	"""
	This function test if the item passed to the island could be collected on the fisher
	@param objFisher : (Fisher) object type fish
	@param itempassed : (Item) is an item passed to the island that can be colected through the fisher
	@param caseStudy : (int) simple numb that represent the actual example
	@return:(None)
	"""
	vectorwithallitems = objFisher.listItemsfromIsland()
	
	try:
		assert(vectorwithallitems[0].find(itempassed.getName())>=0)
	except AssertionError:
		print("Error, item it is not on the island, case study:",caseStudy)
		exit()
	else:
		try:
			objFisher.collectItem(itempassed.getName())
			newvector = objFisher.listItemBackpack()
			assert(newvector[caseStudy].find(itempassed.getName())>0)
		except AssertionError:
			print("Error, the item was not currectly passed by Fisher,case study:",caseStudy)
			exit()
		else:
			print("Test sucessfull, case Study:",caseStudy)

def testingAddListUseItem(numb):
	'''
	This function test if the a "numb" of items that was generated	, can be 
	inserted and other numb2 was correctly used, and the Attack,	Defense,
	Health and backpack keep with integrity
	@param numb:(int) number of items that should be created
	'''
	simpleIsland = Island("Isla bonita")
	hashsimple = hashlib.sha256()
	simplekey = bytes("!_!","latin-1")
	hashsimple.update(simplekey)
	keygen = hashsimple.hexdigest()
	simplefisher = Fisher("simple fisher",100,None,None,simpleIsland,keygen)
	vector = gerandoItem(numb)
	vectorofitems = vector[0]
	vectornameitems = vector[1]
	for i in range(numb):
		checkaddItem(simplefisher,vectorofitems[i],i)
	print("\n\033[92m##### Use test####\n")	
	for j in range(numb):
		checkUseItem(simplefisher,vectornameitems[j],vectorofitems[j],j)

def testDropItems(objFisher,listOfItems,caseStudy):
	"""
	This method test the DropItems method
	he received a list of items that be inserted and check if the return of the function is correct
	@param listOfItems : (array) is an array contains all the Items inserted on the Fisher
	@param caseStudy: (int) is a reference of the test that is be running
	@return :(None)
	"""
	returnOfDrop = objFisher.dropItems()
	try:
		assert(returnOfDrop == listOfItems and objFisher.backpack == None)
	except AssertionError:
		print("Error, the backpack have  something, or don't have all the items required, case Study:",caseStudy)
		exit()
	else:
		print("sucessfull test, case study:",caseStudy)	

def test_ColectGetInfoDropSpells(objFisher, spellinserted,studyCase):
	"""
	This function test three methods, the collectSpells,the getinfoaboutSpellonIsland, and the dropSpells
	@param objFisher :(Fisher) an object type Fisher , that have a island avaliable as actual position
	@param spellinserted:(Spell) that is inserted on the island, that is the actual position of the player
	@param studyCase : (int) integer that inform the actual study of case
	"""
	try:
		assert(objFisher.getinfoaboutSpellonIsland()==1)
	except AssertionError:
		print("Error,The method do not show the spell avaliable, case Study:",studyCase)
		exit()
	else:
		try:
			assert(objFisher.collectSpell()==1)
		except AssertionError:
			print("Error,do not was possible collect the spell from Island, case study:",studyCase)
			exit()
		else:
			try:
				spellcolect = objFisher.dropSpells()
				assert(spellcolect.index(spellinserted)>=0 and objFisher.spellcontainer == None)
			except:
				print("Error, dropping the spells contained, case Study:",studyCase)
				exit()
			else:
				print("test sucessfull, case study:",studyCase)				


def test_getvalueSpells(objFisher,sumprojected,studyCase):
	"""
	his function test the method getValueSpells that make accounting of the speels collected, he work	
	with other function and always move to the right, was described on the function that map the islands.
	@param objFisher : (Fisher) object of type Fisher
	@param sumprojected:(int) integer that represent the total of the values of all the spells collected
	@param studyCase : (integer) informed what the number of the case study
	@return :(None)
	"""
	condition = 0
	totalsum = 0
	while(condition == 0):
		if(objFisher.getinfoaboutSpellonIsland()==1):
			objFisher.collectSpell()
			resp = objFisher.getDirectionsfromIsland()
			if(resp== None): # if is two None , None is not have other (direction)
				condition = 1
			else:
				objFisher.changeIsland("right")
		else:
			resp = objFisher.getDirectionsfromIsland()
			if(resp== None): # if is two None , None is not have other (direction)
				condition = 1
			else:
				objFisher.changeIsland("right")

			
	totalsum = objFisher.getvalueSpell()
	try:
		assert(sumprojected == totalsum)
	except AssertionError:
		print(sumprojected,totalsum)
		print("Error , in the sum of the spells in the Fisher, case study: ",studyCase)
		exit()
		return 0
	else:
		print("Test sucessfull, case study: ",studyCase)
		return 0
		
def createRandomSpell():
	"""
	This function create a random object type Spell
	@param None:
	@return :(Spell) returns an Object type spell
	"""
	valuespell = random.randint(0,100)
	randomname = "Spell" + str(random.randint(-10000,10000))
	newspell = Spell(randomname,valuespell)
	return newspell

def createIslandAndLinkedThem(numbOfIslands):
	"""
	this function create a number of islands :numbOf Islands	
	And link all them on right direction
	@param numbOfIslands:(int) number of islands that is generated
	@return :(island) the first island(the head) of the list
	"""
	if(numbOfIslands > 0):

		first = None
		actual = None
		nextisland = None 
		for i in range(numbOfIslands):
			if(i==0):
				nameisland = "genericIsland" + str(i)+" "
				genericIsland = Island(nameisland)
				first = genericIsland
				actual = first
				nextisland = None
			else:	
				genericIsland = None
				nameisland = "genericIsland" + str(i)+" "
				genericIsland = Island(nameisland)
				nextisland = genericIsland
				actual.adddirection(nextisland,"right")
				actual = nextisland
				nextisland = None

		return(first)
	else:
		return None

def insertedSpellsOnIslandsLink(firstIsland,numbOfIslandslink):
	"""
	this function takes a list of Islands  , and add one Spell each island
	@param firstIslands : (Island) is the head of the list
	@param numbOfIslandslink:(int) is a number of islands that is present on the list
	@return :(list) list contains the total sum of value spells and the list of islands created
 	"""
	actual = firstIsland
	nextisland = None
	totalsum = 0
	for i in range(numbOfIslandslink):
		if(i<numbOfIslandslink-1):
			numb = random.randint(0,100)
			randomspell = Spell("random Spell"+str(i),numb)
			actual.addSpellIsland(randomspell)
			totalsum += numb
			nextisland = actual.getdirection("right")
			actual = nextisland
		else:
			numb = random.randint(0,100)
			randomspell = Spell("random Spell"+str(i),numb)
			actual.addSpellIsland(randomspell)
			totalsum += numb

	answer = [totalsum,firstIsland]	
	return 	answer

def test_ChangeIsland(objFisher,direction,islandCompare,caseStudy):
	"""
	This test uses a direction to move to other island and check if is the same islandCompare(Object)
	and test if the objFisher is in the new islandCompare
	@param objFisher :(Fisher) object Fisher that will be moved to other island
	@param direction :(string) string that is used to change the island
	@param islandCompare :(Island) object that is the destiny for the change of island
	@param caseStudy:(int) case of study of the test
	@return None
	"""
	try:
		objFisher.changeIsland(direction)
		actualIsland = objFisher.getactualIsland()
		assert(objFisher.getactualIsland() == islandCompare and actualIsland.individualsPresent.index(objFisher) >= 0)
	
	except AssertionError:
		print("Error, the island was not found, the direction is wrong, case Study:",caseStudy)
	
	else:
		print("test sucessfull,case study",caseStudy)


def test_getDirectionfromIsland(objFisher,arrayDirections,caseStudy):
	"""
	This test uses a arrayDirections(string) that contains all the directions inserted on the actual position 
	of objFisher, if that array could be found on the directions, the test is sucessfull
	@param objFisher:(Fisher) a object type Fisher that will be tested
	@param arrayDirections:(Array) a array that contains strings that will be tested, if they are in the directions listadas da ilha
	@param caseStudy:(int) case of study of the test
	@return None
	"""
	answer = objFisher.getDirectionsfromIsland()	
	if(answer == None and arrayDirections != None):
		if(len(arrayDirections)==0):
			print("Test sucessfull, Case study:",caseStudy)
		else:	
			print("Error was not inserted the directions, case study:",caseStudy)
			exit()
	else:
		sizeofanswer = len(answer)
		sizeofarray  = len(arrayDirections)
		if(sizeofanswer == sizeofarray):
			vectresp = []
			error = 0
			if(sizeofanswer != 0):
				for i in range(sizeofanswer):
					error = 0
					for j in range(sizeofanswer):
						try:
							assert(arrayDirections[i] == answer[j]) 
						except:
							error +=1
						else:
							error = -1000
					try:
						assert(error < 0)
					except:
						print("Error, direction don't was inserted, case study", caseStudy)
						exit()	

				print("Test sucessfull, Case study:",caseStudy)

				#print("Test sucessfull",caseStudy)

			else:
				print("Test sucessfull",caseStudy)			
		else:
			print("Error was not inserted the directions, case study:",caseStudy)
			exit()	

def test_listenemies(objFisher,arrayenemies,caseStudy):
	"""
	this test uses an array (arrayenemies) of strings and comparing with the method ,if
	all the enemies inserted are show in the method, test sucessfull, otherwise fail
	@param objFisher: (Fisher) that will be used to give a list that will be compared with the array
	@param arrayenemies: (array string) array that will be used for comparison 
	@param caseStudy:(int) case of study of the test
	@return None
	"""
	listofenemies = objFisher.listenemies()
	if(listofenemies == None):
		if(arrayenemies == list):
			if(len(arrayenemies) == 0):
				print("Test sucessfull, case study:",caseStudy)
			else:
				print("Error, the enemies was not inserted correcly, case Study:",caseStudy)
				exit()
		else:
			print("Test sucessfull, case study:",caseStudy)	
	else:
		sizeofenemies = len(listofenemies)
		sizeofarrayenemies = len(arrayenemies)
		cont = 0
		if(sizeofarrayenemies == sizeofenemies):
			for i in range(sizeofenemies):
				condition = 0
				j=0
				while(condition==0):
					if(j<=sizeofarrayenemies-1):
						condition+=1

					if(listofenemies[i] == arrayenemies[j].getDetail()):
						condition+=1
						cont+=1
						arrayenemies.pop(j)
						backup = sizeofarrayenemies
						sizeofarrayenemies = backup -1

					
					j+=1

			if(sizeofenemies == cont):
				print("Test sucessfull, case Study: ",caseStudy)		
			else:
				print("Error, elements or element not found, case study: ",caseStudy)
				exit()
		else:
			print("Error, elements not found in vector, case study: ",caseStudy)
			exit()		


def test_attackEnemy(objFisher,enemy,caseStudy):
	"""
	this test uses an object Fisher(enemy) for testing the method attackEnemy, and 
	measure the effects of the attack on the enemy, and if the items and spells was inserted.
	@param objFisher:(Fisher) the attacker, that will be measure  
	@param enemy:(enemy) that will be attack.
	@param caseStudy:(caseStudy) case of study
	@return None
	"""
	
	if(type(enemy)==Individual):
		islandactual = objFisher.getactualIsland()

		lifeIndividual = enemy.getHealth() 
		defenseIndividual = enemy.getValueDefense()
		Individualattack = enemy.getValueAttack()

		attackerCapacity = objFisher.getValueAttack()
		attackerDefense = objFisher.getValueDefense()
		attackerlife  = objFisher.getHealth()
		attackerItems = len(objFisher.backpack)
		attackerSpells = len(objFisher.spellcontainer)

		result = objFisher.attackEnemy(enemy.getName())

		if((lifeIndividual + defenseIndividual)<= attackerCapacity and result == 1):
			try: # if the object enemy was eliminated
				assert(islandactual.individualsPresent.index(enemy)==0)
			except ValueError:
				
				if(Individualattack >= (attackerDefense + attackerlife) ):
					try:	
						assert(islandactual.individualsPresent.index(objFisher)==0)
					except ValueError:
						print("teste sucessfull, case study:",caseStudy)
					except AssertionError:
						print("Error, the player has died , but not be eliminated, case study:", caseStudy)	
						exit()
				
				elif(Individualattack < (attackerDefense + attackerlife)):
					
					if(attackerDefense <= Individualattack):
						try:
							assert(objFisher.getValueDefense() == 0 and objFisher.getHealth() == (attackerlife + attackerDefense - Individualattack) and attackerSpells == len(objFisher.spellcontainer) and attackerCapacity == objFisher.getValueAttack() and attackerItems == len(objFisher.backpack))
						except AssertionError:
							print("Error, value of defense or health was not update after attack",caseStudy)	
							exit()
						else:
							print("test sucessfull, case study:",caseStudy)
					else:
						try:
							assert(attackerCapacity == objFisher.getValueAttack() and objFisher.getValueDefense() ==(attackerDefense - Individualattack) and objFisher.getHealth() == attackerlife and attackerItems == len(objFisher.backpack) and attackerSpells == len(objFisher.spellcontainer) )
						except AssertionError:
							print("Error, values after attack, was update incorrecly, case Study:",caseStudy)
						else:
							print("test sucessfull, case study:",caseStudy)			
			except AssertionError:
				print("Error, the object don't was eliminated, case study:",caseStudy)
				exit()
		
		elif((lifeIndividual + defenseIndividual) > attackerCapacity and result == 1):
			try: # if the object enemy was eliminated
				assert(islandactual.individualsPresent.index(enemy)>=0)
			except (AssertionError,ValueError) as e:
				print("Error, the object was eliminated incorrecly, case study:",caseStudy)
				exit()
			else:
				if(defenseIndividual > attackerCapacity):
					newlife = lifeIndividual
					newdefense = defenseIndividual - attackerCapacity

				if(defenseIndividual <= attackerCapacity):
					newdefense = 0
					newlife = lifeIndividual + defenseIndividual - (attackerCapacity)
					if(newlife <= 0):
						newlife = None
						Individualattack = None
						newdefense = None	
					
				try:
					assert(enemy.getHealth() == newlife and enemy.getValueDefense() == newdefense and enemy.getValueAttack() == Individualattack)
				except AssertionError:

					print("Error, the heath or attack of Individual was incorrecly sum, case study:", caseStudy)
					exit()
				else:
					if(Individualattack >= (attackerDefense + attackerlife) ):
						try:	
							assert(islandactual.individualsPresent.index(objFisher)>=0)
						except ValueError:
							print("Test sucessfull, case study:", caseStudy)
						else:
							print("Error, the player keep on island incorrecly, case study:", caseStudy)
							exit()
					if(Individualattack < (attackerDefense + attackerlife)):	
						
						if(Individualattack < attackerDefense):
							try:
								assert(objFisher.getHealth() == attackerlife and objFisher.getValueDefense() == (attackerDefense - Individualattack) and objFisher.getValueAttack() == attacker and attackerItems == len(objFisher.backpack) and  attackerSpells== len(objFisher.spellcontainer) )

							except AssertionError:
								print("Error, the values are wrong, the update of values in attack has fail, case study:",caseStudy)
								exit()
							else:
								print("Test sucessfull, case study:", caseStudy)
						else:
							try:
								assert(objFisher.getValueDefense() == 0  and objFisher.getHealth() == (attackerlife + attackerDefense-Individualattack) and objFisher.getValueAttack() == attackerCapacity and attackerItems == len(objFisher.backpack) and  attackerSpells== len(objFisher.spellcontainer))
							except AssertionError:
								print("Error, the Fisher was modify incorrecly, case study:",caseStudy)
								exit()
							else:
								print("Test sucessfull, case study:", caseStudy)		
		if(result == 0):
			try:
				assert(enemy.getHealth() == lifeIndividual and enemy.getValueAttack() == Individualattack and enemy.getValueDefense() == defenseIndividual and objFisher.getValueDefense()==attackerDefense and objFisher.getValueAttack()==attackerCapacity and  objFisher.getHealth() == attackerlife and attackerItems == len(objFisher.backpack) and attackerSpells == len(objFisher.spellcontainer))
			except AssertionError:
				print("Error, the object was modify without the wright properties, case study:", caseStudy)
			else:
				print("Attention, possible error, the object don't was modify, case study:",caseStudy)


	if(type(enemy)==Fisher):
		islandactual = objFisher.getactualIsland()

		lifeIndividual = enemy.getHealth()
		Individualattack = enemy.getValueAttack()
		Individualdefense = enemy.getValueDefense()
		IndividualItems = len(enemy.backpack)
		IndividualSpells = len(enemy.spellcontainer)

		attackerCapacity = objFisher.getValueAttack()
		attackerDefense = objFisher.getValueDefense()
		attackerlife   = objFisher.getHealth()
		attackerItems  = len(objFisher.backpack)
		attackerSpells = len(objFisher.spellcontainer)

		result = objFisher.attackEnemy(enemy.getName())
		
		if((lifeIndividual + Individualdefense) > attackerCapacity):
			
			if(Individualdefense >= attackerCapacity):
				newdefense = 0
				newlife = lifeIndividual + Individualdefense - attackerCapacity

			if(Individualdefense < attackerCapacity):
				newdefense = Individualdefense - attackerCapacity
				newlife = lifeIndividual

			try:
				assert(enemy.getHealth() == newlife and enemy.getValueAttack() == Individualattack and enemy.getValueDefense() == newdefense and  IndividualSpells == len(enemy.spellcontainer) and attackerItems  == len(objFisher.backpack)and objFisher.getValueDefense()==attackerDefense and objFisher.getValueAttack()==attackerCapacity and  objFisher.getHealth() == attackerlife and attackerItems == len(objFisher.backpack) and attackerSpells == len(objFisher.spellcontainer))
		
			except AssertionError:
				print("Error, in the sum of the attack, case study:", caseStudy)			
				exit()
			else:
				print("Test Sucessfull, case study:", caseStudy)

		else:
			
			try:
				assert(islandactual.individualsPresent.index(enemy)>=0)
			except ValueError:
				try:
					assert(objFisher.getValueDefense()==attackerDefense and objFisher.getValueAttack()==attackerCapacity and  objFisher.getHealth() == attackerlife and (attackerItems + IndividualItems) == len(objFisher.backpack) and (attackerSpells + IndividualSpells) == len(objFisher.spellcontainer))		
				except AssertionError:
					print("Error, the Attacker was modify incorrecly, case study:", caseStudy)
					exit()
				else:
					print("test Sucessfull, case study:",caseStudy)
			else:
				print("Error, enemy not was eliminated, case study:",caseStudy)
				exit()
	
	if(type(enemy)==None):
		result = objFisher.attackEnemy(enemy)
		if(result == 0):
			print("test sucessfull, case study:",caseStudy)
		else:
			print("Error, the attack was count when should not:",caseStudy)

def gen_Random_Fisher(objisland,numb):
	"""
	This function generate a random Object of type (Fisher)
	@param objisland :(Island) an object type island that the Fisher will be inserted
	@param numb : (integer) a number that will be insert with the str for making the name
	@return :(Fisher) an Object of type Fisher
	"""
	firsCriterion = random.randint(1,10)
	secondCriterion = random.randint(1,10)
	randomdefense  = Defense("gendefense",firsCriterion,secondCriterion)
	randomweapon  = Weapon("genweapon",firsCriterion,secondCriterion)
	
	hashsimple = hashlib.sha256()
	simplekey = bytes("Key","latin-1")
	hashsimple.update(simplekey)
	#keygen = hashsimple.hexdigest()
	keygendecide = random.randint(0,1)
	keygen = hashsimple.hexdigest()
	
	fisherobj = Fisher("simplefisher"+str(numb),firsCriterion,randomweapon,randomdefense,objisland,keygen)
	objisland.addIndividual(fisherobj)
	return fisherobj

def gen_Random_Individual(objisland,numb):
	"""
	This function generate a random Object of Type (Individual)
	@param Objisland:(Island) object type island that the individual will be inserted
	@param numb :(integer) a number that will be insert with the str for making the name
	@return :(Individual) an Object of type individual
	"""
	firsCriterion = random.randint(1,100)
	secondCriterion = random.randint(1,100)
	individualobj = Individual("Simple Individual"+str(numb),firsCriterion,secondCriterion,secondCriterion)
	objisland.addIndividual(individualobj)
	return individualobj

class voidclass(object):
	def __init__(self,para):
		self.parameter = para
	def getparameter(self):
		return self.parameter

if __name__ == "__main__":
	espadacurta  = Weapon("Espada Curta",100,100)
	cotademalha = Defense("Cota de Malha",100,100)
	island1 = Island("Island Bonita")
	hashsimple = hashlib.sha256()
	simplekey = bytes("Key","latin-1")
	hashsimple.update(simplekey)
	keygen = hashsimple.hexdigest()
	fisherobj = Fisher("simplefisher",100,espadacurta,cotademalha,island1,keygen)
	test_ParametersofFisher(fisherobj,espadacurta,cotademalha,island1,keygen,"Obj 1")
	#--------------#-----------#-----------#------------#
	#forcing strange objects like parameters
	novo = voidclass(1)
	randomlist = []
	randomlist.append("Log")
	randomlist2 = [1,2,15,4,5,6]
	fisherobj = Fisher(novo,novo,novo,novo,novo,novo)
	test_ParametersofFisher(fisherobj,novo,novo,novo,novo,"Forcing_Parameters 1")	
	fisherobj = Fisher(randomlist,randomlist,randomlist,randomlist,randomlist,randomlist)
	test_ParametersofFisher(fisherobj,randomlist,randomlist,randomlist,randomlist,"Forcing_Parameters 2")	
	fisherobj = Fisher(randomlist2,randomlist2,randomlist2,randomlist2,randomlist2,randomlist2)
	test_ParametersofFisher(fisherobj,randomlist2,randomlist2,randomlist2,randomlist2,"Forcing_Parameters 3")	
	# test insert parameters , right and wrong. exhaustion test
	for i in range(1000):
		weapondecide = random.randint(0,2)
		if(weapondecide==2):
			randomweapon  = Defense("genrandom",0,0)
		if(weapondecide==1):
			randomweapon  = Weapon("randomweapon",100,100)
		if(weapondecide==0):
			randomweapon  = None

		defensedecide = random.randint(0,2)
		if(defensedecide==2):
			randomdefense  = Weapon("genrandom",0,0)
		if(defensedecide==1):
			randomdefense  = Defense("randomdefense",100,100)
		if(defensedecide==0):
			randomdefense  = None		
		
		islanddecide = random.randint(0,2)
		if(islanddecide==2):
			randomisland  = Weapon("genrandom",0,0)
		if(islanddecide==1):
			randomisland  = Island("randomisland")
		if(islanddecide==0):
			randomisland  = None
		
		hashsimple = hashlib.sha256()
		simplekey = bytes("Key","latin-1")
		hashsimple.update(simplekey)
		#keygen = hashsimple.hexdigest()
		keygendecide = random.randint(0,1)
		if(keygendecide==2):
			keygen  = Weapon("genrandom",0,0)
		if(keygendecide==1):
			keygen = hashsimple.hexdigest()
		if(keygendecide==0):
			keygen  = None

		fisherobj = Fisher("simplefisher",100,randomweapon,randomdefense,randomisland,keygen)
		# the name and health was not tested because is inherited da class Individual
		test_ParametersofFisher(fisherobj,randomweapon,randomdefense,randomisland,keygen,"exhaustion: "+str(i))	
	#Test Items on Fisher add , list, use
	name1 = "Espada Curta"
	name2 = "Bandagem"
	name3 = "Cotade Malha"
	names = [name1,name2,name3]
	espadacurta  = Weapon("Espada Curta",10,10)
	randomisland = Island("Island Random")
	cotademalha  = Defense("Cotade Malha",10,10)
	bandagem  =  Medkit("Bandagem",25)
	hashsimple = hashlib.sha256()
	simplekey = bytes("999","latin-1")
	hashsimple.update(simplekey)
	keygen = hashsimple.hexdigest()
	fisherobj = Fisher("Sfisher",100,None,None,randomisland,keygen)
	fisherobj.addItemBackpack(espadacurta)
	fisherobj.addItemBackpack(cotademalha)	
	fisherobj.addItemBackpack(bandagem)
#	if(fisherobj.listItemBackpack()!=None):
#		print(fisherobj.listItemBackpack())
#	if(fisherobj.listItemBackpack()==None):
#		print("Empty")
	print(fisherobj.getDetail())	
	print("\nItens detalhados:\n")
	listbefore = fisherobj.listItemBackpack()
	tam = len(listbefore)
	for i in range(tam):
		print(listbefore[i])

	fisherobj.useItemBackpack("Espada Curta")
	
	print("\033[91mAfter")
	listafter =fisherobj.listItemBackpack()
	tam1 = len(listafter)
	testingAddListUseItem(1000)
	
	# test methods lisItemsfromIsland, collectedItem, name of the test_colectandlisItemsIsland 
	hashsimple.update(simplekey)
	keygen = hashsimple.hexdigest()
	newIsland = Island("New Island")
	simpleplayer = Fisher("Jhogo",100,espadacurta, cotademalha,newIsland,keygen)
	newIsland.addIndividual(simpleplayer)
	[items,namesitems] = gerandoItem(1000)
	#vector[0] have 1000 elements
	#vector[1] have 1000 names of the elements
	for i in range(1000):
		actualitem = items[i]
		newIsland.addItem(items[i])
		test_colectandlisItemsIsland(simpleplayer,items[i],i)
	#Test the dropItems method	
	hashsimple.update(simplekey)
	keygen = hashsimple.hexdigest()
	newIsland = Island("New Island")
	simpleplayer = Fisher("Jhogo",100,espadacurta, cotademalha,newIsland,keygen)
	newIsland.addIndividual(simpleplayer)
	[items,namesitems] = gerandoItem(10)
	for i in range(10):
		simpleplayer.addItemBackpack(items[i])
	testDropItems(simpleplayer,items,'1s')
	
	newIsland = Island("New Island")
	simpleplayer = Fisher("Jhogo",100,espadacurta, cotademalha,newIsland,keygen)
	newIsland.addIndividual(simpleplayer)
	[items,namesitems] = gerandoItem(100)
	for i in range(100):
		simpleplayer.addItemBackpack(items[i])
	testDropItems(simpleplayer,items,'2s')

	newIsland = Island("New Island")
	simpleplayer = Fisher("Jhogo",100,espadacurta, cotademalha,newIsland,keygen)
	newIsland.addIndividual(simpleplayer)
	[items,namesitems] = gerandoItem(1000)
	for i in range(1000):
		simpleplayer.addItemBackpack(items[i])
	testDropItems(simpleplayer,items,'3s')	
	#Test collect getinfoaboutSpellIsland ,and Drop Spells
	for i in range(1000):
		randomisland = Island("random Island")
		spellnew = createRandomSpell()
		randomisland.addSpellIsland(spellnew)
		newPlayer = Fisher("Fisher"+str(i),100,espadacurta,cotademalha,randomisland,keygen)
		randomisland.addIndividual(newPlayer)
		test_ColectGetInfoDropSpells(newPlayer,spellnew,str(i)+" test collect spell,get info about spell,drop spell")
	# test of getValueSpells
	island_head = createIslandAndLinkedThem(10)
	[sumtotal,firstisland] = insertedSpellsOnIslandsLink(island_head,10)
	simpleplayer = Fisher("Jhogo",100,espadacurta, cotademalha,firstisland,keygen)
	test_getvalueSpells(simpleplayer,sumtotal,"Test of sum of values spells: 1")	
	# second test getValueSpells
	island_head = createIslandAndLinkedThem(1000)
	[sumtotal,firstisland] = insertedSpellsOnIslandsLink(island_head,1000)
	simpleplayer = Fisher("Jhogo",100,espadacurta, cotademalha,firstisland,keygen)
	test_getvalueSpells(simpleplayer,sumtotal,"Test of sum of values spells: 2")
	# third test getValueSpells
	island_head = createIslandAndLinkedThem(100000)
	[sumtotal,firstisland] = insertedSpellsOnIslandsLink(island_head,100000)
	simpleplayer = Fisher("Jhogo",100,espadacurta, cotademalha,firstisland,keygen)
	test_getvalueSpells(simpleplayer,sumtotal,"Test of sum of values spells: 3")
	# test getdirectionsfromIsland
	#	"direction " +str(key)+ " the island is: " + str(islandkey)
	randomisland  = Island("randomisland")
	randomisland1 = Island("randomisland1")
	randomisland2 = Island("randomisland2")
	randomisland3 = Island("randomisland3")
	randomisland.adddirection(randomisland1,"right")
	randomisland.adddirection(randomisland2,"left")
	randomisland.adddirection(randomisland3,"back")
	arrayanswer = []
	arrayanswer.append("direction"+" right"+" the island is: "+"randomisland1")
	arrayanswer.append("direction"+" left"+" the island is: "+"randomisland2")
	arrayanswer.append("direction"+" back"+" the island is: "+"randomisland3")
	simpleplayer = Fisher("Jhogo",100,espadacurta, cotademalha,randomisland,keygen)
	randomisland.addIndividual(simpleplayer)
	test_getDirectionfromIsland(simpleplayer,arrayanswer,"Test get directions 1")
	
	randomisland  = Island("randomisland")
	randomisland1 = Island("randomisland1")
	randomisland2 = Island("randomisland2")
	randomisland.adddirection(randomisland1,"right")
	randomisland.adddirection(randomisland2,"left")
	arrayanswer = []
	arrayanswer.append("direction"+" right"+" the island is: "+"randomisland1")
	arrayanswer.append("direction"+" left"+" the island is: "+"randomisland2")
	simpleplayer = Fisher("Jhogo",100,espadacurta, cotademalha,randomisland,keygen)
	randomisland.addIndividual(simpleplayer)
	test_getDirectionfromIsland(simpleplayer,arrayanswer,"Test get directions 2")
	
	randomisland  = Island("randomisland")
	arrayanswer = []
	simpleplayer = Fisher("Jhogo",100,espadacurta, cotademalha,randomisland,keygen)
	randomisland.addIndividual(simpleplayer)
	test_getDirectionfromIsland(simpleplayer,arrayanswer,"Test get directions 3")
	#def test_listenemies, Test listenemies
	for i in range(10):
		randomisland  = Island("randomisland")
		simpleplayer  = Fisher("Jhogo",100,espadacurta, cotademalha,randomisland,keygen)
		randomisland.addIndividual(simpleplayer)
		arrayIndividual = []
		numb = random.randint(1,1000) # max 1000 elements	
		for j in range(numb):
			k = random.randint(1,2)
			character = None
			if(k==1):
				character = gen_Random_Fisher(randomisland,j)
				arrayIndividual.append(character)
			if(k==2):
				character = gen_Random_Individual(randomisland,j)
				arrayIndividual.append(character)

		test_listenemies(simpleplayer,arrayIndividual,"Test listenemies"+str(i))
	# test test_attackEnemy ,
	cotademalha  = Defense("Cotade Malha",10,10)
	for i in range(10):
		randomisland  = Island("randomisland")
		simpleplayer  = Fisher("Jhogo",80,espadacurta, cotademalha,randomisland,keygen)
		randomisland.addIndividual(simpleplayer)
		numb = random.randint(1,1000) # max 1000 elements	
		k = random.randint(1,2)
		character = None
		hashsimple.update(simplekey)
		keygen1 = hashsimple.hexdigest()
		character = Fisher("Luizinho",1,espadacurta, cotademalha,randomisland,keygen1)
		character.addItemBackpack(espadacurta)
		randomisland.addIndividual(character)
		# if(k==1):
		# 	character = gen_Random_Fisher(randomisland,j)
		# if(k==2):
		# 	character = gen_Random_Individual(randomisland,j)
		
		test_attackEnemy(simpleplayer,character,"Test attack enemy:"+ str(i))
		#exit()