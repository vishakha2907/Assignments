import unittest
import Palindrome

class testpali(unittest.TestCase):
		
		def test_pali(self):
			self.assertEqual(pali.rev(535),535)
			self.assertEqual(pali.rev(1221),1221)
	    
			
if __name__ == '__main__':
	unittest.main()
	
