import random
correctCount = 0
count = 0

while (count < 10):
	number1 = random.randint(1, 100)
	number2 = random.randint(1, 100)
	if(number1 < number2):
		temp = number1
		number1 = number2
		number2 = temp
	attempt = 0
	while (attempt < 2):
	
		answer = input(f"What is  {number1}  -  {number2} ? ")	

		if(number1 - number2 == answer):
			print("You are correct!\n")
			correctCount = correctCount + 1
			break
		else:
			print("Your answer is wrong. try again!\n")
			attempt = attempt + 1
	count = count + 1 

print(f"Correct count is {correctCount}")