"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        mid = total // 2
        n = len(nums)

        if n == 0:
            return False

        dp = [False] * (mid + 1)
        dp[0] = True

        for num in nums:
            for j in range(mid, num - 1, -1):
                if dp[mid]:
                    return True
                dp[j] = dp[j] or dp[j - num]

        return dp[mid]
