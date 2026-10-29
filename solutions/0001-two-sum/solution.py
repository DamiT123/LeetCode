class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """ O(n^2) Solution
            for i in range(len(nums)):
                for j in range(i + 1, (len(nums))):
                    if nums[i] + nums[j] == target:
                            return [i,j] """
        # O(n) Solution
        seen = {}
        for i, x in enumerate(nums):
            wanted = target - x
            if wanted in seen:
                return [i,seen[wanted]]
            seen[x] = i
            
            
            

            
        
