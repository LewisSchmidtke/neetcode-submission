class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_map = defaultdict(int)

        for letter in magazine:
            freq_map[letter] += 1

        for l in ransomNote:
            if freq_map[l] == 0:
                return False
            
            freq_map[l] -= 1

        return True
