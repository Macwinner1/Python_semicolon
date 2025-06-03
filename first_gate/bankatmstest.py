import bankatms

from unittest import TestCase

class TestBankAtms(TestCase):

	def setUP(self):
		bankatms.account_balance.clear()

	def test_that_bank_atm_function_exists(self):
		bankatms.get_bankatm()

	def test_that_account_balance_function_exists(self):
		response = bankatms.get_account_balance(50000)
		self.assertEqual(response, "Deposit successful")
		
	def test_that_account_balance_cant_go_below_100(self):
		response = bankatms.get_account_balance(10)
		self.assertEqual(response, "deposit can't be less than 100")
		
	def test_that_account_balance_cant_be_negative_number(self):
		response = bankatms.get_account_balance()
		self.assertEqual(response, "No negative deposit")
		
	def test_that_withdrawal_function_exists(self):
		bankatms.get_withdrawal(100)

	def test_that_withdrawal_function_is_working(self):
		bankatms.get_account_balance(50000)
		response = bankatms.get_withdrawal(10000)
		self.assertEqual(response, 40000)
		
	def test_that_withdrawal_that_is_not_500_or_1000(self):
		response = bankatms.get_withdrawal(10300)
		self.assertEqual(response, "Invalid amount")

	def test_transaction_history_function_exists(self):
		bankatms.get_transaction_history()
		
	def test_transaction_history_function_exists(self):
		response = bankatms.get_transaction_history()
		self.assertEqual(response, "Invalid amount")
	
