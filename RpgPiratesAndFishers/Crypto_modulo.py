#!/usr/bin/python3
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------------------------------------------------#
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa,utils
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes, base
from cryptography.exceptions import *
from cryptography.hazmat.backends.interfaces import RSABackend
import os
import sys

"""
This module is developed, for encrypt, decrypt and signal messages
He uses , a dict for store key, value, and public or private.
The module use package cryptography, for cryptography.
crypto is a type for handling with type of key(rsa or aes-256),key,(public or private)
(0)type of key - 'rsa' or 'RSA' when rsa 2048 bytes long ,  when 'aes' or 'AES' when aes-256
(1)key is the object it self
(2)scheme - 1 for public, 2 for private, 0 for symetric
"""

def encrypt_plaintext(crypto_enter,plain_text):
	"""
	This function uses, a third party package to encrypt cypher_text(plaitext encrypt).
	@param crypto_enter:(type crypto is a list[str,obj,int]), is used for encrypt message and indicate the type
	type of key used on the moment.
	@param cypher_text:(bytes), bytes encrypt
	@return :(bytes or int), str the cypher text when sucessfull, int(0) when fail
	"""
	if(type(crypto_enter) == list and type(plain_text) == bytes):
		if(crypto_enter[0] == 'RSA' or crypto_enter[0] == 'rsa'):
			if(crypto_enter[2] == 1):
					try:
						answer = crypto_enter[1].encrypt(plain_text,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
					except AttributeError:
						return 0
					else:
						return answer
			else:
				return 0
		if(crypto_enter[0] == 'AES' or crypto_enter[0] == 'aes'):
			if(crypto_enter[2] == 0):
				if(isinstance(crypto_enter[1], Cipher)):
					try:
						enc = crypto_enter[1].encryptor()
					except:
						return 0
					else:
						answer = enc.update(plain_text) + enc.finalize()
						return answer
				else:
					return 0
			else:
				return 0
		else:
			return 0
	else:
		return 0

def decrypt_cyphertext(crypto_enter,cypher_text):
	"""
	This function uses, a third party package to decrypt cypher_text(plaitext encrypt).
	@param crypto_enter:(type crypto is a list[str,obj,int]), is used for decrypt message, and indicate the
	type of key used on the moment.
	@param cypher_text:(bytes), bytes encrypt
	@return :(bytes or int), str the plaintext when sucessfull, int(0) when fail
	"""
	if(type(crypto_enter) == list and type(cypher_text) == bytes):
		if(crypto_enter[0] =='RSA' or crypto_enter[0] =='rsa'):
			if(crypto_enter[2] == 2):
				try:
					answer =  crypto_enter[1].decrypt(cypher_text,padding.OAEP(mgf=padding.MGF1(algorithm= hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
				except AttributeError:
					return 0
				else:
					return answer
			else:
				return 0
		if(crypto_enter[0] =='AES' or crypto_enter[0] =='aes'):
			if(crypto_enter[2] == 0):
				if(isinstance(crypto_enter[1], Cipher)):
					try:
						dec = crypto_enter[1].decryptor()
					except:
						return 0
					else:
						answer = dec.update(cypher_text) + dec.finalize()
						return answer
		else:
			return 0
	else:
		return 0


def create_type_crypto(type_key,obj_key,scheme):
	"""
	This function create a type crypto, that is used for signing, encrypt and decrypt
	@param type_key:(str) , is RSA or AES, that refer to algorithms used for cryptography
	@param obj_key:(object type of third party package) is the object used for encrypt or decrypt
	@param scheme:(int) , represent the scheme , (1) if is public key(rsa),(2) if is private key(rsa),
	(0)otherwise symetric(AES)
	@return : type crypto or 0, that is a list, [type of key, obj key , scheme]  , otherwise return 0
	"""
	crypto_type = []
	if(type_key == 'rsa' or type_key == 'RSA' or type_key == 'AES' or type_key == 'aes'):
		crypto_type.append(type_key)
		crypto_type.append(obj_key)
		if(type(scheme) == int):
			if(scheme>=0 and scheme<=3):
				crypto_type.append(scheme)
				return crypto_type
			else:
				return 0
		else:
			return 0
	else:
		return 0

def signing_cyphertext(crypto_enter,cypher_text):
	"""
	This function, generate a signature of cypher_text, using a third package library
	@param crypto_enter:(type crypto is a list[str,obj,int]), is used for decrypt message, and sinalize
	type of key used on the moment.
	@param cypher_text:(bytes), bytes encrypt
	@return :(bytes or int), bytes of signature when successful, or 0 otherwise
	"""
	hashing = hashes.Hash(hashes.SHA256(),default_backend())
	if(type(cypher_text) != bytes):
		return 0
	hashing.update(cypher_text)
	word_digest = hashing.finalize()
	if(type(crypto_enter) == list):
		if(crypto_enter[0] == 'RSA' or crypto_enter[0] == 'rsa'):
			if(crypto_enter[2] == 2):
				try:
					answer = crypto_enter[1].sign(word_digest,padding.PSS(mgf= padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH),utils.Prehashed(hashes.SHA256()))
				except:
					return 0
				else:
					return answer
			else:
				return 0
		else:
			return 0
	else:
		return 0


def check_signing_cyphertext(crypto_enter,signing_message,cypher_text):
	"""
	This function check if the verification of signing RSA message is correct(1),
	otherwise return flag answer false(0)
	@param crypto_enter:(type crypto is a list[str,obj,int]), is used for decrypt message, ans sinalize
	type of key used on the moment.
	@param signing_message: (bytes type) 256 bytes lenght, signing that will be test
	@param cypher_text: (bytes type) message , that will be used for the test
	@return :(int)1 the verify is correct, 0 otherwise.
	"""
	if(type(crypto_enter) == list and type(cypher_text) == bytes and type(signing_message) == bytes):
		if(crypto_enter[0] == 'RSA' or crypto_enter[0] == 'rsa'):
			if(crypto_enter[2]==1):
				try:
					test = crypto_enter[1].verify(signing_message,cypher_text,padding.PSS(mgf = padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH),hashes.SHA256())
				except InvalidSignature:
					return 0
				else :
					return 1
			else:
				return 0
	else:
		return 0

def generate_aes_256_key():
	"""
	This function generate a AES 256 bits long, using the package crypthography.
	@param None
	@return: (list[Key_of_AES,random_bytes_cbc,Obj_Cipher_AES]) return a 256 bytes AES key and object AES, or 0
	"""
	try:
		key_dec_enc = os.urandom(32)
		mode_vec = os.urandom(16)
		backend = default_backend()
		cipher = Cipher(algorithms.AES(key_dec_enc),modes.CBC(mode_vec),backend = backend)
	except:
		return 0

	else:
		answer = []
		answer.append(key_dec_enc)
		answer.append(mode_vec)
		answer.append(cipher)
		return answer

def check_if_keys_AES_are_the_same(key_value,random_initiation,crypto_enter):
	"""
	This function check if random bytes of CBC mode, and the key are the same of the object
	@param key_value:(bytes) that represent the key of aes 256 used.
	@param random_initiation : (bytes) that are used for random begin of vector at AES.The text
	it's simple, check if it's possible decrypt a string encrypt with the test key.
	@param crypto_enter:(crypto type) the second element in the list contains the object
	@return :(int) 1 if the random_initiation, and key_value combining with the object type AES,
	0 otherwise.
	"""
	if(type(random_initiation) == bytes and type(key_value) == bytes and type(crypto_enter) == list):
		backend = default_backend()
		cipher_test = Cipher(algorithms.AES(key_value),modes.CBC(random_initiation),backend = backend)
		crypto_2  = create_type_crypto('aes',cipher_test,0)
		validation = b"Text control for"
		tx = encrypt_plaintext(crypto_2,validation)
		try:
			tx1 = decrypt_cyphertext(crypto_enter,tx)
		except:
			return 0
		else:
			if(tx1 == validation):
				return 1
			else:
				return 0
	else:
		return 0

def generate_private_RSA_key():
	"""
	This function generate a private RSA key, using the package cryptography
	@param None
	@return : (obj rsa._RSAPrivateKey or 0) object type RSA private, or 0
	"""
	try:
		answer = rsa.generate_private_key(public_exponent=65537,key_size=4096,backend=default_backend())
	except:
		return 0
	else:
		return answer

def deserialize_key_RSA(pem_format_key):
	"""
	This function deserialize a public key RSA, in PEM formar
	@param pem_format_key : (bytes - pem type) pem key, in bytes
	@return : (object public key RSA or 0) object public key or 0
	"""
	try:
		public_key = serialization.load_pem_public_key(pem_format_key,backend = default_backend())
	except:
		return 0
	else:
		return public_key

def serialize_key_RSA(public_key):
	"""
	This function serialize a public key, with the objective to send to the receptor
	@param public_key: (Object type rsa._RSAPublicKey) it's a public key, that will
	be send thow network
	return :(PEM, bytes fomat) a format of send encryption keys, or 0.
	"""
	try:
		pem_format = public_key.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)
	except:
		return 0
	else:
		return pem_format
