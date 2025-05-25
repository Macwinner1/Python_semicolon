list_of_accounts = []

def get_bankapp():
	return "Welcome to your bank accout"

def create_account(name, phone_number, bin, balance):
	if len(phone_number) < 10:
		raise ValueError("Phone number must be 10 digits")
	if len(bin) < 4 and len(bin) > 4:
		raise ValueError("Pin number must be 4 digits")
	account = []
	account = [name, phone_number, bin, balance]
	list_of_accounts.append(account)
	return "Account created successful"

def vaild_pin_number(account):
	for index in list_of_accounts:
		if index[2] == bin:
			return index[2]
		else:
			return "Invalid pin number"

def total_account_created():
	return len(list_of_accounts)

def valid_account_number(phone_number):
	for index in list_of_accounts:
		if index[1] == phone_number:
			return index[1]
		else:
			return "Account not found"

def withdraw(*args):
	accounts = []

def deposit():
	accounts = []


