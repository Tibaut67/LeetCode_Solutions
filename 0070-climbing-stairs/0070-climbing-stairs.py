class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        if not n == 1:
            if not n == 2:
                for i in range(3, n+1):
                    x = a + b
                    a = b
                    b = x
                return b
            return 2
        return 1



        
        

        