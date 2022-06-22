import unittest
from calculate_mode2 import calculate_mode

class ModeTestCases(unittest.TestCase):

    def test_simple_mode(self):
        
    
    
    def test__calculate_Mode(self):
        output = calculate_mode([1,2,3,3])
        self.assertEqual(output,[3])
    
    def test__calculate_Mode2(self):
        output = calculate_mode([4.5, 0, 0])
        self.assertEqual(output,[0])
        
    def test__calculate_Mode3(self):
        output = calculate_mode([1.5, -1, 1, 1.5])
        self.assertEqual(output,[1.5])
        
    def test__calculate_Mode4(self):
        output = calculate_mode([1,1,2,2])
        self.assertEqual(output,[1,2])
        
    def test__calculate_Mode5(self):
        output = calculate_mode([1,2,3])
        self.assertEqual(output,[1,2,3])

    def test_calculate_Mode_with_words(self):  
        output = calculate_mode(["who", "what", "where", "who"]) 
        self.assertEqual(output,["who"])


if __name__ == "__main__":
      unittest.main()
        