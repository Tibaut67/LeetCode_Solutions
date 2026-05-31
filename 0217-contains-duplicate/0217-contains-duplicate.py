class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for item in nums:
            if item in map:
                return True
            map[item] = True
        return False

