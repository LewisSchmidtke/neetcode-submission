class Solution:
    def climbStairs(self, n: int, k=0) -> int:
        if n == 0:
            return k + 1
        if n < 0:
            return k

        k = self.climbStairs(n - 1, k)
        k = self.climbStairs(n - 2, k)

        return k

