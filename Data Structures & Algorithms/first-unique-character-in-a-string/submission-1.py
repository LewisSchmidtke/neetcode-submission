class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        dupe = set()

        for c in s:
            if c not in seen and c not in dupe:
                seen.add(c)
            
            elif c in seen and c not in dupe:
                seen.remove(c)
                dupe.add(c)
        
        for idx, c in enumerate(s):
            if c in seen:
                return idx
        
        return -1