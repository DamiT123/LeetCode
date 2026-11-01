class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i, x in enumerate(s):
            if x in seen:
                seen[x] = -2
            else:
                seen[x] = i
        for v in seen.values():
            if v != -2:
                return v
        return -1
                

        
        
