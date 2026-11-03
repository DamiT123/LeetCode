class Solution:
    def fib(self, n: int) -> int:
        f = [0, 1]
        next = 0
        for i in range(2, n + 1):
            next = ( f[i - 1] + f[i - 2] )
            f.append(next)
        return (f[n])
        
            
    
            
        
