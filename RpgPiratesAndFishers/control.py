#!/usr/bin/python3
# -*- coding: utf-8 -*-
from gen_map import genenerateItemsToIsland
from gen_map import genMap
from Island import *
from Fisher import Fisher
from Weapon import Weapon
from Defense import Defense
import hashlib
import random

def randomIslandbourne():
	"""
	This function generate a random number, between a range that is present on the map of the game

	@param None:

	@return : (str) that represent a name, that are inside of the game
	"""
	islandNumb = random.randint(0,10)
	nameisland = "island "+ str(islandNumb)
	return nameisland

def insertIntoMap(nameFisher,health,itemAttack,itemDefense,objectMap):
	"""
	This function insert into a random island a Fisher, that paremeters was passed to construct

	@param nameFisher:(str) String that represent the name parameter name in the Fisher
	@param health : (int) integer that represent the total health parameter in the Fisher
	@param itemAttack : (object type Attack) object attack that will be insert into Fisher
	@param itemDefense :(object type Defense) object defense that will be insert into Fisher
	@param objectMap :(dictionary of islands) dictionary of islands that will contains the map


	@return: (array or None) if sucessed the insert of Fisher will return [objectMap,Fisher], with 
	Fisher inserted and objectMap with the Fisher, otherwise None.
	"""
	objhash = hashlib.sha256()
	randnumb = random.randint(-100000,100000)
	word = bytes(str(randnumb),"latin-1")
	objhash.update(word)
	if(type(itemAttack) == Weapon and type(itemDefense) == Defense and type(health) == int):
		if(health < 1 and health > 100):
			health = 60
		randomFisher = Fisher(nameFisher,health,itemAttack,itemDefense,objectMap[randomIslandbourne()],objhash.hexdigest()) 
		try:
			assert(type(randomFisher.getactualIsland)==Island)
		except AssertionError:
			return None
		else:
			final = []
			final.append(objectMap)
			final.append(randomFisher)
			return final # return the final array
	else:
		randomFisher = Fisher(nameFisher,100,genenerateItemsToIsland(random.randint(4,11)),genenerateItemsToIsland(random.randint(12,14)),objectMap[randomIslandbourne()],objhash.hexdigest()) 
		try:
			assert(type(randomFisher.getactualIsland())==Island)
		except AssertionError:
			return None
		else:
			final = []
			final.append(objectMap)
			final.append(randomFisher)
			return final # return the final array

if __name__ == "__main__":
	mainmap  = genMap() # is declared a map
	resposta = insertIntoMap("Brave fisher",0,0,0,mainmap)
	mainmap = resposta[0]
	fisher = resposta[1]
	print(fisher.getinfoaboutSpellonIsland())
	print(fisher.collectSpell())
	print("After :\n")
	print(fisher.getinfoaboutSpellonIsland())
