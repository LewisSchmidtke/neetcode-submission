class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)

        total_shift = 0
        for s_shift in shift:
            if s_shift[0] == 0:
                total_shift -= s_shift[1]
            else:
                total_shift += s_shift[1]
        is_negative = False
        if total_shift < 0:
            is_negative = True

        total_shift = abs(total_shift) % n
        if is_negative:
            total_shift *= -1
        
        result = [""] * n
        for idx, c in enumerate(s):
            new_pos = idx + total_shift
            if is_negative and new_pos <= -n:
                new_pos = (abs(new_pos) % n) * -1
            elif not is_negative and new_pos >= n:
                new_pos = new_pos % n

            result[new_pos] = c

        return "".join(result)


