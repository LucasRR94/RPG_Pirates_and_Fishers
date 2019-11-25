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

"""
This file provide all infrastructure to service of game, controling insert, deletes, checking the fishers alive,
check life, inserting fishers,disconnect fishers of game, clean memory, and create the map.
"""
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
	if(type(dict_fishers) != dict):
		return None
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
		if(type(randomFisher) == Fisher):
			try:
				assert(type(randomFisher.getactualIsland())==Island)
			except AssertionError:
				return None
			else:
				dict_fishers[nameFisher] = randomFisher
				final = []
				final.append(objectMap)
				final.append(randomFisher)
				return final # return the final array
		else:
			return None
	else:
		randomFisher = Fisher(nameFisher,random.randint(50,100),genenerateItemsToIsland(random.randint(4,11)),genenerateItemsToIsland(random.randint(12,14)),objectMap[randomIslandbourne()],word) 
		if(type(randomFisher) == Fisher):
			try:
				assert(type(randomFisher.getactualIsland())==Island)
			except AssertionError:
				return None
			else:
				dict_fishers[nameFisher] = randomFisher
				final = []
				final.append(objectMap)
				final.append(randomFisher)
				return final # return the final array
		else:
			return None

def perform_instruction(parameter_instruction,fisher,option,dict_fisher):
	"""
	This function perform the instruction of the client in the map, returning the response for the action

	@param parameter_instruction:(str) paremeter for a method 
	@param fisher:(object fisher) fisher that will execute the method
	@param option:(int) integer that represent the option of the instruction
	@param dict_fisher: (dict) contains a dictionary of all fishers present on the game
	@return:(string) the result of the instruction on the game
	"""
	if(option==0): #LIFF - list items from Fisher
		return(fisher.listItemBackpack()) 
	
	elif(option==1): #USEI - use item back
		return(fisher.useItemBackpack(parameter_instruction)) pack

	elif(option==2): #CATI - Catch item
		return(fisher.collectItem(parameter_instruction)) 

	elif(option==3): #LSTI - list items from island
		return(fisher.listItemsfromIsland()) 

	elif(option==4): 
		return(fisher.dropItems())

	elif(option==5): # GETS - get info about spells on actual island
		return(fisher.getinfoaboutSpellonIsland()) 

	elif(option==6): #MOVF - move for other island
		return(fisher.changeIsland(parameter_instruction))

	elif(option==7): #DIRI - possible directions Islands
		return(fisher.getDirectionsfromIsland()) 
		
	elif(option==8): #CATS - catch  Spell
		return(fisher.collectSpell()) 

	elif(option==9): #ATQE - Attack Enemie.
		action = fisher.attackEnemy(parameter_instruction) 
		eliminate_fisher_deads(dict_fisher,parameter_instruction)
		return(action)

	elif(option==10):	#GETI - get list of enemies
		return(fisher.listenemies()) 

	elif(option==11):	#REPF - report actual situation of player
		return(fisher.getDetail()) 

	elif(option==12):# EXIN, exit from game
		return(disconnect_player(fisher.getName(),dict_fisher,fisher)) 
	
	else:
		return None

def disconnect_player(name_player,dict_fisher,fish_obj):
	"""
	This function, disconnect the Fisher of the game.If correct is return 1, else 0.
	@param name_player:(str) that is the key for the dictionary of the fishers
	@param dict_fisher:(dictionary of fishers) dictionary of fishers in the game
	@param fish_obj: (object type fisher) fisher that wants to disconect from the game
	@return: 1 if disconect, 0 otherwise
	"""
	# if(fish_obj.disconect_fisher_island() == 1 and eliminate_fisher_deads(dict_fisher,name_player) == 1):
	# 	return 1
	if(fish_obj.disconect_fisher_island() == 1):
		if(eliminate_fisher_deads(dict_fisher,name_player) == 1):
			return 1
		else:
			return 0
	else:
		return 0

def count_number_fishers_alive(dict_fishers,gamerunning):
	"""
	This function , count the number of fishers alive in the  island, if is 1 the number of players 
	alive and the game is running, he catch the number, and form a message of the winner, otherwise 
	,return just return the number of players
	
	@param dict_fishers:(dictionary of fishers objects) a dictionary of all the fishers present on game
	@param gamerunning:(int) indicate if the number of players is bigger or equal 2(1), and gamming is runing
	,otherwise game waits for beggin(0).
	
	@return:(str or int), a message with the winner game, or the number of players otherwise
	"""
	if(gamerunning == 1):
		if(len(dict_fishers) >= 2):
			return len(dict_fishers)	
		elif(len(dict_fishers) == 1):
			answer = ""
			for key, objfisher in dict_fishers.items():
				answer = objfisher.getName()
			return "The winner of game section is "+answer+" , Congratulations!!!, the game is over!!!\n"
		else:
			return "Sorry all the players are dead, more luck in the next round, ;) \n"
	else:
		return len(dict_fishers)

def check_fisher_live(fisher_test):
	"""
	This function is testing, if a object type fisher is live, if name , getValueDefense and getValueAttack,  is not None, or ''
	If the conditions None or '' are found, the function return 0, otherwise 1
	@param fisher_test:(object type Fisher) object type fisher that will be tested, for be alive or dead
	@return:(int) 0 if dead, 1 if is alive, None if the object is not Fisher.
	"""
	if(type(fisher_test) == Fisher):
		if(fisher_test.getName() == '' and fisher_test.getValueDefense() == None and fisher_test.getValueAttack()==None):
			return 0
		else:
			return 1
	else:
		return None

def eliminate_fisher_deads(dict_fishers,name_fisher):
	"""
	This function, check for a specific fisher, if he is dead, he the object is eliminated, and change for "None"
	@param dict_fishers:(dict of fishers) contains all the fisher present on the game
	@param name_fisher:(str) the key for the fisher on the game
	@return: 1 if eliminate object fisher dead, 0 otherwise, error to find or fisher alive
	"""
	if(type(dict_fishers) is dict):
		try:
			obj_fisher_test = dict_fishers[name_fisher]
		except KeyError:
			return 0
		else:
			if(check_fisher_live(obj_fisher_test)==0):
				dict_fishers[name_fisher] = None
				dict_fishers.pop(name_fisher)
				return 1
			else:
				return 0
	else:
		return 0

def create_context_map():
	"""
	This function create the map of the game, and return a dict of Fishers present.The map is composed
	by a array , of total dict of islands and totalspells values present on the map.
	@param None
	@return: array([[dict of Islands objects,total value speels(int)],dict of fishers present])
	"""
	total_fishers = {}
	answer = []
	answer.append(genMap())# is declared a map
	answer.append(total_fishers) # is declared the dictionary of fishers
	return answer

if __name__ == "__main__":
	main_fishers = {}
#	global totalspells
	first = create_context_map()
	mainmap,totalspells = first[0]
	fishers_on_game = first[1]
#	global locks_islands 
	locks_islands = []
	### One lock for each island###
#	for i in range(len(mainmap)):
#		locks_islands.append(threading.Lock())
	###-------------------------###	
#	m = thread_player(1)
#	m.start()	
	simple12 = Weapon("simpl1",10,10)
	simpl22 = Defense("simpl1",10,10)
	fish1  = Fisher("Brave fisher",100,simple12,simpl22,mainmap["island 0"],'0')
	fishers_on_game["Brave fisher"] = fish1
	
	simple1 = Weapon("simpl1",1,1)
	simpl2 = Defense("simpl1",1,1)
	fish11 = Fisher("Looser 1",1,simple1,simpl2,mainmap["island 0"],'0')
	fishers_on_game["Looser 1"] = fish11
	
	a = count_number_fishers_alive(fishers_on_game,1)
	if(a == 0):
		print("The game is running, no winners")
	else:
		print(a)	
	exit()
	
	answer = perform_instruction("Looser 1",fish1,9,fishers_on_game) 	
	#answer = fish1.attackEnemy("Looser 1")
	a = mainmap["island 0"].listIndividuals()
	for i in range(len(a)):
		print(a[i])
	if(answer == 1):
		print("ok")
		if(fish11.getName() == ''):
			print("Looser is dead")
			#answer = fish1.attackEnemy("Intern pirate")
			#a = mainmap["island 0"].listIndividuals()
			#for i in range(len(a)):
			#	print(a[i])
			#print(fish11.getNamelocation())
			if(check_fisher_live(fish11) == 1):
				print("Brave fisher is dead!!")
			print(len(mainmap["island 0"].individualsPresent))
			print(fish11.getDetail())
			try: 
				a = fishers_on_game["Looser 1"]
			except KeyError:
				print("Looser 1 is dead")
			else:
				print("fim")
			
			fish11 = fishers_on_game["Brave fisher"]
			print(fish11.getDetail())
			
		
	else:
		print("Error")
	