from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq_map = defaultdict(int) # O(1) space, maximum 26 key value pairs

        for char in s: #O(s) time
            freq_map[char] += 1
        
        res = [0] * len(s) # O(s) space
        res_pos = 0

        for order_c in order:
            if freq_map[order_c] == 0:
                continue
            
            for _ in range(freq_map[order_c]):
                freq_map[order_c] -= 1
                res[res_pos] = order_c
                res_pos += 1

        for key, value in freq_map.items():
            if value == 0:
                continue
            for _ in range(value):
                res[res_pos] = key
                res_pos += 1

        return "".join(res)