# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.

# Example 1:
# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

# Example 2:
# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def binary_search(nums, target):
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        neg = binary_search(nums, 0)

        pos = len(nums) - binary_search(nums, 1)

        return max(pos, neg)
