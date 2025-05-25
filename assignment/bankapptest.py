import bankapp

from unittest import TestCase 

class TestBankApp(TestCase):
	def test_that_bank_app_function_exists(self):
		bankapp.get_bankapp()

	def test_that_create_account_function_exists(self):
		response = bankapp.create_account("okafor", "8068853611", "3333", 1000)
		self.assertEqual(response, "Account created successful")

	def test_that_vaild_pin_number_function(self):
		response = bankapp.vaild_pin_number("3333")
		self.assertEqual(response, "Invalid pin number")

	def test_that_total_account_created_function(self):
		response = bankapp.total_account_created()
		self.assertEqual(response, 1)

	def test_to_check_for_valid_account_number_function(self):
		response = bankapp.valid_account_number("8068853611")
		self.assertEqual(response, "8068853611")
	
	def test_that_withdraw_function_exists(self):
		bankapp.withdraw()

	def test_that_deposit_function_exists(self):
		bankapp.deposit()
