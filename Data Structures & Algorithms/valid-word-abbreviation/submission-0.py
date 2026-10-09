class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        pointer_w = 0
        pointer_a = 0
        abbr_num = ""

        while pointer_w < len(word) and pointer_a < len(abbr):
            while abbr[pointer_a].isnumeric():
                abbr_num += abbr[pointer_a]
                pointer_a += 1

            if abbr_num:
                abbr_num = int(abbr_num)
                pointer_w = pointer_w + abbr_num

            if word[pointer_w] != abbr[pointer_a]: 
                return False

            pointer_w += 1
            pointer_a += 1

        return True


            
            

            
