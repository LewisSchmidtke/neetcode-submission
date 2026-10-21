class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        self.vowels = {"a", "e", "i", "o", "u"}
        
        prefix = []
        count = 0

        for word in words:
            count += self.check_valid(word)
            prefix.append(count)

        res = []
        for q in queries:
            start, end = q
            if start == end:
                res.append(self.check_valid(words[start]))
            elif start == 0:
                res.append(prefix[end])
            else:
                res.append(prefix[end] - prefix[start - 1])
        
        return res
            

    def check_valid(self, w):
        if w[0] in self.vowels and w[-1] in self.vowels:
            return 1
        
        return 0