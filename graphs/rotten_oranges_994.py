"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = []
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        min_elapsed = 0
        while q:
            r, c, t = q.pop(0)

            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            for d in directions:
                new_r = r + d[0]
                new_c = c + d[1]

                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh -= 1

                        q.append((new_r, new_c, t + 1))

            min_elapsed = t

        return min_elapsed if fresh == 0 else -1
