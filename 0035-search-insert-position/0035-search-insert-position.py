class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target < nums[0]:
            return 0
        
        for i, val in reversed(list(enumerate(nums))):
            if val < target:
                return i + 1
            



       
       
        