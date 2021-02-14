import unittest 
import count
class TestCount(unittest.TestCase):
	
	def test_countDigit(self):
		self.assertEqual(count.countDigit(1564),4)
		self.assertEqual(count.countDigit(495),3)
		self.assertEqual(count.countDigit(85096),5)
		
	def test_countDigit_notEqual(self):
		self.assertNotEqual(count.countDigit(214),6)
		self.assertNotEqual(count.countDigit(5098),9)
		self.assertNotEqual(count.countDigit(897),7)

if __name__ == '__main__':
	unittest.main()
