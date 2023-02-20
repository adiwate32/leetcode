# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

# https://leetcode.com/problems/search-a-2d-matrix/description/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])
        left = 0
        right = rows * cols - 1

        while left <= right:

            # Compute the index of the pivot element and get its value
            pivot = (left + right) // 2
            pivot_ele = matrix[pivot // cols][pivot % cols]

            if pivot_ele == target:
                return True

            # Update the range of search based on the comparison of the pivot element with the target
            if pivot_ele > target:
                right = pivot - 1
            else:
                left = pivot + 1

        return False
