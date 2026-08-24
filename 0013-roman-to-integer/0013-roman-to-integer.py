class Solution:
    def romanToInt(self, s: str) -> int:
        I = s.count("I") * 1
        V = s.count("V") * 5
        X = s.count("X") * 10
        L = s.count("L") * 50
        C = s.count("C") * 100
        D = s.count("D") * 500
        M = s.count("M") * 1000
        add = I + V + X + L + C + D + M

    
        IV = s.count("IV") * 2 
        IX = s.count("IX") * 2
        XL = s.count("XL") * 20
        XC = s.count("XC") * 20
        CD = s.count("CD") * 200
        CM = s.count("CM") * 200
        sub = IV + IX + XL + XC + CD + CM

        result = add - sub
        return result
        
        
        