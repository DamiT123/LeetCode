class Solution:
    def hammingWeight(self, n: int) -> int:
        #bit = []
        count = 0
        while n > 0:
            num = n % 2
            n = n // 2
            #bit.append(num)
            if num == 1:
                count +=1
        return count
        """count = 0
        for x in bit:
            if x == 1:
                count +=1
        return count """


        
