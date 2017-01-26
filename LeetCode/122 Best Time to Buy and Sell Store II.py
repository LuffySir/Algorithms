# Say you have an array for which the ith element is the price of a given stock on day i.

# You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
# design an algorithm to find the maximum profit.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit

        # return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
