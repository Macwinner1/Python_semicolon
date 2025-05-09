yes = "Yes"
no = "No"

problem = input("What is your problem?: ")
reply = input("Have you have this problem before(Yes or No)")

if reply == yes:
	print("well, you have it again.")

if reply == no:
	print("well, you have it now.")