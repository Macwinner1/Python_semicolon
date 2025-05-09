import time
number = int(input("Enter an integer: "))

while number < 1:
	number = int(input("Enter a positive integer: "))

for index in range(number, 0, -1):
	print(index)
	time.sleep(1)
print("Blast Off")