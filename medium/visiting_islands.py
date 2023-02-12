# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# https://leetcode.com/problems/number-of-islands/

from typing import List


def numIslands(grid: List[List[str]]) -> int:

    r, c = len(grid), len(grid[0])

    visited = [[False for _ in range(c)] for _ in range(r)]

    def dfs(i, j):

        if i < 0 or j < 0 or j >= c or i >= r or visited[i][j] or grid[i][j] == "0":
            return
        visited[i][j] = True
        dfs(i, j + 1)
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j - 1)

    count = 0
    for i in range(r):
        for j in range(c):

            if not visited[i][j] and grid[i][j] == "1":
                count += 1
                dfs(i, j)

    return count
