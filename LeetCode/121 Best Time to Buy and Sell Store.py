# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share
# of the stock), design an algorithm to find the maximum profit.

# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

# Input: [7, 6, 4, 3, 1]
# Output: 0
# In this case, no transaction is done, i.e. max profit = 0.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for low in range(len(prices)):
            for high in range(low, len(prices)):
                if prices[low] >= prices[high]:
                    continue
                else:
                    diff = prices[high] - prices[low]
                    if profit < diff:
                        profit = diff
        return profit
