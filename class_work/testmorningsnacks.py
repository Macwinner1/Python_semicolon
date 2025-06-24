import unittest
import morningsnacks
class MyTestCase(unittest.TestCase):
    def test_add_to_list(self):
        list_colors = ["blue", "red", "green"]
        new_color = "yellow"
        self.assertEqual(morningsnacks.add_to_list(list_colors, new_color), ["blue", "red", "green", "yellow"]) # add assertion here

    def test_access_third_element(self):
        list_numbers = [34, 20, 44, 50, 60, 75]
        expected = 44
        self.assertEqual(morningsnacks.access_third_element(list_numbers), expected) # add assertion here

    def test_remove_third_element(self):
        list_numbers = [34, 20, 44, 50, 60, 75]
        expected = [34, 20, 50, 60, 75]
        self.assertEqual(morningsnacks.remove_third_element(list_numbers), expected) # add assertion here

    def test_list_length_of_string(self):
        list_numbers = ["margin", "colon", "program", "one"]
        expected = [6, 5, 7, 3]
        self.assertEqual(morningsnacks.list_length_of_string(list_numbers), expected) # add assertion here

    def test_ascending_list(self):
        list_numbers = [34, 20, 44, 50, 60, 75]
        expected = [20, 34, 44, 50, 60, 75]
        self.assertEqual(morningsnacks.ascending_list(list_numbers), expected) # add assertion here

    def test_even_numbers(self):
        list_numbers = [1, 2, 3, 4, 5, 6, 7]
        expected = [2, 4, 6]
        self.assertEqual(morningsnacks.even_numbers(list_numbers), expected) # add assertion here

    def test_combine_two_list(self):
        list_number_a = [1, 2, 3]
        list_number_b = [4, 5, 6, 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(morningsnacks.combine_two_list(list_number_a, list_number_b), expected) # add assertion here

    def test_more_than_three(self):
        list_strings = ["kings", "cars", "job", "man", "come", "code"]
        expected = ["kings", "cars", "come", "code"]
        self.assertEqual(morningsnacks.more_than_three(list_strings), expected) # add assertion here




if __name__ == '__main__':
    unittest.main()
