class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d1 = {}
        d2 = {}
        new = []
        count = 0
        final = []
        for x in (nums1):
            if x in d1:
                d1[x] += 1
            else:
                d1[x] = 1
        for x in (nums2):
            if x in d2:
                d2[x] += 1
            else:
                d2[x] = 1
        
        for key in d1:
            if key in d2:
                count = min(d1[key], d2[key])
                final.extend([key]* count)
        return final
                
                

        
        



                
        



        
