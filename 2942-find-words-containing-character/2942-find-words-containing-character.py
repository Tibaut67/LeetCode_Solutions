class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ahhh = []
        for i, word in enumerate(words):
            if x in word:
                ahhh.append(i)
        return ahhh

        