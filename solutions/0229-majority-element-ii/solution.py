class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        size = len(nums) // 3
        d = {}
        final = []
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        for key in d:
            if d[key] > size:
                final.append(key)
        return final
