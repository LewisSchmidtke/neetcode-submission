class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        left = 0
        right = 0

        chars_in_sub = set()

        while right < len(s):
            char = s[right]
            if char not in chars_in_sub:
                chars_in_sub.add(char)
                length = (right - left) + 1
                right += 1
                max_length = max(max_length, length)
            else:
                while s[left] != char: # Remove all chars until duplicate is found
                    chars_in_sub.remove(s[left])
                    left += 1
                
                chars_in_sub.remove(s[left]) # Remove duplicate
                left += 1
        
        return max_length
