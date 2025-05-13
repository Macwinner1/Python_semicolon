number = (input("Enter the binary number: "))
counter = 0
sum = 0
value = len(number) * 2

for count in range(1, value, 2):
	for count1 in range(1):
		reminder = int(number) % 10
		number = int(number) // 10
		counter = count * reminder
		sum = sum + counter

print(sum)		

