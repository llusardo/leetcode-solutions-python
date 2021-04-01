"""Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

 

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
 

Constraints:

-231 <= x <= 231 - 1"""

import math

MAX_INT_32 = 2147483647

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        
        reversed = 0
        
        i = x
        
        exp = self.digits(i) - 1

        while i != 0: 
            if i % 10 != 0:
                reversed = (i % 10) * (10 ** exp) + reversed
            else:
                reversed    

            if reversed >= MAX_INT_32 - 1:
                reversed = 0
                break

            i = (i // 10)
            exp = exp - 1
         
        return reversed == x
                
    def digits(self, n: int) -> int:
        if n > 0:
            digits = int(math.log10(n))+1
        elif n == 0:
            digits = 1
        else:
            digits = int(math.log10(-n))+1
        return digits 10    
   
