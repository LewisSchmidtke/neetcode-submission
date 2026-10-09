class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w = 0
        a = 0
        numbers = []
        number = 0
        while a < len(abbr) and w < len(word):
            
            while a < len(abbr) and abbr[a].isnumeric():
                numbers.append(abbr[a])
                a += 1

            if numbers: 
                number = int("".join(numbers))
                numbers = []

            w += number
            number = 0

            if a < len(abbr) and w < len(word) and word[w] != abbr[a]:
                return False
            
            w += 1
            a += 1

        if a < len(abbr) or w < len(word):
            return False

        return True




