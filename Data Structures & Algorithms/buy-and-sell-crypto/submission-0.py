class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        minimum = max(prices)
        day = 0
        while day < len(prices):
            if prices[day] < minimum:
                minimum = prices[day]
            profit = prices[day] - minimum
            if profit > max_profit:
                max_profit = profit
            day += 1
        return max_profit