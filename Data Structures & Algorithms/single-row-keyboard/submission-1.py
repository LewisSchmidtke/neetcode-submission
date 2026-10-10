class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        position_map = [0] * 26
        for idx, letter in enumerate(keyboard):
            position_map[ord(letter) - ord("a")] = idx

        time = 0
        current_pos = 0
        for letter in word:
            letter_pos = position_map[ord(letter) - ord("a")]
            time += abs(letter_pos - current_pos)
            current_pos = letter_pos
        
        return time
