def extract(numbers):

	length = len(numbers)
	numbers = int(numbers)
	value = 0

	for index in range(length):
		value += numbers % 10
		numbers = numbers // 10
	return value

numbers = input("Kindly enter any number from 1 to 10000: ")

total = extract(numbers)
print(total)