class Solution:
    def rotateString(self, s: str, goal: str) -> bool:   
        new = s
        for x in s:
            if s == goal:
                return True
            new = s[1:] + s[0]
            s = new
        return False
        
        
