# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

# Example 1:
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

# Example 2:
# Input: grid = [[3,2],[1,0]]
# Output: 0

# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        i, j = len(grid) - 1, 0

        count = 0

        while i >= 0 and j < len(grid[0]):
            if grid[i][j] < 0:
                count += len(grid[0]) - j
                i -= 1
            else:
                j += 1

        return count
