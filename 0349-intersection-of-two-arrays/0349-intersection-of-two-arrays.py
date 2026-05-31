class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        for i in nums1:
            if i in nums2 and i not in result: 
                result.append(i)  
        return result



        