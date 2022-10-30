import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Game Plan for O(N)
        
        #Only grab the characters using Regular Expressions ad lowercase the s string
        x = re.findall("[a-zA-Z0-9]", s.lower())
        
        #Stride the output from he negative index
        res = x[::-1]
        # and compare
        if str(x) == str(res):
            return True