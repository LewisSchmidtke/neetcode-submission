class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = min(self.dfs(0, len(cost), cost), self.dfs(1, len(cost), cost))
        return min_cost

    def dfs(self, i: int, n: int, cost_arr: List[int]):
        if i >= n:
            return 0

        return cost_arr[i] + min(self.dfs(i + 1, n, cost_arr), self.dfs(i + 2, n, cost_arr))