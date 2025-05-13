for count in range(11):
	for count1 in range(count):
		print('*', end='')
	print()

print()

for count in range(11, 0, -1):
	for count1 in range(count):
		print('*', end='')
	print()
print()

for count in range(11):
	for count1 in range(count):
		print(' ', end='')
	for count2 in range(9, count1, -1):
		print('*', end='')
		
	print()
print()

for count in range(11):
	for count1 in range(10, count, -1):
		print(' ', end='')
	for count2 in range(count1):
		print('*', end='')
		
	print()