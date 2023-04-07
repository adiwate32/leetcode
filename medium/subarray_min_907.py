# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

# Example 1:
# Input: arr = [3,1,2,4]
# Output: 17
# Explanation:
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.

# Example 2:
# Input: arr = [11,81,94,43,3]
# Output: 444

# https://leetcode.com/problems/sum-of-subarray-minimums/description/

from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        MOD = 10**9 + 7

        dp = [0] * len(arr)

        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                prev_smaller = stack[-1]
                dp[i] = dp[prev_smaller] + (i - prev_smaller) * arr[i]
            else:
                dp[i] = (i + 1) * arr[i]

            stack.append(i)

        return sum(dp) % MOD
