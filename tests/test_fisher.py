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
			else:
				print()
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
			else:
				try:
					assert(fisherobj.backpack.index(iteminsert)>=0)
				except (AssertionError,ValueError) as e:
					print("Error, instability on backpack, object not found, case study:\n",CaseStudy)
				else:
					print("Test sucessfull, case study:\n",caseStudy)
		
		if(type(iteminsert)==Item):
			try:
				assert(fisherobj.addItemBackpack(iteminsert)==0)
			except AssertionError:
				print("Error, an object that is not an item was insert incorrecly, case Study:\n",CaseStudy)	
			else:
				print("Test sucessfull, case study:\n",caseStudy)
	else:
		print("Error the element was previous on the backpack, case study: \n"+str(caseStudy))

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
	# print("\nItens detalhados:\n")
	# for i in range(tam1):
	# 	for j in range(3):
	# 		l = listafter[i].find(names[j])
	# 		#print(l)
	# 		if(l>-1):
	# 			print("\n It's presente \n")
	# 			print(listafter[i])

		
	testingAddListUseItem(1000)
			# else:
			# 	print("\n It'not more presente \n")
		#print(listafter[i])
	#print(fisherobj.getDetail())	
	#print(fisherobj.listItemBackpack())
	