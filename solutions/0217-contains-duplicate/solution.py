class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Adding into a non repeating array (set) and checking if the current value is already in the set. (a repeat)
        s = set()
        for x in nums:
            if x in s:
                return True
            else:
                s.add(x)
        return False


        
