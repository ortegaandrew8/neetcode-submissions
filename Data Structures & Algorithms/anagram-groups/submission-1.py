class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Map charCount to list of anagrams
        # Add default to ensure when doing res[(0,0,1...)].append, there is a list if one doesnt already exist
        res = defaultdict(list)

        for s in strs:
            # lowercase letters from a-z
            count = [0] * 26 

            for c in s:
                # make letters index 0-25
                count[ord(c) - ord("a")] += 1

            # Add the string with matching letter counts
            # 'eat' has 1 e, 1 a, 1 t, 'tea' matches that count
            # change to tuple since list cannot be keys
            res[tuple(count)].append(s)
        
        # Dont need keys, just the list of lists
        return list(res.values())