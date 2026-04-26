class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1:
                count += 1
            n = n >> 1 # equal to floor division by 2
        return count