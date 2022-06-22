# The code is written as driver code. Can you convert it to Unit Test?
import unittest
from armstrong_numbers import find_armstrong_numbers


class ArmstrongNumbersTestCase(unittest.TestCase):
  
    def test_returns_a_list(self):
        """
        when you call find_armstrong_numbers, it should return a list
        """
        self.assertEqual(type(find_armstrong_numbers(list(range(0,0)))), list)
    
    def test_returns_the_correct_list_0_to_8(self):
        """
        when you call find_armstrong_numbers(list(range(0,0)))
        when you call find_armstrong_numbers(list(range(0,100)))
        when you call find_armstrong_numbers(list(range(0,999)))
        """
        self.assertEqual(find_armstrong_numbers(list(range(0,8))),[0, 1, 2, 3, 4, 5, 6, 7])
        
    def test_returns_the_correct_list_0_to_99(self):    
        self.assertEqual(find_armstrong_numbers(list(range(0,100))),[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        
    def test_returns_the_correct_list_0_to_999(self):    
        self.assertEqual(find_armstrong_numbers(list(range(0,999))),[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])

if __name__ == '__main__':
    unittest.main()

# print(find_armstrong_numbers([0]) == [0]) 
# print(find_armstrong_numbers(list(range(0, 8))) == [0, 1, 2, 3, 4, 5, 6, 7])
# print(find_armstrong_numbers(list(range(0,100))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(find_armstrong_numbers(list(range(0,999))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])
