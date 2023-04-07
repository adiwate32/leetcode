"""
    Given an integer array nums, return the number of longest increasing subsequences.

    Notice that the sequence has to be strictly increasing.

    Example 1:
    Input: nums = [1,3,5,4,7]
    Output: 2
    Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

    Example 2:
    Input: nums = [2,2,2,2,2]
    Output: 5
    Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
"""
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp, cn = [1] * n, [1] * n

        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        cn[i] = cn[j]
                    elif dp[i] == dp[j] + 1:
                        cn[i] += cn[j]

        max_len = max(dp)

        return sum([cn[i] for i in range(n) if dp[i] == max_len])
