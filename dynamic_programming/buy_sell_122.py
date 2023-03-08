# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

# Find and return the maximum profit you can achieve.


# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

from typing import List


def maxProfit(prices: List[int]) -> int:

    if len(prices) == 0:
        return 0

    profit = []
    for i in range(1, len(prices)):

        profit.append(max(0, prices[i] - prices[i - 1]))

    return sum(profit)


# dynamic programming


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}

        def dfs(i, buying):

            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]
            no_stock = dfs(i + 1, buying)
            if buying:
                profit = dfs(i + 1, not buying) - prices[i]
            else:
                profit = dfs(i + 1, not buying) + prices[i]

            dp[(i, buying)] = max(no_stock, profit)

            return dp[(i, buying)]

        return dfs(0, True)
