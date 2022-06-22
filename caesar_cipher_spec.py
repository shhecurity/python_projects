# Rewrite this in Unit Test
import unittest
from caesar_cipher import caesar_cipher

class TestCaesarCipher(unittest.TestCase):
  
    def testCaesarCipher1(self):
        output = caesar_cipher("Boy! What a string!", -5)
        self.assertEqual(output,"Wjt! Rcvo v nomdib!")
    
    def testCaesarCipher2(self):
        output = caesar_cipher("Hello zach168! Yes here.", 5)
        self.assertEqual(output,"Mjqqt efhm168! Djx mjwj.")
        
    def testCaesarCipher3(self):
        output = caesar_cipher("Hello Zach168! Yes here.", -5)
        self.assertEqual(output,"Czggj Uvxc168! Tzn czmz.")
     
    def testCaesarCipher4(self):
        output = caesar_cipher("What a string!", 5)
        self.assertEqual(output,"Bmfy f xywnsl!")
        
        
if __name__ == "__main__":
      unittest.main()
        
    


print(caesar_cipher("Boy! What a string!", -5) == "Wjt! Rcvo v nomdib!")
print(caesar_cipher("Hello zach168! Yes here.", 5) == "Mjqqt efhm168! Djx mjwj.")
print(caesar_cipher("Hello Zach168! Yes here.", -5) == "Czggj Uvxc168! Tzn czmz.")
