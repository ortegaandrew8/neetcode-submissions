class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Should be same length to be anagram
        if len(s) != len(t):
            return False
        
        # Maintain count hashtable
        s_hash = {}
        t_hash = {}

        for c1, c2 in zip(s,t):

            #Update counters
            s_hash[c1] = s_hash.get(c1, 0) + 1
            t_hash[c2] = t_hash.get(c2, 0) + 1


        for key, value in s_hash.items():

            # Key should exist in t_hash and value should match
            if key not in t_hash or value != t_hash[key]:
                return False

    
        return True