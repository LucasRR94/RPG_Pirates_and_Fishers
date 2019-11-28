from Crypto_modulo import *
import math

def verify_len(content,max_len = 245):
	"""
	This function received the strings that will be send, and calculated how much packets of lenght = @max_len it's necessary for send the message. 
	@param content:(str) represent the content it's necessary to send.
	@param max_len :(int) it's the max size of packet, that actual it's limit for signing the message with RSA algorithm.
	@return : the number of packages necessary for send all the content or 0
	"""
	if(type(content) == bytes):
		size_string = len(content) # content+ ' \r\n '
		total_temp  = size_string/max_len
		total = math.ceil(total_temp)
		return total
	else:
		return 0

def verify_size_slice_content(content_message,max_tam_packet):
	"""
	This function split the content_message, on the max tam available on the packet
	@param content_message : (bytes) string bytes, that will be split
	@param max_tam_packet : (int) the size that it's available on the packet
	@return :(list bytes) of content sliced prepared for being encapsulated on the packed  or 0
	"""
	i = verify_len(content_message,max_tam_packet)
	final_list = []
	if(i!=0):
		for k in range(i):
			if(type(content_message) == bytes):
				message = content_message[k*max_tam_packet:k*max_tam_packet+max_tam_packet] + b' \r\n '
			else:
				message = content_message[k*max_tam_packet:k*max_tam_packet+max_tam_packet] + ' \r\n '
			final_list.append(message)
		return final_list
	else:
		return 0

def mounting_answer(content_list,header,footer):
	"""
	This function ,  will mounting the series of messages, with the list of contents, and the header and footer,
	modifying the footer for representing the protocol. With or without continuation of answers.
	@param content_list: (list of bytes) list of all slices of content, that will form the answers
	@param header: (bytes) headers of message
	@param footer: (bytes) footers of message
	@return :(list or int) list of all the messages bytes, or 0 otherwise
	"""
	if(type(content_list) == list and type(header) == bytes and type(footer) == bytes):
		final_messages = []
		footer_final = ""
		for i in range(len(content_list)):
			if(i==len(content_list)-1):
				temp = footer.decode("utf-8")
				footer_final= "0"+" \r\n "
				footer = bytes(footer_final,"utf-8")
			else:
				temp = footer.decode("utf-8")
				footer_final= "1"+" \r\n "
				footer = bytes(footer_final,"utf-8")

			final_messages.append(header+content_list[i]+footer)
		return final_messages
	else:
		return 0

# def produce_content_message_client(num_state,arg):
# 	"""
# 	This function generate content(between header and footer of messages) encapsulating instructions, arguments or keys.

# 	@param num_state:(int) the number that indicate the necessary content
# 	@param arg:(string or list(case of begg) or object in case of key) argument necessary for generate the content.

# 	@return: (bytes or 0) the content for encapsulate in the message, or 0 in case of fail.
# 	"""
# 	dict_content = {1231:"LIFF",1232:"LSTI",1233:"GETS",1234:"DIRI",1235:"CATS",1236:"GETI",1237:"REPF"}
# 	try:
# 		answer_temp = dict_content[num_state]
# 	except KeyError:
# 		try:
# 			if(i==1 or i==6 or i==9):
# 				answer_temp = arg + " "+" \r\n "
# 			if(i == 3 or i==122 or i==121 or i == 120 or i == 124):
# 				answer_temp = bytes(arg,"utf-8") + " "+" \r\n "
# 			if(i==10):
# 				answer_temp = bytes(arg[0],"utf-8") + " "+" \r\n "+bytes(arg[1],"utf-8") + " "+" \r\n "
# 		except:
# 			return 0
# 		else:
# 			return answer_temp
# 	else:
# 		answer_temp = answer_temp+" "+" \r\n "
# 		return bytes(answer_temp,"utf-8")

def gen_footer(num_state):
	"""
	This function , return a bytes sequence, that represent a footer of message

	@param num_state:(int) that indicate that if has or not continuation

	@return:(bytes) bytes sequence, or 0
	"""
	if(num_state == 1):
		answer_temp = " 1 \r\n "
		return bytes(answer_temp,"utf-8")
	if(num_state == 0):
		answer_temp = " 0 \r\n "
		return bytes(answer_temp,"utf-8")
	else:
		return 0		

def header_definition_client(num_state,version_protocol):
	"""
	This function generate Headers of client messages.
	@param num_state: (int) it's a number that indicate the instruction for header
	@param version_protocol:(str) that indicate the actual version of the game
	@return :(bytes or 0) bytes that are the header of message.
	"""
	dict_headers = {1:"HIII",3:"EXIN",4:"PROC",6:"CONF",7:"EKEY",9:"BEGG",120:"USEI",121:"MOVF",122:"ATQE",123:"GAME",124:"CATI"}
	try:
		answer_temp = dict_headers[num_state]
	except KeyError:
		return 0
	else:
		answer_temp1=" "+str(version_protocol)
		answer_temp = answer_temp+answer_temp1+" "+"\r\n "
		return bytes(answer_temp,"utf-8")

def check_lenght_complete_with_dont_care(message,fixed_lenght = 245):
	"""
	This function check the lenght a message(bytes), and if the lengh it's not equal to fixed_lenght,the
	message it's modified, append 'X' character, until have the specific lenght
	@param message: (bytes) bytes coded at utf-8
	@param fixed_lenght:(int) maximum number of characters in message
	@para :(bytes or int) if have the specific lenght or less(it's modified and return), if is bigger or other problem 0.
	"""
	if(type(message)==bytes and type(fixed_lenght) == int):
		answer_temp = message.decode("utf-8")
		added = ""
		for i in range(fixed_lenght-len(message)):
			added+="X"
		answer_temp1 = answer_temp + added
		answer = bytes(answer_temp1,"utf-8")
		return answer
	else:
		return 0

def prepare_send_socket(list_of_messages,max_lenght):
	"""
	This function check the lenght, and prepare a list, for send message or messages.
	@param message:(list) has one message, or multiple messages.
	@param max_lenght:(int) maximum number of characters in message
	@return:(list of messages) with the correct lenght, or 0
	"""
	if(type(list_of_messages) == list):
		finalanswer = []
		for i in range(len(list_of_messages)):
			if(len(list_of_messages[i]) < max_lenght):
				finalanswer.append(check_lenght_complete_with_dont_care(list_of_messages[i],max_lenght))
			if(len(list_of_messages[i]) == max_lenght):
				finalanswer.append(list_of_messages[i])
			if(len(list_of_messages[i]) > max_lenght):# critic fail in the process	
				print(len(list_of_messages[i]))
				return 0
		return finalanswer
	else:
		return 0

def insert_signing_on_messages(list_messages, crypto_enter):
	"""
	This function, receive a messagem with lenght of 245 bytes long, and append to every message a 512 signing
	using the Crypto_modulo
	@param list_messages:(list) have all the messages that will be signing
	@param crypto_enter_RSA: (Crypto type) have the private key that will signing the messages , in case of error 0.
	@return :(list) of messages appended with signing
	"""
	final_answer = []
	if(type(list_messages) == list):
		if(crypto_enter!=None):
			for i in range(len(list_messages)):
				sig = signing_cyphertext(crypto_enter,list_messages[i])
				final_signing = b" \r\n " + sig
				final_answer.append(list_messages[i]+final_signing)
			return final_answer
		else:
			return list_messages
	else:
		return 0

def prepare_answer_for_send(content,max_lenght_answer,header,footer,crypto_enter):
	"""
	This function encapsulate, functions for, check the lenght of content, mounting content with header and footers,
	append don't care content in answers, and add signing in answers to prepare to send.
	@param content:(bytes) necessary content, for insert on the answer.
	@param max_lenght_answer:(int) maximum , lenght of answer
	@param header:(bytes) header of answer
	@param footer:(bytes) footer of answer
	@param crypto_enter: Crypto type, used for signing.

	@return :(list of messages prepared for send) list of bytes.
	"""
	if(content != None):
		content_list = verify_size_slice_content(content , max_lenght_answer - (len(header + footer) + 6))
		final_messages = mounting_answer(content_list,header,footer)
		prepared_messages = prepare_send_socket(final_messages,max_lenght_answer)
		final_sockets_message = insert_signing_on_messages(prepared_messages,crypto_enter)
		return final_sockets_message
	else:
		create_list = []
		create_list.append(header+footer)
		prepared_messages = prepare_send_socket(create_list,max_lenght_answer)
		final_sockets_message = insert_signing_on_messages(prepared_messages,crypto_enter)
		return final_sockets_message

def mount_answer_client(option_state_machine,secundary_option,content,max_lenght_answer,version_of_software,crypto_enter_signing):
	"""
	This function automatically create the header and footer, mounting the final message , returning the message ready to send

	@param option_state_machine : (str) the actual state or next state, necessary for switch parameters
	@param secundary_option: (int) it's used in case of exist multiple and diferrent types of messages possible to send
	@param content :(Bytes or None) content that will be append in header, and footer.
	@param version_of_software:(str) it's a string that represent the version of software.
	@param crypto_enter_signing:(Crypto enter) this private message it's used for signing the message
	@return : (Bytes or None) the final message ready for be send in the socket,or None

	"""
	final_message_prepared_for_socket = None
	if(option_state_machine == 0):
		final_message_prepared_for_socket = prepare_answer_for_send(content,max_lenght_answer,header_definition_client(1,version_of_software),gen_footer(1),None)

	elif(option_state_machine == 2):
		
		if(secundary_option == 0): #Error finish with Exin
			final_message_prepared_for_socket = prepare_answer_for_send(None,max_lenght_answer,header_definition_client(3,version_of_software),gen_footer(0),None)
		
		else:
			final_message_prepared_for_socket = prepare_answer_for_send(None,max_lenght_answer,header_definition_client(4,version_of_software),gen_footer(0),None)
	
	elif(option_state_machine == 5):
		final_message_prepared_for_socket = prepare_answer_for_send(content,max_lenght_answer,header_definition_client(6,version_of_software),gen_footer(1),None)

	elif(option_state_machine == 7):
		final_message_prepared_for_socket = prepare_answer_for_send(content,max_lenght_answer,header_definition_client(7,version_of_software),gen_footer(1),crypto_enter_signing)

	elif(option_state_machine == 9):
		final_message_prepared_for_socket = prepare_answer_for_send(content,max_lenght_answer,header_definition_client(9,version_of_software),gen_footer(1),crypto_enter_signing)

	elif(option_state_machine == 10):
		
		if(secundary_option == 0): # Nickname it's alredy in use, it's necessary other nickname
			final_message_prepared_for_socket = prepare_answer_for_send(content,max_lenght_answer,header_definition_client(9,version_of_software),gen_footer(1),crypto_enter_signing)
		
		else:
			final_message_prepared_for_socket = prepare_answer_for_send(content,max_lenght_answer,header_definition_client(secundary_option,version_of_software),gen_footer(1),crypto_enter_signing)
	
	elif(option_state_machine == 11 or option_state_machine == 12):
		final_message_prepared_for_socket = prepare_answer_for_send(content,max_lenght_answer,header_definition_client(secundary_option,version_of_software),gen_footer(1),crypto_enter_signing)

	elif(option_state_machine == 14):
		#SEND EXIN
		final_message_prepared_for_socket = prepare_answer_for_send(None,max_lenght_answer,header_definition_client(3,version_of_software),gen_footer(0),crypto_enter_signing)
	
	return final_message_prepared_for_socket

def state_machine_client(actual_state,version_of_software,instruction_arg,max_lenght_message,crypto_enter_RSA,crypto_enter_AES,socket_send):
	"""
	This function, it's state machine, from the client side protocol.This function uses the actual state,
	and the message received, to generate te return and the logic of new state.

	@param actual_state : (int) the actual state from state machine.
	@param version_of_software:(str) informe the actual version of software
	@param instruction_arg:(str or bytes that will be used)
	@param max_lenght_message:(int) it's the maximum lenght of message
	@param crypto_enter_RSA:(list -> type, key,scheme RSA) it's documented at Crypto_modulo
	@param crypto_enter_AES:(list -> type, key,scheme AES) it's documented at Crypto_modulo
	@param socket_send:(Object type socket), object that it's use for send the packet throw network
	@return : (list) the next state and keys generated or 0.
	"""
	if(actual_state == 0):
		crypto_enter = create_type_crypto('rsa',generate_private_RSA_key(),2)
		pem_format   = serialize_key_RSA(crypto_enter[1].public_key())
		final_answer_server = mount_answer_client(0,None,pem_format,max_lenght_message,version_of_software,None)
		#send the message gen
		#print(final_message_prepared_for_socket[0])
		#return[1,crypto_enter]
		return final_message_prepared_for_socket

	elif(actual_state == 1):
		# message received 757 bytes
		message = b""	#action state 1
		pem_format_check = message[0:245]
		return [2,pem_format_check]

	elif(actual_state == 2): # action state 2
		if(instruction_arg == serialize_key_RSA(crypto_enter_RSA[1].public_key())):
			return[4,None]
		else:
			return[3,None]

	elif(actual_state == 3): #action state 3
		#print(final_message_prepared_for_socket)
		final_answer_server = mount_answer_client(2,0,None,max_lenght_message,version_of_software,None)
		return [None,None] # stop thread, and finalize thread
		#send(final_message_prepared_for_socket)

	elif(actual_state == 4): #action state 4
		final_answer_server = mount_answer_client(2,1,None,max_lenght_message,version_of_software,None)
		# header = header_definition_client(4,version_of_software) # action state 4
		# footer = gen_footer(0)
		# final_message_prepared_for_socket = prepare_answer_for_send(None,max_lenght_message,header,footer,None)
		print(final_message_prepared_for_socket)
		#send(final_message_prepared_for_socket)
		return[5,None]

	elif(actual_state == 5): # action state 5
		#receive message
		message = "	"
		content = create_type_crypto('rsa',deserialize_key_RSA(message),1)
		finalMessage = mount_answer_client(actual_state,None,content,max_lenght_message,version_of_software,None)
		#send final message
		return [6,crypto_enter]

	elif(actual_state == 6): # action state 6
		#receive(message)
		# header = header_definition_client(6,version_of_software)
		# footer = gen_footer(1)
		pem_format   = serialize_key_RSA(crypto_enter_RSA[1].public_key())
		# final_message_prepared_for_socket = prepare_answer_for_send(pem_format,max_lenght_message,header,footer,None)
		print(final_message_prepared_for_socket)
		#send_message(final_message_prepared_for_socket)
		#receive_ (message2)
		if(message[0] == '9999'):
			return[8,None]
		if(message[0] == '8588'):
			return[7,None]

	elif(actual_state == 7): # action state 7
		aes_enter = generate_aes_256_key()
		crypto_enter_aes = create_type_crypto('aes',aes_enter[2],0)
		content = aes_enter[0]+ b" \r\n "+ aes_enter[1]+ b" \r\n "
		final_answer_server = mount_answer_client(actual_state,None,content,max_lenght_message,version_of_software,crypto_enter_RSA)
		print(final_answer_server)
		return[9,final_answer_server]

	elif(actual_state == 8): # action state 8
		#receive message
		return[None,None] # finish thread

	elif(actual_state == 9):#send BEGG
		print("Please digit the name of your player, minimus 5 characters, 32 in the maximun\n")
		entrada_user = input()
		entrada_user+= " \r\n "
		content = bytes(entrada_user,"utf-8")
		final_answer_server = mount_answer_client(actual_state,None,content,max_lenght_message,version_of_software,crypto_enter_RSA)
		return [10,None]

	elif(actual_state == 10):
		#received informartion
		message = "Algo"
		if(message =='8976'): #it's necessary change nickname
			print("Please digit the name of your player, minimus 5 characters, 32 in the maximun\n")
			entrada_user = input()
			entrada_user+= " \r\n "
			content = bytes(entrada_user,"utf-8")
			final_answer_server = mount_answer_client(actual_state,0,content,max_lenght_message,version_of_software,crypto_enter_RSA)
			#send information
			return [10,None]	
		
		elif(message =='0000'): #waiting for start
			return [11,None]
		
		elif(message == '7777'):# it's open for start the menu		
			message_construct = menu_User_Option() # return a list -> header , content
			final_answer_server = mount_answer_client(actual_state,message_construct[0],message_construct[1],max_lenght_message,version_of_software,crypto_enter_RSA)
			#send  final_answer_server
			return [12,None]

	elif(actual_state == 11):
		#receive (message)
		if(message == "1111"):
			message_construct = menu_User_Option() # return a list -> header , content
			final_answer_server = mount_answer_client(actual_state,message_construct[0],message_construct[1],max_lenght_message,version_of_software,crypto_enter_RSA)
			return[12,None]
		else: # stop the game
			# print fail
			return [None,None]

	elif(actual_state == 12):
		#receive(message)
		if(message == "2222"):
			message_construct = menu_User_Option() # return a list -> header , content
			final_answer_server = mount_answer_client(actual_state,message_construct[0],message_construct[1],max_lenght_message,version_of_software,crypto_enter_RSA)
			return [12,None]

		if(message == "9999"):
			#print message[1]
			return [14,None]

		if(message == "5555"):
			#print the message
			return [13,None]


	elif(actual_state == 13):
		#finish the resources
		return [None,None]

	elif(actual_state == 14):
		print("Do you wanna disconnect or wait?")
		finish = input()
		if(int(finish) == 1):
			#send EXIN
			final_answer_server = mount_answer_client(actual_state,None,None,max_lenght_message,version_of_software,crypto_enter_RSA)
			#finish resources
			return [None,None]
		else:
			#receive message
			#print message
			return [None,None]

	else: #finish if message not correct
		return [None,None]

def disconnect_or_wait():
	"""
	This function ask for the player if he wanna disconnect(return 1) otherwise he will wait for message of winner
	
	@param None:None

	@return :int 1 if wanna disconnect , 0 if wanna wait 
	"""
	print("Type 1 if you wanna disconnect of game, 0 if you wanna waiting for know the winner")
	enter = input()
	if (enter == '1' or enter == '0'):
		return enter
	else:
		return disconnect_or_wait()	

def menu_User_Option():
	"""
	This function ask for user, what action he want to perform in the game, returning in form of number of instruction and content, ready to use
	@param None
	@param :(list[int,content]) the instruction ready to use, and content or None.
	"""
	dict_header = {0:123,1:120,2:124,3:123,4:123,5:121,6:123,7:123,8:122,9:123,10:123,11:3}
	dict_secundary_content = {0:1231,3:1232,4:1233,6:1234,7:1235,9:1236,10:1237,11:None}
	ok_to_out = 0
	finalAnswer = []
	while(ok_to_out ==0):
		print("\n\nType 0 for list Items from Fisher\nType 1 for use a item\nType 2 for Catch a item on Island\nType 3 for list items from Island\nType 4 for Know if are available Spells on the actual Island\nType 5 move for other island\nType 6 list all possible directions\nType 7 catch Spells if available in the island\nType 8 for Ataque enemie\nType 9 list enemies in the island\nType 10 report the actual situation, health, weapon, defense\nType 11 for exit of map\n\n")
		temp_var_option = input()
		try:
			header_value = dict_header[int(temp_var_option)]
		except KeyError:
			ok_to_out = 0
		else:
			ok_to_out = 1 #it's valid option
			try:
				content_value = dict_secundary_content[int(temp_var_option)]
			except KeyError:
				if(temp_var_option == 1):
					print("Type the name of the item that you want use, that it's present on the backpack!\n")
				
				elif(temp_var_option == 2):
					print("Type the name of the item that you want catch in the island!\n")
				
				elif(temp_var_option == 5):
					print("Type the name of the island that will whant to move!!!\n")
				
				elif(temp_var_option == 8):
					print("Type the name the enemie that you want to atack !\n")
				else:
					ok_to_out = 0
				content = input()
				finalAnswer.append(header_value)
				finalAnswer.append(content)
			else:
				finalAnswer.append(header_value)
				finalAnswer.append(content_value)
	
	return finalAnswer


def behavior_User_Option():
	pass
	
def decrypt_Check_Signing(cypher_or_signedText,actual_state_Crypt,crypto_enter_RSA,crypto_enter_AES):
	"""
	This function check if the text it's encrypt or signing the @cypher_or_signedText, it's use a variable actual_state_Crypt,
	for indentify was it's used in the @cypher_or_signedText, (0) plain text, (1) aes encrypt, (2) rsa encrypt , (3) signed text,
	(4) for signed text encrypt with aes, (5) for signed text encrypt using rsa.
	@param cypher_or_signedText : (Bytes) that it's necessary decrypt or test the signed.
	@param crypto_enter_RSA : (Crypto type document in the project), used for verify signing , and decrypt a packet.
	@param crypto_enter_AES : (Crypto type document in the project), used for decrypt a packet.
	@param actual_state_Crypt: (int) a number that informed if it's crypto with rsa(2), aes(1), and if it's signing(3).
	@return : (String or 0) string with the text check or decrypt, or 0 if it's not possible check the signed or impossible 
	to decrypt
	"""
	base_text = ""
	if(actual_state_Crypt == 0):
		base_text = cypher_or_signedText.decode("utf-8")
	
	if(actual_state_Crypt == 1): #aes encrypt	
		base_text_1 = decrypt_cyphertext(crypto_enter_AES,cypher_or_signedText[0:256])
		base_text = base_text_1.decode("utf-8")

	if(actual_state_Crypt == 2): #rsa encrypt	
		base_text_1 = decrypt_cyphertext(crypto_enter_RSA,cypher_or_signedText[0:256])
		base_text = base_text_1.decode("utf-8")

	if(actual_state_Crypt == 4): #signed message + aes encrypt
		check_signed = signing_cyphertext(crypto_enter_RSA[1].public_key(),cypher_or_signedText[257:769])
		if(check_signed == 0):
			return 0
		base_text_1 = decrypt_cyphertext(crypto_enter_AES,cypher_or_signedText[0:256])
		base_text = base_text_1.decode("utf-8")	

	if(actual_state_Crypt == 5): #signed message + rsa encrypt
		check_signed = signing_cyphertext(crypto_enter_RSA[1].public_key(),cypher_or_signedText[257:769])
		if(check_signed == 0):
			return 0
		base_text_1 = decrypt_cyphertext(crypto_enter_AES,cypher_or_signedText[0:256])
		base_text = base_text_1.decode("utf-8")

	return base_text

def umount_message_client(message_recv,crypto_enter_RSA,crypto_enter_AES,actual_state_Crypt):
	"""
	This function umount a message, separate Header(represent integer) , footer and content, from a messagem received from client
	
	@param message_recv : (Bytes) received message from client.
	@param crypto_enter_RSA : (Crypto type document in the project), used for verify signing , and decrypt a packet.
	@param crypto_enter_AES : (Crypto type document in the project), used for decrypt a packet.
	@param actual_state_Crypt: (int) a number that informed if it's crypto with rsa(2), aes(1), and if it's signing(3), it's necessary
	sum the variables, if it's not encrypt it's 0, if encrypt aes it's 1 , if encrypt with aes and signed it's 4.
	
	@return :the return of the function it's a simple list with the code of message in first position, and the contents 
	entirely at second position, and third it's flag if the message continue or not. Or None
	"""
	if(type(message_recv)!= bytes):
		return None
	else:
		base_text = ""
		base_text = decrypt_Check_Signing(message_recv,actual_state_Crypt,crypto_enter_RSA,crypto_enter_AES)
		if(base_text==0): # Error at decrypt or check signing
			return None
		string_decode = base_text
		temp_part = string_decode.split(" \r\n ")
		catCodeMessage = temp_part[0][0:4]
		finalAnswer = []
		dict_headers = {"HIII":1,"EXIN":3 ,"PROC":4 ,"CONF":6,"EKEY":9,"BEGG":10,"USEI":120,"MOVF":121,"ATQE":122,"GAME":123,"CATI":124}
		try:
			finalAnswer.append(dict_headers[catCodeMessage])	
		except KeyError:
			return None
		else:
			finalAnswer.append(temp_part[1])# copy the content
			if(temp_part[2] == "0"):
				finalAnswer.append(0)# Don't has more messages to received
				return finalAnswer
			if(temp_part[2] == "1"):
				finalAnswer.append(1)# has more messages to received
				return finalAnswer
			else:
				return None
			
