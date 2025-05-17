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
		14 -> Exit

 		"""
exit = True

while exit:
	print(menu)
	menuInput = int(input ())
	match menuInput:
		case 1:
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
		11 <- Back
 
                            """
			print(phonebook)
			pressPhoneBook = int(input()) 
			match pressPhoneBook: 
				case 1:
					search = """
	Search
	0. Back
                            		""" 
					print(search)
				case 2: 
					serviceNos = """

	Service Nos
	0. Back
			    		"""   
					print(serviceNos)
                            
				case 3: 
					addName = """

	Add name
	0. Back
			    		""";   
					print(addName)
                           
				case 4:
					erase = """

	Erase
	0. Back
			    		"""
					print(erase)
                             
				case 5:
					edit = """

	Edit
	0. Back
			    		"""
					print(edit)
                         
				case 6:
					assignTone = """

	Assign tone
	0. Back
			    		"""
					print(assignTone)
                             
				case 7:
					sendBcard = """

	Send b'card
	0. Back
		 	    		""" 
					print(sendBcard)
                          
				case 8: 
					options = """ 

	8. Options 

	1. Type of view 
	2. Memory status 
	3.<- Back


                                    	"""
					print(options) 
					pressOptions = int(input())
                            
					match pressOptions: 
						case 1:
							typeView = """

	Type of view
	0. Back
				    			"""
							print(typeView)
                                    
						case 2:
							memoryStatus = """

	Memory status
	0. Back
				    			""" 
							print(memoryStatus)
                                     
				case 9:
					speedDials = """

	Speed dials
	0. Back
			    		"""   
					print(speedDials) 
                             
				case 10:
					voiceTags = """

	Voice tags
	0. Back
			    		"""   
					print(voiceTags)
		
		case 2:
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
	11 <- Back

                        """
			print(messages)
			pressMessages = int(input())
			match pressMessages: 
				case 1: 
					writeMessages = """

	Write Messages
	0. Back
			    		"""
					print(writeMessages)
                           
				case 2:
					inbox = """

	Inbox
	0. Back
			    		"""
					print(inbox) 
                           
				case 3: 
					outbox = """

	Outbox
	0. Back
			    		"""
					print(outbox)
                             
				case 4: 
					pictureMessages = """

	Picture Messages
	0. Back
			    		"""
					print(pictureMessages)
                            
				case 5:
					templates = """

	Templates
	0. Back
			    		"""
					print(templates)
                             
				case 6:
					smileys = """

	Smileys
	0. Back
			    		"""
					print(smileys)
                             
				case 7:
					messageSettings = """ 

	7. Message Settings 
 
	1. Set 1 
	2. Common 
	3.<- Back

                                    	""" 
					print(messageSettings) 
					pressMessageSettings = int(input()) 
					match pressMessageSettings:
						case 1:
							set1 = """ 

	1. Set 1 
 
	1. Message center number 
	2. Messages sent as 
	3. Message validity
	4.<- back
 
                                            		""" 
							print(set1) 
							pressSet1 = int(input())								
							match pressSet1: 
								case 1: 
									messageCenter = """
   
	Message center number
	0. Back
					    				"""
									print(messageCenter)
                                            
								case 2: 
									messagesSent = """

	Message sent as
	0. Back
					    				"""
									print(messagesSent)
                                             
								case 3:
									messagesValidity = """

	Message validity
	0. Back
					    				"""
									print(messagesValidity)

						case 2:
							common = """ 

	2. Common 
 
	1. Delivery reports 
	2. Reply via same centre 
	3. Character support 
	4.<- Back
							"""
							print(common)
							pressCommon = int(input()); 
							match pressCommon:
								case 1: 
									deliveryReports = """
   
	Delivery reports
	0. Back
									"""
									print(deliveryReports)
                                             
								case 2:
									replyVia = """

	Reply Via same centre
	0. Back
					    				"""
									print(replyVia)
                                             
								case 3:
									characterSupport = """

	Character support
	0. Back
					    				"""
									print(characterSupport)

				case 8:
					infoService = """

	Info Service
	0. Back
			    		"""
					print(infoService)
                         
				case 9:
					voiceMailboxNumber = """

	Voice mailbox number 
	0. Back	
			    		"""
					print(voiceMailboxNumber)
                       
				case 10:
					serviceCommand = """

	Service command editor 
	0. Back
			    		"""
					print(serviceCommand)






		case 3:
			chat = """

		Chat
		0. Back

		    	"""  
			print(chat)

		case 4:
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
			print(callRegister)
			pressCallRegister = int(input())
			match pressCallRegister: 
				case 1:
					missedCalls = """

		Missed calls
		0. Back

			    		"""   
					print(missedCalls) 
                            
				case 2: 
					receivedCalls = """

		Received calls
		0. Back
			    		""" 
					print(receivedCalls) 
                           
				case 3:
					dialledNumbers = """

		Dialled numbers
		0. Back
			    		"""
					print(dialledNumbers)
                       
				case 4:
					eraseRecentCall = """

		Erase recent call lists
		0. Back

			    		"""
					print(eraseRecentCall)
				case 5: 
					showCallDuration = """ 

		5. Show call duration 
 
		1. Last call duration 
		2. All calls' duration 
		3. Received calls' duration
		4. Dialled calls' duration
		5. Clear timers
		6.<- Back

                                            """; 
					print(showCallDuration) 
					pressShowCallDuration = int(input()) 
					match pressShowCallDuration:
						case 1:
							lastCallDuration = """
   
		Last call duration
		0. Back
					    		"""
							print(lastCallDuration)
                                          
						case 2:
							allCallsDuration = """

		All calls' duration 
		0. Back
					    		"""
							print(allCallsDuration) 
                                       
						case 3:
							receivedCallsDuration = """

		Received calls' duration
		0. Back
					    		"""
							print(receivedCallsDuration)
					  
						case 4: 
							dialledCallsDuration = """
   
		Dialled calls' duration

					    		"""
							print(dialledCallsDuration) 
                                         
						case 5:
							clearTimers = """

		Clear timers
		0. Back
					    		"""
							print(clearTimers)
               

						case 6:
							showCallCosts = """ 


		6. Show call costs 
 
		1. Last call cost 
		2. All calls' cost
		3. Clear counters
		4.<- Back

                                            		"""
							print(showCallCosts) 
							pressShowCallCost = int(input())
							match pressShowCallCost:
								case 1:
									lastCallCost = """
   
		Last call cost
		0. Back
					    				"""
									print(lastCallCost) 
                                          
								case 2:
									allCallsCost = """

		All calls' cost 
		0. Back
					    				"""
									print(allCallsCost) 
                                           
								case 3:
									clearCounters = """

		Clear counters
		0. Back
					    				"""
									print(clearCounters)
                                         
                                 

						case 7:
							callCostSettings = """ 


		7. Call cost settings 
 
		1. Call cost limit 
		2. Show costs in
		3.<- Back

                                            		""" 
							print(callCostSettings) 
							pressCallCostSettings = int(input()) 
							match pressCallCostSettings:
								case 1:
									callCostLimit = """
   
		Call cost limit
		0. Back
					    				"""
									print(callCostLimit)
 
								case 2:
									showCostsIn = """

		Show costs in
		0. Back
					    				"""
									print(showCostsIn) 
                                          

						case 8:
									prepaidCredit = """

		Prepaid credit
		0. Back
			    						"""
									print(prepaidCredit)


		case 5:
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
		 10 <-Back

                            """
			print(tones)
			pressTones = int(input()); 
 
			match pressTones:
				case 1:
					ringingTone = """

		Ringing Tone
		0. Back
			    		"""  
					print(ringingTone)
                           
				case 2:
					ringingVolume = """

		Ringing volume
		0. Back
			    		"""
					print(ringingVolume)
                       
				case 3:
					incomingCall = """

		Incoming call alert
		0. Back
			    		"""
					print(incomingCall)
                             
				case 4:
					composer = """

		Composers
		0. Back
					"""
					print(composer)
                            
				case 5:
					messageAlert = """

		Message alert tone
		0. Back
			    		"""
					print(messageAlert) 
                          
				case 6:
					keypadTones = """

		Keypad tones
		0. Back
			    		"""
					print(keypadTones) 
                           
				case 7:
					warningAndGame = """

		Warning and game tones
		0. Back
			    		"""
					print(warningAndGame) 
                         
				case 8:
					vibratingAlert = """

		Vibrating alert
		0. Back
			    		"""
					print(vibratingAlert) 
                         
				case 9:
					screenSaver = """

		Screen saver
		0. Back
			    		"""
					print(screenSaver)
 

		case 6:
			settings = """ 

    		6. Settings 
 
                1 -> Call settings 
            	2 -> Phone settings 
                3 -> Security settings 
                4 -> Restore factory settings
		5 <- Back 
 
                                    """
			print(settings)

		case 7:
			callDivert = """

		Call divert
		0. Back

		    	"""   
			print(callDivert)

		case 8:
			games = """

		Games
		0. Back

		    	"""  
			print(games)

		case 9:
			calculator = """

		Calculator
		0. Back

		    	""";   
			print(calculator)

		case 10:
			reminders = """

		Reminders
		0. Back

		    	""";   
			print(reminders)

		case 11:
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
			print(clock)

		case 12:
			profiles = """

		Profiles
		0. Back

		    	""" 
			print(profiles)

		case 13:
			simServices = """

		SIM services
		0. Back

		    	"""  
			print(simServices)

		case 14:
			exit = False 
		#case _:
			#print("Invalid option")