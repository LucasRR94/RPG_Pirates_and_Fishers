#!/usr/bin/python3
# -*- coding: utf-8 -*-



from Individual import Individual


import random
import string 

def testName(individual,name,caseStudy):
	if(type(name)is str):
		if(len(name) >= 5 and len(name) <= 32):
			try:
				assert(individual.getName() == name)
			except AssertionError:
				print("Error to insert parameter: "+individual.getName()+"case study: "+str(caseStudy)+"\n")
			else:	
				print("Name was correctly insert, case study:" +str(caseStudy)+"\n")
		else:
			try:
				assert((len(individual.getName()))<=32 and (len(individual.getName()))>=5)
			except AssertionError:
				print("Error generated name of name: "+individual.getName()+" case study: "+str(caseStudy)+"\n")
			else:	
				print("Name was correctly insert, case study:" +str(caseStudy)+'\n')
	else:
		try:
			assert((len(individual.getName()))<=32 and (len(individual.getName()))>=5)
		except AssertionError:
			print("Error generated name of name: "+individual.getName()+" case study: "+str(caseStudy)+"\n")
		else:	
			print("Name was correctly insert, case study:" +str(caseStudy)+'\n')
	
def testHealth(individual,parameter,caseStudy):
	if(type(parameter) is int):
		if(parameter>=0 and parameter<=100):
			try:
				assert(individual.getHealth()==parameter)
			except AssertionError:
				print(" \033[91m Error, the parameter health was generate anomalously, study case: "+str(caseStudy))
			else:
				print("Test sucessfull, caseStudy:"+str(caseStudy)+"\n")
		else:
			try:
				assert(individual.getHealth()>=0 and individual.getHealth()<=100)
			except AssertionError:
				print(" \033[91m Error, the parameter health is outside of range, study case: "+str(caseStudy))
			else:
				print("Test sucessfull, caseStudy:"+str(caseStudy)+"\n")
	elif(type(parameter) is str):
		try:
			newparameter = int(parameter)
		except (TypeError,ValueError) as e:
			try:
				assert(individual.getHealth()>=0 and individual.getHealth()<=100)
			except AssertionError:
				print(" \033[91m Error, the parameter health is outside of range, study case: "+str(caseStudy))
			else:
				print("Test sucessfull, caseStudy: "+str(caseStudy)+"\n")
		else:
			if(newparameter>=0 and newparameter<=100):
				try:
					assert(individual.getHealth()==newparameter)
				except AssertionError:
					print(" \033[91m Error, the parameter health was generate anomalously, study case: "+str(caseStudy))
				else:
					print("Test sucessfull, caseStudy:"+str(caseStudy)+"\n")
			else:
				try:
					assert(individual.getHealth()>=0 and individual.getHealth()<=100)
				except AssertionError:
					print(" \033[91m Error, the parameter health is outside of range, study case: "+str(caseStudy))
				else:
					print("Test sucessfull, caseStudy:"+str(caseStudy)+"\n")
	else:
		try:
			assert(individual.getHealth()>=0 and individual.getHealth()<=100)
		except AssertionError:
			print("\033[91m Error, the parameter health is outside of range, study case: "+str(caseStudy))
		else:
			print("Test sucessfull, caseStudy:"+str(caseStudy)+"\n")

def testDefense(individual,parameter,caseStudy):

	if(type(parameter) is int):
		if(parameter>=0 and parameter<=100):
			try:
				assert(individual.getDefense()==parameter)
			except AssertionError:
				print(" \033[91m Error, the parameter defense was generate anomalously, study case: "+str(caseStudy))
			else:
				print("Test sucessfull, caseStudy:"+str(caseStudy)+"\n")
		else:
			try:
				assert(individual.getDefense()>=0 and individual.getDefense()<=100)
			except AssertionError:
				print("\033[91m Error, the parameter defense is outside of range, study case: "+str(caseStudy))
			else:
				print("Test sucessfull, caseStudy:"+str(caseStudy)+"\n")

	elif(type(parameter) is str):
		try:
			newparameter = int(parameter)
		except (TypeError,ValueError) as e:
			try:
				assert(individual.getDefense()>=0 and individual.getDefense()<=100)
			except AssertionError:
				print("\033[91m Error, the parameter defense is outside of range, study case: "+str(caseStudy))
			else:
				print("Test sucessfull, caseStudy: "+str(caseStudy)+"\n")
		else:
			if(newparameter>=0 and newparameter<=100):
				try:
					assert(individual.getDefense()==newparameter)
				except AssertionError:
					print(" \033[91m Error, the parameter defense was generate anomalously, study case: "+str(caseStudy))
				else:
					print("Test sucessfull, caseStudy:"+str(caseStudy)+"\n")
			else:
				try:
					assert(individual.getDefense()>=0 and individual.getDefense()<=100)
				except AssertionError:
					print(" \033[91m Error, the parameter defense is outside of range, study case: "+str(caseStudy))
				else:
					print("Test sucessfull, caseStudy:"+str(caseStudy)+"\n")
	else:
		try:
			assert(individual.getDefense()>=0 and individual.getDefense()<=100)
		except AssertionError:
			print(" \033[91m Error, the parameter defense is outside of range, study case: "+str(caseStudy))
		else:
			print("Test sucessfull, caseStudy:"+str(caseStudy)+"\n")	

def testAttack(individual,parameter,caseStudy):
	if(type(parameter) is int):
		if(parameter>=0 and parameter<=100):
			try:
				assert(individual.getAttack()==parameter)
			except AssertionError:
				print("\033[91m Error, the parameter attack was generate anomalously, study case: "+str(caseStudy))
			else:
				print("Test sucessfull, caseStudy:"+str(caseStudy)+"\n")
		else:
			try:
				assert(individual.getAttack()>=0 and individual.getAttack()<=100)
			except AssertionError:
				print("\033[91m Error, the parameter attack is outside of range, study case: "+str(caseStudy))
			else:
				print("Test sucessfull, caseStudy:"+str(caseStudy)+"\n")
	elif(type(parameter) is str):
		try:
			newparameter = int(parameter)
		except (TypeError,ValueError) as e:
			try:
				assert(individual.getAttack()>=0 and individual.getAttack()<=100)
			except AssertionError:
				print("\033[91m Error, the parameter attack is outside of range, study case: "+str(caseStudy))
			else:
				print("Test sucessfull, caseStudy:"+str(caseStudy)+"\n")
		else:
			if(newparameter>=0 and newparameter<=100):
				try:
					assert(individual.getAttack()==newparameter)
				except AssertionError:
					print(" \033[91m Error, the parameter attack was generate anomalously, study case: "+str(caseStudy))
				else:
					print("Test sucessfull, caseStudy:"+str(caseStudy)+"\n")
			else:
				try:
					assert(individual.getAttack()>=0 and individual.getAttack()<=100)
				except AssertionError:
					print(" \033[91m Error, the parameter attack is outside of range, study case: "+str(caseStudy))
				else:
					print("Test sucessfull, caseStudy:"+str(caseStudy)+"\n")
	else:
		try:
			assert(individual.getAttack()>=0 and individual.getAttack()<=100)
		except AssertionError:
			print("\033[91m Error, the parameter attack is outside of range, study case: "+str(caseStudy))
		else:
			print("Test sucessfull, caseStudy:"+str(caseStudy)+"\n")	



def testParameters(individual,name,parameters,caseStudy):
	testName(individual,name,caseStudy)
	testHealth(individual,parameters,caseStudy)
	testAttack(individual,parameters,caseStudy)
	testDefense(individual,parameters,caseStudy)


def testusignMedkit(individual,intmedkit,caseStudy):
	#individual.usingMedkit(intmedkit) using the int, that can be use for cure
	if(type(intmedkit) is int):
		oldvaluehealth = individual.getHealth()
		pretendvalue = oldvaluehealth + intmedkit 
		if(pretendvalue > 100):
			try:
				assert((individual.usingMedkit(intmedkit) == 1) and (individual.getHealth() == 100))
			except AssertionError:
				print("\033[91m  Error, value added exceeds the limit, study case: "+str(caseStudy)+" Should be : " +str(100)+ " ,Is:"+str(individual.getHealth())+'\n')
				exit()
			else:
				print("Test sucessfull: "+str(caseStudy)+'\n')

		elif(pretendvalue < 0):
			try:
				assert(((individual.usingMedkit(intmedkit) == 0) and (individual.getHealth() == oldvaluehealth)))
			except AssertionError:
				print("\033[91m Error , value added lower than it should, study case: "+str(caseStudy)+" Should be : " +str(oldvaluehealth)+ " ,Is: "+str(individual.getHealth())+'\n')
				exit()
			else:
				print("Test sucessfull: "+str(caseStudy)+'\n')
		else:
			try:
				assert(((individual.usingMedkit(intmedkit) == 1) and (individual.getHealth() == pretendvalue)))
			except AssertionError:
				print("\033[91m Error , value does  not match the sum : "+str(caseStudy)+" Should be : " +str(pretendvalue)+ " ,Is: "+str(individual.getHealth())+'\n')
				exit()
			else:
				print("Test sucessfull: "+str(caseStudy)+'\n')

	elif(type(intmedkit)is str):
		try:
			newnumb = int(intmedkit)
		except (ValueError,TypeError) as e:
			try:
				assert(individual.usingMedkit(intmedkit)==0)
			except:
				print("\033[91m Error , that was added a strange value in health, case study: "+str(caseStudy)+'\n')
				exit()
			else:
				print("Test sucessfull: "+str(caseStudy)+'\n')
		else:
			oldvaluehealth = individual.getHealth()
			pretendvalue = oldvaluehealth + newnumb 
			if(pretendvalue > 100):
				try:
					assert((individual.usingMedkit(intmedkit) == 1) and (individual.getHealth() == 100))
				except AssertionError:
					print("\033[91m Error , value added exceeds the limit, study case: "+str(caseStudy)+" Should be : " +str(100)+ " ,Is: "+str(individual.getHealth())+'\n')
					exit()
				else:
					print("Test sucessfull: "+str(caseStudy)+'\n')
			elif(pretendvalue < 0):
				try:
					assert(((individual.usingMedkit(intmedkit) == 0) and (individual.getHealth() == oldvaluehealth)))
				except AssertionError:
					print("\033[91m Error , value added lower than it should, study case: ",int(caseStudy)+" Should be : "+str(oldvaluehealth)+ " ,Is: "+str(individual.getHealth())+'\n')
					exit()
				else:
					print("Test sucessfull: "+str(caseStudy)+'\n')
			else:
				try:
					assert(((individual.usingMedkit(intmedkit) == 1) and (individual.getHealth() == pretendvalue)))
				except AssertionError:
					print("\033[91m Error , value does  not match the sum : ",int(caseStudy)+" Should be : " +str(pretendvalue)+ " ,Is: "+str(individual.getHealth())+'\n')
					exit()
				else:
					print("Test sucessfull: "+str(caseStudy)+'\n')
	
	else:
		try:
			oldvaluehealth = individual.getHealth()
			assert((individual.usingMedkit(intmedkit) == 0) and (individual.getHealth() == oldvaluehealth))
		except AssertionError:
			print("\033[91m Error Error, that was added a strange value in health, case study: "+str(caseStudy)+" Should be : "+str(pretendvalue)+ " ,Is: "+str(individual.getHealth())+'\n')
			exit()
		else:
			print("Test sucessfull: "+str(caseStudy)+'\n')

def testchangeAttack():
	pass

def testchangeDefense():
	pass

def testgetdamage():
	pass

class simpleClass(object):
	def __init__(self,principal):
		self.principal = principal

if __name__ == "__main__":
	listsimple = []
	simpleobject = simpleClass(1)
	genIndividual = Individual(listsimple,listsimple,listsimple,listsimple)
	testParameters(genIndividual,listsimple,listsimple,"B1")
	genIndividual = Individual(simpleobject,simpleobject,simpleobject,simpleobject)
	testParameters(genIndividual,simpleobject,simpleobject,"B2")
	for i in range(1000):
		tam = random.randint(0,190)
		wordgen = ''
		for j in range(tam): # just to generate random names
			lettersused = str(string.ascii_uppercase + string.digits + string.ascii_lowercase)
			wordgen += random.choice(lettersused)
		genIndividual = Individual(wordgen,tam,tam,tam)
		testParameters(genIndividual,wordgen,tam,i)


	# test using Medkit
	wordgen = ''
	for j in range(25): # just to generate random names
		lettersused = str(string.ascii_uppercase + string.digits + string.ascii_lowercase)
		wordgen += random.choice(lettersused)
	randomhealth = random.randint(0,100)
	for i in range(1000):
		randomhealth = random.randint(0,100)	
		randomkitmed = random.randint(-1000,1000)
		genIndividual = Individual(wordgen,randomhealth,10,10)
		testusignMedkit(genIndividual,randomhealth,i)
	testusignMedkit(genIndividual,listsimple,"C1")
	testusignMedkit(genIndividual,simpleobject,"C2")
