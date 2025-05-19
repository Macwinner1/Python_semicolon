import unittest
import categorize_numbers

class TestCategorizeNumbers(unittest.TestCase):
	def test_categorize_numbers_function_exists(self):
		self.assertTrue(callable(categorize_numbers.categorize_numbers))
		
	def test_function_contains_arguments(self):
		numbers = [70, 35]
		divisor = 7
		categorize_numbers.categorize_numbers(numbers, divisor)
		
	def test_function_returns_result_when_divisible_number_found(self):
		actual = categorize_numbers.categorize_numbers([34, 55, 70, 35, 40], 7)
		expected = [70, 35]
		self.assertEqual(actual, expected)
		
		