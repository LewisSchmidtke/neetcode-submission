class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_map = {
            "b" : 1,
            "a" : 1,
            "l" : 2,
            "o" : 2,
            "n" : 1,
        }
        balloon_indices = [0, 1, 11, 13, 14]

        freq = [0] * 26

        for c in text:
            if c not in balloon_map:
                continue
            freq[ord(c) - ord("a")] += 1

        instances = float("inf")
        for idx in balloon_indices:
            instances = min(instances, int(freq[idx] / balloon_map[chr(idx + ord("a"))]))

        return instances if instances != float("inf") else 0
