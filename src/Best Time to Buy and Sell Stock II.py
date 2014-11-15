class Solution:
    # @param prices, a list of integer
    # @return an integer
    def foo(self, prices):
        # print (prices)
        if len(prices) == 1 or len(prices) == 0:
            return 0
        max_profit = 0
        min_price = 4294967296
        i = 0
        while i < len(prices):
            min_price = min(prices[i], min_price)
            max_profit = max(prices[i] - min_price, max_profit)
            i += 1
        return max_profit

    def maxProfit(self, prices):
        if len(prices) == 1 or len(prices) == 0:
            return 0
        last_price = prices[0]
        last_index = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < last_price:
                profit += self.foo(prices[last_index:i])
                last_index = i
            last_price = prices[i]
        profit += self.foo(prices=prices[last_index:])
        return profit
