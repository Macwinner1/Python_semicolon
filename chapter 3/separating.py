number = int(input("Enter five numbers: "))

reminder = 0

for value in range(5):
	reminder = number // (10 ** (4 - value))
	print(f"{reminder}", end=' ')
	number = number % (10 ** (4 - value))