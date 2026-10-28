class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        result = 0
        while left < right:
            result = numbers[left] + numbers[right]
            if result == target:
                return [left + 1 , right + 1]
            if result < target:
                left += 1
            else:
                right -= 1







    
        