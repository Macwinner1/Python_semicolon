def categorize_numbers(numbers, divisor):
	number_list = []
	for number in numbers:
		if number % divisor == 0:
			number_list.append(number)

	return number_list
	 

