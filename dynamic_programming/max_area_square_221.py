"""
    Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

    Example 1:
    Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    Output: 4

    Example 2:
    Input: matrix = [["0","1"],["1","0"]]
    Output: 1
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        r = len(matrix)
        c = len(matrix[0])
        dp = [[0] * (c + 1) for _ in range(r + 1)]

        max_area = 0
        for i in range(1, r + 1):
            for j in range(1, c + 1):

                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = (
                        min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1
                    )

                    max_area = max(max_area, dp[i][j])

        return max_area * max_area
