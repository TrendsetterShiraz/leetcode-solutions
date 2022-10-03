class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        #One Liner Solution is this:
        # s[::] = s[::-1]
        #This is good but slow.
        
        #This is a two pointer approach:
        left = 0 #Create a left pointer for the array.
        right = len(s) - 1 #Create a Right Pointer for the array.
        while left < right: #While Left is lesser than Right
            temp = s[left] #I make my temporary variable as left pointer first
            s[left] = s[right] #I set my left equal to right like H of HELLO equal to the O
            s[right] = temp #I set my last O OELLO to H from the temporary variable
            left +=1 #Then I Increment my Left
            right -= 1 #Then I decrement my right.
            #This approach is faster than 90% of the submissions on Leetcode.
            #Hee Hee Haa Haa