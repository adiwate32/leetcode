# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

# Example 1:
# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
# Explanation: The smallest element common to both arrays is 2, so we return 2.

# Example 2:
# Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
# Output: 2
# Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

# https://leetcode.com/problems/minimum-common-value/description/

from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        arr1 = nums2 if len(nums1) > len(nums2) else nums1
        arr2 = nums1 if len(nums1) > len(nums2) else nums2

        def binary_search(nums, target):
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return False

        for num in arr1:
            if binary_search(arr2, num):
                return num

        return -1
