class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = [0] * 26
        total_words = len(words)

        for word in words:
            for char in word:
                freq[ord(char) - ord("a")] += 1
        
        for count in freq:
            if count % total_words != 0:
                return False

        return True