def categorize_numbers(numbers, divisor):

	for number in numbers:
		if number % divisor == 0:
			print(number, end=', ')

numbers = [4,6,9,8,10,12]
divisor = 2
categorize_numbers(numbers, divisor)