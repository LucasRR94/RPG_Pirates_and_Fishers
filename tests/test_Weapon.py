#!/usr/bin/python3
# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
from Item import Item 
from Weapon import Weapon
import random
import string 

def testAssignname_Weapon(weapon,name,numberofsum,num):
	if(len(name)<=32 and len(name)>=5):
		try:
			assert weapon.getAttack() == numberofsum
		except(AssertionError):
			print("Error : Attack failed :"+str(num))
		else:
			try:
				assert weapon.getName() == name
			except (AssertionError):
				print("Error : Attack name:"+str(num))
			else:
				print("test successfull, number:",num,'\n')

	else:
		try:
			assert weapon.getAttack() == numberofsum
		except(AssertionError):
			print("Error : Attack failed :"+str(num))
		else:
				print("test successfull, number:",num,'\n')	
	

if __name__ == "__main__":

	sword = Weapon("ICE",100,0)
	sword1 = Weapon("ICE","NVO",10)
	sword2 = Weapon("ICE",2,10)
	sword3 = Weapon("ICE",1,10)
	sword4 = Weapon("ICE",0,0)
	sword5 = Weapon("ICE",100,-110)

	
	print(sword.getDetail())
	print(sword1.getDetail())
	print(sword2.getDetail())
	print(sword3.getDetail())
	print(sword4.getDetail())
	print(sword5.getDetail())
	testAssignname_Weapon(sword,"ICE",100,1)
	testAssignname_Weapon(sword1,"ICE",100,2)
	testAssignname_Weapon(sword2,"ICE",20,3)
	testAssignname_Weapon(sword3,"ICE",10,4)
	testAssignname_Weapon(sword4,"ICE",0,5)
	testAssignname_Weapon(sword5,"ICE",0,6)
	
	for i in range(1000):
		randomimpact1 =  random.randint(0,10)
		randomspeed1 =  random.randint(0,10)
		tam = random.randint(0,100)
		wordgen = ''
		for j in range(tam): # just to generate random names
			lettersused = str(string.ascii_uppercase + string.digits + string.ascii_lowercase)
			wordgen += random.choice(lettersused)
		genericobject = Weapon(wordgen,randomimpact1,randomspeed1)
		testAssignname_Weapon(genericobject,wordgen,randomimpact1*randomspeed1,i)

	print("Test has finished")
