#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Island import Island
from Item import Item
from Weapon import Weapon
from Defense import Defense
from Medkit import Medkit
import random

def test_addItem(islandobj,refereitem,caseStudy):
	"""
	this function is testing the insertion of the elements on the list in the island
	@param islandobj:(island) the obj that will be inserted the elements 
	@param refereitem:(item) the item that will be inserted
	@param caseStudy:(int) the number of study case
	@return None
	"""
	if(isinstance(refereitem,Item)):
		try:
			assert(islandobj.addItem(refereitem) ==1)
		except AssertionError:
			print("Error, don't was inserted the obj, correcly, study case:",caseStudy)
			exit()
		else:
			try:
				assert(islandobj.itemisland.index(refereitem)>=0)
			except AssertionError:
				print("Error, the obj, not found on the list. Case study:", caseStudy)
				exit()
			else:
				print("Test sucessful,case study:",caseStudy)
	else:
		try:
			assert(islandobj.addItem(refereitem) == 0)
		except AssertionError:
			print("Error , a strange object was add into vector, case Study:",caseStudy)
			exit()
		else:
			try:
				assert(islandobj.itemisland.index(refereitem)>=0)
			except ValueError:
				print("Test sucessful,caseStudy:", caseStudy)
			else:
				print("Error, was inserted an strange object in vector, case study:",caseStudy)	
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
if __name__ == "__main__":
	islabonita = Island("Isla Bonita")
	resp = gerandoItem(1000)
	itemsgerados = resp[0]

	for i in range(1000):
		test_addItem(islabonita,itemsgerados[i],i)
