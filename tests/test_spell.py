#!/usr/bin/python3
# -*- coding: utf-8 -*-


from Spell import Spell
import random
import string


def testWellFormated(spellobj,caseStudy):
	try:
		name = spellobj.getName()
		assert(len(name)>=5  and len(name)<=32 and type(name) is str)
	except AssertionError:
		print("Error there is a error on format of name,case study:"+str(caseStudy))
		exit()
	else:
		try:
			value = spellobj.getValue()
			assert(type(value) is int and value >=0 and value <=100)
		except AssertionError:	
			print("Error there is a error in definition of the value of the spell, case study:"+str(caseStudy))	
			exit()
		else:
			print("Test, sucessfull, case study:"+ str(caseStudy))
			return 0
		


def test_spell(spellobj,enter,numbenter,caseStudy):
	if(type(enter) is str):
		if(len(enter)<=32 and len(enter)>=5):
			try:
				assert(spellobj.getName() == enter)
			except AssertionError:
				print("Error Was generate other string for name, anomalously, case Study:"+str(caseStudy))
				exit()
			else:
				if(type(numbenter) is int):
					if(numbenter>=0 and numbenter<=100):
						try:
							assert(spellobj.getValue() == numbenter)
						except AssertionError:
							print("Error Was generate a number, anomalously, case Study:"+str(caseStudy))
							exit()
						else:
							print("Test, sucessfull,case study:"+str(caseStudy))
		else:			
			testWellFormated(spellobj,caseStudy)
	else:
		testWellFormated(spellobj,caseStudy)		


class Fortest(object):

	def __init__(self,numb):
		self.numb  = numb


if __name__ == "__main__":
	listsimple = []
	dicempty = {}
	emptyobj = Fortest(1)
	# first scenario, passing args that don't combine with description
	objtest = Spell(listsimple,1)
	test_spell(objtest,listsimple,1,1)
	objtest = Spell(dicempty,1)
	test_spell(objtest,dicempty,1,2)
	objtest = Spell(emptyobj,1)
	test_spell(objtest,emptyobj,1,3)

	objtest = Spell(1,listsimple)
	test_spell(objtest,1,listsimple,'s1')
	objtest = Spell(1,dicempty)
	test_spell(objtest,1,dicempty,'s2')
	objtest = Spell(1,emptyobj)
	test_spell(objtest,1,emptyobj,'s3')

	# Second scenario, test with whell formated args

	for i in range(1000):
		tam = random.randint(5,32)
		wordgen = ''
		for j in range(tam): # just to generate random names
			lettersused = str(string.ascii_uppercase + string.digits + string.ascii_lowercase)
			wordgen += random.choice(lettersused)
		intgenerated = random.randint(0,100)
		objtest = Spell(wordgen,intgenerated)
		caseStudy ="wellformated"+str(i)
		test_spell(objtest,wordgen,intgenerated,caseStudy)	
