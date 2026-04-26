class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # We have 2 choices each time -> take 1 or 2 steps
        # Initially start from 0 or 1 index
        # Minimize cost to still reach the top
        staircase_height = len(cost)
        cache = [-1] * staircase_height

        min_cost = min(
            self._dfs(0, staircase_height, cache, cost),
            self._dfs(1, staircase_height, cache, cost),
        )
        return min_cost

    def _dfs(self, current_height: int, max_height: int, cache: list[int], cost: list[int]):
        if current_height >= max_height:
            return 0
        
        if cache[current_height] != -1:
            return cache[current_height]
        
        cache[current_height] = min(
            cost[current_height] + self._dfs(current_height + 1, max_height, cache, cost),
            cost[current_height] + self._dfs(current_height + 2, max_height, cache, cost),
        )

        return cache[current_height]
