class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # First Solution
        d = defaultdict(list) #defaultdict(list) so if the key is empty we can still add because it created an empty one automocatically. similar to .get
        for x in strs: # go through each word
            count = [0] * 26
            for c in x: # go through each letter
                count[ord(c) - ord("a")] += 1 # the index is now the index following the alphabet so you add to whichever letter it is.eg a = 80, b = 81, 81 - 80 = 1 = b's place.
            d[tuple(count)].append(x) #tuple allows it so count stays the same there as it changes throughout the code. you append each of the keys that are the same / not
        
        return list(d.values()) #expects a list return type and d.values allown doesnt return it as a list

        # Second Solution
        """groups = defaultdict(list)

        for x in strs:
            key = "".join(sorted(x))
            groups[key].append(x)

        return list(groups.values())"""
            





            


        


        
