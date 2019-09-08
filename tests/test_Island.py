import pytest
import os
import sys
pathfile = os.getcwd()

newpath  = pathfile.split('/')
newpath[len(newpath)-1] = "RpgPiratesAndFishers" 
pathfile = "/".join(newpath)
sys.path.append(pathfile)

from Fisher import Fisher
from Weapon import Weapon
from Defense import Defense
from Island import Island
from Medkit import Medkit
from Spell import Spell
from Item import Item
from Individual import Individual
from libGamePiratesAndFishers import genRandomName

@pytest.mark.parametrize("standartinput",[(["Island 1" , "Island 2" , "Island 1Island 1Island 1Island 1l"])])
def test_getName(standartinput):
	genIsland = Island(standartinput[0])
	assert genIsland.getName() == standartinput[0]
	genIsland = Island(standartinput[1])
	assert genIsland.getName() == standartinput[1]
	genIsland = Island(standartinput[2])
	assert genIsland.getName() != standartinput[2] and len(genIsland.getName()) > 5 and len(genIsland.getName()) <= 32

@pytest.mark.parametrize("standartinput",[ (Defense("Defesa 1",10,10) ,Weapon("Weapon 1",10,10) , Medkit("Bandage",10)),(None ,Island("Island test") , Individual("Random subject",10,10,10))])
def test_addItem(standartinput):
	genIsland = Island("Gen Island")
	if(isinstance(standartinput[0],Item) ):
		assert genIsland.addItem(standartinput[0]) == 1
	if(not(isinstance(standartinput[0],Item))):
		assert genIsland.addItem(standartinput[0]) == 0
	if(isinstance(standartinput[1],Item) ):
		assert genIsland.addItem(standartinput[1]) == 1
	if(not(isinstance(standartinput[1],Item))):
		assert genIsland.addItem(standartinput[1]) == 0
	if(isinstance(standartinput[2],Item) ):
		assert genIsland.addItem(standartinput[2]) == 1
	if(not(isinstance(standartinput[2],Item))):
		assert genIsland.addItem(standartinput[2]) == 0	
	

@pytest.mark.parametrize("standartinput",[ (0,None,Defense("Defesa 1",10,10) ,Weapon("Weapon 1",10,10) , Medkit("Bandage",10)),(None,0,Defense("Defesa 4",10,10) ,Weapon("Weapon 5",10,10) , Medkit("Bandage 9",10))])
def test_getItem(standartinput):	
	genIsland = Island("Gen Island")
	for i in range(len(standartinput)):
		if(isinstance(standartinput[i],Item)):
			assert genIsland.addItem(standartinput[i]) == 1
			assert genIsland.getItem(standartinput[i].getName()) == standartinput[i]
		else:
			assert genIsland.addItem(standartinput[i]) == 0
			assert genIsland.getItem(standartinput[i]) == None
	
	
	
	
	
