class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        combo = nums1 + nums2
        combo.sort()
        full = len(nums1) + len(nums2)
        
        if full % 2 == 0:
            x = full // 2
            y = x - 1
            z = (combo[x] + combo[y]) / 2
            return z
        else:
            return combo[full // 2]