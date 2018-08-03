class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # greedy
        if len(prices) < 2:
            return 0
        # base case
        buy_price = prices[0]
        sell_price = prices[1]
        min_price = min(buy_price, sell_price)
        max_profit = max(0, sell_price - buy_price)

        for price in prices[2:]:
            # case 1
            if price >= sell_price:
                sell_price = price
                max_profit = max(max_profit, (sell_price - buy_price))
                # case 2
            if (price - min_price) > max_profit:
                max_profit = price - min_price
                sell_price = price
                buy_price = min_price
            min_price = min(min_price, price)
        return max_profit
