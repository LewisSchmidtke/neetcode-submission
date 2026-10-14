class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        buy = 0
        sell = 1

        while sell < len(prices):
            current_prof = prices[sell] - prices[buy]
            profit = max(profit, current_prof)

            if prices[sell] <= prices[buy]:
                buy = sell
                sell += 1
            else:
                sell += 1

        return profit

