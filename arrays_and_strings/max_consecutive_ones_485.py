"""
    Given a binary array nums, return the maximum number of consecutive 1's in the array.

    Example 1:
    Input: nums = [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

    Example 2:
    Input: nums = [1,0,1,1,0,1]
    Output: 2

    https://leetcode.com/problems/max-consecutive-ones/description/
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        i, j = -1, 0
        max_ans = 0

        while j < len(nums):
            if nums[j] == 0:
                max_ans = max(max_ans, j - i - 1)
                i = j

            j += 1

        return max(max_ans, j - i - 1)
