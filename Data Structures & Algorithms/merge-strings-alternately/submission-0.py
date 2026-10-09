class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = 0
        w2 = 0

        res = ""
        while w1 < len(word1) or w2 < len(word2):
            if w1 < len(word1):
                res += word1[w1]
            if w2 < len(word2):
                res += word2[w2]
            
            w1 += 1
            w2 += 1

        return res
            
        
