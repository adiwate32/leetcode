"""
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

    Find the maximum profit you can achieve. You may complete at most k transactions.

    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

    Example 1:
    Input: k = 2, prices = [2,4,1]
    Output: 2
    Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

    Example 2:
    Input: k = 2, prices = [3,2,6,5,0,3]
    Output: 7
    Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
"""
from typing import List
import math


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying, t):
            if i >= len(prices) or t >= k:
                return 0

            if (i, buying, t) in dp:
                return dp[(i, buying, t)]
            no_stock = dfs(i + 1, buying, t)
            if buying:
                profit = dfs(i + 1, not buying, t) - prices[i]
            else:
                profit = dfs(i + 1, not buying, t + 1) + prices[i]

            dp[(i, buying, t)] = max(no_stock, profit)

            return dp[(i, buying, t)]

        return dfs(0, True, 0)


# dp(editorial)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # solve special cases
        if not prices or k == 0:
            return 0

        if 2 * k > n:
            res = 0
            for i, j in zip(prices[1:], prices[:-1]):
                res += max(0, i - j)
            return res

        # dp[i][used_k][ishold] = balance
        # ishold: 0 nothold, 1 hold
        dp = [[[-math.inf] * 2 for _ in range(k + 1)] for _ in range(n)]

        # set starting value
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]

        # fill the array
        for i in range(1, n):
            for j in range(k + 1):
                # transition equation
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                # you can't hold stock without any transaction
                if j > 0:
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        res = max(dp[n - 1][j][0] for j in range(k + 1))
        return res
