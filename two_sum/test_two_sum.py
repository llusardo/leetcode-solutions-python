import unittest
from two_sum import Solution

class TwoSumTestCase(unittest.TestCase):
    solution = Solution()
    def test_two_sum(self):
        result = self.solution.twoSum([2,7,11,15], 9)
        self.assertEqual(result, [0,1])

        result = self.solution.twoSum([3,2,4], 6)
        self.assertEqual(result, [1,2])

        result = self.solution.twoSum([3, 3], 6)
        self.assertEqual(result, [0,1])
