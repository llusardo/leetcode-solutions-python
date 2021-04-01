""" 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

from typing import List

class Solution:        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2 :
            raise Exception("Wrong list size, at least two elements are needed")

        dictionary = {}
        
        for i in range(len(nums)):
            res = target - nums[i]
            if res in dictionary :
                return [dictionary[res], i]

            dictionary[nums[i]] = i
        return nums

"""Complexity Analysis:

Time complexity : O(n)O(n). We traverse the list containing nn elements exactly twice. Since the hash table reduces the look up time to O(1)O(1), the time complexity is O(n)O(n).

Space complexity : O(n)O(n). The extra space required depends on the number of items stored in the hash table, which stores exactly nn elements."""