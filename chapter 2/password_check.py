password = input("Kindly enter your password: ")

length = len(password)

if length < 8:
	print("Your Passsword is Very weak!")
else:
	if length == 8:
		print("Your Password is Weak!")
	if length > 8 & length < 16:
		print("Your Password is Strong!")
	if length > 16:
		print("Your password is Very Strong!")