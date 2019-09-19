#!/usr/bin/python3
# -*- coding: utf-8 -*-
from gen_map import genenerateItemsToIsland
from gen_map import genMap
from Island import *
from Fisher import Fisher
from Weapon import Weapon
from Defense import Defense
import threading
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

def gen_Unique_ID(ip_adress):
	"""
	This function generate a unique id for the Fisher, using the ip and a random number

	@param ip_adress :(string) that represent the adress of the client

	@return :(hash sha256) the digest of the sha-256
	"""
	objhash = hashlib.sha256()
	randnumb = random.randint(-100000,100000)
	finalstring = ip_adress + str(randnumb)
	word = bytes(finalstring,"latin-1")
	objhash.update(word)
	digest = objhash.hexdigest()
	return digest

def insertIntoMap(nameFisher,health,itemAttack,itemDefense,objectMap,ip_adress,dict_fishers):
	"""
	This function insert into a random island a Fisher, that paremeters was passed to construct

	@param nameFisher:(str) String that represent the name parameter name in the Fisher
	@param health : (int) integer that represent the total health parameter in the Fisher
	@param itemAttack : (object type Attack) object attack that will be insert into Fisher
	@param itemDefense :(object type Defense) object defense that will be insert into Fisher
	@param objectMap :(dictionary of islands) dictionary of islands that will contains the map
	@param ip_adress :(string) that represent the adress of the client
	@param dict_fishers:(dictionary) of fishers that are present on the map

	@return: (array or None) if sucessed the insert of Fisher will return [objectMap,Fisher], with 
	Fisher inserted and objectMap with the Fisher, otherwise None.
	"""
	word = gen_Unique_ID(ip_adress)
	# a random number is sum to the ip_adress to form a id unique for the player
	cond = 0
	while(cond == 0):
		try:
			assert dict_fishers[word] != None
		except (AssertionError,KeyError) as a:
			cond+=10
		else:	
			word = gen_Unique_ID(ip_adress)

	if(type(itemAttack) == Weapon and type(itemDefense) == Defense and type(health) == int):
		if(health < 1 and health > 100):
			health = 60
		randomFisher = Fisher(nameFisher,health,itemAttack,itemDefense,objectMap[randomIslandbourne()],word) 
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
		randomFisher = Fisher(nameFisher,100,genenerateItemsToIsland(random.randint(4,11)),genenerateItemsToIsland(random.randint(12,14)),objectMap[randomIslandbourne()],word) 
		try:
			assert(type(randomFisher.getactualIsland())==Island)
		except AssertionError:
			return None
		else:
			final = []
			final.append(objectMap)
			final.append(randomFisher)
			return final # return the final array

def perform_instruction(parameter_instruction,fisher,option):
	"""
	This function perform the instruction of the client in the map, returning the response for the action

	@param parameter_instruction:(array of objects) array of objects that are parameter for method used in fisher
	@param fisher:(object fisher) fisher that will execute the method
	@param option:(int) integer that represent the option of the instruction

	@return:(string) the result of the instruction on the game
	"""

	if(option==0): 
		return(fisher.listItemBackpack())
	
	elif(option==1): 
		return(fisher.useItemBackpack(parameter_instruction[0]))

	elif(option==2): 
		return(fisher.collectItem(parameter_instruction[0]))

	elif(option==3): 
		return(fisher.listItemsfromIsland())

	elif(option==4): 
		return(fisher.dropItems())

	elif(option==5): 
		return(fisher.getinfoaboutSpellonIsland())

	elif(option==6): 
		return(fisher.changeIsland(vetorinstrucao[0]))

	elif(option==7): 
		return(fisher.getDirectionsfromIsland())
		
	elif(option==8): 
		return(fisher.collectSpell())

	elif(option==9):	
		return(fisher.attackEnemy(vetorinstrucao[0]))

	elif(option==10):
		return(fisher.listenemies())

	elif(option==11):	
		return(fisher.getDetail())


if __name__ == "__main__":
	main_fishers = {}
	global totalspells
	mainmap,totalspells  = genMap() # is declared a map
	
	resposta = insertIntoMap("Brave fisher",0,0,0,mainmap,"0.0.0.0",main_fishers)
	mainmap = resposta[0]
	fisher = resposta[1]
	