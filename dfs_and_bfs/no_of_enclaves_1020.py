"""
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
"""
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(grid, r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or not grid[r][c]:
                return

            grid[r][c] = 0

            dfs(grid, r - 1, c)
            dfs(grid, r, c - 1)
            dfs(grid, r + 1, c)
            dfs(grid, r, c + 1)

            return

        for r in range(rows):
            if grid[r][0]:
                dfs(grid, r, 0)

            if grid[r][cols - 1]:
                dfs(grid, r, cols - 1)

        for c in range(cols):
            if grid[0][c]:
                dfs(grid, 0, c)

            if grid[rows - 1][c]:
                dfs(grid, rows - 1, c)

        cnt = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    cnt += 1

        return cnt
