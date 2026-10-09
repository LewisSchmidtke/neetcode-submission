class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        frq_map = [0] * 26

        for c in text:
            frq_map[ord(c) - ord("a")] += 1

        b = frq_map[ord('b') - ord('a')]
        a = frq_map[ord('a') - ord('a')]
        l = frq_map[ord('l') - ord('a')] // 2
        o = frq_map[ord('o') - ord('a')] // 2
        n = frq_map[ord('n') - ord('a')]
        
        return min(b, a, l, o, n)