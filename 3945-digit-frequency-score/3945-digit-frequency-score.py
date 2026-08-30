class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        x = 0 #sum
        while n > 0:
            digit = n % 10
            x += digit
            n //= 10
        return x
        