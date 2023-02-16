# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# https://leetcode.com/problems/rotate-array/description/


from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # Get the length of the list of numbers and take the modulus of k with respect to the length
    n = len(nums)
    k = k % n

    # Define a helper function to reverse the order of elements in the list between the start and end indices (inclusive)
    def reverse(start, end, nums):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Reverse the order of all elements in the list
    reverse(0, n - 1, nums)
    # Reverse the order of the first k elements in the list
    reverse(0, k - 1, nums)
    # Reverse the order of the remaining elements in the list
    reverse(k, n - 1, nums)
