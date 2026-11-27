class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # First Solution
        answer = []
        d = {}
        for x in nums:
            d[x] = d.get(x,0) + 1
        for i in range (0, k):
            m = max(d, key = d.get)
            answer.append(m)
            d.pop(m,None)
        return answer
        
            
                    


