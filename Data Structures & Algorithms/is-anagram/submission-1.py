class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = 0
        count_array = [0] * 26 # Frequency map

        # add
        for c in s:
            count_array[ord(c) - ord("a")] += 1
            counter += 1

        # subtract
        for c in t:
            if counter == 0 or count_array[ord(c) - ord("a")] == 0:
                return False
            count_array[ord(c) - ord("a")] -= 1
            counter -= 1

        return counter == 0

        
