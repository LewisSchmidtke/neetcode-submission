class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        lengthW = len(word)
        lengthA = len(abbr)

        w = a = 0

        while a < lengthA and w < lengthW:
            if abbr[a] == "0":
                return False

            if word[w] == abbr[a]:
                a += 1
                w += 1

            elif abbr[a].isalpha(): # Means word[i] != abbr[j]
                return False

            else:
                start = a
                while a < lengthA and abbr[a].isdigit():
                    a += 1
                number = int(abbr[start:a])
                w += number

        return a == lengthA and w == lengthW

