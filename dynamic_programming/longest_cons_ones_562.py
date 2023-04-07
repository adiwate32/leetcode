"""
Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

The line could be horizontal, vertical, diagonal, or anti-diagonal.

Example 1:
Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
Output: 3

Example 2:
Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
Output: 4
"""
from typing import List


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0

        rows = len(mat)
        cols = len(mat[0])

        dp = [[(0, 0, 0, 0)] * (cols + 2) for _ in range(rows + 1)]

        max_ans = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if mat[i - 1][j - 1] == 1:
                    dp[i][j] = (
                        dp[i - 1][j][0] + 1,
                        dp[i - 1][j - 1][1] + 1,
                        dp[i][j - 1][2] + 1,
                        dp[i - 1][j + 1][3] + 1,
                    )
                    max_ans = max(max_ans, max(dp[i][j]))

        return max_ans
