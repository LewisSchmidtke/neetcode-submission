class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}

        trav = 0

        res = []

        while trav < len(s):
            if s[trav] not in vowels:
                res.append(s[trav])
            
            trav += 1

        return "".join(res)
