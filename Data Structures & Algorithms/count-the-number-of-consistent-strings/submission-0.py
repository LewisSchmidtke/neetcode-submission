class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)

        valid = 0

        for w in words:
            val = True

            for c in w:
                if c not in allowed_set:
                    val = False
            
            if val:
                valid += 1

        return valid