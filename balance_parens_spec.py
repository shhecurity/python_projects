import unittest

from balance_parens import balance_parens

class BalanceParensTestCases(unittest.TestCase):
    def test__simple_balanced_parens(self):
        output = balance_parens("()")
        self.assertEqual(output,"()")
        
    def test__simple_balanced_parens_2(self):
        output = balance_parens(")(")
        self.assertEqual(output,"")
    
    def test_extra_closing_parens(self):
        output= balance_parens("a(b)c)")
        self.assertEqual(output,"a(b)c")
        
    def test_advanced_balanced_parens_1(self):
        output= balance_parens("abc(d)e(fgh))(i)j)k")
        self.assertEqual(output, "abc(d)e(fgh)(i)jk")
        
    def test_advanced_balanced_parens_2(self):
        output= balance_parens("abc((d)e(fgh)(i)j(k")
        self.assertEqual(output, "abc(d)e(fgh)(i)jk")

    def test_nested_parens_1(self):
        output= balance_parens("abc(d)(ef(g(h))ij)k)lm()o)p")
        self.assertEqual(output, "abc(d)(ef(g(h))ij)klm()op")

    def test_nested_parens_1(self):
        output= balance_parens("abc(d)(ef(g(h))ij)k)lm()o)p")
        self.assertEqual(output, "abc(d)(ef(g(h))ij)klm()op")

    
if __name__ == "__main__":
    unittest.main()  
# # Add more test cases!...
# print(balance_parens("abc(d)e(fgh))(i)j)k") == "abc(d)e(fgh)(i)jk")
# print(balance_parens("abc((d)e(fgh)(i)j(k") == "abc(d)e(fgh)(i)jk")

# # Challenge: nested parentheses...
# print(balance_parens("abc(d)(ef(g(h))ij)k)lm()o)p") == "abc(d)(ef(g(h))ij)klm()op")