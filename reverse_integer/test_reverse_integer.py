import unittest
from reverse_integer import Solution

MAX_REVERSED_INT_32 = 7463847412

class ReverseIntegerTestCase(unittest.TestCase):
    solution = Solution()
    def test_reverse_integer(self):
        result = self.solution.reverse(123)
        self.assertEqual(result, 321)

        result = self.solution.reverse(-123)
        self.assertEqual(result, -321)

        result = self.solution.reverse(120)
        self.assertEqual(result, 21)

        result = self.solution.reverse(0)
        self.assertEqual(result, 0)

        result = self.solution.reverse(1534236469)
        self.assertEqual(result, 0)
        
        result = self.solution.reverse(1563847412)
        self.assertEqual(result, 0)

        result = self.solution.reverse(27463847412)
        self.assertEqual(result, 0)

        result = self.solution.reverse(MAX_REVERSED_INT_32)
        self.assertEqual(result, 0)

        result = self.solution.reverse(901000)
        self.assertEqual(result, 109)
        
        
        
        