# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

# Example 1:
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

# Example 2:
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0

# https://leetcode.com/problems/max-area-of-island/description/

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        visited = [[False for _ in range(c)] for _ in range(r)]

        max_count = 0

        def dfs(i, j):
            if i < 0 or j < 0 or j >= c or i >= r or visited[i][j] or grid[i][j] == 0:
                return 0
            visited[i][j] = True
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        for i in range(r):
            for j in range(c):
                if not visited[i][j] and grid[i][j] == 1:
                    island_cnt = dfs(i, j)
                    max_count = max(max_count, island_cnt)

        return max_count
