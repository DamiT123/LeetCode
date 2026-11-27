class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """if len(s) !== len(t):
            return False
        first = {}
        second = {}
        for x in s:
            if x in first:
                first[x] += 1
            else:
                first[x] = 1
        for x in t:
            if x in second:
                second[x] += 1
            else:
                second[x] = 1
        return (first == second) """

        #Another method
        if len(s) != len(t):
            return False

        first = {}
        second = {}
        for i in range(len(s)):
            first[s[i]] = 1 + first.get(s[i], 0)
            second[t[i]] = 1 + second.get(t[i], 0)
        return (first == second)

        


    

        
