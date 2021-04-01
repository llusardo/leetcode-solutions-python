"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Example 2:

Input: s = "IV"
Output: 4
Example 3:

Input: s = "IX"
Output: 9
Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999]."""


class Solution:
    """def romanToInt(self, s: str) -> int:
        if  len(s) < 1 or len(s) > 15: 
            raise Exception("Invalid String length")

        romans = list(s)
        i = 0
        result = 0

        while i != len(romans): 
            if romans[i] == 'I':  
                current = 1
                previousDigit = result % 10
                result = result + current 
            elif romans[i] == 'V':
                current = 5
                previousDigit = result % 10
                if previousDigit == 1:
                    current = 4
                    result = result  + current - 1  
                else:
                    result = result  + current  
            elif romans[i] == 'X':
                current = 10
                previousDigit = result % 10
                if previousDigit == 1:
                    current = 9
                    result = result + current - 1
                else:
                    result = result + current    
            elif romans[i] == 'L':
                current = 50
                previousDigit = result % 100
                if previousDigit == 10: 
                    current = 40
                    result = result + current - 10
                else:
                    result = result  + current  
            elif romans[i] == 'C':
                current = 100
                previousDigit = result % 100
                if previousDigit == 10:
                    current = 90
                    result = result + current - 10
                else:
                    result = result + current    
            elif romans[i] == 'D':
                current = 500
                previousDigit = result % 1000
                if previousDigit == 100:
                    current = 400
                    result = result + current - 100
                else:
                    result = result  + current    
            elif romans[i] == 'M':
                current = 1000  
                previousDigit = result % 1000
                if previousDigit == 100:
                    current = 900  
                    result = result + current - 100
                else:
                    result = result  + current                 
            i += 1
            if result > 3999:
                raise Exception("Invalid result range")

        if result < 1:
                raise Exception("Invalid result range") 

        return result"""  

        
    def romanToInt(self, s: str) -> int:
        if  len(s) < 1 or len(s) > 15: 
            raise Exception("Invalid String length")

        roman_dic = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}    

        total = 0
        prev = 0

        for c in s:
            current = roman_dic[c]

            if prev != 0 and prev < current:
                total -= prev + prev

            total += current 

            if total > 3999:
                raise Exception("Invalid result range")
            
            prev = current
            
        return total 
            


        
