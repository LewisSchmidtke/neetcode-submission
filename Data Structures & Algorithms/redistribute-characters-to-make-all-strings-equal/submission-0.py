class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = 0
        length = len(words)

        for word in words:
            count += len(word)

        return count % length == 0