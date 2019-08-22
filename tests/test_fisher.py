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
from libGamePiratesAndFishers import genRandomName

@pytest.mark.parametrize("standartinput,expected",[([Defense("Defense1",10,10) , Weapon("Weapon 1",10,10) , Island("Island 1")] , None)])
def test_init_fisher(standartinput,expected):
	#first test, name is correct
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,genericnumb,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert  genFisher.getName() == namegen
	assert	genFisher.getWeapon() == standartinput[1]
	assert	genFisher.getDefense() == standartinput[0]
	assert  genFisher.getactualIsland() == standartinput[2]
	#second test, name is incorrect, check if is standard
	namegen = genRandomName(100)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,genericnumb,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert (type(genFisher.getName()) is str)
	assert (len(genFisher.getName()) <= 32)
	assert (len(genFisher.getName()) >= 5)
	assert	genFisher.getWeapon() == standartinput[1]
	assert	genFisher.getDefense() == standartinput[0]
	assert  genFisher.getactualIsland() == standartinput[2]
	# third test , no parameter name
	namegen = genRandomName(1)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,genericnumb,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert (type(genFisher.getName()) is str)
	assert (len(genFisher.getName()) <= 32)
	assert (len(genFisher.getName()) >= 5)
	assert	genFisher.getWeapon() == standartinput[1]
	assert	genFisher.getDefense() == standartinput[0]
	assert  genFisher.getactualIsland() == standartinput[2]
	#########################################################
	# testing health , bigger , lower and in the standard
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,1000,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert  genFisher.getName() == namegen
	assert	genFisher.getWeapon() == standartinput[1]
	assert	genFisher.getDefense() == standartinput[0]
	assert  genFisher.getactualIsland() == standartinput[2]
	assert  genFisher.getHealth() > 0
	assert  genFisher.getHealth() <=100
	#second test, life is lower 
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,-1,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert  genFisher.getName() == namegen
	assert	genFisher.getWeapon() == standartinput[1]
	assert	genFisher.getDefense() == standartinput[0]
	assert  genFisher.getactualIsland() == standartinput[2]
	assert  genFisher.getHealth() > 0
	assert  genFisher.getHealth() <=100
	# third test , standard
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,50,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert  genFisher.getName() == namegen
	assert	genFisher.getWeapon() == standartinput[1]
	assert	genFisher.getDefense() == standartinput[0]
	assert  genFisher.getactualIsland() == standartinput[2]
	assert  genFisher.getHealth() == 50
	###########################################################
	# testing the object attack , defense and Island
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,50,standartinput[0],standartinput[1],standartinput[2],idgen)
	assert  genFisher.getName() == namegen
	assert	genFisher.getWeapon() == None
	assert	genFisher.getDefense() == None
	assert  genFisher.getactualIsland() == standartinput[2]
	assert  genFisher.getHealth() == 50
	# testing the object island change by defense
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,50,standartinput[2],standartinput[0],standartinput[1],idgen)
	assert  genFisher.getName() == namegen
	assert	genFisher.getWeapon() == None
	assert	genFisher.getDefense() == standartinput[0]
	assert  genFisher.getactualIsland() == None
	assert  genFisher.getHealth() == 50
	##########################################################
	# testing the digest of sha256, not standard , standard
	namegen = genRandomName(10)
	idgen = genRandomName(63) # not standard
	genericnumb = 100
	genFisher = Fisher(namegen,50,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert  genFisher.getName() == namegen
	assert	genFisher.getWeapon() == standartinput[1]
	assert	genFisher.getDefense() == standartinput[0]
	assert  genFisher.getactualIsland() == standartinput[2]
	assert  genFisher.getHealth() == 50
	assert  type(genFisher.getIdplayer()) is str 
	assert  len(genFisher.getIdplayer()) == 64
	# testing the digest of sha256, not standard , standard
	namegen = genRandomName(10)
	idgen = genRandomName(64) # not standard
	genericnumb = 100
	genFisher = Fisher(namegen,50,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert  genFisher.getName() == namegen
	assert	genFisher.getWeapon() == standartinput[1]
	assert	genFisher.getDefense() == standartinput[0]
	assert  genFisher.getactualIsland() == standartinput[2]
	assert  genFisher.getHealth() == 50
	assert  type(genFisher.getIdplayer()) is str 
	assert  len(genFisher.getIdplayer()) == 64
	assert 	genFisher.getIdplayer() == idgen

@pytest.mark.parametrize("standartinput,expected",[(Island("Island 1") , "Island 1"),(Island("Island 2") , "Island 2")])
def test_getNamelocation(standartinput,expected):
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,genericnumb,None,None,standartinput,idgen)
	assert  genFisher.getNamelocation() == expected


	
@pytest.mark.parametrize("standartinput",[([Defense("Defense actual",10,10), Weapon("Weapon actual",10,10), Island("Island 1") ,Defense("Defense Other",10,10), Weapon("Weapon Other",10,10) , Medkit("Medkit 1",90)])])
def test_addItemBackpack(standartinput):
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,genericnumb,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert  genFisher.getName() == namegen
	assert	genFisher.getWeapon() == standartinput[1]
	assert	genFisher.getDefense() == standartinput[0]
	assert  genFisher.getactualIsland() == standartinput[2]
	assert  len(genFisher.backpack) == 0	
	assert  genFisher.addItemBackpack(standartinput[3]) == 1 
	assert  genFisher.backpack.index(standartinput[3]) == 0
	assert  len(genFisher.backpack) == 1	
	assert  genFisher.addItemBackpack(standartinput[4]) == 1 
	assert  genFisher.backpack.index(standartinput[4]) == 1
	assert  len(genFisher.backpack) == 2	
	assert  genFisher.addItemBackpack(standartinput[5]) == 1 
	assert  genFisher.backpack.index(standartinput[5]) == 2
	assert  len(genFisher.backpack) == 3	

#,([Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Defense("Defense x",10,10), Weapon("Weapon x",10,10) , Medkit("Medkit 2",90)],["Defense x","Weapon x","Medkit 2"])
@pytest.mark.parametrize("standartinput,expected",[([Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Defense("Defense Other",10,10), Weapon("Weapon Other",10,10) , Medkit("Medkit 1",90)] , ["Defense Other","Weapon Other","Medkit 1"]) ,([Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Defense("Defense x",10,10), Weapon("Weapon x",10,10) , Medkit("Medkit 2",90)],["Defense x","Weapon x","Medkit 2"])])
def test_listItemBackpack(standartinput,expected):
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,genericnumb,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert genFisher.listItemBackpack() == 'No Items on backpack'
	genFisher.addItemBackpack(standartinput[3])
	genFisher.addItemBackpack(standartinput[4])
	genFisher.addItemBackpack(standartinput[5])
	val = genFisher.listItemBackpack()
	assert type(val) == str
	assert type(val.index(expected[0])) is int
	assert type(val.index(expected[1])) is int
	assert type(val.index(expected[2])) is int
	genFisher.backpack = []
	assert genFisher.listItemBackpack() == 'No Items on backpack'
	genFisher.addItemBackpack(standartinput[5])
	genFisher.addItemBackpack(standartinput[3])
	genFisher.addItemBackpack(standartinput[4])
	val = genFisher.listItemBackpack()
	assert type(val) == str
	assert type(val.index(expected[0])) is int
	assert type(val.index(expected[1])) is int
	assert type(val.index(expected[2])) is int
	genFisher.backpack = []
	assert genFisher.listItemBackpack() == 'No Items on backpack'
	genFisher.addItemBackpack(standartinput[5])
	genFisher.addItemBackpack(standartinput[3])
	val = genFisher.listItemBackpack()
	assert type(val) == str
	assert type(val.index(expected[0])) is int
	assert type(val.index(expected[2])) is int
	