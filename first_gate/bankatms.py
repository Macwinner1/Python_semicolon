list_of_transactions = {}
list_of_withdrawal = {}
list_of_account_balance = {}
account_balance = [1]

def get_bankatm():
	return "Welcome to Semicolon Bank ATM"
		
def get_account_balance(deposit):
	if deposit < 0:
		return "No negative deposit"
	if deposit < 100 and deposit > 0:
		return "deposit can't be less than 100"
	account_balance[0] = deposit
	account_balance_detail = {"Deposit Amount": deposit}
	list_of_transactions.update(account_balance_detail)
	return "Deposit successful"

def get_withdrawal(amount):
	if amount % 500 != 0 or amount % 1000 != 0:
		return "Invalid amount"
	if amount % 500 == 0 and amount <= 20000 or amount % 1000 == 0 and amount <= 20000:
		check_withdrawable_balance = account_balance[0] * 0.9
		withdrawal_fee = 100
		withdraw = (amount + withdrawal_fee)
	#if withdraw <= check_withdrawable_balance:
		account_balance[0] -= withdraw
		list_of_withdrawal = {"Withdraw Amount": amount}
		list_of_account_balance = {"Current account balance": account_balance}	
		list_of_transactions.update(list_of_withdrawal)
		list_of_transactions.update(list_of_account_balance)

	
		return account_balance[0]
	else:
		return "withdrawal unsuccessful"
		
	return list_of_account_balance, "Withdrawal successful"

def get_transaction_history():
	return list_of_transactions

menu = '''
	WELCOME TO ATM
	
	1. Enter Account balance
	0. Exit

	'''

account_balance = []

print(menu)
exit = True
while exit:
	option = input()
	match option:
		case '1':
			menu1 = '''
			Transaction menu
	
			1. Enter Amount To Withdraw
			2. Show Transaction History
			0. Exit

			'''
			account_balance.append(int(input("Enter Account balance: ")))
			print(get_account_balance(account_balance[0]))
			exit1 = True
			while exit1:
				print(menu1)
				option = input()
				match option:
					case '1':
						amount = int(input("Enter Amount To Withdraw: "))
						print(get_withdrawal(amount))
						print(get_transaction_history())
					case '2':
						print(get_transaction_history())
						exit2 = True
						while exit2:
							option = input()
							match option:
								case '0':
									exit2 = False
					case '0':
						exit1 = False

		case '0':
			exit = False
			
		#default_:
			#print("invalid input")






