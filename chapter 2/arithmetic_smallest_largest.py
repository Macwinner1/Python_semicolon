first_number = int(input("Enter any number: "))
second_number = int(input("Enter any number: "))
third_number = int(input("Enter any number: "))

largest_number = first_number
smallest_number = first_number

sum = first_number + second_number + third_number
product = first_number * second_number * third_number
average = sum / 3

if second_number > largest_number:
	largest_number = second_number

if second_number < smallest_number:
	smallest_number = second_number

if third_number < smallest_number:
	smallest_number = third_number
if third_number > largest_number:
	largest_number = third_number

print("This is the largest number: ", largest_number)
print("This is the smallest number: ", smallest_number)

print("This is the sum of all numbers: ", sum)
print("This is the product of all numbers: ", product)
print("This is the average number: ", average)