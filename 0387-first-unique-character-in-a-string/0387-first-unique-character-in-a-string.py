class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for i in s:
            counts[i] = counts.get(i, 0) + 1
        
        for key, value in counts.items():
            if value == 1: #checks if the key has a value of 1
                return s.index(key) 
        return -1

    

        

        







            
        