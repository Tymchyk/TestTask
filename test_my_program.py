import unittest
from bored_module.bored_api import get_response
from my_program import start
import sys

class TestMyProgram(unittest.TestCase):

    def test_get_response(self):
        dict = {'type':'education', 'participants':1, 'price_min': 20, 'price_max':30,'accessibility_min':0.1,"accessibility_max":100}
        dict1 = {'type':'education', 'participants':1, 'price_min': 0, 'price_max':30,'accessibility_min':0.1,"accessibility_max":100}
        with self.assertRaises(ValueError) as context:
            self.assertEquals(get_response(**dict))
            self.assertEqual(str(context.exception), "No activity found with the specified parameters!")
        self.assertEquals(len(get_response(**dict1)),7)
    
    def test_my_program(self):
        test_new = ["new", "--type", "education"]
        with self.assertRaises(TypeError) as context:
            self.assertEquals(start(test_new))
            self.assertEqual(str(context.exception), "You need to add all parametrs!")
        test_list = ["new", "--type", "education"]
        with self.assertRaises(TypeError) as context:
            self.assertEquals(start(test_new))
            self.assertEqual(str(context.exception), "This command have only one parametrs!")

if __name__ == '__main__':
    unittest.main()
        
