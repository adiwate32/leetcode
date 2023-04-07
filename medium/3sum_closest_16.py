# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

# https://leetcode.com/problems/3sum-closest/description/

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float("inf")

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                # Calculate the current sum
                sum = nums[i] + nums[left] + nums[right]

                # Check if it's equal to the target
                if target == sum:
                    return target

                # Check if it's closer to the target than previous ones
                if abs(target - sum) <= abs(diff):
                    diff = target - sum

                # Move the pointers accordingly
                if target - sum > 0:
                    left += 1
                else:
                    right -= 1

        return target - int(diff)
