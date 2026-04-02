class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        count_m = defaultdict(int)

        for c in magazine:
            count_m[c] += 1

        for c in ransomNote:
            if c not in count_m:
                return False
            
            count_m[c] -= 1

            if count_m[c] == 0:
                del count_m[c]

        return True