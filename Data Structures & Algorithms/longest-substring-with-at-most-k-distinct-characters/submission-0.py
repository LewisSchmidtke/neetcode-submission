class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        right = 0

        table = {}
        curr_length = 0
        max_length = 0

        while right < len(s):
            if s[right] not in table and len(table) < k:
                table[s[right]] = 1
                curr_length += 1
                max_length = max(max_length, curr_length)

            elif s[right] in table and len(table) <= k:
                table[s[right]] += 1
                right += 1
                curr_length += 1
                max_length = max(max_length, curr_length)
                continue

            while len(table) > k:
                table[s[left]] -= 1
                curr_length -= 1
                if table[s[left]] == 0:
                    del table[s[left]]
                left += 1
            right += 1

        max_length = max(max_length, curr_length)
        return max_length