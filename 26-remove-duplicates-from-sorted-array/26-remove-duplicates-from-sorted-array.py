class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        Left = 1
        for Right in range(1,len(nums)):
            if nums[Right] != nums[Right - 1]:
                nums[Left] = nums[Right]
                Left = Left + 1
        return Left