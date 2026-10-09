class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n, m = len(word), len(abbr)
        i = j = 0

        while i < n and j < m:
            if abbr[j] == '0':
                return False

            if word[i] == abbr[j]:
                i += 1
                j += 1

            elif abbr[j].isalpha(): # Means word[i] != abbr[j]
                return False

            else:
                sub_l = 0
                while j < m and abbr[j].isdigit():
                    sub_l = sub_l * 10 + int(abbr[j])
                    j += 1

                i += sub_l

        return i == n and j == m




