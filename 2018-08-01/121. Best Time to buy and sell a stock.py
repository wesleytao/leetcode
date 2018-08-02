class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        start = 0
        buy_day = 0

        sell_price = 0
        sell_day = 0

        end = len(prices) - 1
        buy_price = float('inf')
        sell_day = len(prices) - 1

        while (sell_day > buy_day):
            if buy_price > prices[start]:
                buy_price = prices[start]
                buy_day = start
            if start <= sell_day:
                start = start + 1
            if sell_price < prices[end]:
                sell_price = prices[end]
                sell_day = end
            if end >= buy_day:
                end = end - 1
        # print(sell_day, buy_day)
        return max(0, sell_price - buy_price)

if __name__=="__main__":
    mysol = Solution()
    print(mysol.maxProfit([7,1,5,3,6,4]))