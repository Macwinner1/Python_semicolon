menu = """ 

		Welcome to the menu list 
		Press: 
 
		1 -> Phone book 
		2 -> Messages 
		3 -> Chat 
		4 -> Call register 
		5 -> Tones 
		6 -> Settings 
		7 -> Call divert 
		8 -> Games 
		9 -> Calculator 
		10 -> Reminders 
		11 -> Clock 
		12 -> Profiles 
		13 -> SIM services
		 0 <- Exit

 		"""
exit = True
while exit:
	print(menu)
	menuInput = input()
	match menuInput:
		case '1':
			phonebook = """ 

		1. Phonebook 
 
		1 -> Search 
		2 -> Service Nos. 
		3 -> Add name 
		4 -> Erase 
		5 -> Edit 
		6 -> Assign tone 
		7 -> Send b'card 
		8 -> Options 
		9 -> Speed dials 
		10 -> Voice tags
		0 <- Back
 
                            """
			
			back7 = True
			while back7:
				print(phonebook)
				pressPhoneBook = input() 
				match pressPhoneBook:
					case '0':
						back7 = False 
					case '1':
						search = """
	Search
	0. Back
                            		""" 
						back_7 = True
						while back_7:
							print(search)
							press_search = input()
							match press_search:
								case '0':
									back_7 = False
								case _: 
									print("Invaild option")
					case '2': 
						serviceNos = """

	Service Nos
	0. Back
			    		"""   
						back_8 = True
						while back_8:
							print(serviceNos)
							press_serviceNos = input()
							match press_serviceNos:
								case '0':
									back_8 = False
								case _:
									print("Invaild option")
                            
					case '3': 
						addName = """

	Add name
	0. Back
			    		"""  
						
						back_18 = True
						while back_18:
							print(addName)
							press_addName = input()
							match press_addName:
								case '0':
									back_18 = False
								case _:
									print("Invaild option")
                           
					case '4':
						erase = """

	Erase
	0. Back
			    		"""
						
						back_13 = True
						while back_13:
							print(erase)
							press_erase = input()
							match press_erase:
								case '0':
									back_13 = False
								case _:
									print("Invaild option")
                             
					case '5':
						edit = """

	Edit
	0. Back
			    		"""
						
						back_14 = True
						while back_14:
							print(edit)
							press_edit = input()
							match press_edit:
								case '0':
									back_14 = False
								case _:
									print("Invaild option")
                         
					case '6':
						assignTone = """

	Assign tone
	0. Back
			    		"""
						
						back_15 = True
						while back_15:
							print(assignTone)
							press_assignTone = input()
							match press_assignTone:
								case '0':
									back_15 = False
								case _:
									print("Invaild option")
                             
					case '7':
						sendBcard = """

	Send b'card
	0. Back
		 	    		""" 
						
						back_16 = True
						while back_16:
							print(sendBcard)
							press_sendBcard = input()
							match press_sendBcard:
								case '0':
									back_16 = False
								case _:
									print("Invaild option")
                          
					case '8': 
						options = """ 

	8. Options 

	1. Type of view 
	2. Memory status 
	0.<- Back


                                    	"""
						Back1 = True
						while Back1:
							print(options) 
							pressOptions = input()
							match pressOptions:
								case '0':
									Back1 = False 
								case '1':
									typeView = """

	Type of view
	0. Back
				    			"""
									
									back_10 = True
									while back_10:
										print(typeView)
										press_typeView = input()
										match press_typeView:
											case '0':
												back_10 = False
											case _:
												print("Invaild option")
									
                                    
								case '2':
									memoryStatus = """

	Memory status
	0. Back
				    			""" 
									
									back_10 = True
									while back_10:
										print(memoryStatus)
										press_memoryStatus = input()
										match press_memoryStatus:
											case '0':
												back_10 = False
											case _:
												print("Invaild option")

								case _:
									print("Invaild Input")
                                     
					case '9':
						speedDials = """

	Speed dials
	0. Back
			    		"""   
						
						back_16 = True
						while back_16:
							print(speedDials)
							press_speedDials = input()
							match press_speedDials:
								case '0':
									back_16 = False
								case _:
									print("Invaild option")
                             
					case '10':
						voiceTags = """

	Voice tags
	0. Back
			    		"""   
						
						back_11 = True
						while back_11:
							print(voiceTags)
							press_voiceTags = input()
							match press_voiceTags:
								case '0':
									back_11 = False
								case _:
									print("Invaild option")
					case _:
						print("Invalid option")
							
		
		case '2':
			messages = """ 


	2. Messages 
 
	1 -> Write messages 
	2 -> Inbox 
	3 -> Outbox 
	4 -> Picture messages 
	5 -> Templates 
	6 -> Smileys 
	7 -> Message settings 
	8 -> Info service 
	9 -> Voice mailbox number 
	10 -> Service command editor 
	0 <- Back

                        """
			
			back = True
			while back:
				print(messages)
				pressMessages = input()
				match pressMessages:
					case '0':
						back = False 
					case '1': 
						writeMessages = """

	Write Messages
	0. Back
			    		"""
						
						back_110 = True
						while back_110:
							print(writeMessages)
							press_writeMessages = input()
							match press_writeMessages:
								case '0':
									back_110 = False
								case _:
									print("Invaild option")
						
                           
					case '2':
						inbox = """

	Inbox
	0. Back
			    		"""
						
						back_110 = True
						while back_110:
							print(inbox)
							press_inbox = input()
							match press_inbox:
								case '0':
									back_110 = False
								case _:
									print("Invaild option") 
                           
					case '3': 
						outbox = """

	Outbox
	0. Back
			    		"""
						
						back_111 = True
						while back_111:
							print(outbox)
							press_outbox = input()
							match press_outbox:
								case '0':
									back_111 = False
								case _:
									print("Invaild option") 
                             
					case '4': 
						pictureMessages = """

	Picture Messages
	0. Back
			    		"""
						
						back_112 = True
						while back_112:
							print(pictureMessages)
							press_pictureMessages = input()
							match press_pictureMessages:
								case '0':
									back_112 = False
								case _:
									print("Invaild option")
                            
					case '5':
						templates = """

	Templates
	0. Back
			    		"""
						
						back_112 = True
						while back_112:
							print(templates)
							press_templates = input()
							match press_templates:
								case '0':
									back_112 = False
								case _:
									print("Invaild option")
                             
					case '6':
						smileys = """

	Smileys
	0. Back
			    		"""
						
						back_113 = True
						while back_113:
							print(smileys)
							press_smileys = input()
							match press_smileys:
								case '0':
									back_113 = False
								case _:
									print("Invaild option")
                             
					case '7':
						messageSettings = """ 

	7. Message Settings 
 
	1. Set 1 
	2. Common 
	0.<- Back

                                    	""" 
						
						back2 = True
						while back2:
							print(messageSettings) 
							pressMessageSettings = input() 
							match pressMessageSettings:
								case '0':
									back2 = False
								case '1':
									set1 = """ 

	1. Set 1 
 
	1. Message center number 
	2. Messages sent as 
	3. Message validity
	0.<- back
 
                                            		""" 
									
									back3 = True
									while back3:
										print(set1)
										pressSet1 = input()
										match pressSet1:
											case '0': 
												back3 = False 
											case '1': 
												messageCenter = """
   
	Message center number
	0. Back
					    				"""
												
												back_114 = True
												while back_114:
													print(messageCenter)
													press_messageCenter = input()
													match press_messageCenter:
														case '0':
															back_114 = False
														case _:
															print("Invaild option")
                                            
											case '2': 
												messagesSent = """

	Message sent as
	0. Back
					    				"""
												
												back_115 = True
												while back_115:
													print(messagesSent)
													press_messagesSent = input()
													match press_messagesSent:
														case '0':
															back_115 = False
														case _:
															print("Invaild option")
                                             
											case '3':
												messagesValidity = """

	Message validity
	0. Back
					    				"""
												
												back_116 = True
												while back_116:
													print(messagesValidity)
													press_messagesValidity = input()
													match press_messagesValidity:
														case '0':
															back_116 = False
														case _:
															print("Invaild option")
											case _:
												print("Invalid input")

								case '2':
									common = """ 

	2. Common 
 
	1. Delivery reports 
	2. Reply via same centre 
	3. Character support 
	0.<- Back
							"""
									
									back4 = True
									while back4:
										print(common)
										pressCommon = input() 
										match pressCommon:
											case '0':
												back4 = False
											case '1': 
												deliveryReports = """
   
	Delivery reports
	0. Back
									"""
												
												back_116 = True
												while back_116:
													print(deliveryReports)
													press_deliveryReports = input()
													match press_deliveryReports:
														case '0':
															back_116 = False
														case _:
															print("Invaild option")
                                             
											case '2':
												replyVia = """

	Reply Via same centre
	0. Back
					    				"""
												
												back_117 = True
												while back_117:
													print(replyVia)
													press_replyVia = input()
													match press_replyVia:
														case '0':
															back_117 = False
														case _:
															print("Invaild option")
												
                                             
											case '3':
												characterSupport = """

	Character support
	0. Back
					    				"""
												
												back_118 = True
												while back_118:
													print(characterSupport)
													press_characterSupport = input()
													match press_characterSupport:
														case '0':
															back_118 = False
														case _:
															print("Invaild option")
											case _:
												print("Invalid input")

					case '8':
						infoService = """

	Info Service
	0. Back
			    		"""
						
						back_118 = True
						while back_118:
							print(infoService)
							press_infoService = input()
							match press_infoService:
								case '0':
									back_118 = False
								case _:
									print("Invaild option")
                         
					case '9':
						voiceMailboxNumber = """

	Voice mailbox number 
	0. Back	
			    		"""
						print(voiceMailboxNumber)
						back_121 = True
						while back_121:
							print(voiceMailboxNumber)
							press_voiceMailboxNumber = input()
							match press_voiceMailboxNumber:
								case '0':
									back_121 = False
								case _:
									print("Invaild option")
                       
					case '10':
						serviceCommand = """

	Service command editor 
	0. Back
			    		"""
						
						back_122 = True
						while back_122:
							print(serviceCommand)
							press_serviceCommand = input()
							match press_serviceCommand:
								case '0':
									back_122 = False
								case _:
									print("Invaild option")
					case _:
						print("Invalid input")






		case '3':
			chat = """

		Chat
		0. Back

		    	"""  
			
			back1 = True
			while back1:
				print(chat)
				press_chat = input()
				match press_chat:
					case '0':
						back1 = False
					case _: 
						print("Invalid option")

		case '4':
			callRegister = """ 


		4. Call register 
 
		1 -> Missed calls 
		2 -> Received calls 
		3 -> Dialled numbers 
		4 -> Erase recent call lists 
		5 -> Show call duration 
		6 -> Show call costs 
		7 -> Call cost settings 
		8 -> Prepaid credit 
		9 <- Back

                            """
			
			back1 = True
			while back1:
				print(callRegister)
				pressCallRegister = input()
				match pressCallRegister:
					case '0':
						back1 = False 
					case '1':
						missedCalls = """

		Missed calls
		0. Back

			    		"""   
						
						back_123 = True
						while back_123:
							print(missedCalls)
							press_missedCalls = input()
							match press_missedCalls:
								case '0':
									back_123 = False
								case _:
									print("Invaild option") 
                            
					case '2': 
						receivedCalls = """

		Received calls
		0. Back
			    		""" 
						
						back_124 = True
						while back_124:
							print(receivedCalls)
							press_receivedCalls = input()
							match press_receivedCalls:
								case '0':
									back_124 = False
								case _:
									print("Invaild option") 
                           
					case '3':
						dialledNumbers = """

		Dialled numbers
		0. Back
			    		"""
						
						back_125 = True
						while back_125:
							print(dialledNumbers)
							press_dialledNumbers = input()
							match press_dialledNumbers:
								case '0':
									back_125 = False
								case _:
									print("Invaild option") 
                       
					case '4':
						eraseRecentCall = """

		Erase recent call lists
		0. Back

			    		"""
						
						back_126 = True
						while back_126:
							print(eraseRecentCall)
							press_eraseRecentCall = input()
							match press_eraseRecentCall:
								case '0':
									back_126 = False
								case _:
									print("Invaild option")
					case '5': 
						showCallDuration = """ 

		5. Show call duration 
 
		1. Last call duration 
		2. All calls' duration 
		3. Received calls' duration
		4. Dialled calls' duration
		5. Clear timers
		0<- Back

                                            """ 
						
						back1 = True
						while back1:
							print(showCallDuration) 
							pressShowCallDuration = input() 
							match pressShowCallDuration:
								case '0':
									back1 = False
								case '1':
									lastCallDuration = """
   
		Last call duration
		0. Back
					    		"""
									
									back_123 = True
									while back_123:
										print(lastCallDuration)
										press_lastCallDuration = input()
										match press_lastCallDuration:
											case '0':
												back_123 = False
											case _:
												print("Invaild option")
                                          
								case '2':
									allCallsDuration = """

		All calls' duration 
		0. Back
					    		"""
									
									back_124 = True
									while back_124:
										print(allCallsDuration)
										press_allCallsDuration = input()
										match press_allCallsDuration:
											case '0':
												back_124 = False
											case _:
												print("Invaild option") 
                                       
								case '3':
									receivedCallsDuration = """

		Received calls' duration
		0. Back
					    		"""
									
									back_125 = True
									while back_125:
										print(receivedCallsDuration)
										press_receivedCallsDuration = input()
										match press_receivedCallsDuration:
											case '0':
												back_125 = False
											case _:
												print("Invaild option")
					  
								case '4': 
									dialledCallsDuration = """
   
		Dialled calls' duration
		0. Back

					    		"""
									
									back_126 = True
									while back_126:
										print(dialledCallsDuration)
										press_dialledCallsDuration = input()
										match press_dialledCallsDuration:
											case '0':
												back_126 = False
											case _:
												print("Invaild option") 
                                         
								case '5':
									clearTimers = """

		Clear timers
		0. Back
					    		"""
									
									back_127 = True
									while back_127:
										print(clearTimers)
										press_clearTimers = input()
										match press_clearTimers:
											case '0':
												back_127 = False
											case _:
												print("Invaild option") 
               

					case '6':
						showCallCosts = """ 


		6. Show call costs 
 
		1. Last call cost 
		2. All calls' cost
		3. Clear counters
		0.<- Back

                                            		"""
						
						back2 = True
						while back2:
							print(showCallCosts) 
							pressShowCallCost = input()
							match pressShowCallCost:
								case '0':
									back2 = False
								case '1':
									lastCallCost = """
   
		Last call cost
		0. Back
					    				"""
									
									back_128 = True
									while back_128:
										print(lastCallCost)
										press_lastCallCost = input()
										match press_lastCallCost:
											case '0':
												back_128 = False
											case _:
												print("Invaild option")
									 
                                          
								case '2':
									allCallsCost = """

		All calls' cost 
		0. Back
					    				"""
									
									back_129 = True
									while back_129:
										print(allCallsCost)
										press_allCallsCost = input()
										match press_allCallsCost:
											case '0':
												back_129 = False
											case _:
												print("Invaild option") 
                                           
								case '3':
									clearCounters = """

		Clear counters
		0. Back
					    				"""
									
									back_130 = True
									while back_130:
										print(clearCounters)
										press_clearCounters = input()
										match press_clearCounters:
											case '0':
												back_130 = False
											case _:
												print("Invaild option")
                                         
                                 

					case '7':
						callCostSettings = """ 


		7. Call cost settings 
 
		1. Call cost limit 
		2. Show costs in
		0.<- Back

                                            		""" 
						
						back3 = True
						while back3:
							print(callCostSettings) 
							pressCallCostSettings = input() 
							match pressCallCostSettings:
								case '0':
									back3 = False
								case '1':
									callCostLimit = """
   
		Call cost limit
		0. Back
					    				"""
									
									back_131 = True
									while back_131:
										print(callCostLimit)
										press_callCostLimit = input()
										match press_callCostLimit:
											case '0':
												back_131 = False
											case _:
												print("Invaild option")
 
								case '2':
									showCostsIn = """

		Show costs in
		0. Back
					    				"""
									
									back_132 = True
									while back_132:
										print(showCostsIn)
										press_showCostsIn = input()
										match press_showCostsIn:
											case '0':
												back_132 = False
											case _:
												print("Invaild option") 
                                          

					case '8':
						prepaidCredit = """

		Prepaid credit
		0. Back
			    						"""
						
						back_133 = True
						while back_133:
							print(prepaidCredit)
							press_prepaidCredit = input()
							match press_prepaidCredit:
								case '0':
									back_133 = False
								case _:
									print("Invaild option")
					case _:
						print("Invalid input")


		case '5':
			tones = """ 

                 5. Tones 
 
                 1 -> Ringing tone 
                 2 -> Ringing volume 
                 3 -> Incoming call alert 
                 4 -> Composer 
                 5 -> Message alert tone 
                 6 -> Keypad tones 
                 7 -> Warning and game tones 
                 8 -> Vibrating alert 
                 9 -> Screen saver 
		 0 <-Back

                            """
				
			
			back1 = True
			while back1:
				print(tones)
				pressTones = input() 
 
				match pressTones:
					case '0':
						back1 = False
					case '1':
						ringingTone = """

		Ringing Tone
		0. Back
			    		"""  
						
						back_14 = True
						while back_14:
							print(ringingTone)
							press_ringingTone = input()
							match press_ringingTone:
								case '0':
									back_14 = False
								case _:
									print("Invaild option")
                           
					case '2':
						ringingVolume = """

		Ringing volume
		0. Back
			    		"""
						
						back_15 = True
						while back_15:
							print(ringingVolume)
							press_ringingVolume = input()
							match press_ringingVolume:
								case '0':
									back_15 = False
								case _:
									print("Invaild option")
                       
					case '3':
						incomingCall = """

		Incoming call alert
		0. Back
			    		"""
						
						back_16 = True
						while back_16:
							print(incomingCall)
							press_incomingCall = input()
							match press_incomingCall:
								case '0':
									back_16 = False
								case _:
									print("Invaild option")
                             
					case '4':
						composer = """

		Composers
		0. Back
					"""
						
						back_17 = True
						while back_17:
							print(composer)
							press_composer = input()
							match press_composer:
								case '0':
									back_17 = False
								case _:
									print("Invaild option")
                            
					case '5':
						messageAlert = """

		Message alert tone
		0. Back
			    		"""
						print(messageAlert)
						back_17 = True
						while back_17:
							print(composer)
							press_composer = input()
							match press_composer:
								case '0':
									back_17 = False
								case _:
									print("Invaild option") 
                          
					case '6':
						keypadTones = """

		Keypad tones
		0. Back
			    		"""
						
						back_18 = True
						while back_18:
							print(keypadTones)
							press_keypadTones = input()
							match press_keypadTones:
								case '0':
									back_18 = False
								case _:
									print("Invaild option") 
                           
					case '7':
						warningAndGame = """

		Warning and game tones
		0. Back
			    		"""
						
						back_19 = True
						while back_19:
							print(warningAndGame)
							press_warningAndGame = input()
							match press_warningAndGame:
								case '0':
									back_19 = False
								case _:
									print("Invaild option") 
                         
					case '8':
						vibratingAlert = """

		Vibrating alert
		0. Back
			    		"""
						
						back_21 = True
						while back_21:
							print(vibratingAlert)
							press_vibratingAlert = input()
							match press_vibratingAlert:
								case '0':
									back_21 = False
								case _:
									print("Invaild option") 
                         
					case '9':
						screenSaver = """

		Screen saver
		0. Back
			    		"""
						
						back_22 = True
						while back_22:
							print(screenSaver)
							press_screenSaver = input()
							match press_screenSaver:
								case '0':
									back_22 = False
								case _:
									print("Invaild option")
					case _: 
						print("Invalid input")
 

		case '6':
			settings = """ 

    		6. Settings 
 
                1 -> Call settings 
            	2 -> Phone settings 
                3 -> Security settings 
                4 -> Restore factory settings
		0 <- Back 
 
                                    """
			
			back19 = True
			while back19:
				print(settings)
				pressSetting = input() 
				match pressSetting:
					case '0':
						back19 = False 
					case '1':
						callSettings = """ 

		1. Call settings 
 
		1. Automatic redial 
		2. Speed dialling 
		3. Call waiting options
		4. Own number sending
		5. Phone line in use
		6. Automatic answer
		0.<- Back


                                            """ 
						
						back8 = True
						while back8:
							print(callSettings) 
							pressCallSettings = input() 
							match pressCallSettings:
								case '0':
									back8 = False
								case '1':
									automaticRedial = """
   
		Automatic redial
		0. Back
					    		"""
									
									back_1 = True
									while back_1:
										print(automaticRedial)
										press_automaticRedial = input()
										match press_automaticRedial:
											case '0':
												back_1 = False
											case _: 
												print("invaild option")
										
                                             
								case '2':
									speedDialling = """

		Speed dialling
		0. Back
					    		"""
									
									back_10 = True
									while back_10:
										print(speedDialling)
										press_speedDialling = input()
										match press_speedDialling:
											case '0':
												back_10 = False
											case _: 
												print("invaild option") 
                                           
								case '3':
									callWaiting = """

		Call waiting options
		0. Back
					    """
									
									back_11 = True
									while back_11:
										print(callWaiting)
										press_callWaiting = input()
										match press_callWaiting:
											case '0':
												back_11 = False
											case _: 
												print("invaild option")
					   
								case '4':
									ownNumber = """
   
		Own number sending
		0. back
					    """
									
									back_12 = True
									while back_12:
										print(ownNumber)
										press_ownNumber = input()
										match press_ownNumber:
											case '0':
												back_12 = False
											case _: 
												print("invaild option") 
                                         
								case '5':
									phoneLineIn = """

		Phone line in use
		0. Back
					    """
									
									back_13 = True
									while back_13:
										print(phoneLineIn)
										press_phoneLineIn = input()
										match press_phoneLineIn:
											case '0':
												back_13 = False
											case _: 
												print("invaild option") 
                                        
								case '6':
									automaticAnswer = """

		Automatic answer
		0. Back
					    """
									
									back_14 = True
									while back_14:
										print(automaticAnswer)
										press_automaticAnswer = input()
										match press_automaticAnswer:
											case '0':
												back_14 = False
											case _: 
												print("invaild option")

								case _:
									print("invalid input")

					case '2': 
						phoneSetting = """ 

		2. Phone setting 

		1. Language 
		2. Cell info display
		3. Welcome note
		4. Network selection
		5. Lights
		6. Confirm SIM service actions
		0.<- Back


                                            """
						
						back13 = True
						while back13:
							print(phoneSetting) 
							pressPhoneSettings = input() 
							match pressPhoneSettings:
								case '0':
									back13 = False 
								case '1':
									language = """
   
		Language
		0. Back
					    """
									
									back_1 = True
									while back_1:
										print(language)
										press_language = input()
										match press_language:
											case '0':
												back_1 = False
											case _: 
												print("invaild option") 
                                      
								case '2':
									cellInfoDisplay = """

		Cell info display
		0. Back
					    """
									
									back_2 = True
									while back_2:
										print(cellInfoDisplay)
										press_cellInfoDisplay = input()
										match press_cellInfoDisplay:
											case '0':
												back_2 = False
											case _: 
												print("invaild option")  
                                   
								case '3':
									welcomeNote = """

		Welcome note
		0. Back
					    """
									
									back_3 = True
									while back_3:
										print(welcomeNote)
										press_welcomeNote = input()
										match press_welcomeNote:
											case '0':
												back_3 = False
											case _: 
												print("invaild option")
					
								case '4':
									networkSelection = """
   
		Network selection
		0. Back
					    """
									
									back_4 = True
									while back_4:
										print(networkSelection)
										press_networkSelection = input()
										match press_networkSelection:
											case '0':
												back_4 = False
											case _: 
												print("invaild option") 
                                   
								case '5':
									lights = """

		Lights
		0. Back
					    """
									
									back_5 = True
									while back_5:
										print(lights)
										press_lights = input()
										match press_lights:
											case '0':
												back_5 = False
											case _: 
												print("invaild option") 
                                          
								case '6':
									confirmSIM = """

		Confirm SIM service actions
		0. Back
					    """
									
									back_6 = True
									while back_6:
										print(confirmSIM)
										press_confirmSIM = input()
										match press_confirmSIM:
											case '0':
												back_6 = False
											case _: 
												print("invaild option")

								case _:
									print("Invaild input") 
                                
					case '3':
						securitySetting = """ 


		3. Security settings
 
		1. PIN code request 
		2. Call barring service 
		3. Fixed dialling
		4. Closed user group
		5. Phone security
		6. Change access codes
		0.<- Back


                                            """
						
						back4 = True
						while back4:
							print(securitySetting) 
							pressSecuritySetting = input() 
							match pressSecuritySetting:
								case '0':
									back4 = False
 
								case '1':
									codeRequest = """
   
		PIN code request
		0. Back
					    """
									
									back_7 = True
									while back_7:
										print(codeRequest)
										press_codeRequest = input()
										match press_codeRequest:
											case '0':
												back_7 = False
											case _: 
												print("invaild option")
									 
                                           
								case '2':
									callBarringService = """

		Call barring service
		0. Back
					    """
									
									back_8 = True
									while back_8:
										print(callBarringService)
										press_callBarringService = int(input())
										match press_callBarringService:
											case '0':
												back_8 = False
											case _: 
												print("invaild option")
                                            
								case '3':
									fixedDialling = """

		Fixed dialling
		0. Back
					    """
									
									back_9 = True
									while back_9:
										print(fixedDialling)
										press_fixedDialling = input()
										match press_fixedDialling:
											case '0':
												back_9 = False
											case _: 
												print("invaild option")
					 
								case '4':
									closedUserGroup = """
   
		Closed user group
		0. Back
					    """
									
									back_10 = True
									while back_10:
										print(closedUserGroup)
										press_closedUserGroup = input()
										match press_closedUserGroup:
											case '0':
												back_10 = False
											case _: 
												print("invaild option") 
                                        
								case '5':
									phoneSecurity = """

		Phone security
		0. Back
					    """
									
									back_11 = True
									while back_11:
										print(phoneSecurity)
										press_phoneSecurity = input()
										match press_phoneSecurity:
											case '0':
												back_11 = False
											case _: 
												print("invaild option") 
                                         
								case '6':
									changeAccessCodes = """

		Change access codes
		0. Back
					    """
									
									back_12 = True
									while back_12:
										print(changeAccessCodes)
										press_changeAccessCodes = input()
										match press_changeAccessCodes:
											case '0':
												back_12 = False
											case _: 
												print("invaild option")  

								case _:
									print("invaild input")
                                      
					case '4':
						restoreFactory = """

		Restore factory setting
		0. Back
			    	     """
						
						back_13 = True
						while back_13:
							print(restoreFactory)
							press_restoreFactory = input()
							match press_restoreFactory:
								case '0':
									back_13 = False
								case _: 
									print("invaild option") 

					case _:
						print("Invaild input")


		case '7':
			callDivert = """

		Call divert
		0. Back

		    	"""   
			
			back = True
			while back:
				print(callDivert)
				pressCallDivert = input()
				match pressCallDivert:
					case '0':
						back = False
					case _: 
						print("Invaild Input")

		case '8':
			games = """

		Games
		0. Back

		    	"""  
			
			back = True
			while back:
				print(games)
				pressGames = input()
				match pressGames:
					case '0':
						back = False
					case _: 
						print("Invaild Input")

		case '9':
			calculator = """

		Calculator
		0. Back

		    	"""   
			
			back = True
			while back:
				print(calculator)
				pressCalculator = input()
				match pressCalculator:
					case '0':
						back = False
					case _: 
						print("Invaild Input")

		case '10':
			reminders = """

		Reminders
		0. Back

		    	"""   
			
			back = True
			while back:
				print(reminders)
				pressReminders = input()
				match pressReminders:
					case '0':
						back = False 
					case _: 
						print("Invalid option")

		case '11':
			clock = """ 
			
		11. Clock 
 
		1 -> Alarm clock 
		2 -> Clock settings 
		3 -> Date setting 
		4 -> Stopwatch 
		5 -> Countdown timer 
		6 -> Auto update of date and time 
		0 <- Back


                        """
			back = True
			while back:
				print(clock)
				pressClock = input() 
				match pressClock:
					case '0': 
						back = False
					case '1':
						alarmClock = """

		Alarm Clock
		0. Back

			    """
						
						back1 = True
						while back1:
							print(alarmClock)
							pressAlarmClock = input()
							match pressAlarmClock:
								case '0':
									back1 = False
								case _: 
									print("Invalid option") 

					case '2':
						clockSettings = """

		Clock settings
		0. Back

			    """
						
						back1 = True
						while back1:
							print(clockSettings) 
							pressClockSettings = input()
							match pressClockSettings:
								case '0':
									back1 = False
								case _: 
									print("Invalid option")

					case '3':
						dateSetting = """

		Date setting
		0. Back

			    """
						
						back1 = True
						while back1:
							print(dateSetting) 
							pressDateSetting = input()
							match pressDateSetting:
								case '0':
									back1 = False
								case _: 
									print("Invalid option") 


					case '4':
						stopwatch = """

		Stopwatch
		0. Back

			    """
						
						back1 = True
						while back1:
							print(stopwatch) 
							pressStopwatch = input()
							match pressStopwatch:
								case '0':
									back1 = False
								case _: 
									print("Invalid option") 

 
					case '5':
						countdownTimer = """

		Countdown timer
		0. Back

			    """
						
						back1 = True
						while back1:
							print(countdownTimer)
							pressCountdownTimer = input()
							match pressCountdownTimer:
								case '0':
									back1 = False
								case _: 
									print("Invalid option")


					case '6':
						AutoUpdate = """

		Auto update of date and time
		0. Back
					"""
						
						back1 = True
						while back1:
							print(AutoUpdate) 
							pressAutoUpdate = input()
							match pressAutoUpdate: 
								case '0':
									back1 = False
								case _: 
									print("Invalid option")

					case _: 
						print("Invalid option")
			

		case '12':
			profiles = """

		Profiles
		0. Back

		    	""" 
			
			back1 = True
			while back1:
				print(profiles)
				press_profiles = input()
				match press_profiles:
					case '0':
						back1 = False
					case _: 
						print("Invalid option")
				

		case '13':
			simServices = """

		SIM services
		0. Back

			"""  
			
			back1 = True
			while back1:
				print(simServices)
				press_sim_services = input()
				match press_sim_services:
					case '0':
						back1 = False
					case _: 
						print("Invalid option")

		case '0':
			exit = False 
		case _:
			print("Invalid option")


