class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        new_array = []
        for i in range(len(prices)-1):
            if prices[i+1]-prices[i] > 0:
                new_array.append(prices[i+1]-prices[i])
        return(sum(new_array))