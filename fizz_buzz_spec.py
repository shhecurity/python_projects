#write a program that returns the numbers from 1 to 100, but for multiples of 3 return "Fizz" instead of the number and for multiples of 5 return "Buzz" instead of the number.  For numbers that are multiples of both three and five, return "FizzBuzz" instead of the number.
import unittest # imports the Unit Test library
from fizz_buzz import fizzbuzz# import the fizzbuzz method from fizzbuzz.py

class FizzbuzzTestCase(unittest.TestCase):
    """Tests for fizzbuzz.py."""

    def test_returns_a_list(self):
        """When you call fizzbuzz(), you should get a list back"""
        self.assertEqual(type(fizzbuzz()), list)

    def test_returns_an_array_of_100_items(self):
        """When you call fizzbuzz(), you should get 100 items back"""
        self.assertEqual(len(fizzbuzz()), 100)

    def test_returns_the_correct_array(self):
        """When you call fizzbuzz(), you should get the correct elements back"""
        self.assertEqual(fizzbuzz(), [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "Fizzbuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "Fizzbuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "Fizzbuzz", 46, 47, "Fizz", 49, "Buzz", "Fizz", 52, 53, "Fizz", "Buzz", 56, "Fizz", 58, 59, "Fizzbuzz", 61, 62, "Fizz", 64, "Buzz", "Fizz", 67, 68, "Fizz", "Buzz", 71, "Fizz", 73, 74, "Fizzbuzz", 76, 77, "Fizz", 79, "Buzz","Fizz", 82, 83, "Fizz", "Buzz", 86, "Fizz", 88, 89, "Fizzbuzz", 91, 92, "Fizz", 94, "Buzz", "Fizz", 97, 98, "Fizz", "Buzz"])

if __name__ == '__main__':
    unittest.main()