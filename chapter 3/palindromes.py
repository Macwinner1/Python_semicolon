number = int(input("Enter any number to check for palindrome number: "))
def is_palindrome(number):

	first_number = number

	reverse_number = 0

	while number > 0:
		reminder = number % 10
		reverse_number = reverse_number * 10 + reminder
		number = number // 10
	return first_number == reverse_number

if is_palindrome(number):
	print("this is a palindrome number")

else:
	print("this is not a palindrome number")
