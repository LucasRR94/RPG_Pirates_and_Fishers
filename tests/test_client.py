import pytest
import os
import sys
import builtins
from base64 import b64encode

pathfile = os.getcwd()

newpath  = pathfile.split('/')
newpath[len(newpath)-1] = "RpgPiratesAndFishers"
pathfile = "/".join(newpath)
sys.path.append(pathfile)

from client import *
from Crypto_modulo import *

@pytest.mark.parametrize("standartinput,expectedResult", [ (os.urandom(1024) , 5) , (os.urandom(10) , 1) , (os.urandom(245) , 1) ])
def test_verify_len(standartinput,expectedResult):
	assert verify_len(standartinput,) == expectedResult

@pytest.mark.parametrize("standartinput,expectedResult", [ (os.urandom(1024) , 5) , (os.urandom(10) , 1) , (os.urandom(245) , 1) ])
def test_verify_size_slice_content(standartinput,expectedResult):
	res = verify_size_slice_content(standartinput,245)
	assert type(res) == list
	acumulator = b""
	for i in range(expectedResult):
		actual = res[i]
		acumulator += actual[0:len(actual)-4]
	assert acumulator == standartinput

@pytest.mark.parametrize("standartinput,expectedResult",[(os.urandom(20000),82) , (os.urandom(300000),1225)])
def test_mounting_answer(standartinput,expectedResult):
	list_messages = mounting_answer(verify_size_slice_content(standartinput,245),header_definition_client(1,"0.0.0"),gen_footer(1))
	assert len(list_messages) == expectedResult
	header_def = header_definition_client(1,"0.0.0")
	header_com = header_def.split(b" \r\n ")
	acum_content = b""
	for k in list_messages:
		actual = k.split(b" \r\n ")
		acum_content+=actual[1] # taking content
		assert header_com[0] == actual[0]
		if(k == list_messages[len(list_messages)-1]):
			assert actual[2] == b'0'
		else:
			assert actual[2] == b'1'
	assert acum_content == standartinput	# comparing with original content

@pytest.mark.parametrize("standartinput,expectedResult",[(os.urandom(20000),0) , (1,b" 1 \r\n "),(0,b" 0 \r\n "),(10,0)])
def test_get_footer(standartinput,expectedResult):
	assert gen_footer(standartinput) == expectedResult

@pytest.mark.parametrize("standartinput,expectedResult",[(1,b"HIII 0.0.0 \r\n "),(3,b"EXIN 0.0.0 \r\n "),(4,b"PROC 0.0.0 \r\n "),(6,b"CONF 0.0.0 \r\n "),(7,b"EKEY 0.0.0 \r\n "),(9,b"BEGG 0.0.0 \r\n "),(120,b"USEI 0.0.0 \r\n "),(121,b"MOVF 0.0.0 \r\n "),(122,b"ATQE 0.0.0 \r\n "),(123,b"GAME 0.0.0 \r\n "),(124,b"CATI 0.0.0 \r\n "),(os.urandom(1024),0),(100,0),(None,0)])
def test_header_definition_client(standartinput,expectedResult):
	assert header_definition_client(standartinput,"0.0.0") == expectedResult

@pytest.mark.parametrize("standartinput,expectedResult",[([b"HIII 0.0.0 \r\n ",2014],2),([b"HIII 0.0.0 \r\n ",245],1),([b"Nada \r\n",None],0)])
def test_check_lenght_complete_with_dont_care(standartinput,expectedResult):
	if(expectedResult == 1): # it's mean that the result expecte is 245 bytes type 
		assert len(check_lenght_complete_with_dont_care(standartinput[0],standartinput[1])) == 245 
		assert type(check_lenght_complete_with_dont_care(standartinput[0],standartinput[1])) == bytes
		assert (check_lenght_complete_with_dont_care(standartinput[0],standartinput[1]).split(b" \r\n "))[0] == standartinput[0][0:len(standartinput)-6]  
	if(expectedResult == 2): # second param speak the lenght of stream
		assert len(check_lenght_complete_with_dont_care(standartinput[0],standartinput[1])) == standartinput[1]
		assert type(check_lenght_complete_with_dont_care(standartinput[0],standartinput[1])) == bytes
		assert (check_lenght_complete_with_dont_care(standartinput[0],standartinput[1]).split(b" \r\n "))[0] == standartinput[0][0:len(standartinput)-6]  
	if(expectedResult == 0):	 # expect the answer of error
		assert check_lenght_complete_with_dont_care(standartinput[0],standartinput[1]) == 0

@pytest.mark.parametrize("standartinput,expectedResult",
	[
	([[b"HIII 0.0.0 \r\n ",b"HIII 0.0.0 \r\n ",b"H"],16],[3,16]),
	([[b"aaaHIII 0.0.0 \r\n ",b"HIII 0.0.0 \r\n ",b"H"],16],[0,16])
	])
def test_prepare_send_socket(standartinput,expectedResult):
	if(expectedResult[0] == 0):
		assert prepare_send_socket(standartinput[0],standartinput[1]) == 0
	else:
		assert len(prepare_send_socket(standartinput[0],standartinput[1])) == expectedResult[0]
		list_messages =prepare_send_socket(standartinput[0],standartinput[1])
		for i in range(expectedResult[0]):
			assert len(list_messages[i]) == expectedResult[1]


@pytest.mark.parametrize("standartinput,expectedResult",[([1,bytes(b64encode(os.urandom(1024)).decode("utf-8"),"utf-8")],1),([1,"String whatever"],0)])
def test_insert_signing_on_messages(standartinput,expectedResult):
	#a = prepare_send_socket(,245)
	#print((mounting_answer((verify_size_slice_content(standartinput[1],245 - ( (len(header_definition_client(1,"0.0.0")) + len(gen_footer(1))) - 6))),header_definition_client(1,"0.0.0"),gen_footer(1))))
	objkey = generate_private_RSA_key()
	key_rsa = create_type_crypto('rsa',objkey,2) 
	pkey_rsa = create_type_crypto('rsa',objkey.public_key(),1)
	x = prepare_send_socket((mounting_answer((verify_size_slice_content(standartinput[1], 245 - ( (len(header_definition_client(1,"0.0.0")) + len(gen_footer(1))) + 3))),header_definition_client(1,"0.0.0"),gen_footer(1))),245)
	a = insert_signing_on_messages(x,key_rsa)
	if (expectedResult == 1):
		for i in a:
			message = i[0:245]
			signing = i[245:len(i)]
			sg = signing.split(b" \r\n ")
			b = check_signing_cyphertext(pkey_rsa,sg[1],message)
			assert b == expectedResult
	else:
		a == expectedResult	

@pytest.mark.parametrize("standartinput",[
	([1,"pirata mal encarado",120,"pirata mal encarado",1]),
	([2,"Lock",124,"Lock",1]),
	([5,"manzus",121,"manzus",1]),
	([8,"kjada",122,"kjada",1]),
	([0,"pirata mal encarado",123,1231,1]),
	([1,"pirata mal encarado",120,"pirata mal encarad",0]),
	([2,"Lock",124,"Loc",0]),
	([5,"manzus",121,"anzus",0]),
	([11,None,3,None,1]),
	([11,None,4,None,0]),
	([3,"Algo",123,"Algo",0]),
	([3,"Algo",123,1232,1]),
	([6,"Algo",123,1234,1]),
	([7,"Algo",123,1235,1]),
	([9,"Algo",123,1236,1]),
	([10,"Algo",123,1237,1]),
	([6,"Algo",123,"Algo",0]),
	([7,"Algo",123,"Algo",0]),
	([9,"Algo",123,"Algo",0]),
	([10,"Algo",123,"Algo",0]),
	])
def test_menu_User_Option(standartinput,mocker):
	res=""
	# 123:"GAME"
	# dict_header = {6:123,7:123,9:123,10:123}
	# dict_secundary_content = {6:1234,7:1235,9:1236,10:1237}
	
	mocker.patch('builtins.input',side_effect=[standartinput[0],standartinput[1]])
	if(standartinput[4]==0):
		assert menu_User_Option() != [standartinput[2],standartinput[3]]
	else:	
		assert menu_User_Option() == [standartinput[2],standartinput[3]]

	


