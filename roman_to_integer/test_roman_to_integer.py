import unittest
from roman_to_integer import Solution

class RomanToIntegerTestCase(unittest.TestCase):
    solution = Solution()
    
    def test_roman_to_integer(self):
        self.assertRaises(Exception, self.solution.romanToInt, '')

        self.assertRaises(Exception, self.solution.romanToInt, 'IIIIIIIIIIIIIIII')

        self.assertRaises(Exception, self.solution.romanToInt, 'MMMM')
        
        result = self.solution.romanToInt('III')
        self.assertEqual(result, 3)

        result = self.solution.romanToInt('IV')
        self.assertEqual(result, 4)

        result = self.solution.romanToInt('IX')
        self.assertEqual(result, 9)

        result = self.solution.romanToInt('LVIII')
        self.assertEqual(result, 58)

        result = self.solution.romanToInt('MCMXCIV')
        self.assertEqual(result, 1994)

        result = self.solution.romanToInt('MXXI')
        self.assertEqual(result, 1021)

        result = self.solution.romanToInt('MMII')
        self.assertEqual(result, 2002)

        result = self.solution.romanToInt('MMMCMXCIX')
        self.assertEqual(result, 3999)
        
        
        
        
        