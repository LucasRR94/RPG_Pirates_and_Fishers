#!/usr/bin/python3
# -*- coding: utf-8 -*-

from libGamePiratesAndFishers import *
import random

def funcTestLibLimitedNumber(enter,limit,testnumb):
	if(limit==0):
		testvariable = makeSureThatIsnumberLimited(enter,10)
		try:
			assert(type(testvariable)==int)
		except AssertionError:
			print("Error, in type of return, number of test",testnumb,"Type:",type(testvariable))
			exit()
		else:
			return 1
	else:
		testvariable = makeSureThatIsnumberLimited(enter,limit)
		try:
			assert(type(testvariable)==int)
		except AssertionError:
			print("Error, in type of return, number of test",testnumb,"Type:",type(testvariable))
			exit()
		else:
			try:
				assert(testvariable >= 0 and testvariable<=limit)

			except AssertionError:
				print("Error, in type limit of values , number of test",testnumb,"the number is",testvariable," The limit is:",limit)
				exit()	
			else:
				return 1	

class Testclass(object):
	def __init__(self,enter):
		self.enter = enter
	def getEnter(self):
		return enter

class SecondTestclass(object):
	def __init__(self,enter):
		self.enter = enter

####################################################


def funcTestassertIfIsWeelFormat(enter,testnumb):
	testwordgen = assertIfIsWeelFormat(enter)
	tamword = len(testwordgen)
	try:
		tam = len(enter) 
	except NameError:
		try:
			assert(tamword>=5 and tamword<33)
		except AssertionError:
			print("Error, in the size of names generated , number of letters in name: ",tamword," Number of test:",testnumb)
			exit()
		else:
			return 1

	except TypeError: # then enter is not an number
		try:
			assert(tamword>=5 and tamword<33)
		except AssertionError:
			print("Error, in the size of names generated , number of letters in name: ",tamword," Number of test:",testnumb)
			exit()
		else:
			return 1
					
	else:
		if(tam >= 5 and tam <= 32):
			try:
				assert(testwordgen == enter)
			except AssertionError:
				print(" The generator, is generated a word unnecessarily, generated: ",testwordgen," name generated: ",enter," Number of test",testnumb)		
				exit()
			else:
				return 1
		else:
			try:
				assert(tamword>=5 and tamword<33)
			except AssertionError:
				print("Error, in the size of names generated , number of letters in name",tamword," Number of test:",testnumb)
				exit()
			else:
				return 1
			finally:
				return 1		

		 

if __name__ == "__main__":
	listtest = []
	objecttest1 = Testclass(1)
	objecttest2 = SecondTestclass(1)
	firstString = "ASDASDJVCJVJXCVJXC"
	secondString= "As"
	thirdString = "1"
	fourString= "DAJDJASHDCBBXCJXZCKJJHH@!DHADASDAJSDJJ!J#@!JNCNSNDCSDKCKDSCNSCN"	
	for i in range(10):
		funcTestLibLimitedNumber(10,100,1)
		funcTestLibLimitedNumber(10,0,2)
		funcTestLibLimitedNumber(1,100,3)
		funcTestLibLimitedNumber(1,0,4)
		funcTestLibLimitedNumber(objecttest1,100,5)	
		funcTestLibLimitedNumber(objecttest1,0,6)
		funcTestLibLimitedNumber(objecttest2,100,6)	
		funcTestLibLimitedNumber(objecttest2,0,7)
		funcTestLibLimitedNumber(firstString,100,8)	
		funcTestLibLimitedNumber(firstString,0,9)
		funcTestLibLimitedNumber(secondString,100,10)	
		funcTestLibLimitedNumber(secondString,0,11)
		funcTestLibLimitedNumber(thirdString,100,12)	
		funcTestLibLimitedNumber(thirdString,0,13)
		funcTestLibLimitedNumber(fourString,100,14)	
		funcTestLibLimitedNumber(fourString,0,15)
		funcTestLibLimitedNumber(listtest,100,16)	
		funcTestLibLimitedNumber(fourString,0,17)
	# testar a funcao que gera nomes.
	funcTestassertIfIsWeelFormat(listtest,1001)
	funcTestassertIfIsWeelFormat(objecttest1,1002)
	funcTestassertIfIsWeelFormat(objecttest2,1003)
	funcTestassertIfIsWeelFormat(firstString,1004)
	funcTestassertIfIsWeelFormat(secondString,1005)
	funcTestassertIfIsWeelFormat(thirdString,1006)
	funcTestassertIfIsWeelFormat(fourString,1007)
	for i in range(1000):
		tam = random.randint(0,100)
		wordgen = ''
		for i in range(tam): # just to generate random names
			lettersused = str(string.ascii_uppercase + string.digits + string.ascii_lowercase)
			wordgen += random.choice(lettersused)	
		funcTestassertIfIsWeelFormat(wordgen,i)
		funcTestassertIfIsWeelFormat(tam,i)