# Given an array of distinct integers arr, where arr is sorted in ascending order, return the smallest index i that satisfies arr[i] == i. If there is no such index, return -1.

# Example 1:
# Input: arr = [-10,-5,0,3,7]
# Output: 3
# Explanation: For the given array, arr[0] = -10, arr[1] = -5, arr[2] = 0, arr[3] = 3, thus the output is 3.

# Example 2:
# Input: arr = [0,2,5,8,17]
# Output: 0
# Explanation: arr[0] = 0, thus the output is 0.

# Example 3:
# Input: arr = [-10,-5,3,4,7,9]
# Output: -1
# Explanation: There is no such i that arr[i] == i, thus the output is -1.

# https://leetcode.com/problems/fixed-point/description/

from typing import List


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == mid:
                ans = mid
                right = mid - 1
            elif arr[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1

        return ans
