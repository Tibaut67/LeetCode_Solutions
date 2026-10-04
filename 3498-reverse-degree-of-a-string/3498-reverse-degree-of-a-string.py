class Solution:
    def reverseDegree(self, s: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        revAlphabet = alphabet[::-1]
        result = 0
        mapping = {char: idx for idx, char in enumerate(revAlphabet, start=1)}

        for i, char in enumerate(s, start=1):
            result += i * mapping[char]


        return result