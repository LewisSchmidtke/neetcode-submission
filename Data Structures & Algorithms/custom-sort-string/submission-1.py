class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = [0] * 26

        for c in s:
            s_count[ord(c) - ord("a")] += 1 
        
        res = []

        for o in order:
            freq = s_count[ord(o) - ord("a")]

            if freq == 0:
                continue

            res.extend([o] * freq)
            s_count[ord(o) - ord("a")] = 0
        
        for idx, count in enumerate(s_count):
            if count != 0:
                res.extend([chr(idx + ord("a"))] * count)

        return "".join(res)
            


            
