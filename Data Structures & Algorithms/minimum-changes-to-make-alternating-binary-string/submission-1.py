class Solution:
    def minOperations(self, s: str) -> int:
        first = s[0]

        if s[0] == '1':
            start_one = True
        else:
            start_one = False

        ops = 0

        for index, c in enumerate(s):
            if c == '1':
                if start_one and index % 2 != 0 or not start_one and index % 2 == 0:
                    ops += 1
            else:
                if start_one and index % 2 == 0 or not start_one and index % 2 != 0:
                    ops += 1

        if ops > len(s) // 2:
            return len(s) - ops

        return ops

            

