class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # t should be substring in s:
        # 1. check if its already substring -> result 0
        # 2. if incomplete, check how many characters of t are subsequence in s and get length of t - chars in s

        chars_of_t_in_s = 0 # O(1)
        s_pointer = 0 # O(1)

        for c in t: # O(n)
            while s_pointer < len(s): # total max O(m)
                if c == s[s_pointer]: # O(1)
                    chars_of_t_in_s += 1
                    s_pointer += 1
                    break
                s_pointer += 1
            
        return len(t) - chars_of_t_in_s

    # Space O(1), Time O(n + m)