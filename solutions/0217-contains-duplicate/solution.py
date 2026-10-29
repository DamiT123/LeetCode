class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """ s = set()
            for i, x in enumerate(nums):
                s.add(x)
                if len(s) != i + 1:
                    return True
            return False """
        s = set()
        for x in nums:
            if x in s:
                return True
            s.add(x)
        return False


        
