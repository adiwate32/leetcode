"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10
"""
from typing import List


class Solution:
    def minimumTotal(self, mat: List[List[int]]) -> int:
        rows = len(mat)

        for r in range(1, rows):
            cols = len(mat[r])
            for c in range(cols):
                if c == 0:
                    mat[r][c] += mat[r - 1][0]

                elif c == cols - 1:
                    mat[r][c] += mat[r - 1][c - 1]

                else:
                    mat[r][c] += min(mat[r - 1][c - 1], mat[r - 1][c])

        return min(mat[rows - 1])
