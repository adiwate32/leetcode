# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
# Return the modified image after performing the flood fill.

# Example 1:
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

# Example 2:
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0, so no changes are made to the image.

# https://leetcode.com/problems/flood-fill/description/

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, new_color: int
    ) -> List[List[int]]:
        # get the number of rows and columns in the image
        rows, cols = len(image), len(image[0])

        # get the current color of the pixel
        color = image[sr][sc]

        # if the current color is the same as the new color, return the image
        if color == new_color:
            return image

        # define a DFS function to fill the pixels with the new color
        def dfs(sr, sc):
            # if the current pixel has the same color as the starting pixel
            if image[sr][sc] == color:
                # set the current pixel to the new color
                image[sr][sc] = new_color
                # recurse to the left pixel if there is one
                if sc >= 1:
                    dfs(sr, sc - 1)
                # recurse to the right pixel if there is one
                if sc + 1 < cols:
                    dfs(sr, sc + 1)
                # recurse to the top pixel if there is one
                if sr >= 1:
                    dfs(sr - 1, sc)
                # recurse to the bottom pixel if there is one
                if sr + 1 < rows:
                    dfs(sr + 1, sc)

        # call the DFS function to start filling the pixels with the new color
        dfs(sr, sc)

        return image
