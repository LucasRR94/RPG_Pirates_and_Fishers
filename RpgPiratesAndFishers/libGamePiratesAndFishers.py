#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import string

def genRandomName(tam):
	""" 
		This Function generate random Strings, it receive a length of Strings.Its possible to 
		create strings that are composed by lowercase , uppercase  and numbers
		

		@param tam :(int) it's number that inform to the function the length of string, that will be generate.

		@return : (String) A random string , with the length that is informed in parameter
	"""
	wordgen = ''
	for i in range(tam):
		lettersused = str(string.ascii_uppercase+string.digits+string.ascii_lowercase)
		wordgen += random.choice(lettersused)
	return wordgen

def lenCheckString(word):
	""" 
		This Function test the size of a string passed by args, if is not between 5 and 32 characters, it return 0
		else return 1
		

		@param tam :(int) it's number that inform to the function the length of string, that will be generate.

		@return : (String) A random string , with the length that is informed in parameter
	"""
	tam = len(str(word))
	if(tam < 5 or tam >  32):
		return 0
	else:
		return 1


def assertFormat(enter):
	""" 
		This Function test if the argument is String between 5 and 32 characteres, if is not, return 0, if is return 1.
		

		@param enter :(unknow) could be an integer or string or other type of data that will be passed by the user.

		@return : (int) 0 or 1, 1 if is a string between 5 and 32 characters, 0 if is not.
	"""
	wordnew = str(enter)
	if((type(enter) == str)):
		return(lenCheckString(enter))
	else:
		try:
			wordnew = str(enter) 
		except TypeError:
			wordnew = "PAT" # have just three caracteres
		finally:
			return(lenCheckString(wordnew))

def assertIfIsWeelFormat(enter):
	""" 
		This Function test if the argument is String between 5 and 32 characters, if is not, return a random name
		generator between 5 ... 32 characters, if is return the argument enter passed.
		

		@param enter :(unknow) could be an number or string that will be passed by the user.

		@return : (string) between 5 ... 32 characters
	"""
	if(assertFormat(enter) == 1):
		return enter
	if(assertFormat(enter) == 0):
		return (genRandomName(random.randint(5,32)))

def makeSureThatIsnumberLimited(enter,limit):
	""" 
		This Function test if the argument enter is a integer, and test if the number is inside of ranger
		between 0...100

		

		@param enter :(unknow) could be an number or string that will be passed.
		@param limit :(limit) number between 0 and 100, that limits the return

		@return : (int) integer between 0 ... 100 .
	"""
	if(type(enter)== str):
		try:
			newnumb = int(enter)
		except ValueError:
			newnumb = random.randint(0,limit)
		else:
			if(newnumb > limit):
				newnumb = limit
			if(newnumb < 0):
				newnumb = 0
		finally:
			return newnumb
	elif(type(enter) == int):
		newnumb = enter
		if(newnumb > limit):
				newnumb = limit
		if(newnumb < 0):
				newnumb = 0	
		return newnumb
	else:
		return	(random.randint(0,limit))