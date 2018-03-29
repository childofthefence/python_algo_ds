import unittest

from valid_number import ValidNumber


class TestValidNumber(unittest.TestCase):
	
	def setUp(self):
		pass
	
	def test_non_number(self):
		
		self.assertFalse(ValidNumber.is_number('abc'))
		
	def test_valid_number(self):
		
		self.assertTrue(ValidNumber.is_number('0.1'))
		
	def test_scientific(self):
		self.assertTrue(ValidNumber.is_number('1e12'))
	
	
if __name__ == '__main__':
	unittest.main()
