#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Fisher import *

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
	
#	for i in range(1000):
#		fisherobj = Fisher("simplefisher",100,espadacurta,cotademalha,island1,keygen)
#		test_ParametersofFisher(fisherobj,espadacurta,cotademalha,island1,keygen,"Obj 1")	