class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # On^2
        """for i, x in enumerate(nums):
            need = target - x
            for j in range(i+1, len(nums)):
                if nums[j] == need:
                    return [i,j]"""
        
        #On
        prevnums = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in prevnums:
                return [prevnums[diff], i]
            prevnums[x] = i



           

            
            
            

            
        
