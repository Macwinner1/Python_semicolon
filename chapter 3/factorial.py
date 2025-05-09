
number = int(input("Enter any nonnegative number: "))
def factorial_iterative(number):
	result = 1

	for index in range(1, number + 1):
		result *= index
	return result
result = factorial_iterative(number)
print(f"The factorial of {number} is {result}")