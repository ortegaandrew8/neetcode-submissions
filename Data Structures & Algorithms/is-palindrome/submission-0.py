class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Pointer at start and end of string
        l = 0
        r = len(s) - 1

        while l < r:

            # Move string while not alphanumeric characters
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            # Case insensitive
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        
        return True