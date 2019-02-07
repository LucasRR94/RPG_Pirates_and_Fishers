#!/usr/bin/python3
# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
from Item import * 
from Defense import *

def testAssignname_Defense(weapon,name,numberofsum,num):
	try:
		#print (weapon.getDefense())
		assert weapon.getDefense() == numberofsum
		try:
			assert weapon.getName() == name
		except (AssertionError):
			print("Error : Defense name:"+str(num))
	except(AssertionError):
		print("Error : Defense failed :"+str(num))

	

if __name__ == "__main__":

	sword = Defense("ICE",10,10)
	sword1 = Defense("ICE","NVO",10)
	sword2 = Defense("ICE",2,10)
	sword3 = Defense("ICE",1,10)
	sword4 = Defense("ICE",0,0)
	sword5 = Defense("ICE",100,-110)


	testAssignname_Defense(sword,"ICE",100,1)
	testAssignname_Defense(sword1,"ICE",100,2)
	testAssignname_Defense(sword2,"ICE",20,3)
	testAssignname_Defense(sword3,"ICE",10,4)
	testAssignname_Defense(sword4,"ICE",0,5)
	testAssignname_Defense(sword5,"ICE",0,6)

	print("Test has finished")