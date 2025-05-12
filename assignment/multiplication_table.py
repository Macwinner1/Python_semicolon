
print("              Multiplication  Table\n")
print("     1    2    3    4    5    6    7    8    9")
print("--------------------------------------------------")

for index in range(1, 10):
	print(index, "|  " , end='')
	for index2 in range(1, 10):
		result = index * index2
		print(f"{result: <5}", end='')
	print( )
