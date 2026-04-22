class Solution:
    def tribonacci(self, n: int) -> int:
        def dfs(n):
            if n == 2:
                return 1

            if n < 2:
                return n

            if n in cache:
                return cache[n]

            cache[n] = dfs(n - 3) + dfs(n - 2) + dfs(n - 1)
            return cache[n]

        cache = {}
        return dfs(n)