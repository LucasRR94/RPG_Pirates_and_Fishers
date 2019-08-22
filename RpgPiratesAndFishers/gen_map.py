#!/usr/bin/python3
# -*- coding: utf-8 -*-
from Island import *
from Medkit import Medkit
from Defense import Defense
from Weapon import Weapon
from Spell import Spell
from Item import Item
from Individual import Individual

#This script gen a cluster os islands, that will the represent by a initial island that poits to the others
def genSpellforIsland(num):
	"""
	This function is capable of return objects, spell object type when received parameter num, a integer that can
	switch between different type of objects.

	@param num : (integer) range between 1 and 4

	@return : object type spell
	"""
	if(num==1):
		spelldragon = Spell("Dragon Spell",100)
		return spelldragon
	
	if(num==2):
		spellsnake = Spell("Snake Spell",70)
		return spellsnake
	
	if(num==3):
		spellrabbit = Spell("Rabbit spell",90)
		return spellrabbit
	
	if(num==4):
		spellfox = Spell("fox spell",130)
		return spellfox
	
	else:
		return None 
		
def genIndividualforIsland(num):	
	"""
	This function generate objects type Individual,the individuals switch accordidly the parameter num

	@param num: (integer) number that choose the type of pirate

	@return : object type individual
	"""
	if(num == 0 or num == 1):
		pirateintern = Individual("Intern pirate",20,30,20)
		return pirateintern
	
	if(num == 2):
		piratenoob = Individual("Noob pirate",30,20,10)
		return piratenoob
	
	if(num==3):
		piratepro  = Individual("Pro Pirate",40,30,30) 
		return piratapro
	
	else:
		return None

	
def genenerateItemsToIsland(num):	
	"""
	This function generate the items, items like Weapons, defese and medkit
	
	@param num : (int) that choose the item
	
	@param : (obj type Item) will be return a object of type item
	"""
	if(num==1 or num ==0):
		bandage = Medkit("Bandage",10)
		return bandage
	
	if(num==2):
		antibiotic = Medkit("Antibiotic injection",40)
		return antibiotic
	
	if(num==3):		
		injectinflammatory  = Medkit("inflammatory injection",50)
		return injectinflammatory
	
	if(num==4):
		dagger  = Weapon("Dagger",2,8) 		    
		return dagger
	
	if(num==5):
		poniard = Weapon("Poniard",3,7)		    
		return poniard
	
	if(num==6):
		shortSword = Weapon("Short Sword",5,6)    
		return shortSword
	
	if(num==7):
		longSword = Weapon("Long Sword",7,5)    
		return longSword
	
	if(num==8):
		shortAx = Weapon("Short ax",8,5)   
		return shortAx
	
	if(num==9):
		longAx = Weapon("Long ax",8,6)   
		return longAx
	
	if(num==10):
		shortHammer = Weapon("Long Hammer",5,9)   
		return shortHammer	
	
	if(num==11):
		longHammer = Weapon("Long Hammer",6,9)   
		return longHammer
	
	if(num==12):
		lightShield = Defense("Light Shield",5,8) 
		return lightShield
	
	if(num==13):
		heavyShield = Defense("Heavy Shield",9,5) 
		return heavyShield
	
	if(num==14):
		chainmail  = Defense("Chainmail",10,7)   
		return chainmail
	
	else:
		return None

def genMap():
	"""
	This function generate the map of the game, it return a pointer to the first island that generate is the beginning, call island 0,
	the map constains , eleven islands, with diffent items, spells and enemys
	
	@param None
	
	@return : dictionary of islands, that are index by the name island +("0" ..."10"), eleven in total
	"""  
	Mapgenerate = {} # the entire map generated
	
	nameisland= "island 0" 
	island0 = Island(nameisland)
	Mapgenerate["island 0"] = island0
	
	nameisland= "island 1" 
	island1 = Island(nameisland)
	Mapgenerate["island 1"] = island1

	nameisland= "island 2" 
	island2 = Island(nameisland)
	Mapgenerate["island 2"] = island2
	
	nameisland= "island 3" 
	island3 = Island(nameisland)
	Mapgenerate["island 3"] = island3
	
	nameisland= "island 4" 
	island4 = Island(nameisland)
	Mapgenerate["island 4"] = island4
	
	nameisland= "island 5" 
	island5 = Island(nameisland)
	Mapgenerate["island 5"] = island5
	
	nameisland= "island 6" 
	island6 = Island(nameisland)
	Mapgenerate["island 6"] = island6
	
	nameisland= "island 7" 
	island7 = Island(nameisland)
	Mapgenerate["island 7"] = island7
	
	nameisland= "island 8" 
	island8 = Island(nameisland)
	Mapgenerate["island 8"] = island8
	
	nameisland= "island 9" 
	island9 = Island(nameisland)
	Mapgenerate["island 9"] = island9
	
	nameisland= "island 10" 
	island10 = Island(nameisland)
	Mapgenerate["island 10"] = island10
	
	cont = 4
	island0.addSpellIsland(genSpellforIsland(2))
	island0.addItem(genenerateItemsToIsland(1))
	island0.addItem(genenerateItemsToIsland(cont%14))
	island0.addIndividual(genIndividualforIsland(cont%3))
	island0.adddirection(island1,"center")
	island0.adddirection(island2,"right")
	island0.adddirection(island4,"left")
	island0.adddirection(island3,"back")
	
	cont+=1
	island1.addSpellIsland(genSpellforIsland(1))
	island1.addItem(genenerateItemsToIsland(2))
	island1.addItem(genenerateItemsToIsland(cont%14))
	island1.addIndividual(genIndividualforIsland(cont%3))
	island1.adddirection(island9,"center")
	island1.adddirection(island2,"right")
	island1.adddirection(island4,"left")
	island1.adddirection(island0,"back")
	
	cont+=1
	island2.addSpellIsland(genSpellforIsland(4))
	island2.addItem(genenerateItemsToIsland(1))
	island2.addItem(genenerateItemsToIsland(cont%14))
	island2.addIndividual(genIndividualforIsland(cont%3))
	island2.adddirection(island1,"center")
	island2.adddirection(island0,"left")
	island2.adddirection(island3,"back")
	
	cont+=1
	island3.addSpellIsland(genSpellforIsland(1))
	island3.addItem(genenerateItemsToIsland(3))
	island3.addItem(genenerateItemsToIsland(cont%14))
	island3.addIndividual(genIndividualforIsland(cont%3))
	island3.adddirection(island0,"center")
	island3.adddirection(island2,"right")
	island3.adddirection(island4,"left")
	island3.adddirection(island10,"back")
	
	cont+=1
	island4.addSpellIsland(genSpellforIsland(3))
	island4.addItem(genenerateItemsToIsland(1))
	island4.addItem(genenerateItemsToIsland(cont%14))
	island4.addIndividual(genIndividualforIsland(cont%3))
	island4.adddirection(island9,"center")
	island4.adddirection(island0,"right")
	island4.adddirection(island5,"left")
	island4.adddirection(island10,"back")
	
	cont+=1
	island5.addSpellIsland(genSpellforIsland(1))
	island5.addItem(genenerateItemsToIsland(2))
	island5.addItem(genenerateItemsToIsland(cont%14))
	island5.addIndividual(genIndividualforIsland(cont%3))
	island5.adddirection(island6,"center")
	island5.adddirection(island4,"right")
	island5.adddirection(island7,"left")
	island5.adddirection(island8,"back")
	
	cont+=1
	island6.addSpellIsland(genSpellforIsland(2))
	island6.addItem(genenerateItemsToIsland(3))
	island6.addItem(genenerateItemsToIsland(cont%14))
	island6.addIndividual(genIndividualforIsland(cont%3))
	island6.adddirection(island9,"center")
	island6.adddirection(island4,"right")
	island6.adddirection(island7,"left")
	island6.adddirection(island5,"back")
	
	cont+=1
	island7.addSpellIsland(genSpellforIsland(3))
	island7.addItem(genenerateItemsToIsland(1))
	island7.addItem(genenerateItemsToIsland(cont%14))
	island7.addIndividual(genIndividualforIsland(cont%3))
	island7.adddirection(island6,"center")
	island7.adddirection(island5,"right")
	island7.adddirection(island8,"back")
	
	cont+=1
	island8.addSpellIsland(genSpellforIsland(4))
	island8.addItem(genenerateItemsToIsland(1))
	island8.addItem(genenerateItemsToIsland(cont%14))
	island8.addIndividual(genIndividualforIsland(cont%3))
	island8.adddirection(island5,"center")
	island8.adddirection(island4,"right")
	island8.adddirection(island7,"left")
	island8.adddirection(island10,"back")
	
	cont+=1
	island9.addSpellIsland(genSpellforIsland(1))
	island9.addItem(genenerateItemsToIsland(3))
	island9.addItem(genenerateItemsToIsland(cont%14))
	island9.addIndividual(genIndividualforIsland(cont%3))
	island9.adddirection(island1,"right")
	island9.adddirection(island6,"left")
	island9.adddirection(island4,"back")
	
	cont+=1
	island10.addSpellIsland(genSpellforIsland(2))
	island10.addItem(genenerateItemsToIsland(2))
	island10.addItem(genenerateItemsToIsland(cont%14))
	island10.addIndividual(genIndividualforIsland(cont%3))
	island10.adddirection(island4,"center")
	island10.adddirection(island3,"right")
	island10.adddirection(island8,"left")
	
	
	return Mapgenerate

