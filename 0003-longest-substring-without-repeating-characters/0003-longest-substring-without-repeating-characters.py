class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # If we've seen the character and it's inside our current window
            if s[right] in char_map and char_map[s[right]] >= left:
                # Move the left pointer to the right of the previous occurrence
                left = char_map[s[right]] + 1
            
            # Update the last seen index of the character
            char_map[s[right]] = right
            
            # Update the maximum length found so far
            max_length = max(max_length, right - left + 1)
        return max_length      