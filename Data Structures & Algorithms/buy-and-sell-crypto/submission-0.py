class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        left = 0
        right = 1

        while right < len(prices):
            buy = prices[left]
            sell = prices[right]

            max_profit = max((sell - buy), max_profit)

            if sell <= buy:
                left += 1
                right = left + 1
            else:
                right += 1

        return max_profit
