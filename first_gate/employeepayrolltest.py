import employeepayroll

from unittest import TestCase

class TestEmployeepayroll(TestCase):

	def test_that_employee_hours_is_not_above_168(self):
		response = employeepayroll.employee_tax_calculate(200, 30, 40, 10)
		self.assertEqual(response, "hours above weekly hours")

	def test_that_employee_tax_calculate_function_exists(self):
		employeepayroll.employee_tax_calculate(20, 30, 20, 10)

	def test_that_employee_details_function_exists(self):
		name = "kow"
		employee_details(name)
		
	def test_that_employee_tax_calculate_function_works(self):
		response = employeepayroll.employee_tax_calculate(20, 30, 20, 10)
		self.assertEqual(response, "deductions successful")
	
	def test_that_deduction_works(self):
		response = employeepayroll.employee_tax_calculate(100, 30, 40, 10)
		self.assertEqual(response, "deductions successful")

	
	def test_that_employee_details_function_works(self):
		response = employeepayroll.employee_details("kow")
		self.assertEqual(response, "")

