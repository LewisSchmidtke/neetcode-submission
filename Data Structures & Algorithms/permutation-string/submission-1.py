class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        frequency_map = [0] * 26
        temp_map = [0] * 26
        running_sum = 0

        for char1 in s1:
            frequency_map[ord(char1) - ord("a")] += 1
            running_sum += 1

        length_sub_seq = len(s1)

        left = 0
        for pos, char in enumerate(s2):
            temp_map[ord(char) - ord("a")] += 1
            if temp_map == frequency_map:
                return True

            if pos - left + 1 <= length_sub_seq:
                print("if")
                continue

            temp_map[ord(s2[left]) - ord("a")] -= 1

            if temp_map == frequency_map:
                return True
            
            left += 1   

        return False



