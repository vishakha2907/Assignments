import unittest
import frequency
class Test_Frequency(unittest.TestCase):
	
	def test_frequency(self):
		self.assertEqual(frequency.frequencyDigits(11175,1),3)
		self.assertEqual(frequency.frequencyDigits(89999,9),4)
		self.assertEqual(frequency.frequencyDigits(794499,4),2)
		self.assertEqual(frequency.frequencyDigits(1234,5),0)
		
	def test_notperfect(self):
	    self.assertEqual(frequency.frequencyDigits(-231012,3),0)
		
		
if __name__ == '__main__':
	unittest.main()
