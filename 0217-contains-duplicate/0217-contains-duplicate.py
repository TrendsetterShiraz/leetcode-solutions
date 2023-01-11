class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 0:
            return False
        duplicates = {}
        for n in nums:
            if n in duplicates:
                # As soon as you spot a duplicate, exit
                return True
            else:
                # Just a placeholder for the value						
                duplicates[n] = 1
        return False