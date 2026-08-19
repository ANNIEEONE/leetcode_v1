class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        end = 0
        
        # Helper function to expand around a given center and return the length
        def expandAroundCenter(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Length of the palindrome is (right - left - 1) 
            # because the loop breaks when the condition is violated
            return right - left - 1

        for i in range(len(s)):
            # Check for odd-length palindromes (single character center)
            len1 = expandAroundCenter(i, i)
            # Check for even-length palindromes (two character center)
            len2 = expandAroundCenter(i, i + 1)
            
            max_len = max(len1, len2)
            
            # If we found a longer palindrome, update the start and end pointers
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        # Return the longest palindromic substring
        return s[start:end + 1]