#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Medkit import Medkit
import random
import string 


#def testcreationclass(medkit,name,healing,numbCase):

def testifparameterIsBeeingused(medkit,parameter,caseNumb):
	if(type(parameter) is int):
		if(parameter >= 0 and parameter<101):
			try:
				assert(medkit.getHealing() == parameter)
			except AssertionError:
				print("Error parameter well format not set, error , case study:",str(caseNumb))
		else:
			try:
				assert(medkit.getHealing()==0)
			except AssertionError:
				print("\033[91m  Error, other wrong number seted case numb: ",str(caseNumb),"\n")
			else:
				print("test successful")

def testnameinclass(medkit,name,healing,numbCase):
	if(len(name)>=5 and len(name)<=32):
		try:
			assert (medkit.getName() == name)
		except AssertionError:
			return("\033[91m Error, there problems in setting of name,Number of teste:",' Tn'+str(numbCase)+'\n')
		else: # test the healing values
			try:
				assert ((type(medkit.getHealing()) is int) and (medkit.getHealing() > 0 and medkit.getHealing()< 101))
			except AssertionError:
				return("\033[91m Error of type insert values in class, study case:",' Tn'+str(numbCase)+'\n')	
			else:
				return("Ok,test successful, case study:",' Tn'+str(numbCase)+'\n')
	else:
		if(len(medkit.getName())>=5 and len(medkit.getName())<=32 ):
			try:
				assert ((type(medkit.getHealing()) is int) and (medkit.getHealing() >= 0 and medkit.getHealing()< 101))
			except AssertionError:
				return("\033[91m Error of type insert values in class, study case:",' Tn'+str(numbCase)+'\n')	
			else:
				return("Ok,test successful, case study:",' Tn'+str(numbCase)+'\n')
		else:
			return("\033[91m Error on formatted of name, case study:",' Tn'+str(numbCase)+'\n')		

class RandomClass(object):
	def __init__(self,numb):
		self.numb = numb



def testhealingreturn(medkit,numbCase):	
	try:
		assert(len(medkit.getName())>=5 and len(medkit.getName())<=32)
	except AssertionError:
		print("\033[91m  Error, in the format of name,","Testforcedhealing"+str(numbCase))
	else:
		try:
			assert((type(medkit.getHealing()) is int) and (medkit.getHealing() >= 0 and medkit.getHealing()< 101))
		except AssertionError:
			print("\033[91m  Error in format of numb healing, case of test:","Testforcedhealing"+str(numbCase))
		else:
			print("test successful: ","Testforcedhealing"+str(numbCase))


def testhealinguse(medkit,healingprovid,numbCase):
	try:
		used = medkit.useHealing()
		assert((used == healingprovid))
	except AssertionError:
		print("Error in case of test: "+str(numbCase)+" ,Shoud bee provide: "+str(healingprovid)+",Was provide: "+str(used)+'\n')
	else:
		try:
			assert(medkit.getHealing() == 0)
		except AssertionError:
			print("Error, object was not destroyed, study case: "+str(numbCase))	
		else:
			print("Test successful, study case:"+str(numbCase))	
				
if __name__ == "__main__":
	# first fase : test, forced names that can't be use
	for i in range(1000):
		tam = random.randint(0,100)
		wordgen = ''
		for j in range(tam): # just to generate random names
			lettersused = str(string.ascii_uppercase + string.digits + string.ascii_lowercase)
			wordgen += random.choice(lettersused)
		genobject = Medkit(wordgen,tam)
		print(testnameinclass(genobject,wordgen,tam,i))
		testifparameterIsBeeingused(genobject,tam,i)
	
	# second fase: test ,different parameters in healing that can't be use
	wordgen = ''
	tam = random.randint(101,1000)
	for j in range(tam): # just to generate random names
		lettersused = str(string.ascii_uppercase + string.digits + string.ascii_lowercase)
		wordgen += random.choice(lettersused)

	randomList =[1]
	randomString = "m"
	randClass = RandomClass(10)
	genobject = Medkit(wordgen,randomList)
	testhealingreturn(genobject,1)
	genobject = Medkit(wordgen,randomString)
	testhealingreturn(genobject,2)
	genobject = Medkit(wordgen,randClass)
	testhealingreturn(genobject,3)
	# third fase : using method getHealing, test if destroy the object
	for i in range(1000):
		tam = random.randint(1,100)
		useObjectTest = Medkit(wordgen,tam)
		testhealinguse(useObjectTest,tam,i)