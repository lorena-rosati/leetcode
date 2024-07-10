class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        l, r, max_profit = 0, 1, 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1

        return max_profit