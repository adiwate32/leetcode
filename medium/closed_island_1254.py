"""
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
"""
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(grid, r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False

            if grid[r][c] == 1:
                return True

            grid[r][c] = 1
            isClosed = True

            dir_x = [0, 1, 0, -1]
            dir_y = [1, 0, -1, 0]

            for i in range(4):
                r_n = r + dir_x[i]
                c_n = c + dir_y[i]

                if not dfs(grid, r_n, c_n):
                    isClosed = False

            return isClosed

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and dfs(grid, r, c):
                    count += 1

        return count
