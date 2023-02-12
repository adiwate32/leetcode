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


def searchRange(nums: List[int], target: int) -> List[int]:

    if len(nums) == 0:
        return [-1, -1]

    def search_low(nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid - 1

            if nums[mid] < target:
                left = mid + 1

        return left

    def search_high(nums, target):

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1

            if nums[mid] <= target:
                left = mid + 1

        return right

    low = search_low(nums, target)
    high = search_high(nums, target)

    if low >= 0 and high < len(nums) and low <= high:
        return [low, high]
    else:
        return [-1, -1]
