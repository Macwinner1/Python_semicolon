import unittest
from list_of_random import *

class MyTestCase(unittest.TestCase):
    def test_get_length_works(self):
        number = {30, 40, 50, 60, 70, 80, 90, 100}
        length = get_length(number)
        self.assertEqual(length, 8)  # add assertion here

    def test_that_get_sum_of_even_numbers_works(self):
        number = [30, 40, 50, 60, 70]
        result = get_sum_of_even_numbers(number)
        self.assertEqual(result, 100)

    def test_that_get_sum_of_odd_numbers_works(self):
        number = [30, 40, 50, 60, 70, 80, 90, 100]
        result = get_sum_of_odd_numbers(number)
        self.assertEqual(result, 240)

    def test_that_get_multiply_of_element_at_every_third_position_works(self):
        number = {3, 4, 5, 6, 7, 8, 9, 10, 2}
        result = get_multiply_of_element_at_every_third_position(number)
        self.assertEqual(result, 80)

    def test_that_get_the_average_of_all_element_works(self):
        number = {3, 4, 5, 6, 7, 8, 9, 10, 2}
        result = get_the_average_of_all_elements(number)
        self.assertEqual(result, 6)


