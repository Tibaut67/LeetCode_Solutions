class Solution:
    def mirrorDistance(self, n: int) -> int:
        revNum = int(str(n)[::-1])
        result = abs(revNum - n)
        return result
