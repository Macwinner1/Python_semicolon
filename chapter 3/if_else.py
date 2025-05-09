print("Enter two intergers, and i will tell you the relationship between the two intergers")

number1 = int(input("Enter first interger: "))
number2 = int(input("Enter second interger: "))

if number1 == number2:
	print(number1, "is Equal to", number2)
else:
	print(number1, "is not Equal to", number2)
if number1 < number2:
	print(number1, "is Less than", number2)
else:
	print(number1, "is Greater than", number2)
if number1 <= number2:
	print(number1, "is Less than or Equal to", number2)
else:
	print(number1, "is Greater than or Equal to", number2)