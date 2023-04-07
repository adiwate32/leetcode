"""
    Given an integer array nums and an integer k, return the maximum length of a 
    subarray
    that sums to k. If there is not one, return 0 instead.

    Example 1:
    Input: nums = [1,-1,5,-2,3], k = 3
    Output: 4
    Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

    Example 2:
    Input: nums = [-2,-1,2,1], k = 1
    Output: 2
    Explanation: The subarray [-1, 2] sums to 1 and is the longest.
"""
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        hash_map = {}
        prefix_sum = max_len = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum == k:
                max_len = i + 1

            if prefix_sum - k in hash_map:
                max_len = max(max_len, i - hash_map[prefix_sum - k])

            if prefix_sum not in hash_map:
                hash_map[prefix_sum] = i

        return max_len
