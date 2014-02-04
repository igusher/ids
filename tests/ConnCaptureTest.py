import unittest
from capturemodel.ConnectionCapture import *

class TestConnCapture(unittest.TestCase):
	def setUp(self):
		self.connCapture = ConnectionCapture(['m1','m2'],['v1','v2'])

	def test_ctor(self):
		self.assertEqual(self.connCapture.features['m2'], 'v2');

if __name__ == '__main__':
	unittest.main()
