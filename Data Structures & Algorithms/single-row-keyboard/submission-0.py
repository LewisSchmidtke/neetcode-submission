class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        keymap = {}
        for index, char in enumerate(keyboard):
            keymap[char] = index

        time = 0
        prev_char = keyboard[0]
        for character in word:
            time += abs(keymap[prev_char] - keymap[character])
            prev_char = character

        return time


