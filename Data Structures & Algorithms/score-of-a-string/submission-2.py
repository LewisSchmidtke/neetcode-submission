class Solution:
    def scoreOfString(self, s: str) -> int:
        left = 0
        right = 1

        score = 0

        while right < len(s):
            score += abs((ord(s[right]) - ord(s[left])))
            left += 1
            right += 1
        
        return score
        