#!/usr/bin/python3
# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
from Item import * 
from Defense import *
import random
import string 

def testAssignname_Defense(defense,name,numberofsum,num):
	if(len(name) >= 5 and len(name) <= 32):
		try:
			#print (defense.getDefense())
			assert defense.getDefense() == numberofsum
			try:
				assert defense.getName() == name
			except (AssertionError):
				print(" \033[91m Error : Defense name:"+str(num))
		except(AssertionError):
			print("\033[91m Error : Defense failed :"+str(num))
	else:
		try:
			#print (defense.getDefense())
			assert defense.getDefense() == numberofsum
		except(AssertionError):
			print("\033[91m Error : Defense failed :"+str(num))


def testfuncgetDamage(defense,damage,caseStudy):
	capacitydefense = defense.getDefense()
	if(capacitydefense > damage):
		try:
			assert defense.reportDamage(damage) == (capacitydefense-damage)
		except AssertionError:
				return "\033[91m Error in calculum of the values,case of test:"+str(caseStudy)+"\n"
		else:
				return "\033[93m Passed in test:" + str(caseStudy)
	else: # Class call the destructor, because that object not exist anymore.
		try:
			assert defense.reportDamage(damage) == 0
		except AssertionError:
				return "\033[91m Error in calculum of the values,case of test:"+str(caseStudy)+"\n"
		else:
				#print(defense.getDefense())
				#print(defense.getDetail())
				return "\033[93m Passed in test:"+str(caseStudy)

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
	
	for i in range(1000):
		"""
		Will generate 1000 diferent names, like capacity of defense
		, and will add in function of testfuncgetDamage
		"""
		tam = random.randint(0,100)
		randomnumb1 =  random.randint(0,10)
		randomnumb2 =  random.randint(0,10)
		wordgen = ''
		for j in range(tam): # just to generate random names
			lettersused = str(string.ascii_uppercase + string.digits + string.ascii_lowercase)
			wordgen += random.choice(lettersused)
		newdefense = Defense(wordgen,randomnumb1,randomnumb2)
		damage_random = random.randint(0,25) # low numbers 
		print(testfuncgetDamage(newdefense,damage_random,"L"+str(i)))
		#testfuncgetDamage(newdefense,damage_random,"L"+str(i))
		newdefense = Defense(wordgen,randomnumb1,randomnumb2)
		damage_random = random.randint(75,100) # big  numbers	
		print(testfuncgetDamage(newdefense,damage_random,"B"+str(i)))
		#testfuncgetDamage(newdefense,damage_random,"L"+str(i))
		
		
	print("Test has finished")
