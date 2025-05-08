passes = 0
fails = 0
vaild = 0


while vaild != 10:
	score = int(input("Enter Student Score here: "))
	if score == 1:
		passes += 1
		vaild += 1

	if score == 2:
		fails += 1
		vaild += 1
print("this is passed: ", passes)
print("this is failed: ", fails)
print("this is the vaild: ", vaild)