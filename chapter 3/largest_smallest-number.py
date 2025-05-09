
numbers = int(input("Enter any number: "))
largest_number = numbers
smallest_number = numbers
sum = largest_number
product = largest_number
average = 0
for row in range(3):
	numbers = int(input("Enter any number: "))

	if numbers > largest_number:
		largest_number = numbers

	if numbers < smallest_number:
		smallest_number = numbers 
	sum = sum + numbers
	product = product * numbers
average = sum / 4




print("This is the largest number: ", largest_number)
print("This is the smallest number: ", smallest_number)

print("This is the sum of all numbers: ", sum)
print("This is the product of all numbers: ", product)
print("This is the average number: ", average)