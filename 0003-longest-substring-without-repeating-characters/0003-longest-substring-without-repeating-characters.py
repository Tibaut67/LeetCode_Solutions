class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        highest = 0
        seen = set()
        left = 0
        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(char)
            if len(seen) > highest:
                highest = len(seen)
        return highest

            

        