class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}

        for index, s_char in enumerate(s):
            if s_char not in char_map:
                char_map[s_char] = t[index]
            else:
                if char_map[s_char] != t[index]:
                    return False
        
        return True