class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        base = ord(s[0])

        for s_char in s[1:]:
            char_val = ord(s_char)
            score += abs(base - char_val)
            base = char_val

        return score



