class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for word_nr in range(len(words)):
            for char_nr in range(len(words[word_nr])):
                if char_nr >= len(words) or word_nr >= len(words[char_nr]) or words[word_nr][char_nr] != words[char_nr][word_nr]:
                    return False
        
        return True

