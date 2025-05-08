number = int(input("Enter any number to check for palindrome number: "))

lastNumber = number % 100
firstNumber = number / 1000

if(lastNumber == firstNumber):
	print("This is a palindrome number: ", number)

else:
	print("This is not a palindrome number: ", number)