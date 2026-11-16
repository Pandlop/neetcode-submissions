class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float("inf")
        max_profit = 0

        for price in prices:
            profit = price - min_val
            if profit > max_profit:
                max_profit = profit

            if price < min_val:
                min_val = price

        return max_profit

        