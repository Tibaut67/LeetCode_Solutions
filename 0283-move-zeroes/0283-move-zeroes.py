class Solution(object):
    def moveZeroes(self, nums):
        x = 0
        for i in range(len(nums)): 
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[x]
                nums[x] = temp
                x += 1
        return nums
           

        