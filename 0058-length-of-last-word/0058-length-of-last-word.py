class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        x = s.strip()
        for i in reversed(x):
            if i != " ":
                count += 1
            else: 
                break  
        return count

        