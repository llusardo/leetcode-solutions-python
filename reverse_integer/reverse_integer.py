"""Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
 

Constraints:

-231 <= x <= 231 - 1"""

import math

MAX_INT_32 = 2147483647

class Solution:
    def reverse(self, x: int) -> int:
        reversed = 0
        i = abs(x)
        
        while i != 0: 
            reversed = reversed * 10 + i % 10
          
            if reversed >= MAX_INT_32 - 1:
                reversed = 0
                break

            i //= 10

        if x < 0:
            reversed = - reversed  

        return reversed         
