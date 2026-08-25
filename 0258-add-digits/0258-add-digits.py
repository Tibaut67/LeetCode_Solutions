class Solution(object):
    def addDigits(self, num):
        x = len(str(num))
        while x > 1:
            total = sum(map(int, str(num)))
            num = total
            x = len(str(total))
        return num



        
        