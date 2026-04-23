class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i, n):
            if i >= n:
                return 1 if i == n else 0
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = dfs(i + 1, n) + dfs(i + 2, n)
            return cache[i]

        cache = [-1] * n
        return dfs(0, n)

