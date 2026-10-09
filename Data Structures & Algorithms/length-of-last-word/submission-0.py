class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        words = [word for word in words if word] # Remove strings that are just spaces
        return len(words[-1])