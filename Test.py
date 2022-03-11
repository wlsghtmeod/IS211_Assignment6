import unittest
import conversions
import conversions_refactored
from conversions_refactored import ConversionNotPossible

class MyTest(unittest.TestCase):

    #Temperature Conversion Unittest
    def test_CtoK(self):
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(300),573.15, places=2)

    def test_CtoF(self):
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(300), 572.00, places=2)

    def test_FtoK(self):
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(300), 422.04, places=2)
    
    def test_FtoC(self):
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(300), 148.89, places=2)
    
    def test_KtoF(self):
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(300), 80.33, places=2)
    
    def test_KtoC(self):
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(300), 26.85, places=2)
    
    #Refactored Conversion
    #Temperature Conversion
    def test_convert_same(self):
        self.assertEqual(conversions_refactored.convert('C','C',300), 300)
    
    def test_convert_CtoK(self):
        self.assertAlmostEqual(conversions_refactored.convert('C','K',300),573.15, places=2)
    
    def test_convert_CtoF(self):
        self.assertAlmostEqual(conversions_refactored.convert('C','F',300), 572.00, places=2)

    def test_convert_FtoK(self):
        self.assertAlmostEqual(conversions_refactored.convert('F','K',300), 422.04, places=2)

    def test_convert_FtoC(self):
        self.assertAlmostEqual(conversions_refactored.convert('F','C',300), 148.89, places=2)
    
    def test_convert_KtoC(self):
        self.assertAlmostEqual(conversions_refactored.convert('K','C',300), 26.85, places=2)
    
    def test_convert_KtoF(self):
        self.assertAlmostEqual(conversions_refactored.convert('K','F',300), 80.33, places=2)
    
    #Distance Conversion
    def test_convert_MtoMi(self):
        self.assertAlmostEqual(conversions_refactored.convert('M','Mi',300),0.19, places=2)
    
    def test_convert_MtoY(self):
        self.assertAlmostEqual(conversions_refactored.convert('M','Y',300), 328.08, places=2)
    
    def test_convert_MitoM(self):
        self.assertAlmostEqual(conversions_refactored.convert('Mi','M',300),482803.2, places=2)

    def test_convert_MitoY(self):
        self.assertAlmostEqual(conversions_refactored.convert('Mi','Y',300),528000.00, places=2)
    
    def test_convert_YtoM(self):
        self.assertAlmostEqual(conversions_refactored.convert('Y','M',300),274.32, places=2)
    
    def test_convert_YtoMi(self):
        self.assertAlmostEqual(conversions_refactored.convert('Y','Mi',300),0.17, places=2)

    #Raising ConversionNotPossible Exception
    def test_convert_Raise_Error(self):
        self.assertAlmostEqual(conversions_refactored.convert('Y','C',300),0.17, places=2)

    #Same Unit Conversion
    def test_convert_Same(self):
        self.assertEqual(conversions_refactored.convert('C','C',300),300)


if __name__ == "__main__":
    unittest.main()