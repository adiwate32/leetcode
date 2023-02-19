# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

# https://leetcode.com/problems/sort-colors/description/

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Set p0 as the pointer for the next 0 to be placed at the start of the array
        p0 = curr = 0

        # Set p2 as the pointer for the next 2 to be placed at the end of the array
        p2 = len(nums) - 1

        while curr <= p2:

            if nums[curr] == 0:
                # If the current element is 0, swap it with the element at p0, increment p0 and curr
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1

            elif nums[curr] == 2:
                # If the current element is 2, swap it with the element at p2, decrement p2
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                # If the current element is 1, increment curr
                curr += 1
