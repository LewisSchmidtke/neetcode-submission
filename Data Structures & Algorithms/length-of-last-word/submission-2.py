class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right_pointer = len(s) - 1
        score = 0
 
        while right_pointer >= 0 and s[right_pointer] == " ":
            right_pointer -= 1
        
        while right_pointer >= 0 and s[right_pointer] != " ":
            right_pointer -= 1
            score += 1
        
        return score