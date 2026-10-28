class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        found = set()
        for i in nums:
            if i not in found:
                found.add(i)
        
        for i in range(len(nums)+1):
            if i not in found:
                return i

        