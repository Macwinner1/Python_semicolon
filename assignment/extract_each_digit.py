numbers = (input("Kindly enter any number from 1 to 10000: "))

length = len(numbers)
numbers = int(numbers)
value = 0
for index in range(length):
	value += numbers % 10
	numbers = numbers // 10

print(f"This is total sum of this above number {value}")