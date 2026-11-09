class Solution:
    def climbStairs(self, n: int) -> int:
        prev = {}

        prev[1] = 1
        prev[2] = 2
        
        if n == 1:
            return prev[1]
        elif n == 2:
            return prev[2]

        for i in range(3, n + 1):
            prev[i] = prev[i-1] + prev[i - 2]
        
        return prev[n]
