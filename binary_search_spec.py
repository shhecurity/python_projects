import unittest

from binary_search import binary_search

class BinarySearchTestCases(unittest.TestCase):
    
    def test_handles_empty_array(self):
        output = binary_search(1, [])
        self.assertEqual(output,-1)
        
    def test__simple_binary_search(self):
        output = binary_search(1, [1,2,3,4,5])
        self.assertEqual(output,0)
    
    def test_number_not_in_array(self):
        output= binary_search(5, [2,4,6,8,10])
        self.assertEqual(output, -1)
        
    def test_simple_binary_search_2(self):
        output = binary_search(2, [1,2,3,4,5])
        self.assertEqual(output,1)
    
    def test_simple_binary_search_3(self):
        output = binary_search(3, [1,2,3,4,5])
        self.assertEqual(output,2)
        
    def test_simple_binary_search_4(self):
        output = binary_search(5, [1,2,3,4,5])
        self.assertEqual(output,4)
        
        
# test_array = [1,2,3,4,5]
        
# print(binary_search(1, test_array) == 0)
# print(binary_search(2, test_array) == 1)
# print(binary_search(3, test_array) == 2)
# print(binary_search(4, test_array) == 3)
# print(binary_search(5, test_array) == 4)


# super_big_array = [1,5,7,2,3,8,4,9]
# print(binary_search(7, super_big_array) == 5)
# print(binary_search(6, super_big_array) == -1)


    
if __name__ == "__main__":
    unittest.main()  