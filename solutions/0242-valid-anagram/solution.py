class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        d2 = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for c in t:
            if c in d2:
                d2[c] += 1
            else:
                d2[c] = 1
        return d2 == d
        
    

        
