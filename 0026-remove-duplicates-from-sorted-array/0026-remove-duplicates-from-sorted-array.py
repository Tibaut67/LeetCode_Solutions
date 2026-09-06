class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[x] = nums[i]
                x += 1
        return x
        