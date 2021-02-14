import unittest
import Alpha

class TestCharAlpha(unittest.TestCase):

    
    #TO CHECK WHETHER THE NUMBER GIVEN IS A POSITIVE INTEGER
    def test_numbinput(self):
        self.assertGreater(Alpha.numbinput(3), 0)
        self.assertRaises(ValueError,Alpha.numbinput, 0)
        self.assertRaises(ValueError,Alpha.numbinput, -6)        
        self.assertRaises(TypeError,Alpha.numbinput,6.23)
        self.assertRaises(TypeError,Alpha.numbinput, True)
        self.assertRaises(TypeError,Alpha.numbinput, "string")

        
if __name__=='__main__':
    unittest.main()

                 
