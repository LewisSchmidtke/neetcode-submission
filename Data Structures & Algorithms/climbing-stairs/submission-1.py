class Solution:
    def climbStairs(self, n: int) -> int:
        self.res = 0
        self.climb(n)
        return self.res

    def climb(self, height):
        if height < 0:
            return None

        if height == 0:
            self.res += 1
        
        else:
            self.climb(height - 2)
            self.climb(height - 1)
