questions = {1: "What is capital of Nigeria? ", 2: "What will you say jollof rice is? ", 3: "what is capital of united kingdom ?", 4: "what is the capital of france? ", 5: "how many hours makes a day?", 6: "how many days makes a week? ", 7: "how many days makes a year that is not a leap year?", 8: "how many days makes a leap year?", 9: "who is the president of Nigeria?", 10: "what will you say an apple is? "}
	

def userinput_check(user_input):
	if user_input > 10 or user_input < 1:
		return "Invalid input"
	else:
		return "valid input"

def question_list(user_input):
	return questions
	
def answer_list(user_input):
	answers = {1: {1:"lagos", 2: "abuja", 3: "onitsha", 4: "ogun"}, 2:{1: "food", 2: "nut", 3: "fruit", 4: "garri"}, 3:{1: "london", 2: "accra", 3: "everton", 4: "manchester"}, 4:{1: "volta", 2: "france", 3: "malta", 4: "paris"}, 5:{1: "36 hours", 2: "48 hours", 3: "24 hours", 4: "25 hours"}, 6:{1: "6 days", 2: "66 days", 3: "7 days", 4: "5 days"}, 7:{1: "365 days", 2: "366 days", 3: "367 days", 4: "355 days"}, 8:{1: "365 days", 2: "366 days", 3: "367 days", 4: "355 days"}, 9:{1: "Peter obi", 2: "Tinubu", 3: "shittima", 4: "Dangote"}, 10:{1: "food", 2: "nut", 3: "fruit", 4: "garri"}}
	return answers
	
def checker_list(user_input, answer_input):
	answer = answer_list(user_input).get(user_input).get(answer_input)
	return answer 

def correct_pick(user_input, answer_input):
	correct = {1: "abuja", 2: "food", 3: "london", 4: "paris", 5: "24 hours", 6: "7 days", 7: "365 days", 8: "366 days", 9: "Tinubu", 10: "fruit"}
	answer = answer_list(user_input).get(user_input).get(answer_input)
	for key, value in correct.items():
		if value == answer:
			return "correct answer"
	else:
		return "wrong answer"
		counter = counter + 1
		


def shuffle_question():
	questions = question_list([randon.randint(1, 10)])
	return questions
	
	
menu = '''
============================================
	Interactive Quiz:
	
	Enter 1 - 10 to pick a question.
=============================================
	'''	


print(menu)
user_input = int(input())	
print(question_list(user_input).get(user_input))
print(answer_list(user_input).get(user_input))
answer_input = int(input())
print(correct_pick(user_input, answer_input))
print(checker_list(user_input, answer_input))








