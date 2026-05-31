class Solution:
    def isPalindrome(self, x: int) -> bool:
        # y = reversed int as str
        y = str(x)[::-1]

        if str(x) == y: 
            return True
        elif str(x) != y: 
            return False

        