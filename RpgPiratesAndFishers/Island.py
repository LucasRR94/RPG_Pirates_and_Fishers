#!/usr/bin/python3
# -*- coding: utf-8 -*-

from libGamePiratesAndFishers import assertFormat


class Island():
	""" 
		This class Define object type Island, that represent the one scenario possible in application.
		Can have players, items and spell. That is responsible to manage all interactions between players
		with itens, spelll and with other players.
	""" 
	def __init__(self,name):
		""" 
		Initializing the class Island, it's the constructor, of the class island
		that carrier all the attributes of the scenario, and give support to all the 
		actions of the player in the applicationn
		
		@param name : (string) constains the name of Island
		
		@return : None
		"""
		self.name = assertFormat(name)

		
	# def addIndividual(self):

	# def getIndividual(self):

	# def addSpell(self):

	# def getSpell(self):

	# def addItem(self):

	# def getItem(self):

	# def adddirection(self):

	# def getdirection(self):

	# def getListdirections(self):

	# def getDetailIsland(self):

	