import rot13_cipher 
from unittest import TestCase

class TestRot13(TestCase):
	def test_that_rot13_cipher_function_exists(self):
		rot13_cipher.rot13_cipher()

	def test_that_get_rot13_cipher_function_works(self):
		response = rot13_cipher.get_rot13_cipher("Hello, world!")
		self.assertEqual(response, "Uryyb, jbeyq!")