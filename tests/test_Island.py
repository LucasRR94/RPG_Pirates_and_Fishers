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

def test_getItem(islandobj,nameofitem,refereitem,caseStudy):
	if(isinstance(refereitem,Item)):
		try:
			result = islandobj.getItem(nameofitem) 
			assert(result==refereitem)
		except AssertionError:
			print("\033[91mError, o item don't was present on the list, caseStudy",caseStudy)
		else:
			try:
				assert(islandobj.itemisland.index(refereitem)>=0)
			except (ValueError,AssertionError) as e:
				print("Test sucessful,case study:",caseStudy)
			else:
				print("\033[91mError,the element keeped on the list, case study:",caseStudy)

	else:
		try:
			assert(islandobj.getItem(nameofitem)==None)
		except AssertionError:
			print("\033[91mError, the item was inserted incorrecly, case study:",caseStudy)
		else:
			try:
				assert(islandobj.itemisland.index(refereitem)>=0)
			except (AssertionError,ValueError) as e :
				print("Test sucessful, study case:", caseStudy)				
			else:
				print("\033[91mError, and the strange obj was found on the list,case study:",caseStudy)					
		
def test_listItem(islandobj,refereitem,caseStudy):
	if(isinstance(refereitem,Item)):
		try:
			detailsfromitems = islandobj.getListItems()
			assert(findindetailsname(detailsfromitems,refereitem.getName())==1)
		except AssertionError:
			print("\033[91mError, not was found the item inside of the list, case study:", caseStudy)
		else:
			print("Test sucessful, case study:",caseStudy)
	else:
		try:
			detailsfromitems = islandobj.getListItems()
			assert(findindetailsname(detailsfromitems,refereitem.getName())==0)
		except AssertionError:
			print("Test sucessful, case study:",caseStudy)
		else:
			print("\033[91mError, not was found the item inside of the list, case study:", caseStudy)
			
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

def findindetailsname(listdetails,nameofitem):

	if(type(listdetails) is list):
		if(len(listdetails)==0):
			return 0
		else:
			tam = len(listdetails)
			for i in range(tam):
				position = listdetails[i].find(nameofitem)
				if(position!=-1):
					return 1
			return 0
	else:
		return 0 
if __name__ == "__main__":
	islabonita = Island("Isla Bonita")
	resp = gerandoItem(1000)
	itemsgerados = resp[0]
	l = []
	for i in range(1000):
		test_addItem(islabonita,itemsgerados[i],i)
	print("\n\033[92m###Test list###")	
	for i in range(1000):
		test_listItem(islabonita,itemsgerados[i],i)	


	print("\n\033[92m###Test Get###")	
	for i in range(1000):
		test_getItem(islabonita,itemsgerados[i].getName(),itemsgerados[i],i)	
	test_getItem(islabonita,"Welfer",1,"not in island 1")
	test_getItem(islabonita,"Floyd",l,"not in island 2")	