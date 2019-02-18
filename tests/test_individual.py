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
				assert(((individual.usingMedkit(intmedkit) == 1) and (individual.getHealth() == oldvaluehealth)))
			except AssertionError:
				print("\033[91m Error , value added lower than it should, study case: "+str(caseStudy)+" Should be : " +str(oldvaluehealth)+ " ,Is: "+str(individual.getHealth())+'\n')
				exit()
			else:
				print("Test sucessfull: "+str(caseStudy)+'\n')
		
		elif(pretendvalue < oldvaluehealth):
			try:
				assert(((individual.usingMedkit(intmedkit) == 1) and (individual.getHealth() == oldvaluehealth)))
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
			elif(pretendvalue < 0 and newnumb < 0):
				try:
					assert(((individual.usingMedkit(intmedkit) == 1) and (individual.getHealth() == oldvaluehealth)))
				except AssertionError:
					print("\033[91m Error , value added lower than it should, study case: "+str(caseStudy)+" Should be : "+str(oldvaluehealth)+ " ,Is: "+str(individual.getHealth())+'\n')
					exit()
				else:
					print("Test sucessfull: " +str(caseStudy)+'\n')
			elif(pretendvalue < oldvaluehealth):
				try:
					assert(((individual.usingMedkit(intmedkit) == 1) and (individual.getHealth() == oldvaluehealth)))
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
	
	else:
		try:
			oldvaluehealth = individual.getHealth()
			assert((individual.usingMedkit(intmedkit) == 0) and (individual.getHealth() == oldvaluehealth))
		except AssertionError:
			print("\033[91m Error Error, that was added a strange value in health, case study: "+str(caseStudy)+" Should be : "+str(pretendvalue)+ " ,Is: "+str(individual.getHealth())+'\n')
			exit()
		else:
			print("Test sucessfull: "+str(caseStudy)+'\n')



def testchangeAttack(individual,newattack,caseStudy):
	#individual.changeAttack((int) newattackvalue) --> function
	if(type(newattack) is int):
		oldvalueattack = individual.getAttack()
		resultfunc = individual.changeAttack(newattack)
		if(newattack > 100):
			try:
				assert((resultfunc == oldvalueattack) and (individual.getAttack() == 100))
			except AssertionError:
				print("\033[91m  Error, value added exceeds the limit, study case: "+str(caseStudy)+" Should be : " +str(100)+ " ,Is:"+str(individual.getAttack())+'\n')
				exit()
			else:
				print("Test sucessfull: "+str(caseStudy)+'\n')

		elif(newattack < 0):
			try:
				assert((resultfunc == oldvalueattack) and (individual.getAttack() == 0))
			except AssertionError:
				print("\033[91m Error , value added lower than it should, study case: "+str(caseStudy)+" Should be : " +str(resultfunc)+ " ,Is: "+str(individual.getAttack())+'\n')
				exit()
			else:
				print("Test sucessfull: "+str(caseStudy)+'\n')
		else:
			try:
				assert((resultfunc == oldvalueattack) and (individual.getAttack() == newattack))
			except AssertionError:
				print("\033[91m Error , value does  not match the sum : "+str(caseStudy)+" Should be : " +str(newattack)+ " ,Is: "+str(individual.getAttack())+'\n')
				exit()
			else:
				print("Test sucessfull: "+str(caseStudy)+'\n')

	elif(type(newattack) is str):
		try:
			newnumb = int(newattack)
		except (ValueError,TypeError) as e:
			try:
				resultfunc = individual.changeAttack(newattack)
				assert(resultfunc[0]==None)
			except:
				print("\033[91m Error , that was added a strange value in attack, case study: "+str(caseStudy)+'\n')
				exit()
			else:
				print("Test sucessfull: "+str(caseStudy)+'\n')
		else:
			oldvalueattack = individual.getAttack()
			if(newnumb > 100):
				try:
					resultfunc = individual.changeAttack(newnumb)
					assert((resultfunc == oldvalueattack ) and (individual.getAttack() == 100))
				except AssertionError:
					print("\033[91m Error , value added exceeds the limit, study case: "+str(caseStudy)+" Should be : " +str(100)+ " ,Is: "+str(individual.getDefense())+'\n')
					exit()
				else:
					print("Test sucessfull: "+str(caseStudy)+'\n')

			elif(newnumb < 0):
				try:
					resultfunc = individual.changeAttack(newnumb)
					assert((resultfunc == oldvalueattack ) and (individual.getAttack() == 0))
				except AssertionError:
					print("\033[91m Error , value added lower than it should, study case: ",int(caseStudy)+" Should be : "+str(oldvalueattack)+ " ,Is: "+str(individual.getAttack())+'\n')
					exit()
				else:
					print("Test sucessfull: " +str(caseStudy)+'\n')
			else:
				try:
					resultfunc = individual.changeAttack(newnumb)
					assert((resultfunc == oldvalueattack ) and (individual.getAttack() == newnumb))
				except AssertionError:
					print("\033[91m Error , value does  not match the sum : ",int(caseStudy)+" Should be : " +str(pretendvalue)+ " ,Is: "+str(individual.getAttack())+'\n')
					exit()
				else:
					print("Test sucessfull: "+str(caseStudy)+'\n')

	else:
		oldvalueattack = individual.getAttack()
		try:
			resultfunc = individual.changeAttack(newattack)
			assert((individual.getAttack()==oldvalueattack) and (not(individual.getAttack() == newattack)) and(resultfunc[0] == None))
		except AssertionError:
			print("\033[91m Error, anomalously sum tho the attribute attack, Case study: ",caseStudy,"\n")
			exit()
		else:
			print("Test sucessfull, case study: ",caseStudy,"\n")



def testchangeDefense(individual,newdefense,caseStudy):
	#individual.changeDefense((int) newdefense(value) --> function
	if(type(newdefense) is int):
		oldvaluedefense = individual.getDefense()
		resultfunc = individual.changeDefense(newdefense)
		if(newdefense > 100):
			try:
				assert((resultfunc == oldvaluedefense) and (individual.getDefense() == 100))
			except AssertionError:
				print("\033[91m  Error, value added exceeds the limit, study case: "+str(caseStudy)+" Should be : " +str(100)+ " ,Is:"+str(individual.getDefense())+'\n')
				exit()
			else:
				print("Test sucessfull: "+str(caseStudy)+'\n')

		elif(newdefense < 0):
			try:
				assert((resultfunc == oldvaluedefense) and (individual.getDefense() == 0))
			except AssertionError:
				print("\033[91m Error , value added lower than it should, study case: "+str(caseStudy)+" Should be : " +str(resultfunc)+ " ,Is: "+str(individual.getDefense())+'\n')
				exit()
			else:
				print("Test sucessfull: "+str(caseStudy)+'\n')
		else:
			try:
				assert((resultfunc == oldvaluedefense) and (individual.getDefense() == newdefense))
			except AssertionError:
				print("\033[91m Error , value does  not match the sum : "+str(caseStudy)+" Should be : " +str(newdefense)+ " ,Is: "+str(individual.getDefense())+'\n')
				exit()
			else:
				print("Test sucessfull: "+str(caseStudy)+'\n')

	elif(type(newdefense) is str):
		try:
			newnumb = int(newdefense)
		except (ValueError,TypeError) as e:
			try:
				resultfunc = individual.changeDefense(newdefense)
				assert(resultfunc[0]==None)
			except:
				print("\033[91m Error , that was added a strange value in defense, case study: "+str(caseStudy)+'\n')
				exit()
			else:
				print("Test sucessfull: "+str(caseStudy)+'\n')
		else:
			oldvaluedefense = individual.getDefense()
			if(newnumb > 100):
				try:
					resultfunc = individual.changeDefense(newnumb)
					assert((resultfunc == oldvaluedefense ) and (individual.getDefense() == 100))
				except AssertionError:
					print("\033[91m Error , value added exceeds the limit, study case: "+str(caseStudy)+" Should be : " +str(100)+ " ,Is: "+str(individual.getDefense())+'\n')
					exit()
				else:
					print("Test sucessfull: "+str(caseStudy)+'\n')

			elif(newnumb < 0):
				try:
					resultfunc = individual.changeDefense(newnumb)
					assert((resultfunc == oldvaluedefense ) and (individual.getDefense() == 0))
				except AssertionError:
					print("\033[91m Error , value added lower than it should, study case: ",int(caseStudy)+" Should be : "+str(oldvaluedefense)+ " ,Is: "+str(individual.getDefense())+'\n')
					exit()
				else:
					print("Test sucessfull: " +str(caseStudy)+'\n')
			else:
				try:
					resultfunc = individual.changeDefense(newnumb)
					assert((resultfunc == oldvaluedefense ) and (individual.getDefense() == newnumb))
				except AssertionError:
					print("\033[91m Error , value does  not match the sum : ",int(caseStudy)+" Should be : " +str(pretendvalue)+ " ,Is: "+str(individual.getDefense())+'\n')
					exit()
				else:
					print("Test sucessfull: "+str(caseStudy)+'\n')

	else:
		oldvaluedefense = individual.getDefense()
		try:
			resultfunc = individual.changeDefense(newdefense)
			assert((individual.getDefense()==oldvaluedefense) and (not(individual.getDefense() == newdefense)) and(resultfunc[0] == None))
		except AssertionError:
			print("\033[91m Error, anomalously sum tho the attribute defense, Case study: ",caseStudy,"\n")
			exit()
		else:
			print("Test sucessfull, case study: ",caseStudy,"\n")

	

def testgetdamage(individual,causeDamage,caseStudy):
	#individual.getDamage(causeDamage) # that is responsible by passing a damage to defense and health 0...200
	if((type(causeDamage) is str) or (type(causeDamage) is int)):
		newnumb = causeDamage
		if(type(causeDamage) is str):
			try:
				newnumb = int(causeDamage)
			except ValueError:
				backuphealth  = individual.getHealth()
				backupdefense = individual.getDefense()
				result = individual.getDamage(causeDamage)
				try:
					assert(result == 0 and backupdefense == individual.getDefense() and backuphealth  == individual.getHealth())
				except AssertionError:
					print("Error, anomalously, not possible convert str object, subtracted from health ou defense, case study: "+str(caseStudy))
					return 0
				else:
					print("Test sucessfull,not possible convert str object, case study:"+str(caseStudy))
					return 0

			if(newnumb > 0):
				if(newnumb <= individual.getDefense()):
					valueexceedofdefense = individual.getDefense() - newnumb
					backuphealth = individual.getHealth()
					try:
						result = individual.getDamage(newnumb)
						assert(result == 1 and backuphealth == individual.getHealth() and valueexceedofdefense == individual.getDefense())
					except AssertionError:
						print("Error , that was necessary this value for defense: "+str(valueexceedofdefense)+"but function returns : "+str(individual.getDefense())+"case study: "+str(caseStudy))
					else:
						print("Test sucessfull, case study: "+str(caseStudy))
				else:
					backuphealth = individual.getHealth()
					backupdefense = individual.getDefense()
					result = individual.getDamage(newnumb)
					valueexceedofdefense = newnumb - backupdefense 
					if(valueexceedofdefense >= backuphealth): # death
						try:
							assert(individual.getHealth() == None and individual.getDefense()==None and individual.getAttack() == None and result == 1)
						except AssertionError:
							print("Error, (case when defense and health exist )this object should that be destroyed, study case: "+str(caseStudy))
						else:
							print("Test sucessfull, Study case: "+str(caseStudy))
					else:	#alive
						try:
							assert(individual.getDefense() == 0 and individual.getHealth() == (backuphealth - valueexceedofdefense) and result == 1)
						except AssertionError:
							print("Error, (case when defense was gone and there is just health),health should be: "+str((backuphealth - valueexceedofdefense))+" it is: "+str(individual.getHealth())+" Case study: "+str(caseStudy))
						else:
							print("Test sucessfull, Study case: "+str(caseStudy))	
			else:
				backuphealth  = individual.getHealth()
				backupdefense = individual.getDefense()
				result = individual.getDamage(newnumb)
				try:
					assert(result == 1 and backupdefense == individual.getDefense() and backuphealth  == individual.getHealth())
				except AssertionError:
					print("Error, (Case numb less than zero ), anomalously subtracted from health ou defense, case study: "+str(caseStudy))
					return 0
				else:
					print("Test sucessfull, case study:"+str(caseStudy))
					return 0

		
	else:
		backuphealth  = individual.getHealth()
		backupdefense = individual.getDefense()
		result = individual.getDamage(causeDamage)
		
		try:
			assert(result == 0 and backupdefense == individual.getDefense() and backuphealth  == individual.getHealth())
		except AssertionError:
			print("Error, (object is not a str or int)anomalously subtracted from health ou defense, case study: "+str(caseStudy))
		else:
			print("Test sucessfull, case study:"+str(caseStudy))
	return 0
	#pass

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
		randomkitmed2 = random.randint(-1000,100)
		genIndividual = Individual(wordgen,randomhealth,10,10)
		testusignMedkit(genIndividual,randomhealth,('f'+str(i)))
		testusignMedkit(genIndividual,randomkitmed2 ,('s'+str(i)))
		testusignMedkit(genIndividual,str(randomkitmed),('fs'+str(i)))
		testusignMedkit(genIndividual,str(randomkitmed2),('ss'+str(i)))
	randomhealth = random.randint(0,100)
	genIndividual = Individual(wordgen,randomhealth,10,10)
	testusignMedkit(genIndividual,listsimple,"C1")
	testusignMedkit(genIndividual,simpleobject,"C2")
	# test testchangeAttack 
	testchangeAttack(genIndividual,listsimple,"O1")
	testchangeAttack(genIndividual,simpleobject,"O2")
	for i in range(1000):
		randomparameter = random.randint(0,100)	
		randomattack = random.randint(-1000,1000)
		randomattack2 = random.randint(-1000,100)
		genIndividual = Individual(wordgen,randomparameter,randomparameter,randomparameter)
		testchangeAttack(genIndividual,randomattack,('testchangeAttack: '+str(i)))
		testchangeAttack(genIndividual,randomattack2,('testchangeAttack1: '+str(i)))
		testchangeAttack(genIndividual,str(randomattack),('testchangeAttacks:'+str(i)))
		testchangeAttack(genIndividual,str(randomattack2),('testchangeAttackss:'+str(i)))
	
	# test testchangeDefense
	randomdefense = random.randint(0,100)
	genIndividual = Individual(wordgen,10,10,randomdefense)
	testchangeDefense(genIndividual,listsimple,"D1")
	testchangeDefense(genIndividual,simpleobject,"D2")
	for i in range(1000):
		randomparameter = random.randint(0,100)	
		randomDefense = random.randint(-1000,1000)
		randomDefense2 = random.randint(-1000,100)
		genIndividual = Individual(wordgen,randomparameter,randomparameter,randomparameter)
		testchangeDefense(genIndividual,randomDefense,('testchangeDefense: '+str(i)))
		testchangeDefense(genIndividual,randomDefense2,('testchangeDefense1:'+str(i)))
		testchangeDefense(genIndividual,str(randomDefense),('testchangeDefenses:'+str(i)))
		testchangeDefense(genIndividual,str(randomDefense2),('testchangeDefensess:'+str(i)))
	#testgetdamage
	genIndividual = Individual(wordgen,100,100,100)
	testgetdamage(genIndividual,listsimple,"OS1")
	testgetdamage(genIndividual,simpleobject,"OS2")
	testgetdamage(genIndividual,"Norad","OS3")
	testgetdamage(genIndividual,"-1000","OS4")
	
	#exit()
	for i in range(1000):
		randomparameter = random.randint(1,100)	
		randomdamagevalue = random.randint(-1000,1000)
		genIndividual = Individual(wordgen,randomparameter,randomparameter,randomparameter)
		testgetdamage(genIndividual,randomdamagevalue,('testgetdamage: '+str(i)))
		testgetdamage(genIndividual,str(randomdamagevalue),('testgetdamages:'+str(i)))
		