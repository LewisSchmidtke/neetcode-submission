class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq_map = [0] * 26
        for c in s:
            freq_map[ord(c) - ord("a")] += 1
        
        uneven_letter_frequencies = 0

        for x in range(26):
            if freq_map[x] % 2 != 0:
                uneven_letter_frequencies += 1
            
            if uneven_letter_frequencies > 1:
                return False

        return True