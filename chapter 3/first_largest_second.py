first_largest = 0
second_largest = 0

for index2 in range(11):
	number = int(input("Enter a number: ")) 
	if number > first_largest:
		second_largest = first_largest
		first_largest = number

	elif number > second_largest:
		second_largest = number



print("The largest number: ", first_largest)
print("The Second largest number: ", second_largest)