class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = 0
        length = len(words)

        if length == 1:
            return True

        for word in words:
            count += len(word)

        return count % length == 0 and count != length