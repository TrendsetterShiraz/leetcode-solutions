class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        #One Liner Solution:
        # return nums + nums #But this is cheating LOL...
        
        # A 3 Liner Solution which shows you know your stuff.
        for i in range(len(nums)): #Go Through each element of nums.
            nums.append(nums[i]) #Append it to the existing nums.
        return nums #return it.