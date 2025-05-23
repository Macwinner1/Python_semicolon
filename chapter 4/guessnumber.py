import random

count = True
number = random.randint(1, 1000)
while count:
	guess = int(input("Guess my number between 1 and 1000 with the fewest guesses:"))
	if guess == number:
		print("Congratulations. You guessed the number!")
		play_again = int(input("Do you want to play again? press(1) for Yes and press(2) for Exit:"))
		number = random.randint(1, 1000)
		
		if play_again == 1:
			count = True
		if play_again == 2:
			count = False	
	elif guess > number:
		print("Too high. Try again")
	elif guess < number:
		print("Too low. Try again")
	

