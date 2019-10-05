import pytest
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa,utils
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes, base
from cryptography.exceptions import *  
import os
import sys
pathfile = os.getcwd()

newpath  = pathfile.split('/')
newpath[len(newpath)-1] = "RpgPiratesAndFishers" 
pathfile = "/".join(newpath)
sys.path.append(pathfile)

from Crypto_modulo import *




@pytest.mark.parametrize("standartinput",[('rsa',rsa.generate_private_key(public_exponent=65537,key_size=4096,backend=default_backend()), 2 , os.urandom(245)),('aes',os.urandom(32),0, os.urandom(1024)),('rsa',((rsa.generate_private_key(public_exponent=65537,key_size=4096,backend=default_backend())).public_key()) , 1 , os.urandom(245))])
def test_encrypt_plaintext(standartinput):
	type_crypto = []
	type_crypto.append(standartinput[0])
	if(type(standartinput[1])==bytes):
		modevec = os.urandom(16)
		backend = default_backend()
		cipher = Cipher(algorithms.AES(standartinput[1]),modes.CBC(modevec),backend = backend)
		type_crypto.append(cipher)
	else:
		type_crypto.append(standartinput[1])
	
	type_crypto.append(standartinput[2])
	encrypt_text = encrypt_plaintext(type_crypto,standartinput[3])
	if(type(standartinput[1]) == bytes):
		assert type(encrypt_text) == bytes
	elif(type(standartinput[1]) != bytes):
		if(standartinput[0] == 'rsa' and standartinput[2] == 1):
			assert type(encrypt_text) == bytes
		else:
			assert type(encrypt_text) == int
	pass
	
@pytest.mark.parametrize("standartinput",[('rsa',rsa.generate_private_key(public_exponent=65537,key_size=4096,backend=default_backend()), 2,os.urandom(245) ),('aes',os.urandom(32),0,os.urandom(1024)),('rsa',((rsa.generate_private_key(public_exponent=65537,key_size=4096,backend=default_backend())).public_key()) , 1,os.urandom(245))])
def test_decrypt_cyphertext(standartinput):
	type_crypto = []
	type_crypto.append(standartinput[0])
	if(type(standartinput[1])==bytes):
		modevec = os.urandom(16)
		backend = default_backend()
		cipher = Cipher(algorithms.AES(standartinput[1]),modes.CBC(modevec),backend = backend)
		type_crypto.append(cipher)
		type_crypto.append(0)
	else:
		if(standartinput[2]==2):
			type_crypto.append(standartinput[1].public_key())
		else:
			type_crypto.append(standartinput[1])
		type_crypto.append(1)	
	
	encrypt_text  = encrypt_plaintext(type_crypto,standartinput[3]) 
	if(encrypt_text != 0): #RSA
		if(standartinput[2]!=0):
			type_crypto.pop(1)
			type_crypto.pop(1)
			type_crypto.append(standartinput[1])
			type_crypto.append(standartinput[2])
	dencrypt_text = decrypt_cyphertext(type_crypto,encrypt_text)	
	if(type(standartinput[1]) == bytes): #AES
		assert dencrypt_text == standartinput[3]
	else:
		if(standartinput[2] == 2):
			assert dencrypt_text == standartinput[3]
		else:
			assert dencrypt_text == 0
			type_crypto.pop(2)
			type_crypto.append(2)
			dencrypt_text = decrypt_cyphertext(type_crypto,encrypt_text)
			assert dencrypt_text == 0

@pytest.mark.parametrize("standartinput",[('rsa',None, 2),('aes',None,0,),('rsa',None,1,),('a',None,1),('rsa',None,10)])
def test_create_type_crypto(standartinput):
	if(standartinput[0]=='a' or standartinput[2]>=10):
		assert create_type_crypto(standartinput[0],standartinput[1],standartinput[2]) == 0
	else:
		assert type(create_type_crypto(standartinput[0],standartinput[1],standartinput[2])) == list 

@pytest.mark.parametrize("standartinput",[('rsa',rsa.generate_private_key(public_exponent=65537,key_size=4096,backend=default_backend()), 2,os.urandom(245) ),('aes',os.urandom(32),0,os.urandom(1024)),('rsa',((rsa.generate_private_key(public_exponent=65537,key_size=4096,backend=default_backend())).public_key()) , 1,os.urandom(245))])
def test_signing_cyphertext(standartinput):
	crypto_enter = []
	for i in range(3):
		crypto_enter.append(standartinput[i])
	if(standartinput[2] == 2):
	 	assert type(signing_cyphertext(crypto_enter,standartinput[3])) == bytes
	else:
	 	assert signing_cyphertext(crypto_enter,standartinput[3]) == 0
	 	crypto_enter.pop(2)
	 	crypto_enter.append(2)
	 	assert signing_cyphertext(crypto_enter,standartinput[3]) == 0
	
def test_check_signing_cyphertext():
	pass



