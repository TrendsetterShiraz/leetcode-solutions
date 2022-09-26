import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        st1 = "".join(re.split("[^a-zA-Z0-9]*", s))
        st2 = st1[::-1]
        if st1.lower() == st2.lower():
            return True