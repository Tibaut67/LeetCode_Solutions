class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0 
        x = 0 
        for i in range(len(s) - 1):
            x = abs(ord(s[i]) - ord(s[i+1]))
            result = x + result
        return result
        