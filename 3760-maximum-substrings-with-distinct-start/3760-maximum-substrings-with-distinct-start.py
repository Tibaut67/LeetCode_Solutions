
class Solution:
    def maxDistinct(self, s: str) -> int:
        seen = set()
        count = 0
        for i in s: 
            if i not in seen:
                count += 1 
                seen.add(i)
            else:
               seen.add(i)
        return count
