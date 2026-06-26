class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Store values to look for differences
        seen = {}

        for i, x in enumerate(nums):
            diff = target - x

            if diff in seen:
                # Seen is in the past, so can assume it will always come first in the returned list
                return [seen[diff], i]
            # Store index for the number (smaller index first)
            if x not in seen:
                seen[x] = i
        
        return False

