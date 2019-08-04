#!/usr/bin/python3
# -*- coding: utf-8 -*-
from Island import *


#This script gen a cluster os islands, that will the represent by a initial island that poits to the others
def genSpellforIsland(self,num):
	if(num==1):
		spelldragon = Magia("Dragon Spell",100)
		return spelldragon
	if(num==2):
		spellsnake = Magia("Snake Spell",70)
		return spellsnake
	if(num==3):
		spellrabbit = Magia("Rabbit spell",90)
		return spellrabbit
	if(num==4):
		Spellfox = Magia("fox spell",130)
		return spellfox
	else:
		return None 
		
def genIndividualforIsland(self,num):	
	if(num == 1):
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

	
def genenerateItemsToIsland(self,num):	
	"""
	This function generate the items, items like Weapons, defese and medkit
	
	@param num : (int) that choose the item
	
	@param : (obj type Item) will be return a object of type item
	"""
	if(num==1):
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
		lightShield = Defense("Light Shield",5,4)    # 20 de defesa
		return lightShield
	if(num==13):
		heavyShield = Defense("Heavy Shield",4,6)   # 24 de defesa
		return heavyShield
	if(num==14):
		chainmail  = Defense("Chainmail",9,4)   # 36 de defesa
		return chainmail
	else:
		return None

def genMapaRandon():
	"""
	This function generate the map of the game, it return a pointer to the first island that generate is the beginning, call island 0,
	the map constains , eleven islands, with diffent items, spells and enemys
	
	@param None
	
	@return :(object type islands) the island 0
	"""  
	nameisland= "island 0" 
	island0 = Island(nameisland)
	nameisland= "island 1" 
	island1 = Island(nameisland)
	nameisland= "island 2" 
	island2 = Island(nameisland)
	nameisland= "island 3" 
	island3 = Island(nameisland)
	nameisland= "island 4" 
	island4 = Island(nameisland)
	nameisland= "island 5" 
	island5 = Island(nameisland)
	nameisland= "island 6" 
	island6 = Island(nameisland)
	nameisland= "island 7" 
	island7 = Island(nameisland)
	nameisland= "island 8" 
	island8 = Island(nameisland)
	nameisland= "island 9" 
	island9 = Island(nameisland)
	nameisland= "island 10" 
	island10 = Island(nameisland)
	island0.addItem(genenerateItemsToIsland(1))
	island0.adddirection(island1,"center")
	island0.adddirection(island2,"right")
	island0.adddirection(island4,"left")
	island0.adddirection(island3,"back")
	island1.adddirection(island9,"center")
	island1.adddirection(island2,"right")
	island1.adddirection(island4,"left")
	island1.adddirection(island0,"back")
	island2.adddirection(island1,"center")
	island2.adddirection(island0,"left")
	island2.adddirection(island3,"back")
	island3.adddirection(island0,"center")
	island3.adddirection(island2,"right")
	island3.adddirection(island4,"left")
	island3.adddirection(island10,"back")
	island4.adddirection(island9,"center")
	island4.adddirection(island0,"right")
	island4.adddirection(island5,"left")
	island4.adddirection(island10,"back")
	island5.adddirection(island6,"center")
	island5.adddirection(island4,"right")
	island5.adddirection(island7,"left")
	island5.adddirection(island8,"back")
	island6.adddirection(island9,"center")
	island6.adddirection(island4,"right")
	island6.adddirection(island7,"left")
	island6.adddirection(island5,"back")
	island7.adddirection(island6,"center")
	island7.adddirection(island5,"right")
	island7.adddirection(island8,"back")
	island8.adddirection(island5,"center")
	island8.adddirection(island4,"right")
	island8.adddirection(island7,"left")
	island8.adddirection(island10,"back")
	island9.adddirection(island1,"right")
	island9.adddirection(island6,"left")
	island9.adddirection(island4,"back")
	island10.adddirection(island4,"center")
	island10.adddirection(island3,"right")
	island10.adddirection(island8,"left")
	return island4

