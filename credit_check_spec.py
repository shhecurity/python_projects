# Can you translate this driver code to unit tests?

from credit_check import credit_check
import unittest

class CreditCheck(unittest.TestCase):
    
        def test_is_valid_1(self):
            self.assertEqual(credit_check("5541808923795240"),"The number is valid!")
         
        def test_is_valid_2(self):
            self.assertEqual(credit_check("4024007136512380"),"The number is valid!")
            
             
        def test_is_valid_3(self):
              self.assertEqual(credit_check("6011797668867828"),"The number is valid!")   

        def test_is_invalid_1(self):
              self.assertEqual(credit_check("5541801923795240"),"The number is not valid!")   
              
        def test_is_invalid_2(self):
              self.assertEqual(credit_check("4024007106512380"),"The number is not valid!")  
              
        def test_is_invalid_3(self):
              self.assertNotEqual(credit_check("6011797668868728"),"The number is valid!")  
        
        def test_is_return_string(self):
            self.assertEqual(type(credit_check("6011797668868728")),str)
            
        def test_check_input_legnth(self):
             self.assertEqual(credit_check("60117868728"), "Invalid input!")      
            
            
# print(credit_check('5541808923795240') == "The number is valid!")
# print(credit_check("4024007136512380") == "The number is valid!")
# print(credit_check("6011797668867828") == "The number is valid!")

# print(credit_check("5541801923795240") == "The number is invalid!")
# print(credit_check("4024007106512380") == "The number is invalid!")
# print(credit_check("6011797668868728") == "The number is invalid!")






if __name__=='__main__':
    unittest.main()