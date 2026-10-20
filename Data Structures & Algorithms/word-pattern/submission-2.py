class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_map = {}
        seen_words = set()
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        for idx, word in enumerate(words):
            pat = pattern[idx]
            if pat not in pattern_map and word not in seen_words:
                pattern_map[pat] = word
                seen_words.add(word)
            elif pat not in pattern_map and word in seen_words:
                return False
            else:
                match = pattern_map[pat]
                if match != word:
                    return False

        return True
        

