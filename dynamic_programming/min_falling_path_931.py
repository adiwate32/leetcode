"""
    Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

    A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

    Example 1:
    Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
    Output: 13
    Explanation: There are two falling paths with a minimum sum as shown.

    Example 2:
    Input: matrix = [[-19,57],[-40,-5]]
    Output: -59
    Explanation: The falling path with a minimum sum is shown.

    https://leetcode.com/problems/minimum-falling-path-sum/description/
"""
from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        for r in range(1, rows):
            for c in range(0, cols):
                if 0 < c < cols - 1:
                    grid[r][c] += min(
                        grid[r - 1][c + 1], grid[r - 1][c], grid[r - 1][c - 1]
                    )

                if c == 0:
                    grid[r][c] += min(grid[r - 1][c], grid[r - 1][c + 1])

                if c == cols - 1:
                    grid[r][c] += min(grid[r - 1][c], grid[r - 1][c - 1])

        return min(grid[rows - 1][:cols])