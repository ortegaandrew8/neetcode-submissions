class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        # In case of multiple numbers appearing same frequency, make it list, +1 to make it clearer when assigning 
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            # Update count of how many times number appears
            count[n] = 1 + count.get(n,0)
        
        for n,c in count.items():
            # Append number to the number of counts
            # Number appears 6 times, it goes to index 6
            freq[c].append(n)
        
        res = []

        # Walk through frequency backwards (to get highest appearances)
        for i in range(len(freq) - 1, 0, -1):
            # Go through numbers at list at specified index
            for n in freq[i]:
                res.append(n)
                # Can stop once reach frequency needed
                if len(res) == k:
                    return res
