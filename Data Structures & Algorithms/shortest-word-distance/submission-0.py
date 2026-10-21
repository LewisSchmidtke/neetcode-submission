class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pos1 = None
        pos2 = None

        min_dist = float("inf")

        for idx, word in enumerate(wordsDict):
            if word == word1:
                pos1 = idx
            if word == word2:
                pos2 = idx

            if pos1 is not None and pos2 is not None:
                min_dist = min(min_dist, abs(pos2-pos1))
            
        return min_dist
            