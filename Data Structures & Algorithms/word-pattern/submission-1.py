class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        word_to_pattern = {}
        pattern_to_word = {}

        for index, p in enumerate(pattern):
            if p not in pattern_to_word:
                pattern_to_word[p] = words[index]

            if words[index] not in word_to_pattern:
                word_to_pattern[words[index]] = p

            if pattern_to_word[p] != words[index] or word_to_pattern[words[index]] != p:
                return False

        return True