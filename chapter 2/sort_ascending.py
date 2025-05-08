first_number = int(input("Enter a number: "))
second_number = int(input("Enter a number: "))
third_number = int(input("Enter a number: "))

temp = 0

if third_number < second_number:
	temp = second_number
	second_number = third_number 
	third_number = temp

if first_number > second_number:
	temp = first_number
	first_number = second_number
	second_number = temp

if second_number > third_number:
	temp = second_number
	second_number = third_number
	third_number = temp 

print(first_number, second_number,third_number)