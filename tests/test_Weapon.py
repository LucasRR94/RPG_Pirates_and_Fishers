#!/usr/bin/python3
# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
from Item import Item 
from Weapon import Weapon

def testAssignname_Weapon(weapon,name,numberofsum,num):
	try:
		assert weapon.getAttack() == numberofsum
		try:
			assert weapon.getName() == name
		except (AssertionError):
			print("Error : Attack name:"+str(num))
	except(AssertionError):
		print("Error : Attack failed :"+str(num))

	

if __name__ == "__main__":

	sword = Weapon("ICE",100,0)
	sword1 = Weapon("ICE","NVO",10)
	sword2 = Weapon("ICE",2,10)
	sword3 = Weapon("ICE",1,10)
	sword4 = Weapon("ICE",0,0)
	sword5 = Weapon("ICE",100,-110)


	testAssignname_Weapon(sword,"ICE",100,1)
	testAssignname_Weapon(sword1,"ICE",100,2)
	testAssignname_Weapon(sword2,"ICE",20,3)
	testAssignname_Weapon(sword3,"ICE",10,4)
	testAssignname_Weapon(sword4,"ICE",0,5)
	testAssignname_Weapon(sword5,"ICE",0,6)

	print("Test has finished")
