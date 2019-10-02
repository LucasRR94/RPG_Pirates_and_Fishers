import pytest
import os
import sys
pathfile = os.getcwd()

newpath  = pathfile.split('/')
newpath[len(newpath)-1] = "RpgPiratesAndFishers" 
pathfile = "/".join(newpath)
sys.path.append(pathfile)

from Fisher import Fisher
from Weapon import Weapon
from Defense import Defense
from Island import Island
from Medkit import Medkit
from Spell import Spell
from Item import Item
from Individual import Individual
from libGamePiratesAndFishers import genRandomName
from Control_game import *

@pytest.mark.parametrize("standartinput",[([Weapon("simpl1",10,10),Defense("simpl1",10,10),Weapon("simpl1",1,1),Defense("simpl1",1,1)])])
def test_count_number_fishers_alive(standartinput):
	first = create_context_map()
	mainmap,totalspells = first[0]
	dict_fishers = first[1]
	fisher1 = Fisher("Brave fisher",100,standartinput[0],standartinput[1],mainmap["island 0"],'0')
	fisher2 = Fisher("Looser 1",1,standartinput[2],standartinput[3],mainmap["island 0"],'0')
	result = count_number_fishers_alive(dict_fishers,1) 
	assert type(result) is str
	assert result.index("Sorry all the players are dead,") >= 0 
	dict_fishers["Brave fisher"] = fisher1
	dict_fishers["Looser 1"] = fisher2
	assert count_number_fishers_alive(dict_fishers,0) == 2
	assert count_number_fishers_alive(dict_fishers,1) == 2
	answer = perform_instruction("Looser 1",fisher1,9,dict_fishers)
	result = count_number_fishers_alive(dict_fishers,1)
	print(result)
	assert type(result) == str
	assert result.index("The winner of game")>=0
	assert result.index("Brave fisher") >=0

@pytest.mark.parametrize("standartinput",[([Weapon("simpl1",10,10),Defense("simpl1",10,10),Weapon("simpl1",1,1),Defense("simpl1",1,1)])])
def test_check_fisher_live(standartinput):
	first = create_context_map()
	mainmap,totalspells = first[0]
	dict_fishers = first[1]
	fisher1 = Fisher("Brave fisher",100,standartinput[0],standartinput[1],mainmap["island 0"],'0')
	fisher2 = Fisher("Looser 1",1,standartinput[2],standartinput[3],mainmap["island 0"],'0')	
	assert check_fisher_live(fisher1) == 1
	assert check_fisher_live(fisher2) == 1
	dict_fishers["Brave fisher"] = fisher1
	dict_fishers["Looser 1"] = fisher2
	answer = perform_instruction("Looser 1",fisher1,9,dict_fishers)
	assert check_fisher_live(fisher1) == 1
	assert check_fisher_live(fisher2) == 0
	assert check_fisher_live(first) == None

@pytest.mark.parametrize("standartinput",[("fish1",90,Weapon("weapon1",10,10),Defense("defense1",10,10),"0.0.0.0"),("fish2",100,Weapon("weapon2",1,1),None,"1.1.1.1")])
def test_insertIntoMap(standartinput):
	first = create_context_map()
	mainmap,totalspells = first[0]
	dict_fishers = first[1]
	basicstring = "island "
	for j in range(11):
		island_name = ""
		island_name = basicstring+str(j)
		for i in (mainmap[island_name].listIndividuals()):
			try:
				l = i.index(standartinput[0])
			except ValueError:
				pass
			else:
				raise Exception("Error!!!!, fishers alredy on list")	
	mainmap,fisher1 = insertIntoMap(standartinput[0],standartinput[1],standartinput[2],standartinput[3],mainmap,standartinput[4],dict_fishers)
	resp = 0
	for j in range(11):
		island_name = ""
		island_name = basicstring+str(j)
		for i in (mainmap[island_name].listIndividuals()):
			try:
				l = i.index(standartinput[0])
			except ValueError:
				pass
			else:
				resp+=1
				
	assert resp == 1, "Error the Fisher was not inserted"
	assert dict_fishers[standartinput[0]] == fisher1
	assert  insertIntoMap(standartinput[0],standartinput[1],standartinput[2],standartinput[3],mainmap,standartinput[4],None) == None
	mainmap , fisherrandom= insertIntoMap("Randomfisher",None,None,None,mainmap,"98.98.98.98",dict_fishers)
	resp = 0
	for j in range(11):
		island_name = ""
		island_name = basicstring+str(j)
		for i in (mainmap[island_name].listIndividuals()):
			try:
				l = i.index(standartinput[0])
			except ValueError:
				pass
			else:
				resp+=1
	for j in range(11):
		island_name = ""
		island_name = basicstring+str(j)
		for i in (mainmap[island_name].listIndividuals()):
			try:
				l = i.index("Randomfisher")
			except ValueError:
				pass
			else:
				resp+=1
	assert resp == 2 ,"Error, the map not insert all individuals"
	assert dict_fishers["Randomfisher"] == fisherrandom
	assert dict_fishers[standartinput[0]] == fisher1

@pytest.mark.parametrize("standartinput",[("fish1",90,Weapon("weapon1",10,10),Defense("defense1",10,10),"0.0.0.0"),("fish2",100,Weapon("weapon2",1,1),None,"1.1.1.1")])
def test_perform_instruction(standartinput):
	first = create_context_map()
	mainmap,totalspells = first[0]
	dict_fishers = first[1]
	mainmap,fisher1 = insertIntoMap(standartinput[0],standartinput[1],standartinput[2],standartinput[3],mainmap,standartinput[4],dict_fishers)
	assert type(perform_instruction(None,fisher1,0,None)) is str 
	assert perform_instruction(None,fisher1,0,None) == "No Items on backpack"
	assert type(perform_instruction(None,fisher1,3,None)) is str 
	assert perform_instruction(None,fisher1,3,None).index("Item") >= 0
	vec = perform_instruction(None,fisher1,3,None).split(":")
	vec2 = vec[1]
	vec = vec2.split("\n")
	assert perform_instruction(vec[0],fisher1,2,None) == 1
	assert (perform_instruction(None,fisher1,0,None)).index(vec[0])>=0
	assert type(perform_instruction(vec[0],fisher1,1,None)) is int
	assert type(perform_instruction(None,fisher1,1,None)) is int
	a = perform_instruction(None,fisher1,1,None)
	if(a !="No Items on backpack"):
		assert type(perform_instruction(None,fisher1,4,None)) is list
	
	assert type(perform_instruction(None,fisher1,5,None)) is str
	assert (perform_instruction(None,fisher1,5,None)).index("island") > 0
	count = 0 
	a = perform_instruction(None,fisher1,5,None)
	if(a == "Spells available in island"):
		count+=1
	if(a == "No spell present on the island"):
		count+=1
	assert count == 1, "Error, verify spells"
	assert type(perform_instruction(None,fisher1,7,None)) is str		
	count = 0
	for i in range(4):
		a = perform_instruction(None,fisher1,7,None)
		if(a.index("island")>=0):
			try:
				a.index("right")>=0
			except ValueError:
				try:
					a.index("center")>=0
				except ValueError:
					try:
						a.index("back")>=0
					except ValueError:
						try:
							a.index("left")
						except ValueError:
							raise Exception("None directions found!!!")
						else:
							count+=1
					else:
						count+=1
				else:
					count+=1

			else:
				count+=1
			
	assert count >=1, "Error, providing directions on islands"
	l = a.split(" ")
	assert (perform_instruction(l[1],fisher1,6,None)) == 1
	assert (perform_instruction(None,fisher1,8,None)) == "Sucess on collect spell\n"
	assert (perform_instruction(None,fisher1,10,None)).index("Name of individual")>=0
	string_enimies = (perform_instruction(None,fisher1,10,None))
	final_name_enemies = string_enimies.split(":")
	name_enemie = final_name_enemies[1]
	final_name_enemies = name_enemie.split("\n")[0]
	assert perform_instruction(final_name_enemies,fisher1,9,dict_fishers) == 1
	assert (perform_instruction(None,fisher1,11,None)).index(fisher1.getName())>=0
	assert (perform_instruction(fisher1.getName(),fisher1 ,12,dict_fishers)) == 1
	assert len(dict_fishers) == 0

@pytest.mark.parametrize("standartinput",[("fish1",90,Weapon("weapon1",10,10),Defense("defense1",10,10),"0.0.0.0",Spell("Spell 1",10),Spell("Spell 2",11),Defense("Defesa s1",10,2),Weapon("Weapon",3,5)),("fish2",100,Weapon("weapon2",1,1),None,"1.1.1.1",Spell("Spell 1",10),Spell("Spell 2",11),Defense("Defesa s1",1,5),Weapon("Weapona",3,7))])
def test_disconnect_player(standartinput):
	first = create_context_map()
	mainmap,totalspells = first[0]
	dict_fishers = first[1]
	numberitems = 0
	mainmap,fisher1 = insertIntoMap(standartinput[0],standartinput[1],standartinput[2],standartinput[3],mainmap,standartinput[4],dict_fishers)
	numberitems = 2
	assert dict_fishers[standartinput[0]] == fisher1
	location = fisher1.getactualIsland()
	numberspells = location.statusSpell()
	assert fisher1.collectSpell() == "Sucess on collect spell\n"
	(fisher1.getactualIsland()).addSpellIsland(standartinput[5])
	numberspells+=1
	assert fisher1.collectSpell() == "Sucess on collect spell\n"
	(fisher1.getactualIsland()).addSpellIsland(standartinput[6])
	assert fisher1.collectSpell() == "Sucess on collect spell\n"
	numberspells+=1
	if(location.getListItems()!= None):
		if(len(location.getListItems())>0):
			numberitems+=len(location.getListItems())
	assert fisher1.addItemBackpack(standartinput[7]) == 1
	assert fisher1.addItemBackpack(standartinput[8]) == 1
	numberitems+=2
	assert disconnect_player(fisher1.getName(),dict_fishers,fisher1) == 1
	takespells = location.getSpell()
	assert len(takespells) == numberspells
	assert len(location.getListItems())== numberitems


@pytest.mark.parametrize("standartinput",[("fish1",1,Weapon("weapon1",10,10),Defense("defense1",10,10),"0.0.0.0"),("fish2",100,Weapon("weapon2",10,10),None,"1.1.1.1")])
def test_eliminate_fisher_deads(standartinput):
	first = create_context_map()
	mainmap,totalspells = first[0]
	dict_fishers = first[1]
	basicstring = "island "
	numberitems = 0
	mainmap,fisher1 = insertIntoMap(standartinput[0],standartinput[1],standartinput[2],standartinput[3],mainmap,standartinput[4],dict_fishers)
	assert dict_fishers[fisher1.getName()] == fisher1
	assert eliminate_fisher_deads(dict_fishers,fisher1.getName()) == 0 
	assert disconnect_player(fisher1.getName(),dict_fishers,fisher1) == 1
	fisher1 = Fisher("Fisher1",100,standartinput[2],standartinput[3],mainmap["island 1"],standartinput[4])
	dict_fishers[fisher1.getName()] = fisher1 
	fisher2 = Fisher("Fisher looser",2,standartinput[2],Defense("Min",1,1),mainmap["island 1"],0)
	dict_fishers[fisher2.getName()] = fisher2
	count = 0
	for i in (mainmap["island 1"]).listIndividuals():
		if(i == fisher1.getDetail() or i == fisher2.getDetail()):
			count+=1
	assert count == 2
	assert fisher1.attackEnemy(fisher2.getName()) == 1
	assert fisher2.getName() == ''
	assert dict_fishers["Fisher looser"] == fisher2
	count = 0
	for i in (mainmap["island 1"]).listIndividuals():
		if(i == fisher1.getDetail() or i == fisher2.getDetail()):
			count+=1
	assert count ==1 
	assert eliminate_fisher_deads(dict_fishers,"Fisher looser") == 1
	try:
		 a = dict_fishers["Fisher looser"]
	except KeyError:
		pass
	else:
		raise Exception("Error, should be removed!!!")

