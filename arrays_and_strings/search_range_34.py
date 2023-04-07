# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(nums, first=True):
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    if first:
                        if mid == left or nums[mid - 1] < target:
                            return mid

                        else:
                            right = mid - 1

                    else:
                        if mid == right or nums[mid + 1] > target:
                            return mid

                        else:
                            left = mid + 1

                elif nums[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1

            return -1

        left_ele = search(nums)

        if left_ele == -1:
            return [-1, -1]

        right_ele = search(nums, False)

        return [left_ele, right_ele]
