class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        L, R = 0, 1

        while R < len(prices):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                maxP = max(profit, maxP)
            else:
                L = R
            R += 1
        return maxP 
        