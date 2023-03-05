# Given an integer array nums, return the length of the longest strictly increasing
# subsequence
# .

# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

# https://leetcode.com/problems/longest-increasing-subsequence/description/

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)  # Initialize dp array with all 1's

        for i in range(len(nums)):  # Traverse the input array
            for j in range(i):  # Traverse the input array up to i
                if (
                    nums[i] > nums[j]
                ):  # Check if current number is greater than previous number
                    dp[i] = max(
                        dp[i], dp[j] + 1
                    )  # Update dp array for longest increasing subsequence

        return max(dp)  # Return length of longest increasing subsequence
