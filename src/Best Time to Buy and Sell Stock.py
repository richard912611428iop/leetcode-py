class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices:
            return 0
        max_profit = 0
        min_price = 1 << 31
        i = 0
        while i < len(prices):
            min_price = min(prices[i], min_price)
            max_profit = max(prices[i] - min_price, max_profit)
            i += 1
        return max_profit
