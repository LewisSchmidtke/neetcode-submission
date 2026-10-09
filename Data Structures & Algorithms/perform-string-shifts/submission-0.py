class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = 0 # left negative, right positive
        for shift_m in shift:
            if shift_m[0] == 0:
                total_shift -= shift_m[1]
            else:
                total_shift += shift_m[1]

        len_s = len(s)
        total_shift = total_shift % len_s

        if total_shift == 0:
            return s
        
        new_s = ["a"] * len_s

        for index, c in enumerate(s):
            if total_shift < 0: # shift left
                new_index = index - total_shift
            else:
                new_index = index + total_shift

            if new_index >= len_s:
                new_index -= len_s

            new_s[new_index] = c

        return "".join(new_s)