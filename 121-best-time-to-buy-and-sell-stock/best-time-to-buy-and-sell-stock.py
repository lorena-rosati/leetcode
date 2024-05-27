class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0

        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff > 0:
                maxProfit = max(maxProfit, diff)
            else:
                l = r
            r += 1
        return maxProfit