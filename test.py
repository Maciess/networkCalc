import unittest
from binary import *
from octet2 import *
from main import *
class binTest(unittest.TestCase):

	def test_add(self):

		self.assertEqual(Binary(0)+Binary(0), Binary(0))


	def test_or(self):

		self.assertEqual(Binary(1) or Binary(0), Binary(1))
		self.assertEqual(Binary(0) or Binary(0), Binary(0))
		self.assertEqual(Binary(1) or Binary(1), Binary(1))


	def test_and(self):

		self.assertEqual(Binary(1) and Binary(0), Binary(0))
		self.assertEqual(Binary(0) and Binary(0), Binary(0))
		self.assertEqual(Binary(1) and Binary(1), Binary(1))

	def test_neg(self):

		self.assertEqual(~~Binary(1), Binary(1))
		
	def test_convert(self):
		number = 128
		self.assertEqual(Binary.deconvert(Binary.convert(number)), number)

	def test_error(self):

		with self.assertRaises(AssertionError):
			Octet(300)
			Octet(-1)
			Octet(15).u0b([1]*9)
			Octet(15).udecimal(256)
class octetTest(unittest.TestCase):

	def test_neg(self):

		self.assertEqual(~~Octet(145), Octet(145))

	def test_error(self):

		with self.assertRaises(AssertionError):
			Octet(300)
			Octet(-1)
			Octet(15).u0b([1]*9)
			Octet(15).udecimal(256)
			

class test_Calc(unittest.TestCase):

	def test_ValidAddres(self):
		self.assertTrue(Network_Calc.isValidAddres('168.0.0.1'))
		self.assertTrue(Network_Calc.isValidAddres('168.17.0.1'))
		self.assertFalse(Network_Calc.isValidAddres('168.0.0.256'))
		self.assertFalse(Network_Calc.isValidAddres('256.0.0.0'))

		

if __name__ == '__main__':
    unittest.main()