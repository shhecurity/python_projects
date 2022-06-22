# Can you translate this driver code to unit tests?
import unittest
from palindrome import palindrome

class TestForPalindromes(unittest.TestCase):

    def test__palindrome1(self):
        output = palindrome('racecar')
        self.assertEqual(output,True)
    
    def test__palindrome2(self):
        output = palindrome('Noon')
        self.assertEqual(output,True)
    
    def test__palindrome3(self):
        output = palindrome('ciVic')
        self.assertEqual(output,True)
        
    def test__palindrome4(self):
        output = palindrome('nice')
        self.assertEqual(output,False)
        
    def test__palindrome5(self):
        output = palindrome(434)
        self.assertEqual(output,True)
    
    def test__palindrome6(self):
        output = palindrome(123)
        self.assertEqual(output,False)
        
    def test__palindrome7(self):
        output = palindrome('bomb')
        self.assertEqual(output,False)
        
    def test__palindrome8(self):
        output = palindrome('Sore was I ere I saw Eros.')
        self.assertEqual(output,True)
        
    def test__palindrome9(self):
        output = palindrome('A man, a plan, a canal -- Panama')
        self.assertEqual(output,True)


if __name__ == "__main__":
      unittest.main()
        
    

# This should return a bunch of trues
# print(palindrome('racecar') == True)
# print(palindrome('Noon') == True)
# print(palindrome('ciVic') == True)
# print(palindrome('nice') == False)
# print(palindrome(434) == True)
# print(palindrome(123) == False)
# print(palindrome('bomb') == False)

# print("The following should be True if you're trying to do the extra portion of this challenge")
# print(palindrome('Sore was I ere I saw Eros.') == True)
# print(palindrome('A man, a plan, a canal -- Panama') == True)

