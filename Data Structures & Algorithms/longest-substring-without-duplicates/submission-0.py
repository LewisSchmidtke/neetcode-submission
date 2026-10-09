class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_unique_string_length = 0
        sub_string_set = set()

        left = 0 
        right = 0
        while right < len(s):
            current_char = s[right]
            if left == right or current_char not in sub_string_set:
                sub_string_set.add(current_char)
                right += 1
            else:
                max_unique_string_length = max(len(sub_string_set), max_unique_string_length)
                while current_char in sub_string_set:
                    sub_string_set.remove(s[left])
                    left += 1

        return max_unique_string_length
