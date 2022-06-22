import unittest

from pad_array import pad

class OptimalChangeTestCases(unittest.TestCase):
    
    def test_pad_array_by_two_with_default(self):
        output = pad([1,2,3], 5)
        self.assertEqual(output, [1,2,3,None,None])
        
    def test_pad_array_by_two_strings(self):
        output = pad([1,2,3], 5, 'apple')
        self.assertEqual(output, [1,2,3,'apple', 'apple'])    
        
    def test_pad_array_with_no_pad(self):
        output = pad([1,2,3], 3)
        self.assertEqual(output, [1,2,3])    
        
if __name__ == "__main__":
    unittest.main()  