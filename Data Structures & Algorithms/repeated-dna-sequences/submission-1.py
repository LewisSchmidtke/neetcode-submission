class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mapping = {
            "A" : 0,
            "C" : 1,
            "G" : 2,
            "T" : 3
        }

        seen = set()
        unique = set()

        if len(s) <= 10:
            return []
        
        ident = 0
        for i in range(10):
            ident = ident * 4 + mapping[s[i]]

        seen.add(ident)
        point = 10

        while point < len(s):
            ident = (ident * 4 + mapping[s[point]]) % (4 ** 10)

            if ident not in seen:
                seen.add(ident)
            else:
                unique.add(s[point - 9: point + 1])
            point += 1
        
        return list(unique)
