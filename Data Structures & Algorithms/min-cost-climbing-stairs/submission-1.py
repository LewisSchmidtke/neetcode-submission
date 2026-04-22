class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i: int, n: int):
            if i >= n:
                return 0

            if cache[i] != "-inf":
                return cache[i]

            cache[i] = cost[i] + min(dfs(i + 1, n), dfs(i + 2, n))
            return cache[i]
        
        cache = ["-inf"] * len(cost)
        x = min(dfs(0, len(cost)), dfs(1, len(cost)))
        return x
