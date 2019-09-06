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
from Individual import Individual
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
	

@pytest.mark.parametrize("standartinput",[(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Defense("Defense x",10,10), Weapon("Weapon x",10,10) , Medkit("Medkit 1",99)),(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Defense("Defense x",10,10), Weapon("Weapon x",10,10) , Medkit("Medkit 1",45))])
def test_useItemBackpack(standartinput):
	#############################################################
	#using medkit
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 10
	genFisher = Fisher(namegen,genericnumb,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert genFisher.addItemBackpack(standartinput[3]) == 1
	assert genFisher.addItemBackpack(standartinput[4]) == 1
	assert genFisher.addItemBackpack(standartinput[5]) == 1
	assert len(genFisher.backpack) == 3 # add all the items
	medkitgeneric = standartinput[5]
	totalsum = genericnumb + medkitgeneric.getHealing() 
	if totalsum > 100:
		totalsum = 100
	genFisher.useItemBackpack(medkitgeneric.getName())
	assert len(genFisher.backpack) == 2 # used the item Medkit
	assert genFisher.getHealth() == totalsum
	details = genFisher.listItemBackpack()
	assert type(details.index(standartinput[3].getName())) is int
	assert type(details.index(standartinput[4].getName())) is int
	###############################################################
	#change weapons and defense
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 10
	genFisher = Fisher(namegen,genericnumb,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert genFisher.addItemBackpack(standartinput[3]) == 1
	assert genFisher.addItemBackpack(standartinput[4]) == 1
	assert len(genFisher.backpack) == 2
	genFisher.useItemBackpack(standartinput[3].getName())
	assert len(genFisher.backpack) == 2 
	assert genFisher.getDefense() == standartinput[3]
	assert type(genFisher.backpack.index(standartinput[0])) is int # Is present on the backpack
	assert len(genFisher.backpack) == 2
	genFisher.useItemBackpack(standartinput[4].getName())
	assert len(genFisher.backpack) == 2 
	assert genFisher.getWeapon() == standartinput[4]
	assert type(genFisher.backpack.index(standartinput[1])) is int # Is present on the backpack

@pytest.mark.parametrize("standartinput",[(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Defense("Defense x",10,10), Weapon("Weapon x",10,10) , Medkit("Medkit 1",99)),(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Defense("Defense x",10,10), Weapon("Weapon x",10,10) , Medkit("Medkit 1",45))])
def test_collectItem(standartinput):
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,genericnumb,standartinput[1],standartinput[0],standartinput[2],idgen)
	standartinput[2].addItem(standartinput[3])
	standartinput[2].addItem(standartinput[4])
	standartinput[2].addItem(standartinput[5])
	assert len(genFisher.backpack) == 0
	assert len(standartinput[2].itemisland) == 3
	assert genFisher.collectItem(standartinput[3].getName()) == 1
	assert len(standartinput[2].itemisland) == 2
	assert len(genFisher.backpack) == 1
	assert genFisher.collectItem(standartinput[4].getName()) == 1
	assert len(standartinput[2].itemisland) == 1
	assert len(genFisher.backpack) == 2
	assert genFisher.collectItem(standartinput[5].getName()) == 1
	assert len(standartinput[2].itemisland) == 0
	assert len(genFisher.backpack) == 3
	val = genFisher.listItemBackpack()
	assert type(val) == str
	assert type(val.index(standartinput[3].getName())) is int
	assert type(val.index(standartinput[4].getName())) is int
	assert type(val.index(standartinput[5].getName())) is int

@pytest.mark.parametrize("standartinput",[(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Defense("Defense x",10,10), Weapon("Weapon x",10,10) , Medkit("Medkit 1",99)),(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Defense("Defense x",10,10), Weapon("Weapon x",10,10) , Medkit("Medkit 1",45))])
def test_listItemsfromIsland(standartinput):
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,genericnumb,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert (genFisher.listItemsfromIsland() == "No items on actual island")
	assert (standartinput[2].addItem(standartinput[3]) ==1)
	assert type(genFisher.listItemsfromIsland()) == str and genFisher.listItemsfromIsland().index(standartinput[3].getName()) > 0
	assert (standartinput[2].addItem(standartinput[4]) ==1)
	assert type(genFisher.listItemsfromIsland()) == str and genFisher.listItemsfromIsland().index(standartinput[4].getName()) > 0
	assert (standartinput[2].addItem(standartinput[5]) ==1)
	assert type(genFisher.listItemsfromIsland()) == str and genFisher.listItemsfromIsland().index(standartinput[5].getName()) > 0
	assert type(genFisher.listItemsfromIsland()) == str and genFisher.listItemsfromIsland().index(standartinput[3].getName()) > 0 and genFisher.listItemsfromIsland().index(standartinput[4].getName()) > 0 and genFisher.listItemsfromIsland().index(standartinput[5].getName()) > 0
	assert genFisher.collectItem(standartinput[5].getName())  == 1
	try:
		with (genFisher.listItemsfromIsland().index(standartinput[5].getName())) > 0 :
			raise AssertionError('Should not be found anymore')
	except ValueError:
		assert type(genFisher.listItemsfromIsland()) == str and genFisher.listItemsfromIsland().index(standartinput[3].getName()) > 0 and genFisher.listItemsfromIsland().index(standartinput[4].getName()) > 0
		assert genFisher.collectItem(standartinput[4].getName())  == 1
		try:
			with (genFisher.listItemsfromIsland().index(standartinput[4].getName())) > 0 :
				raise AssertionError('Should not be found anymore')
		except ValueError:
			assert type(genFisher.listItemsfromIsland()) == str and genFisher.listItemsfromIsland().index(standartinput[3].getName()) > 0
			assert genFisher.collectItem(standartinput[3].getName())  == 1
			assert(genFisher.listItemsfromIsland() == "No items on actual island")
			temp_object = Defense("Defense now",9,10)
			assert standartinput[2].addItem(temp_object) == 1
			assert genFisher.listItemsfromIsland().index(temp_object.getName()) > 0




@pytest.mark.parametrize("standartinput",[(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Defense("Defense x",10,10), Weapon("Weapon x",10,10) , Medkit("Medkit 1",99)),(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Defense("Defense x",10,10), Weapon("Weapon x",10,10) , Medkit("Medkit 1",45))])
def test_dropItems(standartinput):
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,genericnumb,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert genFisher.addItemBackpack(standartinput[3]) == 1
	assert genFisher.addItemBackpack(standartinput[4]) == 1
	assert genFisher.addItemBackpack(standartinput[5]) == 1
	assert type(genFisher.listItemBackpack()) == str and genFisher.listItemBackpack().index(standartinput[3].getName()) > 0 and genFisher.listItemBackpack().index(standartinput[4].getName()) > 0 and genFisher.listItemBackpack().index(standartinput[5].getName()) > 0
	backpacktemp = genFisher.dropItems() 
	assert genFisher.listItemBackpack() == 'No Items on backpack'
	assert (backpacktemp.index(standartinput[3])) >= 0  and (backpacktemp.index(standartinput[4])) >= 0 and (backpacktemp.index(standartinput[5])) >= 0

@pytest.mark.parametrize("standartinput",[(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Spell("Spell 1",10), Spell("Spell 2 ",10) , Spell("Spell 3",99)),(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Spell("Spell 3",99), Spell("Spell 1 ",1) , Spell("Spell 2",5))])
def test_dropSpells(standartinput):
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,genericnumb,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert standartinput[2].addSpellIsland(standartinput[3]) == 1
	assert genFisher.collectSpell() == 'Sucess on collect spell\n'
	assert standartinput[2].addSpellIsland(standartinput[4]) == 1
	assert genFisher.collectSpell() == 'Sucess on collect spell\n'
	assert standartinput[2].addSpellIsland(standartinput[5]) == 1
	assert genFisher.collectSpell() == 'Sucess on collect spell\n'
	assert genFisher.getvalueSpell() > 0
	spellcontainertemp = genFisher.dropSpells()
	assert type(spellcontainertemp) is list
	assert genFisher.getvalueSpell() == 0
	assert spellcontainertemp.index(standartinput[3]) >=0 and spellcontainertemp.index(standartinput[4]) >= 0 and spellcontainertemp.index(standartinput[5]) >=0


@pytest.mark.parametrize("standartinput",[(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Spell("Spell 1",10), Spell("Spell 2 ",10) , Spell("Spell 3",99)),(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Spell("Spell 3",99), Spell("Spell 1 ",1) , Spell("Spell 2",5))])
def test_getvalueSpell(standartinput):
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,genericnumb,standartinput[1],standartinput[0],standartinput[2],idgen)
	total = 0
	for i in range(3):
		total+= standartinput[3+i].getValue()
		standartinput[2].addSpellIsland(standartinput[i+3])
		genFisher.collectSpell()
		assert genFisher.getvalueSpell() == total


@pytest.mark.parametrize("standartinput",[(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Spell("Spell 1",10), Spell("Spell 2 ",10) , Spell("Spell 3",99)),(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Spell("Spell 3",99), Spell("Spell 1 ",1) , Spell("Spell 2",5))])
def test_getinfoaboutSpellonIsland(standartinput):
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,genericnumb,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert genFisher.getinfoaboutSpellonIsland() == "No spell present on the island"
	assert standartinput[2].addSpellIsland(standartinput[3])
	assert genFisher.getinfoaboutSpellonIsland() == "Spells available in island"
	assert genFisher.collectSpell() == "Sucess on collect spell\n"
	assert genFisher.getinfoaboutSpellonIsland() == "No spell present on the island"
	assert standartinput[2].addSpellIsland(standartinput[4])
	assert genFisher.getinfoaboutSpellonIsland() == "Spells available in island"
	assert genFisher.collectSpell() == "Sucess on collect spell\n"
	assert genFisher.getinfoaboutSpellonIsland() == "No spell present on the island"
	assert standartinput[2].addSpellIsland(standartinput[5])
	assert genFisher.getinfoaboutSpellonIsland() == "Spells available in island"
	assert genFisher.collectSpell() == "Sucess on collect spell\n"
	assert genFisher.getinfoaboutSpellonIsland() == "No spell present on the island"  

@pytest.mark.parametrize("standartinput",[(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"), Defense("Defense x",10,10),Weapon("Weapon x",10,10),Spell("Spell 1",10),Spell("Spell 2",100),Island("Island 2")),(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Weapon("Weapon x",10,10),Defense("Defense x",10,10),Spell("Spell 2",19),Spell("Spell 1",20),Island("Island 3"))])
def test_changeIsland(standartinput):	
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,genericnumb,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert genFisher.getactualIsland() == standartinput[2]
	genFisher.addItemBackpack(standartinput[3])
	standartinput[2].addItem(standartinput[4])
	standartinput[2].addSpellIsland(standartinput[5])
	genFisher.collectSpell()
	standartinput[2].addSpellIsland(standartinput[6])
	standartinput[2].adddirection(standartinput[7],"left")
	genFisher.changeIsland("left")
	assert genFisher.getactualIsland() == standartinput[7]
	assert genFisher.listItemBackpack().index(standartinput[3].getName()) > 0
	assert standartinput[2].getItem(standartinput[4].getName()) == standartinput[4] 
	assert genFisher.getvalueSpell() == standartinput[5].getValue()
	assert standartinput[2].getSpell() ==standartinput[6]
	assert standartinput[7].getIndividual(genFisher.getName()) == genFisher
	assert standartinput[2].getIndividual(genFisher.getName()) == None

@pytest.mark.parametrize("standartinput",[(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Island("Island XX"),Island("Island 5"),Island("Island 9"),Island("Island x"),),(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Island("Island 2"),Island("Island z1"),Island("Island X1"),Island("Island 99"))])
def test_getDirectionsfromIsland(standartinput):	
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,genericnumb,standartinput[1],standartinput[0],standartinput[2],idgen)
	assert standartinput[2].adddirection(standartinput[3],"left") == 1
	assert genFisher.getDirectionsfromIsland().index(standartinput[3].getName()) > 0
	assert genFisher.getDirectionsfromIsland().index("left") > 0
	assert standartinput[2].adddirection(standartinput[4],"center") == 1
	assert genFisher.getDirectionsfromIsland().index(standartinput[4].getName()) > 0
	assert genFisher.getDirectionsfromIsland().index("center") > 0
	assert standartinput[2].adddirection(standartinput[5],"back") == 1
	assert genFisher.getDirectionsfromIsland().index(standartinput[5].getName()) > 0
	assert genFisher.getDirectionsfromIsland().index("back") > 0
	assert standartinput[2].adddirection(standartinput[6],"right") == 1
	assert genFisher.getDirectionsfromIsland().index(standartinput[6].getName()) > 0
	assert genFisher.getDirectionsfromIsland().index("right") > 0
	assert genFisher.getDirectionsfromIsland().index(standartinput[3].getName()) > 0 and  genFisher.getDirectionsfromIsland().index(standartinput[4].getName()) > 0 and genFisher.getDirectionsfromIsland().index(standartinput[5].getName()) > 0 and genFisher.getDirectionsfromIsland().index(standartinput[6].getName()) > 0

@pytest.mark.parametrize("standartinput",[(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Spell("Spell 1",10), Spell("Spell 2",99)),(Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),Spell("Spell X1",19), Spell("Spell z2",29))])
def test_collectSpell(standartinput):
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genericnumb = 100
	genFisher = Fisher(namegen,genericnumb,standartinput[1],standartinput[0],standartinput[2],idgen)
	total = 0
	for i in range(2):
		assert standartinput[2].addSpellIsland(standartinput[3+i]) == 1
		assert genFisher.collectSpell() == "Sucess on collect spell\n"
		assert genFisher.collectSpell() == "Fail in collect spell\n"
		total += standartinput[3+i].getValue()
		assert total == genFisher.getvalueSpell()


@pytest.mark.parametrize("standartinput",[(100,Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),1,1,1,Defense("Defense x",1,1), Weapon("Weapon x",1,1)),(1,Defense("Defense actual",1,1), Weapon("Weapon actual",1,1),Island("Island 1"),100,100,100,Defense("Defense x",10,10), Weapon("Weapon x",10,10))])
def test_attackEnemy_Individual(standartinput):
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genattack = standartinput[2].getAttack()
	gendefense = standartinput[1].getDefense()
	genFisher = Fisher(namegen,standartinput[0],standartinput[2],standartinput[1],standartinput[3],idgen)
	#Create obj Individual
	genIndividual = Individual("GenericIndividual",standartinput[4],standartinput[5],standartinput[6])
	assert standartinput[3].addIndividual(genIndividual) == 1
	assert genFisher.attackEnemy("GenericIndividual") == 1
	totalhit = standartinput[6] - (standartinput[2].getAttack())
	totalhit2 = gendefense - (standartinput[5])
	if(totalhit < 0): # defense is destroyed
		totalhit+=standartinput[4]
		# Death of attacked Individual
		if(totalhit<=0):
			assert standartinput[3].getIndividual(genIndividual.getName()) == None
		# It's not dead the Individual
		if(totalhit>0):
			assert standartinput[3].getIndividual(genIndividual.getName()) == genIndividual
			assert genIndividual.getHealth() ==  standartinput[4] + (standartinput[6] - genattack)
	if(totalhit > 0): #defense still exist 
		assert standartinput[3].getIndividual(genIndividual.getName()) == genIndividual
		assert genIndividual.getHealth() == standartinput[4]
		assert genIndividual.getValueDefense() == (standartinput[6] - standartinput[2].getAttack())
	if(totalhit2 < 0): # the defense of the attacker is destroy
		totalhit2+= standartinput[0]
		# Death of the attacker
		if(totalhit2 <= 0):
			assert standartinput[3].getIndividual(genFisher) == None
		# the attacker remains in the game
		else: 
			assert standartinput[3].getIndividual(genFisher) == genFisher
			assert genFisher.getValueDefense() == 0 and  genFisher.getHealth() == (gendefense - standartinput[5])
	if(totalhit2 >= 0): # the defense of the attacker still resist
		assert standartinput[3].getIndividual(genFisher.getName()) == genFisher
		assert genFisher.getValueDefense() 	== (standartinput[1].getDefense() - standartinput[5])
		assert genFisher.getHealth() == standartinput[0]	

@pytest.mark.parametrize("standartinput",[(100,Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),1,Defense("Defense x",1,1), Weapon("Weapon x",1,1),Defense("Defense z",1,1),Spell("Spell 1",10)),(1,Defense("Defense actual",1,1), Weapon("Weapon actual",1,1),Island("Island 1"),100,Defense("Defense x",10,10), Weapon("Weapon x",10,10), Weapon("Weapon k",1,1),Spell("Spell 2",10))])
def test_attackEnemy_Fisher(standartinput):
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	idgen2 = genRandomName(64)
	genattack = standartinput[2].getAttack()
	gendefense = standartinput[1].getDefense()
	genFisher = Fisher(namegen,standartinput[0],standartinput[2],standartinput[1],standartinput[3],idgen)
	#Create obj Individual
	backattack = standartinput[6].getAttack()
	backdefense = standartinput[5].getDefense()
	genIndividual = Fisher("Generic Fisher",standartinput[4],standartinput[6],standartinput[5],standartinput[3],idgen2)
	assert genIndividual.addItemBackpack(standartinput[7]) == 1
	assert standartinput[3].addSpellIsland(standartinput[8]) == 1
	assert genIndividual.collectSpell().index("Sucess") >= 0
	assert genFisher.getvalueSpell() == 0
	assert genFisher.listItemBackpack().index("No Items") >=0
	totalhit = standartinput[5].getDefense() - (standartinput[2].getAttack())
	assert genFisher.getHealth() == standartinput[0]
	assert genFisher.getValueDefense() == standartinput[1].getDefense()
	assert genFisher.getValueAttack() == standartinput[2].getAttack()
	assert (genFisher.attackEnemy("Generic Fisher")) == 1
	if(totalhit < 0): # defense is destroyed
		totalhit+=standartinput[4]
		# Death of attacked Individual
		if(totalhit<=0):
			assert standartinput[3].getIndividual(genIndividual.getName()) == None
		# It's not dead the Individual
		if(totalhit>0):
			assert standartinput[3].getIndividual(genIndividual.getName()) == genIndividual
			assert genIndividual.getHealth() ==  standartinput[4] + (standartinput[6] - genattack)
			assert genFisher.listItemBackpack().index(standartinput[7].getName()) >=0
			assert genFisher.getValueSpell() == standartinput[8].getValue()
	if(totalhit > 0): #defense still exist 
		assert standartinput[3].getIndividual(genIndividual.getName()) == genIndividual
		assert genIndividual.getHealth() == standartinput[4]
		assert genIndividual.getValueDefense() == (backdefense - genattack)
	
	
	

@pytest.mark.parametrize("standartinput",[(100,Defense("Defense actual",10,10), Weapon("Weapon actual",10,10),Island("Island 1"),1,Defense("Defense x",1,1), Weapon("Weapon x",1,1),Defense("Defense z",1,1),Spell("Spell 1",10)),(1,Defense("Defense actual",1,1), Weapon("Weapon actual",1,1),Island("Island 1"),100,Defense("Defense x",10,10), Weapon("Weapon x",10,10), Weapon("Weapon k",1,1),Spell("Spell 2",10))])
def test_listenemies(standartinput):
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	idgen2 = genRandomName(64)
	genattack = standartinput[2].getAttack()
	gendefense = standartinput[1].getDefense()
	genFisher = Fisher(namegen,standartinput[0],standartinput[2],standartinput[1],standartinput[3],idgen)
	assert genFisher.listenemies().index("No enemies in actual island!!!") >= 0
	genIndividual = Individual("Generic Individual",standartinput[4],standartinput[4],standartinput[4])
	standartinput[3].addIndividual(genIndividual)
	assert genFisher.listenemies().index("Generic Individual") >=0 and genFisher.listenemies().index("Health of individual:"+str(standartinput[4])) >=0 and genFisher.listenemies().index("Attack of individual:"+str(standartinput[4])) >=0 and genFisher.listenemies().index("Defense of individual:"+str(standartinput[4])) >=0
	genFisher2 = Fisher("Generic Fisher",standartinput[4],standartinput[6],standartinput[5],standartinput[3],idgen2)
	assert genFisher2.listenemies().index("Generic Individual") >=0 and genFisher.listenemies().index("Health of individual:"+str(standartinput[4])) >=0 and genFisher.listenemies().index("Attack of individual:"+str(standartinput[4])) >=0 and genFisher.listenemies().index("Defense of individual:"+str(standartinput[4])) >=0	
	assert genFisher.listenemies().index("Generic Fisher")>=0 and genFisher.listenemies().index("Health of individual:"+str(standartinput[4])) >=0  and genFisher.listenemies().index("Attack of individual:"+str(standartinput[5].getDefense())) >=0 and genFisher.listenemies().index("Attack of individual:"+str(standartinput[6].getAttack())) >=0
	assert genFisher2.listenemies().index(namegen) >=0 and genFisher2.listenemies().index("Health of individual:"+str(standartinput[0])) >=0 and genFisher2.listenemies().index("Attack of individual:"+str(standartinput[2].getAttack())) >=0 and genFisher2.listenemies().index("Defense of individual:"+str(standartinput[1].getDefense())) >=0		
	try:
		with (genFisher.listenemies().index(namegen) >= 0):
			raise ("Problems , he reconized himself as enemy")
	except ValueError:
		try:
			with(genFisher2.listenemies().index("Generic Fisher") >= 0):
				raise ("Problems , he reconized himself as enemy")
		except ValueError:
			pass		

@pytest.mark.parametrize("standartinput",[(100,Defense("Defense actual",10,10), Weapon("Weapon actual",1,10),Island("Island 1"),Defense("Defense x",9,9), Weapon("Weapon x",5,5),Defense("Defense z",1,1)),(1,Defense("Defense actual",1,1), Weapon("Weapon actual",1,1),Island("Island 1"),Defense("Defense x",1,2), Weapon("Weapon x",10,10), Weapon("Weapon k",1,1))])
def test_getDetail(standartinput):
	namegen = genRandomName(10)
	idgen = genRandomName(64)
	genattack = standartinput[2].getAttack()
	gendefense = standartinput[1].getDefense()
	genFisher = Fisher(namegen,standartinput[0],standartinput[2],standartinput[1],standartinput[3],idgen)
	assert genFisher.getDetail().index(standartinput[1].getName()) >= 0 and genFisher.getDetail().index(str(standartinput[1].getDefense())) >=0 
	assert genFisher.getDetail().index(standartinput[2].getName()) >= 0 and genFisher.getDetail().index(str(standartinput[2].getAttack())) >=0
	assert genFisher.addItemBackpack(standartinput[4]) == 1
	assert genFisher.addItemBackpack(standartinput[5]) == 1
	assert genFisher.addItemBackpack(standartinput[6]) == 1
	var = genFisher.useItemBackpack(standartinput[4].getName())
	assert var[0] == 1
	assert genFisher.getDetail().index(standartinput[4].getName()) >=0 and genFisher.getDetail().index(str(standartinput[4].getDefense()))
	var2 = genFisher.useItemBackpack(standartinput[5].getName())
	assert var2[0] == 1
	assert genFisher.getDetail().index(standartinput[5].getName()) >=0 and genFisher.getDetail().index(str(standartinput[5].getAttack()))
	