import unittest
from palindrome_number import Solution

class IsPalindromeTestCase(unittest.TestCase):
    solution = Solution()
    def test_is_palindrome(self):
        result = self.solution.isPalindrome(121)
        self.assertEqual(result, True)

        result = self.solution.isPalindrome(-123)
        self.assertEqual(result, False)

        result = self.solution.isPalindrome(10)
        self.assertEqual(result, False)


        
        
        