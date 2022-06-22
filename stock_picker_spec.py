# Rewrite this in Unit Test
import unittest
from stock_picker import picker

class TestStockPicker(unittest.TestCase):
    
    def test_simple_stock_picker_1(self):
        output = picker([1,2,4])
        self.assertEqual(output,[0,2])
    
    def test_stock_picker_1(self):
        output = picker([17,3,6,9,15,8,6,1,10])
        self.assertEqual(output,[1,4])

    def test_stock_picker_2(self):
        output = picker([3,17,6,9,18,15,6,1,10])
        self.assertEqual(output,[0,4])
        
    
    def test_stock_picker_3(self):
        output = picker([1,17,6,9,8,15,6,3,19])
        self.assertEqual(output,[0,8])

    def test_stock_picker_4(self):
        output = picker([19,17,6,9,8,15,6,3,1])
        self.assertEqual(output,[2,5])
    
if __name__ == "__main__":
    unittest.main()  
    
    
# print(picker([1,17,6,9,8,15,6,3,19]) == [0,8])
# print(picker([19,17,6,9,8,15,6,3,1]) == [2,5])
