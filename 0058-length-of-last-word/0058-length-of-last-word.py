class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        balls = s.strip()
        for i in reversed(balls):
            if i != " ":
                count += 1
            else: 
                break  
        return count

        